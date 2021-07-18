import re

PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)[-A-Za-z\d!_@#$%^&*.=~+|?><,]{8,}$" # Minimum eight characters, at least one letter and one number with some normal special sign
# EMAIL_REGEX = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$" # Used in ASP.NET by the RegularExpressionValidator.
CONTAINER_REGEX = r"^[a-z][a-z0-9_]{3,8}$" # Only lowercase character, number and '_' without number as the first letter and with 3 to 8 characters.
USER_NAME_REGEX = r"[-a-zA-Z0-9_]{3,25}" # Only letters, numbers, '_' and '-' with 3 to 25 characters.

def validate_password(password):
    return re.fullmatch(PASSWORD_REGEX, password)

def validate_user_name(name):
    return re.fullmatch(USER_NAME_REGEX, name)

def validate_container_name(ct_name):
    return re.fullmatch(CONTAINER_REGEX, ct_name)

# def validate_email(email):
#     return re.fullmatch(email, EMAIL_REGEX)