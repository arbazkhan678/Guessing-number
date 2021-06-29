# Guessing number
while True:
    num = int(input("ENTER ANY NUMBER "))
    if num > 5:
        print("ENTER A LOWE NUMBER")
        continue
    if num < 5:
        print("ENTER A HIGH NUMBER")
        continue
    else:
        print("PERFECT NUMBER")
        break