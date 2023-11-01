#!/usr/bin/python3
dig = 0
while dig <= 89:
    if dig % 10 == 0:
        dig += 1 + dig // 10
    if dig == 89:
        print("{:02d}".format(dig), end='\n')
    else:
        print("{:02d}".format(dig), end=", ")    
    dig += 1
