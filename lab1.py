
import numpy as np


def Menu():
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Bài 1")
            array = [1, 2, 3, 4, 5, 6, 12, 8, 9]
            trungbinhcong = np.mean(array)
            print("Mảng cần tính: ",array)
            print("Trung bình cộng của dãy số: ",round(trungbinhcong,2))

        elif choice == 2:
            print("Bài 2")
            vector = np.array([1,2,3,4,5,6,7,8,9])
            sum = np.sum(vector)
            print("Mảng cần tính: ", vector)
            print("Tổng số của mảng 1 chiều: ",sum)

        elif choice == 3:
            print("Bài 3")
            vector1 = np.array([[1,2,3],
                                [4,5,6]])
            sum1 = np.sum(vector1[:,0])
            print("Mảng cần tính: ")
            print(vector1)
            print("Tổng của cột: ",sum1)

        elif choice == 4:
            print("Kết thúc!")
            break

        else:
            print("Lỗi")

Menu()





