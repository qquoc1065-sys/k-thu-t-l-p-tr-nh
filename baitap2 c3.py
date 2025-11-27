try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

pay = hours * rate
print("Pay:", pay)

