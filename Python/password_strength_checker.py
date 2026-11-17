def check_password_strength(password):
    count=0
    if len(password)>=8:
        count += 1
    if any(c.isdigit() for c in password):
        count += 1
    if any(c.isupper() for c in password):
        count += 1
    if any(c.islower() for c in password):
        count += 1
    if any(c in "!@#$%^&*()-_=+[{]}\"|;:'\",<.>/?`~" for c in password):
        count += 1
    return count

password=input("Enter your password:")
if " " in password:
    print("Password should not contain spaces.")
else:
    strength=check_password_strength(password)
    if strength<=2:
        print("Weak password")
    elif strength<=4:
        print("Medium password")
    else:
        print("Strong password")