def verify_email(email):
    if not email[0].isalpha():
        return False
    if "@" not in email or "." not in email:
        return False
    if email.count("@") != 1:
        return False
    if email.count(".") < 1:
        return False
    if email.index("@") > email.rindex("."):
        return False
    if email[-1] == "." or email[email.index(".")+1] == ".":
        return False
    
    return True

email = input("")
if verify_email(email):
    print("Valid")
else:
    print("Invalid")
