#!/usr/bin/env python
# bar.py - Bennet's acceptance ratio method for free energy calculation

import sys, math

if len(sys.argv) < 4:
    print "Bennet's acceptance ratio method"
    print "usage: bar.py temperature datafile01 datafile10 [clo chi]"
    print "  datafile01 contains (U_1 - U_0)_0 in 2nd column"
    print "  datafile10 contains (U_0 - U_1)_1 in 2nd column"
    print "  (first column is index, time step, etc. and is ignored)"
    print "  clo and chi are optional guesses bracketing the solution"
    sys.exit()

if len(sys.argv) == 6:
    clo = float(sys.argv[4])
    chi = float(sys.argv[5])
else:
    clo = -50.0
    chi =  50.0
    
def fermi(x):
    return 1.0 / (1.0 + math.exp(x / rt))

def sumfermi(eng, c):
    sum = 0
    for du in eng:
        sum += fermi(du + c)
    return sum

def bareq(c):
    sum0 = sumfermi(eng01, -c)
    sum1 = sumfermi(eng10, c)
    return sum1 - sum0

def bisect(func, xlo, xhi, xtol = 1.0e-4, maxit = 20):
    if xlo > xhi:
        aux = xhi
        xhi = xlo
        xlo = aux
    if func(xlo) * func(xhi) > 0.0:
        print("error: root not bracketed by interval")
        sys.exit(2)
    for i in range(maxit):
        xmid = (xlo + xhi) / 2.0
        if func(xlo) * func(xmid) < 0.0:
            xhi = xmid
        else:
            xlo = xmid
        if xhi - xlo < xtol:
            return xmid
    return xmid

print "Bennet's acceptance ratio method"
print sys.argv[1], " K"
rt = 0.008314 * float(sys.argv[1])

eng01 = []                                # read datafiles
with open(sys.argv[2], 'r') as f:
    for line in f:
        if line.startswith('#'):
            continue
        eng01.append(float(line.split()[1]))
n0 = len(eng01)

eng10 = []
with open(sys.argv[3], 'r') as f:
    for line in f:
        if line.startswith('#'):
            continue
        eng10.append(float(line.split()[1]))
n1 = len(eng10)

ln_n1n0 = math.log(n1/n0)

print "n0 = ", n0
print "n1 = ", n1
print "ln(n1/n0) = ", ln_n1n0
print "solving..."

c = bisect(bareq, clo, chi)

sum0 = sumfermi(eng01, -c)
sum1 = sumfermi(eng10, c)
delta = math.log(sum1/sum0) + c - ln_n1n0

print "c = ", c
print "sum0 = ", sum0
print "sum1 = ", sum1
print "deltaF = ", delta

