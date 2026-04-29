with open ("file.txt", "w") as file:
    #doc toan bo -> 1 string
    content = file.read()

    #doc tung dong -> list cac dong
    lines = file.readlines()
    #["line 1\n", "line 2\n", "line 3\n"]

    #doc 1 dong tai 1 thoi diem - tiet kiem bo nho
    for line in file:
        print(line.strip()) #loai bo ky tu xuong dong \n

# ghi gile
# "w" — ghi mới, XÓA nội dung cũ
with open("output.txt", "w") as f:
    f.write("Dòng đầu tiên\n")
    f.write("Dòng thứ hai\n")

# "a" — ghi tiếp, GIỮ nội dung cũ
with open("output.txt", "a") as f:
    f.write("Dòng bổ sung\n")  


    ########## Làm việc với CSV — rất phổ biến

import csv
# đọc file CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # mỗi row là một list
# ghi file CSV
students = [
    {"name": "An", "score": 9.0},
    {"name": "Tuan", "score": 7.0},
]
with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()   # ghi dòng tiêu đề
    writer.writerows(students)


# làm việc với file JSON
import json
# đọc file JSON
with open("data.json", "r") as f:
    data = json.load(f)  # data là một dict hoặc list tùy cấu trúc JSON
    print(data["name"])

# ghi file JSON
person = {"name": "An", "age": 20, "city": "Hanoi"}

with open("data.json", "w") as f:
    json.dump(person, f, indent=4)  # indent=4 để format đẹp

# kiem tra file ton tai truoc khi doc
import os

if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        data = json.load(f)
        print(data)
else:
    print("File không tồn tại.")