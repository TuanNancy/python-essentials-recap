# Cách thông thường
t1 = (1, 2, 3)

# Không cần ngoặc (tuple packing)
t2 = 4, 5, 6

# Tuple rỗng
t3 = ()

# Tuple 1 phần tử (cần dấu phẩy)
t4 = (42,)   # nếu không có dấu phẩy, nó là số integer 42

t = (1,1,1, 2, 3, 4, 5)
print(t)
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t[0:2])
print(t[1:3])
print(t[:2])
print(t[2:])
print(t[:])

print(t.count(1))
print(t.index(1))

print(1 in t)
print(6 in t)

#packing and unpacking
person = ("Tuan", 20, "HCM")
name, age, city = person
print(name, age, city)

###
point = (10, 20)
x, y = point
print(x, y)

###
a = 5
b = 10
a,b = b,a
print(a, b)

### Tuple có thể chứa nhiều kiểu dữ liệu
t = ("Tuan", 20, 8.5, True)
print(t)

###
t = ((1, 2), (3, 4), (5, 6))
print(t[1])
print(t[1][0])
print(t[:2])

### duyet for trong tuple
for item in t:
    print(item)

#Tuple trong hàm

def get_info():
    return "An", 20

result = get_info()
print(result)        # ('An', 20)
print(type(result))

