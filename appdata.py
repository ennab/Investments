from collections import deque
from array import array
from sys import getsizeof
from appabstract import Bond

que = deque([])
que.append(2)
que.append(5)
que.append("b")
que.popleft()
que.pop()

print(que)
# i = input("Inser Number")
print("-----------------------")
numbers = array("i", [1, 2, 3])

numbers[0] = 1
print(numbers)
numberslist = [1, 2, 1, 3, 1]
print(numberslist)
numbersset = set(numberslist)
numbersset2 = {1, 4}
print(numbersset)
print("-----------------------")
print(numbersset | numbersset2)
print(numbersset & numbersset2)
print(numbersset - numbersset2)
print(numbersset ^ numbersset2)
print("-----------------------")
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
point["y"] = 30
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
if point.get("a") == None:
    print("not exist")
del point["x"]
for key in point:
    # for llop over a dictionary will return the key
    print(key, point[key])  # and then we use the key to get the values
for key, value in point.items():
    # .items will re a tuple
    print(key, value)


values = {x: x*2 for x in range(5)}
print(values)


sentence = "Hello"
char_freq = {}
for char in sentence:
    if char_freq.get(char) == None:
        char_freq[char] = 1
    else:
        char_freq[char] += 1

char_freq_sort = sorted(
    char_freq.items(), key=lambda item: item[1], reverse=True)

print(char_freq_sort[0][0])

print("-----------------------")


def comp(val):
    return val != ""


print(comp("5"))


b = Bond()
print(b.get_balance())
