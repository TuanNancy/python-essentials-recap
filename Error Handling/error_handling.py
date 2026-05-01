from unittest import result


numbers = [1, 2, 3, 4, 5]
try:
    print(numbers[10])  # This will raise an IndexError
except IndexError:
    print("Index khong ton tai")


def chia(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print ("Khong the chia cho 0")
    except TypeError:
        print ("Cac gia tri phai la so")
    except Exception as e:
        print(f"Co loi xay ra: {e}")
    else:        
        return result

chia(10, 2)     # 5.0
chia(10, 0)     # Không chia được cho 0!
chia(10, "a")   # Sai kiểu dữ liệu!
