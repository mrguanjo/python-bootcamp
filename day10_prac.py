
# def format_name(f_name, l_name):
#     """Take a fist and last name and format it 
#     to return the title case version of the name."""
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f">>> My First name is {formatted_f_name} and My Surname is {formatted_l_name}."

# format_name()
# formatted_string = format_name(f_name="yOnUnGMiN", l_name="JO")

# print(formatted_string)

# month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

# month_days[1] = 29
# print(month_days[1])

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

num1 = int(input("첫번째 숫자를 입력하세요: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("위 연산자 중 하나를 입력하세요: ")
num2 = int(input("두번째 숫자를 입력하세요: "))

calc_func = operations[operation_symbol]
answer = calc_func(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")