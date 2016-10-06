# -*- coding: utf-8 -*-
"""
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.

Test Cases:
                  
	      Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09
      
                
                  
	      Test Case 2:
	      balance = 999999
	      annualInterestRate = 0.18
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 90325.03
       
       
Randomized Test Case 1
balance = 419476; annualInterestRate = 0.2
Output:
Lowest Payment: 38220.93

Randomized Test Case 2
balance = 36597; annualInterestRate = 0.15
Output:
Lowest Payment: 3262.4

Randomized Test Case 3
balance = 376302; annualInterestRate = 0.18
Output:
Lowest Payment: 33989.51

Randomized Test Case 4
balance = 399193; annualInterestRate = 0.15
Output:
Lowest Payment: 35585.66

Randomized Test Case 5
balance = 346858; annualInterestRate = 0.22
Output:
Lowest Payment: 31879.49

Randomized Test Case 6
balance = 411089; annualInterestRate = 0.22
Output:
Lowest Payment: 37782.93

Randomized Test Case 7
balance = 18254; annualInterestRate = 0.22
Output:
Lowest Payment: 1677.71

Randomized Test Case 8
balance = 240071; annualInterestRate = 0.15
Output:
Lowest Payment: 21400.88

Randomized Test Case 9
balance = 218974; annualInterestRate = 0.15
Output:
Lowest Payment: 19520.21

Randomized Test Case 10
balance = 393820; annualInterestRate = 0.21
Output:
Lowest Payment: 36039.37

@author: ibrahim
"""
def card_balance(balance, monthly_interest_rate, monthly_payment):
    for i in range(12):
        monthly_unpaid_balance = balance - monthly_payment
        balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    
    return balance
    


balance = 320000
annualInterestRate = 0.2

monthly_interest_rate = annualInterestRate / 12.0


lower_bound = balance / 12.0
upper_bound = (balance * (1 + monthly_interest_rate)**12) /12.0

payment = 0
while(True):
    payment = (lower_bound + upper_bound) / 2
    new_bal = round(card_balance(balance, monthly_interest_rate, payment), 2)
    if(new_bal < 0.1):
        upper_bound = payment
    elif(new_bal > 0.1):
        lower_bound = payment
    else:
        break
    
print("Lowest Payment:", round(payment, 2))