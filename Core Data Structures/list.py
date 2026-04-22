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


#6. insert(): them phan tu vao vi tri index
print_title("insert()")

fruits = ["apple", "banana", "cherry", "orange"]
print("Before:", fruits)

fruits.insert(2, "mango")
print("After insert(2, 'mango'):", fruits)

#7. extend(): them list vao list
print_title("extend()")

fruits = ["apple", "banana", "cherry", "orange"]
print("Before:", fruits)

fruits.extend(["mango", "pineapple"])
print("After extend(['mango', 'pineapple']):", fruits)

#8. index(): tra ve vi tri cua phan tu trong list
print_title("index()")

fruits = ["apple", "banana", "cherry", "orange"]
print("List:", fruits)

print("index('banana'):", fruits.index("banana"))
print("index('cherry'):", fruits.index("cherry"))
print("index('orange'):", fruits.index("orange"))

#9. count(): dem so lan xuat hien cua phan tu trong list
print_title("count()")

fruits = ["apple", "banana", "cherry", "orange", "banana"]
print("List:", fruits)

print("count('banana'):", fruits.count("banana"))
print("count('cherry'):", fruits.count("cherry"))
print("count('orange'):", fruits.count("orange"))
print("count('mango'):", fruits.count("mango"))
print("count('pineapple'):", fruits.count("pineapple"))

#10. sort(): sap xep list
print_title("sort()")

fruits = ["apple", "banana", "cherry", "orange", "banana"]
print("List:", fruits)

fruits.sort()
print("After sort():", fruits)

fruits.sort(reverse=True)
print("After sort(reverse=True):", fruits)

#11 sorted(): sap xep list va tra ve list moi
print_title("sorted()")

fruits = ["apple", "banana", "cherry", "orange", "banana"]
print("List:", fruits)

sorted_fruits = sorted(fruits)
print("After sorted():", sorted_fruits)

sorted_fruits = sorted(fruits, reverse=True)
print("After sorted(reverse=True):", sorted_fruits)