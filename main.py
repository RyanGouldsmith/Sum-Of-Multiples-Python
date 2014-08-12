#!/usr/bin/python 
def main():
    #the total to be added up
    total = 0
    n = 0
    #the limit which you want it to be
    CONST_LIMIT = 1000
    #list of multiples
    list_multiples = [3, 5]
    while (n < CONST_LIMIT):
        #checks to see if it is a multiple
        if any (n % i == 0 for i in list_multiples):
            #total the numbers
            total += n 
        n += 1
    #print the total value
    print(total)

if __name__ == "__main__":
    main()
