import random
def esély_számítás(a, b, c, d, e):
    esély1 = random.randint(1, 100)
    if esély1 < a:
        return 1
    elif a < esély1 < a+b:
        return 2
    elif a+b < esély1 < a+b+c:
        return 3
    elif a+b+c < esély1 < a+b+c+d:
        return 4
    elif a+b+c+d < esély1 < a+b+c+d+e:
        return 5
    else:
        return 6

def esély_számítás(a, b, c, d):
    esély1 = random.randint(1, 100)
    if esély1 < a:
        return 1
    elif a < esély1 < a+b:
        return 2
    elif a+b < esély1 < a+b+c:
        return 3
    elif a+b+c < esély1 < a+b+c+d:
        return 4
    else:
        return 5

def esély_számítás(a, b, c):
    esély1 = random.randint(1, 100)
    if esély1 <= a:
        return 1
    elif a < esély1 <= a+b:
        return 2
    elif a+b < esély1 <= a+b+c:
        return 3
    else:
        return 4
    
def esély_számítás(a, b):
    esély1 = random.randint(1, 100)
    if esély1 <= a:
        return 1
    elif a < esély1 <= a+b:
        return 2
    else:
        return 3

def esély_számítás(a):
    esély1 = random.randint(1, 100)
    if esély1 <= a:
        return 1
    else:
        return 2