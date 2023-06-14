import re

def suggest_password(password):
    # Define password strength criteria
    min_length = 8
    has_uppercase = re.search(r"[A-Z]", password)
    has_lowercase = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)
    has_special_char = re.search(r"[!@#$%^&*()-=_+|;':\",.<>/?\[\]{}]", password)

    # Generate suggestions based on password strength criteria
    suggestions = []
    if len(password) < min_length:
        suggestions.append(f"Increase the password length to at least {min_length} characters.")
    if not has_uppercase:
        suggestions.append("Include uppercase characters (e.g., A-Z and Special characters like ('@' ',' '$' '#' etc)).")
    if not has_lowercase:
        suggestions.append("Include lowercase characters (e.g., a-z and Special characters like ('@' ',' '$' '#' etc)).")
    if not has_digit:
        suggestions.append("Include digits (e.g., 0-9).")
    if not has_special_char:
        suggestions.append("Include special characters (e.g., !@#$%^&*).")

    return suggestions

# Simulate password events
while True:
    password = input("Enter your password: ")
    suggestions = suggest_password(password)
    if suggestions:
        print("Your password is weak. Consider the following suggestions:")
        for suggestion in suggestions:
            print("- " + suggestion)
    else:
        print("Your password is strong. Good job!")
    print()
