with open ("file.txt", "w") as file:
    #doc toan bo -> 1 string
    content = file.read()

    #doc tung dong -> list cac dong
    lines = file.readlines()
    #["line 1\n", "line 2\n", "line 3\n"]

    #doc 1 dong tai 1 thoi diem - tiet kiem bo nho
    for line in file:
        print(line.strip()) #loai bo ky tu xuong dong \n