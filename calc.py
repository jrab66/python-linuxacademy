#!/usr/bin/env python3.7


def calcular_dvd(hdd,tb=False):
    dvd = 4.7
    total = float(hdd)/dvd
    if tb==True:
        total=float(hdd)*1024/dvd
    if total%1!=0:
        total= total+1
    return total

def main():
    hdd = raw_input("enter size of disk: ")
    tb = raw_input(" enter 1 for tb")
    if int(tb)==1:
        tb=True
    total = int(calcular_dvd(hdd,tb))
    print(total)
main()
