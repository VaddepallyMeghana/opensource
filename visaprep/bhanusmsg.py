import re
number = input().strip()
pattern_10_digits = r"^\d{10}$"
pattern_country_code = r"^\+\d{1,2} \d{10}$"
if re.match(pattern_10_digits, number) or re.match(pattern_country_code, number):

    digits = re.sub(r"[^\d]", "", number)
    if sum(map(int, digits[-10:])) > 0:
        print("Correct")
    else:
        print("Incorrect")
else:
    print("Incorrect")
