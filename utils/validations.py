import re
from datetime import datetime
import dateparser

# Extract date from natural language query
def extract_date(text):
    date = dateparser.parse(text)
    return date.strftime("%Y-%m-%d") if date else None

# Validate email format
def validate_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email)

# Validate phone number format
def validate_phone_number(phone_number):
    pattern = r"^[1-9]\d{9}$"
    return re.match(pattern, phone_number)