def F(w,h):
	if w&1 and h&1: return 0
	if w<h: w,h = h,w

	r = 0
	x = 1
	while x**2 <= w*h:
		if (w*h)%x!=0 or x==h:
			x += 1
			continue
	
	        if w%(w-x)==0 or x%(x-h)==0:
	            r += 1
                    x += 1

          return r

def G(N):
    s = 0
    for w in range(1, N+1):
        for h in range(1, w+1):
            s += F(w,h)

    return s
print r,s
