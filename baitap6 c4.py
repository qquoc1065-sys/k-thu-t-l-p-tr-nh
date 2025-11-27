def computepay(hours, rate):
    if hours > 40:
        regular = 40 * rate
        overtime = (hours - 40) * rate * 1.5
        return regular + overtime
    else:
        return hours * rate

h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))
print("Pay:", computepay(h, r))
