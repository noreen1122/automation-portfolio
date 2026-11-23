def to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    return (celsius * 9/5) + 32

assert to_fahrenheit(0) == 32
# Exercice 2

def week_stats(temp):
    """
    Returns a dictionary with the average, minimum, and maximum temperature for a week.
    """
    return {
       max(temp), min(temp), round(sum(temp) / len(temp), 1)
    }
assert week_stats([20, 22, 19, 21, 23, 18, 20]) == { 23,  18,  20.4}
# Exercice 3
population= {
"Karachi": 20_000_000,
    "Lahore": 13_000_000,
    "Faisalabad": 3_700_000,
    "Rawalpindi": 3_300_000,
}
def big_cities(population, limit = 5_000_000):
    """
    Returns a list of cities with a population greater than the limit.
    """
    return [city for city, pop in population.items() if pop > limit]

assert big_cities(population) == ["Karachi", "Lahore"]

#  exercise 4

leads = [
    {"name": "Ayesha Khan", "city": "Lahore", "budget": 8_500_000, "phone": "0300-1234567"},
    {"name": "Bilal Ahmed", "city": "Karachi", "budget": 3_200_000, "phone": "+92 321 7654321"},
    {"name": "Sana Malik", "city": "Lahore", "budget": 12_000_000, "phone": "923331112223"},
]
from collections import Counter
import json

def count_cities(leads):
    """
    Returns a dictionary with the count of leads per city.
    """
    city_count = {}
    for lead in leads:
        city = lead["city"]
        city_count[city] = city_count.get(city, 0) + 1
    return city_count
assert count_cities(leads) == {"Lahore": 2, "Karachi": 1}

# Exercise 5
def premium_names(leads, min_budget=5_000_000):
    """
    Returns a list of names of leads with a budget greater than or equal to min_budget.
    """
    return [lead["name"].upper() for lead in leads if lead["budget"] >= min_budget]

assert premium_names(leads) == ["AYESHA KHAN", "SANA MALIK"]

# Exercise 6
leads= {"name": "Ayesha Khan", "phone": "0300-1234567"}
import json
def read_leads(text):
    """"" perses a JSON string of leads and return (name, phone).
    """
    leads = json.loads(text)
    return [(lead["name"], lead["phone"]) for lead in leads]
assert read_leads('[{"name": "Ayesha Khan", "phone": "0300-1234567"}]') == [("Ayesha Khan", "0300-1234567")]

#exercise 7

import re

def normalize_phone(phone):
    """
    Normalize a phone number to the format +92XXXXXXXXXX.
    """
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)
    
    # Check if the number starts with '0' or '92'
    if digits.startswith('0'):
        digits = '92' + digits[1:]  # Replace leading 0 with 92
    elif not digits.startswith('92'):
        digits = '92' + digits  # Add 92 if it doesn't start with 92
    
    return '+' + digits

assert normalize_phone("0300-1234567") == "+923001234567"

#exercise 8


def save_and_load(leads, path):
    """Write leads to JSON, read them back, and assert equality."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(leads, f, indent=2, ensure_ascii=False)

    with open(path, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    assert loaded == leads
    return loaded


reloaded_leads = save_and_load(leads, "leads.json")
assert reloaded_leads == leads

# Exercise 9

# 9. Merge defaults with user overrides
def merge_settings(defaults, user):
    merged = defaults.copy()
    merged.update(user)
    return merged
assert merge_settings({"theme": "light", "language": "en"}, {"language": "fr"}) == {"theme": "light", "language": "fr"}


# 10. Format amount as 'PKR 1,500,000'
def format_pkr(amount):
    return f"PKR {amount:,}"
assert format_pkr(1500000) == "PKR 1,500,000"


print("Day 2 completed: All assertions passed!")