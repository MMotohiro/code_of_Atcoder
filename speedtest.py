import time
import random

N, M = map(int, input().split())    #N個の頂点のグラフ、M回ランダムアクセス
#LRD = [[random.randrange(0, N), random.randrange(0, N),random.randrange(0, N)] for i in range(M)]
LRD = [[5,5,5] for i in range(M)]
#N,M 説明
print(f"{N}x{N}配列,{M}回ランダムアクセス")
print()

# リストオンリー
if N <= 10000:
    print("リストオンリー")
    start = time.time()
    graph = [[0 for _ in range(N)] for _ in range(N)]
    elapsed_time = time.time() - start
    print(f"初期化：{elapsed_time:6f}秒")

    start = time.time()
    for L, R, D in LRD:
        graph[L][R] = D
        #graph[R][L] = -D
    elapsed_time = time.time() - start
    print(f"ランダムアクセス：{elapsed_time:6f}秒")
    print()

    print(f"{N*N}x{1}配列,{M}回ランダムアクセス")
    print("リストオンリー")
    start = time.time()
    graph = [0 for _ in range(N*N)]
    elapsed_time = time.time() - start
    print(f"初期化：{elapsed_time:6f}秒")

    start = time.time()
    for L, R, D in LRD:
        graph[L*R] = D
        #graph[R][L] = -D
    elapsed_time = time.time() - start
    print(f"ランダムアクセス：{elapsed_time:6f}秒")
    print()

    del start
    del graph
