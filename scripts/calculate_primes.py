
prime_numbers = []
top_number = int(input('Please write the top value: '))

def checking_prime():
    for num in range(top_number + 1):
        if num > 1:
            for n in range(2, num):
                if num % n == 0:
                    break
            else:
                prime_numbers.append(num)
                print(prime_numbers[-1])        

def main():  
    checking_prime()
    

if __name__=="__main__":
    main()
