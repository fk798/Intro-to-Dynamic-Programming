# top down - memoization
memo = {0: 0, 1: 1} # base cases included
def fib_memo(n):
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

print(fib_memo(6))
print(memo)

# bottom up - tabulation
def fib_tab(n):
    f = [i for i in range(n + 1)]
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

print(fib_tab(6)) # [0, 1, 1, 2, 3, 5, 8]

# top down is simpler to write with recursion - use memoization to store results to reduce number of recursive calls

# bottom up is difficult to write but more efficient (less storage in stack for recursive calls)

# top down = recursion, bottom up = iteration