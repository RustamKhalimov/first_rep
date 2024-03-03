s = str(input("Input string :"))
a = True
s = s.lower()
for i in range(len(s)):
    if s[i] != s[-i - 1]:
        a = False
print(a)        