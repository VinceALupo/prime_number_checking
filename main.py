
# The testing print lines have been commented out.  
# If you want to see the program reason out prime number divisiblity, 
# feel free to uncomment some of those lines as desired.

import math


def determine_higher_iteration(current_highest, latest_iteration):
    if latest_iteration > current_highest:
        return latest_iteration
    else:
        return current_highest

def is_prime_via_semi_brute_force(num):
    if num <= 1:
        #print(num, "  NOT a prime, <= 1")
        return False, 0
    else: 
        the_sqrt = math.sqrt(num) 
        floored_sqrt = int(math.floor( the_sqrt ))
        
        if the_sqrt == floored_sqrt:
            #print(num, " NOT a prime, has an even sqrt")
            return False, 0

        # Loop from 2 to the square root of num (round down the sqrt of num if not an even sqrt)
        i = 2
        number_is_prime = True
        iteration_count = 0
       
           
        while i <= floored_sqrt:  
            iteration_count += 1
            
            # If num is evenly divisible by any number in this range then it's not prime                  
            if num % i == 0:  
                #print(num, "  NOT a prime, because", num, " %", i, " == 0     ", iteration_count, " iterations" ) # and therefore perfectly divisible by another number")
                number_is_prime = False
                return number_is_prime, iteration_count
            else:
                if i == 2: 
                    # next we will check the first odd number of relevance, 3
                    i += 1
                else:
                    # next we will check the next odd number and so on 
                    i += 2
                
        #print("                            ", num, " is prime     ", iteration_count, " iterations")
        return number_is_prime, iteration_count


known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 
227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 
359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 
431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 
577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 
733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 
887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997 ]

def is_prime_via_first_only_checking_known_primes(num):
    if num <= 1:
        #print(num, "  NOT a prime, <= 1")
        return False, 0 
    else: 
        the_sqrt = math.sqrt(num) 
        floored_sqrt = int(math.floor( the_sqrt ))
        
        if the_sqrt == floored_sqrt:
            #print(num, " NOT a prime, has an even sqrt")
            return False, 0

        # Loop from 2 to the square root of num (round down the sqrt of num if not an even sqrt)
        prime_index = 0
        i = known_primes[prime_index]
        length_known_primes = len(known_primes)
        iteration_count = 0

        number_is_prime = True

        while i <= floored_sqrt:  
            iteration_count += 1

            # If num is evenly divisible by any number in this range then it's not prime                  
            if num % i == 0:  
                #print(num, "  NOT a prime, because", num, " %", i, " == 0" ) # and therefore perfectly divisible by another number")
                number_is_prime = False
                return number_is_prime, iteration_count
            else:
                if prime_index + 1 < length_known_primes:
                    #next we will check the next known prime
                    prime_index += 1
                    i = known_primes[prime_index]
                else:
                    # if out of known primes, next we will check the next odd number and so on 
                    i += 2
                
        #print("                            ", num, " is prime")
        return number_is_prime, iteration_count


# Main function to test the prime-checking function
def main():
    
    print("---------------------------------------------------------------")
    prime_numbers = []  
    highest_iteration_count = 0                    
    average_iteration_count = 0
    total_iteration_count = 0

    # Loop through each test case and print whether it passed or failed
    for i  in range(2, 5000):
        results = is_prime_via_semi_brute_force(i)
        this_iteration_count = results[1]

        highest_iteration_count = determine_higher_iteration(highest_iteration_count, this_iteration_count)
        total_iteration_count = total_iteration_count + this_iteration_count
        average_iteration_count = total_iteration_count / i

        if results[0]:
            prime_numbers.append(i)

    #print(prime_numbers)

    print("semi brute force method - checking divisibility of the number by 2, 3 and odd numbers from there")
    print("highest iteration == ", highest_iteration_count)
    print("average iterations == ", average_iteration_count)
    print(len(prime_numbers), " primes found from 2 to 5000")


    print("---------- more optimal method...----------")
    prime_numbers = []
    highest_iteration_count = 0                    
    average_iteration_count = 0
    total_iteration_count = 0

    for i  in range(2, 5000):
        results = is_prime_via_first_only_checking_known_primes(i)
        this_iteration_count = results[1]

        highest_iteration_count = determine_higher_iteration(highest_iteration_count, this_iteration_count)
        total_iteration_count = total_iteration_count + this_iteration_count
        average_iteration_count = total_iteration_count / i

        if results[0]:
            prime_numbers.append(i)

    #print(prime_numbers)

  
    print("more optimal method - checking only known primes is more efficient.  We can skip unprime numbers because those are divisible by primes we are already checking.")  
    print("highest iteration == ", highest_iteration_count)
    print("average iterations == ", average_iteration_count)
    print(len(prime_numbers), " primes found from 2 to 5000")

# Run the main function
if __name__ == "__main__":
    main()
