year  = int(raw_input())
if ((year%4 == 0) & (year%100 != 0)) or (year%400 == 0):
    print "entered year is leap year"
else:
    print "not leap year"