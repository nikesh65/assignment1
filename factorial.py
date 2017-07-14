num = int(raw_input())
def fact(num):
    if (num == 0 & num == 1):
        return num
    else:
        return num * fact(num-1)
