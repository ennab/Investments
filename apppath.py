from pathlib import Path
from time import ctime
import csv

path = Path.home()
path = Path("appdata.py")

print(path)
#path = path.with_suffix(".txt")

print(path)
path = path.absolute()
print(path)

print(ctime(path.stat().st_ctime))

with open(path.absolute(), "r") as file:
    print(file.readline())


with open("cvsfile.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["tra", "product", "qty"])
    writer.writerow([1, "phone", 100])
    writer.writerow([2, "phone2", 100])
    writer.writerow([3, "phone3", 100])

total_qty = 0
with open("cvsfile.csv", "r") as csvreadfile:
    reader = csv.reader(csvreadfile)

    for line in reader:
        if reader.line_num == 1:
            pass
        else:
            total_qty = total_qty + int(line[2])


print(total_qty)
