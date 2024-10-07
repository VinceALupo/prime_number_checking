# prime_number_checking
demonstrates knowledge of python.  calculates prime numbers from 2 to 5000 in an efficient way, and a less efficient way.  Compares the two.


The output of this program looks like this:


---------------------------------------------------------------

semi brute force method - checking divisibility of the number by 2, 3 and odd numbers from there

highest iteration ==  35

average iterations ==  5.238847769553911

669  primes found from 2 to 5000

---------- more optimal method...----------

more optimal method - checking only known primes is more efficient.  We can skip unprime numbers because those are divisible by primes we are already checking.

highest iteration ==  19

average iterations ==  3.7341468293658733

669  primes found from 2 to 5000

