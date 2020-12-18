s = str(input())

def format(s):
    if len(s) >= 3:
        if s[-3:] != "ing":
            s += "ing"
        else:
            s += "ly"
    return s

print(format(s))