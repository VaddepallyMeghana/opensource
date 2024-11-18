def count(str):
    v=set("aeiouAEIOU")
    num_v=0
    num_c=0
    for char in str:
        if char.isalpha():
            if char in v:
                num_v+=1
            else:
                num_c+=1
    return num_v, num_c
str=input().strip()
v_count, c_count=count(str)
print(f"{v_count},{c_count}")
