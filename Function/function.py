from audioop import avg


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
