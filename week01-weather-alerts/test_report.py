"""Unit tests for alert rules in report.py."""

from report import find_alerts


def test_heat_alert() -> None:
    """Trigger a heat alert when max_c meets or exceeds heat_c."""
    rows = [
        {
            "date": "2026-06-01",
            "max_c": 44,
            "min_c": 30,
            "rain_mm": 0.0,
            "rain_chance": 5,
        }
    ]
    alerts = find_alerts("Lahore", rows, heat_c=40, rain_chance=60)
    assert alerts == ["HEAT Lahore 2026-06-01: 44 °C"]


def test_no_alert() -> None:
    """Return an empty list when temperatures and rain stay below thresholds."""
    rows = [
        {
            "date": "2026-11-22",
            "max_c": 25,
            "min_c": 12,
            "rain_mm": 0.0,
            "rain_chance": 10,
        }
    ]
    alerts = find_alerts("Islamabad", rows, heat_c=40, rain_chance=60)
    assert alerts == []
