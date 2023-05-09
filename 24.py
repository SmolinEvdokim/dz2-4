N = int(input())
a = list(map(int, input().split()))

s = []
for i in range(N):
    s.append(a[i] + a[(i-1)%N] + a[(i+1)%N])

max_s = max(s)
print(max_s)
