"""Small, reusable HTTP helper: timeouts, retries with back-off, logging."""

import logging
import time
import requests

log = logging.getLogger(__name__)
RETRY_STATUS = {429, 500, 502, 503, 504}


def get_json(url, params=None, retries=3, backoff=2.0, timeout=10):
    """GET a URL and return the parsed JSON. Retries network errors and 429/5xx."""
    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(url, params=params, timeout=timeout)
            if resp.status_code in RETRY_STATUS:
                raise requests.HTTPError(f"HTTP {resp.status_code}", response=resp)
            resp.raise_for_status()
            return resp.json()
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as err:
            status = getattr(err.response, "status_code", None)
            if status and status not in RETRY_STATUS:
                log.error("Request failed with %s, not retrying: %s", status, url)
                raise
            if attempt == retries:
                log.error("Giving up after %d attempts: %s", attempt, err)
                raise
            wait = backoff ** attempt
            log.warning("Attempt %d failed (%s). Retrying in %.0f s", attempt, err, wait)
            time.sleep(wait)