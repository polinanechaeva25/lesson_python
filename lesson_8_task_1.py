import re


def email_parse(email):
    if not email.count('.') or not email.count('@'):
        msg = f'wrong email: {email}'
        raise ValueError(msg)
    pattern = re.compile(r"(?P<username>\w+)(@)(?P<domain>\w+\.\w+)")
    check = pattern.finditer(email)
    for i in check:
        print(i.groupdict())


email_parse('polina2000_21@mail.ru')
