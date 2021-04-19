#!/usr/bin/env python3

xstr = lambda s : "" if s is None else str(s)

def identifySublist(digitCharList):
    #implement your code here
    pass
  
def main():
    lst = [9, 'd', 'c', 4, 1, 2, 'b', 0, 2, 3]
    result = identifySublist(lst)
    print(xstr(result))

if __name__ == "__main__":
    main()