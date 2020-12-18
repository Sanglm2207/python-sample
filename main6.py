str = str(input())

# def longstr(str):
#     lst = []
#     for v in str.split(" "):
#         if len(v) > 3:
#             lst.append(v)
#         return lst

def longstr(str):
    print([i for i in str.split(" ") if len(i) > 3])

longstr(str)