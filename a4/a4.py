"""	COEN 239 - assignment 4

	Name: Alexander Hadiwijaya (ahadiwijaya)
	Student ID: W1342311
"""

import math
import sys

# constant
a = pow(7, 5);
b = pow(2, 31) - 1;

# initialize
m = 10;		# number of arrivals and service times
Ta = 200;	# inter-arrival time
Ts = 100;	# service time

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
#	Calculate arrival time
##
def arrival(u):
	return (-1 * Ta) * math.log(u);

##
#	Calculate service time
##
def service(v):
	return (-1 * Ts) * math.log(v);

##
#	Waiting time of customer
##
def waiting(w, s, a):
	return max(w + s - a, 0);

##
#	Helper function to beautifully print
##
def printAns(A, S, W):
	am = A/m;
	sm = S/m;
	print("m \t sm \t\t am \t\t wm \t\t um = sm/am");
	print("%d \t %f \t %f \t %f \t %f" % (m, sm, am, W/m, sm/am));
	return;

##
#	
##
def main():
	x_n = 727633698;
	y_n = 1521138112;
	u_n = 0;
	v_n = 0;
	a_n = 0;
	s_n = 0;
	w_n = 0;
	A = 0;
	S = 0;
	W = 0;

	for i in range(m):
		u_n = utilization(x_n);
		v_n = utilization(y_n);
		a_n = arrival(u_n);
		s_n = service(v_n);
		w_n = waiting(w_n, s_n, a_n);
		# finally
		A += a_n;
		S += s_n;
		W += w_n;
		# update x and y last
		x_n = nextSeed(x_n);
		y_n = nextSeed(y_n);

	printAns(A, S, W);
	return;

if __name__ == '__main__':
	if len(sys.argv) > 1:
		m = int(sys.argv[1]);
	main();