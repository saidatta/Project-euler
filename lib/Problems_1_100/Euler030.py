def power_of_digits(n, p):
    digit_sum = 0
    while n > 0:
        d = n % 10
        n = n // 10
        digit_sum = digit_sum + pow(d, p)
    return digit_sum


print(sum(n for n in range(2, 355000) if power_of_digits(n, 5) == n))


# int result = 0;
#
# for (int i = 2; i < 355000; i++) {
# int sumOfPowers = 0; int number = i;
#   while (number > 0) {
# int d = number % 10;
# number /= 10;
#
# int temp = d;
# for(int j = 1; j < 5; j++){
# temp *= d;
# }
# sumOfPowers += temp;
# }
#
# if (sumOfPowers == i) {
# result += i;
# }
# }