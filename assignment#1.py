#assignment1

#문제 5 풀이
ss = 'Python'
for i in range(0, len(ss)): 
    print(ss[i] + '$', end='')  


#문제 11 풀이

import re
text = "파이썬 ### CookBook $$$ @@@ 열공중 1234"

text2 = re.sub(r'[^가-힣A-Za-z]', '', text)

print(text2)


# 문제 9 
inStr, outStr = "Python", ""
strLen = len(inStr)

for i in range(strLen):
    outStr += inStr[strLen - 1-i]
print("내용을 거꾸로 출력 --> %s"% outStr)