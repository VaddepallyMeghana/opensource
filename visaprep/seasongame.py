try:
    A = int(input().strip()) 
except EOFError:
    print("Invalid")  
    exit()
if 3 <= A <= 5:
    print("Spring")
elif 6 <= A <= 8:
    print("Summer")
elif 9 <= A <= 11:
    print("Autumn")
elif A == 12 or A == 1 or A == 2:
    print("Winter")
else:
    print("Invalid")
