import sys
input = sys.stdin.readline

loca = list(map(str, input().split()))

x,y,w,h = int(loca[0]),int(loca[1]),int(loca[2]),int(loca[3])

print(min(abs(x-0),abs(y-0),abs(x-w),abs(y-h)))