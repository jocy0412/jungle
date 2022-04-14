import sys
text = str(sys.stdin.readline().strip())
boom = str(sys.stdin.readline().strip())

for x in range(len(boom)):
    text = text.replace(boom[x],"")

if text :
    print(text)
else :
    print('FRULA')