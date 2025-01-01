import re

# Check if the email is valid
def check_email(email: str):

    pattern = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'

    # Check if the email format is valid
    if not re.match(pattern, email):
        return {"result": False, "message": "Invalid email address."}

    return {"result": True, "message": "Email is valid."}

# Check if the password is valid
def check_password(password: str, confirm_password: str):

    # Check if the password length is less than 8 characters
    if len(password) < 8:
        return {"result": False, "message": "Password must be at least 8 characters."}

    # Compere the password and confirm password
    if password != confirm_password:
        return {"result": False, "message": "Passwords do not match."}

    return {"result": True, "message": "Password is valid."}


    

