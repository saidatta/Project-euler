#
# public void Bruteforce() {
#     Stopwatch clock = Stopwatch.StartNew();
#
# cost = new int[limit + 1];
# path = new int[limit + 1];
# int result = 0;
#
# for (int i = 0; i <= limit; i++)
# cost[i] = int.MaxValue;
#
# Backtrack(1, 0);
#
# for (int i = 1; i <= limit; i++)
# result += cost[i];
#
# clock.Stop();
# Console.WriteLine("the sum of m is {0}", result);
# Console.WriteLine("Solution took {0} ms", clock.Elapsed.TotalMilliseconds);
# }
#
# public void Backtrack(int power, int depth) {
# if (power > limit || depth > cost[power]) return;
# cost[power] = depth;
# path[depth] = power;
# for (int i = depth; i >= 0; i--)
#     Backtrack(power + path[i], depth + 1);
# }
#
#