emails_dict = {}
email = input("Email: ")
while email != "":
    name = email.split("@")[0]
    str = " "
    name = str.join(name.split(".")).title()
    is_your_name = input("Is your name {}? (Y/n)".format(name))
    if is_your_name == 'Y' or is_your_name == 'y':
        emails_dict[email] = name
    else:
        name = input("Name: ")
        emails_dict[email] = name
    email = input("Email: ")
for item in emails_dict.keys():
    print("{0} ({1})".format(emails_dict[item], item))