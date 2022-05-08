import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    home = list(int(input()) for _ in range(N))
    home.sort() # 1, 2, 4, 8, 9

    start = 1
    end = home[-1] - home[0] # 8
    res = 0

    while start <= end :
        dist = (start + end) // 2 # 4 설치하는 거리
        count = 1
        curr = home[0]
        for i in range(1, N):
            if home[i] >= curr + dist : # 현재위치 + 설치거리보다 같거나 크면 집의좌표가 크면 설치
                count += 1 # 공유기 설치 갯수 + 1
                curr = home[i] # 현재위치는 집 위치

        if count < M : # 설치목표 갯수보다 적게 설치했을 때
            end = dist - 1 # end 값은 설치하는 거리보다 -1
        else : # 설치 목표 갯수보다 크거나 같게 설치했을 때
            start = dist + 1 # start 값은 설치하는 값보다 + 1
            res = dist # 결과값 저장

    print(res)
main()