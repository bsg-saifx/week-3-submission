import re

class InvalidEmailError(Exception): 
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return self.error

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise InvalidEmailError(f"{email} is invalid")
    return True

if __name__ == "__main__":
    emails = [
        "abcd@email.com",
        "abc@.com",
        "abc@email",
        "abc@em.c"
    ]
    for email in emails:
        try:
            validate_email(email)
            print(f"{email} is valid")
        except InvalidEmailError as e:
            print(e)
