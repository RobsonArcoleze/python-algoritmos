import re

def validate_pass(password: str):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    matches = re.match(pattern, password)
    return bool(matches)


print(validate_pass("amerca1@"))