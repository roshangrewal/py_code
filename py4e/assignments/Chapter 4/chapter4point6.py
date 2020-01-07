def computepay(h,r):
	if h <= 40:
		gross = h * r
	else:
		gross = (40 * r) + (r * 1.5 * (h - 40) )
	return gross

hrs = input("Enter Hours:")
ho = float(hrs)
rate = input("Enter Rate: ")
ra = float(rate)
p = computepay(ho,ra)
print (p)
