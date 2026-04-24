#cach 1: dung {}
person = {
    "name": "John", 
    "age": 30, 
    "city": "New York"
}

#cach 2: dung dict()
person = dict(name="John", age=30, city="New York")

#cach 3: tu list cac tuple
items = [("name", "John"), ("age", 30), ("city", "New York")]
person = dict(items)

#dict rong
empty = {} # hoac empty = dict()


person_example = {
    "name": "Tuan", 
    "age": 25, 
    "city": "New York"
}
# lay gia tri theo key
print(person_example["name"]) # Tuan
# neu key khong ton tai, se xay ra loi KeyError

#dung get() de lay gia tri, 
#neu key khong ton tai, se tra ve None hoac gia tri mac dinh
print(person_example.get("name")) # Tuan
print(person_example.get("country")) # None
print(person_example.get("country", "Unknown")) # Unknown

# them / sua gia tri
person_example["country"] = "USA" # them key "country" voi gia tri "USA"
person_example["age"] = 26 # sua gia tri cua key "age"

# xoa
del person_example["city"] # xoa key "city" va gia tri tuong ung
age = person_example.pop("age")
print(age) # xoa key "age" va tra ve gia tri
person_example.clear() # xoa tat ca key va gia tri, dict se tro thanh rong

infor_tuan = {"name": "Tuan", "age": 25, "city": "Hanoi"}

infor_tuan.keys() # tra ve mot dict_keys chua tat ca key
infor_tuan.values() # tra ve mot dict_values chua tat ca gia tri
infor_tuan.items() # tra ve mot dict_items chua tat ca cap (key, value) nhu tuple

# duyet qua dict
for key in infor_tuan:
    print(key, infor_tuan[key])

for key, value in infor_tuan.items():
    print(key, value)         # tương tự

# Kiểm tra key tồn tại
if "name" in person:
    print("Có")


# Hợp nhất dict (Python 3.9+)
other = {"job": "developer", "age": 30}   # age sẽ ghi đè
infor_tuan.update(other)   # cập nhật person
# hoặc: merged = person | other   (tạo dict mới)
print(infor_tuan)

#dict comprehension
squares = {x: x**2 for x in range(5)} # tao dict voi key la x va value la x^2

# Lọc
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# Đếm số lần xuất hiện của các từ trong câu
sentence = "hello world hello python"
words = sentence.split()
counter = {}
for word in words:
    counter[word] = counter.get(word, 0) + 1
print(counter)   # {'hello':2, 'world':1, 'python':1}

# Hoặc dùng collections.Counter (chuyên dụng)
from collections import Counter
print(Counter(words))