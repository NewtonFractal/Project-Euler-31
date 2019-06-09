import time
start = time.time()

def coin_sums(x):
    ways = [x] * 201
    ways[x] = 1
    for x in [1,2,5,10,20,50,100,200]:
        for y in range(x, 201):
            ways[y] += ways[y-x]
    print(ways[200])

coin_sums(0)

end = time.time()
print(end - start)