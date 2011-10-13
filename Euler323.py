factorial = {0:1}
for i in range(1, 33):
    factorial[i] = factorial[i-1] * i
 
bits = 32
 
comb = lambda n, k: factorial[n] // (factorial[k] * factorial[n-k])
 
dp = {
    (0, 0) : 1
}
 
def get_value(*args):
    if args in dp:
        return dp[args]
 
    length, rem = args
    if length > 0 and rem == 0:
        return 0
    if length == 0 and rem > 0:
        return 0
    result = 0
    for i in range(bits+1):
        for overlooked in range(max(0, i-rem), min(i, bits-rem)+1):
            result += get_value(length-1, rem-i+overlooked) * ((comb(bits-rem, overlooked) * comb(rem, i-overlooked) / (2 ** bits)))
 
    dp[args] = result
    return result
 
iters = 50
 
if __name__ == '__main__':
    result = 0
    for i in range(1, iters+1):
        result += get_value(i, bits) * i
    print("The result is:", result)
