limit = int(input())
recorded = int(input())
over = recorded - limit
fine = 100 if 1<=over<=20 else 270 if 20<over<=30 else 500 if over>30 else 0
print(f"You are speeding and your fine is ${fine}." if fine!=0 else "Congratulations, you are within the speed limit!")