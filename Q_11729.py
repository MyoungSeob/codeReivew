
def hanoi(n, a, b, c):
    # a= 원래 있던 곳 b = 경유하는 곳 c = 목적지 n = 원반의 수
    
    if n == 1 : 
        print(a, c)
        # 원반이 하나만 있으면 그냥 목적지로 옮기면 끝
    else : 
        hanoi(n-1, a, c, b) 
        print(a, c)
        hanoi(n-1, b, a, c)
        # 원반이 하나 이상이면, 원래 위치에서 경유지와 목적지를 둘 다 이용해야 함.
        # 재귀함수인 'hanoi()'가 원반의 개수 당 2번씩 호출된다.

N = int(input())

total_mov = 2**N -1
print(total_mov)
hanoi(N, 1, 2, 3)