# int sequenceLength = 0;
#
# for (int i = 1000; i > 1; i--) {
# if (sequenceLength >= i) {
# break;
# }
#
# int[] foundRemainders = new int[i];
# int value = 1;
# int position = 0;
#
# while (foundRemainders[value] == 0 && value != 0) {
# foundRemainders[value] = position;
# value *= 10;
# value %= i;
# position++;
# }
#
# if (position - foundRemainders[value] > sequenceLength) {
# sequenceLength = position - foundRemainders[value];
# }
# }


sequenceLength = 0
for i in range(1000, 1, -1):
    if sequenceLength >= i:
        break

    foundRemainders = [0] * i
    value, position = 1, 0

    while foundRemainders[value] == 0 and value != 0:
        foundRemainders[value] = position
        value *= 10
        value %= i
        position += 1

    if position - foundRemainders[value] > sequenceLength:
        sequenceLength = position - foundRemainders[value]


print(sequenceLength+1)