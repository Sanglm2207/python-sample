#Initial list
res = []

# Input lengths
print("Nhap do dai cuar mang:")
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    print("Nhap phan tu thu ")
    n = int(input())
    res.append(n)


def evenNum(res):
    answer = []
    for i in res:
        if i % 2 == 0:
            answer.append(i)
    print(str(answer))

evenNum(res)
