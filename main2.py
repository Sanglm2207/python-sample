def task_ex1():
    s = "Lai Minh Sang"
    x = "Codelearn.io"
    #dùng để chuyển 1 chuỗi về dạng in hoa
    print(s.upper())

    if len(s) < 2:
        print("")
    else:
        print(s[0:2] + s[-2:])

    s = x[0:2] + s[2:]
    x = s[0:2] + x[2:]

    print(s + " " + x)
    '''
     lower(): dùng để chuyển 1 chuỗi về dạng in thường
    isalnum(): dùng để kiểm tra xem một xâu có chỉ chứa các ký tự chữ và số hay không. (true/false)
     isalpha(): dùng để kiểm tra xem một chuỗi có chứa toàn các ký tự chữ không (true/false)    
    '''
#task_ex1()

def task_ex2():
    s = str(input())
    # Chuyển chuỗi s thành list
    s = s.split(" ")
    # Hàm reverse chỉ có tác dụng với list,
    s.reverse()
    # Có thể ghi là s = " ".join(s), chuyển list thành chuỗi
    # print(s)
    print(" ".join(s))  # Lúc này s trở thành chuỗi

task_ex2()


def evenNum(abc):
    ans = []
    for i in abc:
        if i % 2 == 0:
            ans.append(i)
    print(str(ans))


evenNum(abc)
