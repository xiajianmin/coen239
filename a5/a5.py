"""	COEN 239 - assignment 5

	Name: Alexander Hadiwijaya (ahadiwijaya)
	Student ID: W1342311
"""

import sys
import argparse
import math

# constant
a = pow(7, 5);
b = pow(2, 31) - 1;

# initialize
Ta = 200.0;
Ts = 100.0;
te = 10000000.0;

##
#	Calculate the next seed
#	x : xn-1 seed
##
def nextSeed(x):
	return (a * x) % b;

##
#	
#	Return: real number in the interval (0, 1)
##
def utilization(x):
	return float(x) / b;

##
#	Calculate arrival / service time
##
def expntl(T, u):
	return (-1 * T) * math.log(u);

def main():
	n = 0.0; t1 = 0.0; t2 = te; time = 0.0;
	B = s = 0.0; C = 0.0; tn = time;
	x_n = 727633698; y_n = 1521138112;

	while (time < te):
		u_n = utilization(x_n);
		v_n = utilization(y_n);
		if t1 < t2: # event 1: arrival
			time = t1; s += n * (time - tn);
			n += 1; tn = time;
			t1 = time + expntl(Ta, u_n);
			if n == 1:
				tb = time;
				t2 = time + expntl(Ts, v_n);
		else: # event 2: completion
			time = t2; s += n * (time - tn);
			n -= 1; tn = time;
			C += 1;
			if n > 0:
				t2 = time + expntl(Ts, v_n);
			else:
				t2 = te;
				B += time - tb;

		# update x and y last
		x_n = nextSeed(x_n);
		y_n = nextSeed(y_n);

	X = C / time;
	U = B / time;
	L = s / time;
	W = L / X;

	print "X \t U \t L \t W";
	print("%f \t %f \t %f \t %f" % (X, U, L, W));
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser();
	parser.add_argument("-e", "--te", help="custom period time is measured", type=int);
	parser.add_argument("-s", "--ts", help="custom service time per customer", type=int);
	args = parser.parse_args();

	if args.te:
		te = args.te * 1.0;
	if args.ts:
		Ts = args.ts * 1.0;

	main();