# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Welcome to {location}")


# something = 123에서 "somthing"이 파라미터이고, "123"이 Argument이다. 즉 Argument는 우리가 입력한 데이터를 말하고, 파라미터는 우리가 입력한 데이터를 저장한 이름을 지칭한다.
# 정확히는 파라미터는 "함수에 전달된 데이터의 이름".
# Argument는 "그 데이터의 실제 값".
# greet_with(location=input("위치를 입력하세요. : "), name=input("이름을 입력하세요. : "))

prime_check_int_1 = int(13 / 13)
prime_check_int_2 = int(13 / 1)

print(prime_check_int_1)
print(prime_check_int_2)
