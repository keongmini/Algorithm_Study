import sys

input = sys.stdin.readline              # 안하면 시간초과 발생

N, M = map(int, input().split())

pokemons = dict()

for i in range(1, N + 1):
    pokemon = input().rstrip()                  # sys.stdin.readline 은 줄 끝에 개행 문자까지 포함 하기 때문에 개행 문자 제거 필수
    pokemons[str(i)] = pokemon
    pokemons[pokemon] = i

for _ in range(M):
    q = input().rstrip()
    print(pokemons[q])