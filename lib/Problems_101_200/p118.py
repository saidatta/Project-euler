# private int CheckPartitions(int startIndex, int prev) {
#     int count = 0;
# for (int i = startIndex; i < perm.Length; i++) { //form the number x of the digits startIndex -> i
# int number = 0;
# for(int j = startIndex; j <= i; j++){
#     number = number * 10 + perm[j];
# }
#
# //We only count ordered sets,
# //check that the current number
#                          // is larger than the previous
# if(number < prev) continue;
#
# //Check that number is prime
# if(!IsPrime(number)) continue;
#
# // No more digits so return
# if(i == (perm.Length-1)) return count + 1;
#
# count += CheckPartitions(i + 1, number);
# }
#
# return count;
# }

