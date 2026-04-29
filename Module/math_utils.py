def add(a,b):
    return a + b


# Đoạn này chỉ chạy khi file được chạy TRỰC TIẾP
# Không chạy khi bị import từ file khác
if __name__ == "__main__":
    print(add(3, 4))   # chỉ chạy khi: python math_utils.py