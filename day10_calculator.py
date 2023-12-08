from calculator_art import logo
# Add
def add(n1, n2):
    return n1 + n2
# Subtract
def subtract(n1, n2):
    return n1 - n2
# Multiply
def multiply(n1, n2):
    return n1 * n2
# Divide
def divide(n1, n2):
    return n1 / n2
operations = {"+": add,
              "-": subtract,
              "*": multiply, 
              "/": divide 
              }

def calculator():
    print(logo)
    num1 = float(input("첫번째 숫자를 입력하세요: "))
    for symbol in operations:
        print(symbol)
    wanting_continue = True
    while wanting_continue:
        operation_symbol = input("연산자를 입력하세요: ")
        num2 = float(input("다음 숫자를 입력하세요: "))

        calc_func = operations[operation_symbol]
        answer = calc_func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        conti = input("이어서 계산하시겠습니까? (y/n): ").lower()
        if conti == "n":
            wanting_continue = False
            ask = input("완전히 종료하시겠습니까? (y/n): ").lower()
            if ask == "y":
                exit()
            elif ask == "n":
                calculator()
        elif conti == "y":
            num1 = answer

calculator()