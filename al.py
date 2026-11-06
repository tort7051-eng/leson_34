result = []

def divider(a, b):
    if a < b:
        raise ValueError("Перше число менше другого")

    if b > 100:
        raise IndexError("Друге число більше 100")

    return a / b

data = [
    (10, 2),(2, 5),("123", 4),(18, 0),([], 15),(8, 4),(150, 101)]

for key, value in data:
    try:
        res = divider(key, value)
        result.append(res)

    except Exception as error:
        print("Тип помилки:", type(error).__name__)
        print("Опис помилки:", error)
        print("--------------------")

print("Результат:", result)
