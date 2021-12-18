import hashlib


def count_sub(word):
    count = 0
    sub_set = set()
    sub_set_hash = set()
    for i in range(1, len(word)):
        sub = word[:i]
        sub_set_hash.add(hashlib.sha256(sub.encode()).hexdigest())
        sub_set.add(sub)
    for i in range(1, len(word)):
        sub = word[i:]
        sub_set_hash.add(hashlib.sha256(sub.encode()).hexdigest())
        sub_set.add(sub)
    sub_set_hash.add(hashlib.sha256(word[1:-1].encode()).hexdigest())
    sub_set.add(word[1:-1])
    return f"Количество уникальных подстрок в слове {word}: {count + len(sub_set_hash)}\n" \
           f"{sub_set}"


print(count_sub(input("Введите слово для подсчёта: ")))
