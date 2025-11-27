def computegrade(score):
    if score > 1.0 or score < 0.0:
        return "Bad score"
    if score > 0.9:
        return "A"
    elif score > 0.8:
        return "B"
    elif score > 0.7:
        return "C"
    elif score > 0.6:
        return "D"
    else:
        return "F"

s = input("Enter score: ")
try:
    sc = float(s)
    print(computegrade(sc))
except:
    print("Bad score")
