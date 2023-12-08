# We live 4680 weeks, if we could live 90 years
# So, How many weeks do I remain for living?

age = input("현재 나이를 입력해주세요 : \n")

age_as_int = int(age)

age_i_left = 52*(90-age_as_int)

print(f"90살까지 살 경우, 현재 당신은 {age_i_left} 주 남았습니다.")

age_percentage_i_lived = ((4680-age_i_left) / 4680)*100

# round()는 반올림 함수. 원하는 자리수는 ()안에 ,후 숫자로 표기.
print(f"90살까지 살 경우, 현재 당신은 {round(age_percentage_i_lived, 1)} % 살았습니다.")
