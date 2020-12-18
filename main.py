# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    print("Nhap 1 so di ban ei")
    n = int(input())
    answer = 0

    for i in range(1, n + 1):
        answer += i / (i + 1)
        print(round(answer, 6))


def print_list():
    print("Do dai list:")
    n = int(input())
    lst = []
    for i in range(n):
        print("Phan tu thu ")
        lst.append(int(input()))
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    print(min_value)


#print_hi()
print_list()