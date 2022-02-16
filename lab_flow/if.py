x = input("Enter your birth month as a number (1=jan, 2=feb, etc.): ")

x = int(x)

if x == 0:
    answer = input("Did you mean January?").lower()
    if answer == "yes":
            x = 1
    else:
        print("Cannot proceed. Month not valid.")
        exit(1)

if not (x >= 1 and x <=12):
    print(f"{x} is not a valid month.")
    exit(1)

if x == 1:
    print("You were born in the first month of the year.")
else:
    print("You were not born in the first month of the year.")

if x == 12 or (x >= 1 and x <= 2):
    print("Winter")
elif x >= 3 and x <= 5:
    print("Spring")
elif x >= 6 and x <= 8:
    print("Summer")
elif x >=9 and x<= 11:
    print("Fall") 
