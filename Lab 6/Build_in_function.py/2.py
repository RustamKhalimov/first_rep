s = str(input("Input string :"))
upper_count = 0
lower_count = 0
for i in s: 
    if i.isupper():
        upper_count = upper_count + 1
    elif i.islower():
        lower_count = lower_count + 1
print("count_of_uppers :" , upper_count)
print("count_of_lowers :" , lower_count)             