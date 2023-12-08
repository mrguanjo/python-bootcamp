# [+] Tip Calculator.
print("Welcome to the tip calculator.")

bill_total = float(input("What was the total bill? $"))

bill_split = int(input("How many people to split the bill? "))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# 아래 두 문장 이어서 출력 필요. f-sting
# 결과값 소수점 아래 한자리로 제한 필요. round(x, 2)
tip_as_pay = bill_total/bill_split*(1 + tip/100)

# tip_pay_as_float1 = round(tip_as_pay, 2)
# 150달러, 5명, 12퍼의 경우, round(x,2)를 사용해도
# 33.6이라는 소수점 아래 한자리만 표기하는데
# 아래 방색으로 소수점 두자리까지 표현 가능.
tip_pay_as_float1 = "{:.2f}".format(tip_as_pay)

# print("Each person should pay: {}".format(tip_pay_as_float1))

print(f"Each person should pay : ${tip_pay_as_float1}")
