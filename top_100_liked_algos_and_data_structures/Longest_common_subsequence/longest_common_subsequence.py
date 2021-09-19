def lcs(x, y, m, n):
    if m == 0 or n == 0: return 0
        
    if x[m - 1] == y[n - 1]: return lcs(x, y, m - 1, n - 1) + 1;

    return max(lcs(x, y, m, n - 1), lcs(x, y, m - 1, n))

x = "ABCBDAB"
y = "BDCABA"

print(f'The length of the LCS of {x} and {y} is: ', lcs(x, y, len(x), len(y)))
 