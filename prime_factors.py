def get_prime_factors(number):
          factors = []
          divisor = 2
          while divisor <= number:
               if number % divisor == 0:
                    factors.append(divisor)
                    number = number // divisor
               else:
                    divisor +=1
          return factors
     
def main():
    number =24
    print(get_prime_factors(number))

if __name__ == "__main__":
     main()
     