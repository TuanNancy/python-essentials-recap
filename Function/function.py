from audioop import avg
from math import e
import numbers


def greet():
    print("Hello, World!")

greet()


def greet_name(name):
    print(f"Hello, {name}!")
greet_name("Tuan")

def add(a, b):
    return a + b
result = add(5, 3)
print(result)

def greet_default(name="you"):
    print(f"Hello, {name}!")
greet_default()
greet_default("Tuan")

def introduce(name, age):
    print(f"{name} is {age} years old.")
introduce(age=20, name="Tuan") # introduce(name="Tuan", age=20) # Thứ tự không quan trọng

#  *args 
# cho nhiều tham số vị trí (đóng gói thành tuple).

def sum_all(*args): 
    return sum(args)

print(sum_all(1, 2, 3))  # Output: 6

# **kwargs
# cho nhiều tham số từ khóa (đóng gói thành dict).
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Tuan", age=20, city="HCM")

# hàm trả về nhiều giá trị thực chất là 1 tuple
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

min_val, max_val, total = stats([1, 2, 3, 4, 5])
print(min_val, max_val, total)


#lamda là hàm ẩn danh, thường dùng cho các hàm đơn giản, ngắn gọn.

students = [("John", 85), ("Jane", 92), ("Doe", 78)]
students_sorted = sorted(students, key=lambda x: x[1])

students_box =[
    {"name": "An", "score": 85},
    {"name": "Tuan", "score": 92},
    {"name": "Binh", "score": 78}
]

sorted_students = sorted(students_box, key=lambda x: x["score"])

for s in sorted_students:
    print(f"{s['name']}: {s['score']}")


#filter

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# --- FILTER ---
# Cũ (lambda)
even = list(filter(lambda x: x % 2 == 0, numbers))

# Mới (comprehension)
even = [x for x in numbers if x % 2 == 0]


# --- MAP ---
# Cũ (lambda)
squares = list(map(lambda x: x ** 2, numbers))

# Mới (comprehension)
squares = [x ** 2 for x in numbers]


# --- MAP + FILTER kết hợp ---
# Cũ (lambda) — bắt đầu rối
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

# Mới (comprehension) 
result = [x ** 2 for x in numbers if x % 2 == 0]