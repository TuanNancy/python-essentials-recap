# Python list recap
# Cac vi du duoc tach rieng de de hoc va de doan ket qua.


def print_title(title):
    print(f"\n--- {title} ---")


# 1. append(): them phan tu vao cuoi list
print_title("append()")

fruits = ["apple", "banana", "cherry"]
print("Before:", fruits)

fruits.append("orange")
print("After append('orange'):", fruits)


# 2. remove(): xoa phan tu dau tien co gia tri trung khop
print_title("remove()")

fruits = ["apple", "banana", "cherry", "banana"]
print("Before:", fruits)

fruits.remove("banana")
print("After remove('banana'):", fruits)


# 3. pop(): xoa va tra ve phan tu theo index
print_title("pop()")

fruits = ["apple", "banana", "cherry", "orange"]
print("Before:", fruits)

removed_fruit = fruits.pop(2)
print("Removed by pop(2):", removed_fruit)
print("After pop(2):", fruits)

last_fruit = fruits.pop()
print("Removed by pop():", last_fruit)
print("After pop():", fruits)


# 4. Truy cap phan tu bang index
print_title("index")

fruits = ["apple", "banana", "cherry", "orange"]
print("List:", fruits)
print("fruits[0]:", fruits[0])
print("fruits[-1]:", fruits[-1])


# 5. Cat list bang slicing: list[start:stop]
# start duoc lay, stop khong duoc lay.
print_title("slicing")

fruits = ["apple", "banana", "cherry", "orange"]
print("List:", fruits)

print("fruits[0:2]:", fruits[0:2])
print("fruits[1:3]:", fruits[1:3])
print("fruits[:2]:", fruits[:2])
print("fruits[2:]:", fruits[2:])
print("fruits[:]:", fruits[:])
print("fruits[-2:]:", fruits[-2:])
