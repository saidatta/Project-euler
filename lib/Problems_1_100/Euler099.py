from math import log

mv = 0
ml = 0
ln = 0

for e_line in open('../base_exp.txt'):
	ln+=1
	base,exp = e_line.split(',')
	value = int(exp)*log(int(base))
	if value > mv:
		mv,ml = value,ln
print(ml)
