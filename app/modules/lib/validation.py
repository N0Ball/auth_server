import re

PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)[-A-Za-z\d!_@#$%^&*.=~+|?><,]{8,}$" # Minimum eight characters, at least one letter and one number with some normal special sign
USER_NAME_REGEX = r"[-a-zA-Z0-9_]{3,25}" # Only letters, numbers, '_' and '-' with 3 to 25 characters.

def validate_password(password):
    return re.fullmatch(PASSWORD_REGEX, password)

def validate_user_name(name):
    return re.fullmatch(USER_NAME_REGEX, name)

# def validate_email(email):
#     return re.fullmatch(email, EMAIL_REGEX)