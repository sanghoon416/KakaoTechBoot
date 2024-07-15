# 간단한 계산기 클래스를 작성하세요. 이 클래스는 덧셈, 뺄셈, 곱셈, 나눗셈 메서드를 포함합니다.
# 사용자로부터 두 숫자와 연산자를 입력받아 계산 결과를 출력하는 프로그램을 작성하세요.

# __add__: + 연산자
# __sub__: - 연산자
# __mul__: * 연산자
# __truediv__: / 연산자

class Calculator:
    def __init__(self, num):
        if num.isdigit():
            num = int(num)
        self.num = num

    def __add__(self, other):
        return self.num + other.num
    
    def __sub__(self, other):
        return self.num - other.num
    
    def __mul__(self, other):
        return self.num * other.num
    
    def __truediv__(self, other):
        return self.num / other.num
    
c1 = Calculator(input(int))
com = input()
c2 = Calculator(input(int))

if com == '+':
    print(c1 + c2)
elif com == '-':
    print(c1 - c2)
elif com == '*':
    print(c1 * c2)
elif com == '/':
    print(c1 / c2)
else: 
    print("잘못된 입력입니다")