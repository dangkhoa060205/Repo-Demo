# hello.py - File mẫu để thực hành lab
from datetime import datetime


def greet(name):
    return f"Xin chào, {name}!"


def main():
    name = input("Nhập tên của bạn: ")
    print(greet(name))
    print("Thời gian hiện tại:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


if __name__ == "__main__":
    main()
