print("Welcom to the rollercoaster!")

height = int(input("What is your height in cm?\n"))

if (height >= 120):
    print("You can ride the rollercoaster!!!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("please pay $7.")
    elif age <= 55 and age >= 45:
        bill = 0
        print("You are Free! Enjoy!!!")
    else:
        bill = 12
        print("Please pay $12.")

    want_photos = input("Do you want a photo taken? Y or N : ")
    if want_photos == "Y":
        bill += 3
        print(f"Your final bill is ${bill}.")
else:
    print("Sorry... You can't ride that...")
