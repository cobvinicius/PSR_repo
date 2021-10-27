#!/usr/bin/python3

maximum_number = 10001

def isPrime(value):
    #print('\nChecking if ' + str(value) + ' is prime:')
    for i in range(2,value):
        remainder = value % i
        #print('Division by ' + str(i) + ' is ' + str(remainder))
        if remainder == 0:
            #print(str(value) + ' is not prime because division by ' + str (i) + ' has 0 remainder')
            return False
    return True

def main():
    #print("Starting to compute prime numbers up to " + str(maximum_number - 1))
    count = 0
    for i in range(1, maximum_number):
        if isPrime(i):
            count += 1
            print('Number ' + str(i) + ' is prime.')
        else:
            #print('Number ' + str(i) + ' is not prime.')
            pass

    #print('Between 1 and ' + str(maximum_number) + ' there are ' + str(count) + ' prime numbers')

if __name__ == "__main__":
    main()



# https://www.youtube.com/watch?v=k54xcw7RVCo&list=PLQN09mzV5mbLK9OvKQf1ZfXpPlBi461zp&index=2&ab_channel=MiguelArmandoRiemdeOliveira
