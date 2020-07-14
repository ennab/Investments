import math
balance = 5000.513
name = "Omar"
print(type(balance))
print(id(balance))
name = f" {name} {balance}"
print(name)
name = name.strip()
print(name.upper())
print(name.find("pro"))
print("Omar" in name)
print(round(balance, 2))
print(math.floor(balance))
print(f"is digit {name.isdigit()}")

if len(name) >= 100:
    print("long name")
elif math.floor(balance) != 5000:
    pass
else:
    print("yes")
print("---------------")
x = range(5, 10, 2)
print(list(x))
print("---------------")
names = ["omar", "aya"]
for name in names:
    if name.lower().startswith("o") or name.lower().startswith("a"):
        print("found")
else:
    print("not found")
print("---------------")


def sumnum(num1: int, num2: int) -> tuple:
    return (num1, num2)


total = 1
for num in sumnum(10, 20):
    total = total*num
print(total)


def save_user(user):
    print(user["name"])


investment = [{"id": 1, "name": "omar", "location":  "TX"},
              {"id": 2, "name": "omar2", "location":  "TX2"},
              {"id": 3, "name": "omar3", "location":  "TX3"}]
users = {"id": 1, "name": "omar", "location":  "TX"}
save_user(users)
print(investment[1]["name"])
print("---------------")
letters = ["a", "b", "c"]
numbers = [1, 2, 5, 3, 4, 5, 6, 7, 8, 9]
print(letters + numbers)
print(numbers[2:4:2])

for index, num in enumerate(numbers):
    print(index, num)

if 5 in numbers:
    print(numbers.index(5))
numbers.sort(reverse=True)
print(numbers)


def sort_item(item):
    return item[0]


numletter = [("d", 4), ("a", 1), ("b", 2), ("c", 3)]
# numletter.sort(key=sort_item)
numletter.sort(key=lambda item: item[0])
print(numletter)
print(list(map(lambda item: item["name"], investment)))
print({item["name"] for item in investment})
print("filtered", list(
    filter(lambda item: item["location"] == "TX", investment))[0]["id"])
for it in map(lambda item: item[0], numletter):
    print(it)
print("---------------")
list1 = [1, 2, 3]
list2 = [1, 3, 4]
print(list(zip(list1, list2)))


obj = list1.pop()
print(obj)
print(list1)
