import hashlib
from uuid import uuid4

url_salt = uuid4().hex
url_1 = "url_address_1"
url_1_hash = hashlib.sha512(url_1.encode() + url_salt.encode()).hexdigest()
url_2 = "url_address_2"
url_2_hash = hashlib.sha512(url_2.encode() + url_salt.encode()).hexdigest()
url_3 = "url_address_3"
url_3_hash = hashlib.sha512(url_3.encode() + url_salt.encode()).hexdigest()
hash_dict = {"url_address_1": url_1_hash, "url_address_2": url_2_hash, "url_address_3": url_3_hash}


def url_hash_func(url):
    url_hash = hashlib.sha512(url.encode() + url_salt.encode()).hexdigest()
    c = len(hash_dict)
    if url in hash_dict:
        return f"Хеш страницы: {url_hash}"
    else:
        c += 1
        hash_dict["url_address_" + str(c)] = url_hash
        return "Страница записана в кэш"


print(url_hash_func("url_address_1"))
print(url_hash_func("url_address_2"))
print(hash_dict)
print(url_hash_func("url_address_4"))
print(url_hash_func("url_address_5"))
print(hash_dict)
