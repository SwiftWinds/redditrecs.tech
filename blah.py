def Solve (N, A):
    best = float("inf")
    for e in A:
        if abs(e) < best or (abs(e) == best and e > best):
            best = e
    return best
    
N = input()
A = list(map(int, input().split()))
out_ = Solve(N, A)
print (out_)