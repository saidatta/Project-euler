# List<BigInteger> a = new List<BigInteger>();
#
# for (int b = 2; b < 400; b++) {
#     BigInteger value = b;
# for (int e = 2; e < 50; e++) {
# value *= b;
#
# if (DigitSum(value) == b) {
# a.Add(value);
# }
# if (a.Count > 50) break;
# }
# if (a.Count > 50) break;
# }

def digits_sum(a):
    sumTotal = 0
    for i in range(len(str(a))):
        sumTotal += a // 10 ** i % 10
    return sumTotal


a = []
for b in range(2, 400):
    value = b
    for e in range(2, 50):
        value *= b
        if digits_sum(value) == b:
            a.append(pow(b, e))
        # if len(a) > 50:
        #     break
    if len(a) > 50:
        break
a.sort()
print(a[29])
