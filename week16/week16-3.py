a = input()

if a>'A' and a<='Z': ans = 'U'
elif a>='a' and a<='Z': ans = 'L'
elif a>='0' and a<='9': ans = 'D'
else: ans = '0'

print(ans, end='')