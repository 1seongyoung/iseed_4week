# 문제 3 코드
def plus(v1, v2, v3):
    result = v1 + v2 + v3
    return result
hap = plus(100,200,300)
print(hap)


# 문제 4 코드
var = 100

def f1():
    print(var)  

def f2():
    var = 10 
    print(var)

var = 100
f1()
f2()

# 문제 8 코드
def myFunc(p1=0, p2=0, p3=0):
    ret = p1 + p2 + p3
    return ret



print("매개변수 없이 호출 =>", myFunc())
print("매개변수 1개 호출 =>", myFunc(1))
print("매개변수 2개 호출 =>", myFunc(1, 2))
print("매개변수 3개 호출 =>", myFunc(1, 2, 3))



#문제 11 코드
def addNumber(num):
    if num == 1:      
        return 1
    else:
        return num + addNumber(num - 1)  

print(addNumber(100))
