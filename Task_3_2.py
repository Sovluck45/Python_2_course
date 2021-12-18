from uuid import uuid4
import hashlib

db_dict = {"user": ()}
salt = uuid4().hex
password = input("Введите пароль: ")
res_hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
print(f"В базе данных хранится строка: {res_hash}")
db_dict["user"] = res_hash
password_check = input("Введите пароль ещё раз для проверки: ")
check_res_hash = hashlib.sha256(salt.encode() + password_check.encode()).hexdigest()
if check_res_hash == db_dict.get("user"):
    print("Вы ввели правильный пароль")
else:
    print("Вы введи неправильный пароль")
