# List<int> p = new List<int>();
# p.Add(1);
#
# int n = 1;
# while(true){
# int i = 0;
# int penta = 1;
# p.Add(0);
#
# while (penta <= n){
# int sign = (i % 4 > 1) ? -1 : 1;
# p[n] += sign * p[n - penta];
# p[n] %= 1000000;
# i++;
#
# int j = (i % 2 == 0) ? i / 2 + 1 : -(i / 2 + 1);
# penta = j * (3 * j - 1) / 2;
# }
#
# if (p[n] == 0) break;
# n++;
# }
#


p = [1]
n = 1
while True:
    i, penta = 0, 1
    p.append(0)

    while penta <= n:

        # coin partitions are pentagonal numbers.
        # https://en.wikipedia.org/wiki/Partition_(number_theory) Integer Partitions
        # p(n) = p(n – 1)  + p(k – 2) – p(k – 5) – p(k – 7) + p(k – 12) + p(k – 15) – p(k – 22)…
        # where p(0) = 1 and p(n)  = 0 for n < 0.
        sign = -1 if (i % 4 > 1) else 1
        p[n] += sign * p[n - penta]
        p[n] %= 1_000_000
        i += 1

        # The sequence to use are the generalized pentagonal numbers which are given on the form f(k) = k(3k-1)/2 for
        # both negative and positive k.  This can be written as a positive sequence of integers m=1,2,3,…. such that
        j = i // 2 + 1 if (i % 2 == 0) else -(i // 2 + 1)
        penta = j * (3 * j - 1) // 2

    if p[n] == 0:
        break
    n += 1

print(p)