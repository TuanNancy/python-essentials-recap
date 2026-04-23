#set

s = {1, 2, 3}

# Thêm phần tử
s.add(4)           # {1,2,3,4}
s.add(2)           # vẫn {1,2,3,4} (không trùng)

# Xóa phần tử
s.remove(3)        # xóa 3, nếu không có sẽ báo lỗi KeyError
s.discard(5)       # xóa 5 nếu có, không có thì bỏ qua (không lỗi)
s.pop()            # xóa và trả về một phần tử bất kỳ (set không có thứ tự)
s.clear()          # xóa toàn bộ

# Kiểm tra tồn tại
if 2 in s:
    print("Có 2")


##Các phép toán tập hợp (quan trọng)
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
print(A | B)
print(A.union(B))
print(A & B)
print(A.intersection(B))
print(A - B)
print(A.difference(B))
print(B - A)
print(B.difference(A))
print(A ^ B)
print(A.symmetric_difference(B))
print(B ^ A)
print(B.symmetric_difference(A))

