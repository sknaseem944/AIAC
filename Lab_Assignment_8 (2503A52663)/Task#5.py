"""Date validation and formatting."""

from datetime import datetime
import re


def validate_and_format_date(date_str):
    """Return a valid MM/DD/YYYY date as YYYY-MM-DD, or Invalid Date."""
    if not isinstance(date_str, str) or not re.fullmatch(
        r"(?:0[1-9]|1[0-2])/(?:0[1-9]|[12]\d|3[01])/\d{4}", date_str
    ):
        return "Invalid Date"

    try:
        return datetime.strptime(date_str, "%m/%d/%Y").strftime("%Y-%m-%d")
    except ValueError:
        return "Invalid Date"


# AI-generated assertion test cases
assert validate_and_format_date("10/15/2023") == "2023-10-15"
assert validate_and_format_date("02/30/2023") == "Invalid Date"
assert validate_and_format_date("01/01/2024") == "2024-01-01"
assert validate_and_format_date("02/29/2024") == "2024-02-29"
assert validate_and_format_date("13/01/2023") == "Invalid Date"

print("All date validation tests passed.")