print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

currency = bill[0]


def string_stripper(num):
    return float(num[1:])


def tip_generator(total_bill, tip_percent, num_people):
    useful_bill = float(string_stripper(total_bill))
    bill_plus_tip = useful_bill * (1 + (tip_percent / 100))
    each_pay = bill_plus_tip / num_people
    return "{:.2f}".format(each_pay)


print(f"Each person should pay {currency}{tip_generator(bill, tip, number_of_people)}")
