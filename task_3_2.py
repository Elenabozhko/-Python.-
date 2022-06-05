import uuid
import hashlib
import json


def hash_password(login1, password1):
    salt = uuid.uuid4().hex
    pass_hash = hashlib.sha256(salt.encode() + password1.encode()).hexdigest() + ':' + salt
    with open('passwords.json', 'r+', encoding='utf-8') as p:
        passs = p.read()
        if passs:
            pass_dict = json.loads(passs)
            pass_dict[login1] = pass_hash
        else:
            pass_dict = {login1: pass_hash}
    with open('passwords.json', 'w+', encoding='utf-8') as p:
        elem = json.dumps(pass_dict)
        p.write(elem)
    return pass_hash


def check_password(login1, user_pass):
    with open('passwords.json', 'r', encoding='utf-8') as p:
        passwords = json.loads(p.read())
        password1, salt = passwords[login1].split(':')
    return password1 == hashlib.sha256(salt.encode() + user_pass.encode()).hexdigest()


new_login = input('Введите логин: ')
new_password = input('Введите пароль: ')
hash_password(new_login, new_password)

print('Проверить пароль')
login = input('Введите логин: ')
password = input('Введите пароль: ')
if check_password(login, password):
    print('Вы ввели правильный пароль')
else:
    print('Пароль не верный')