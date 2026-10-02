"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("enter source of IP")    
value = float(input("enter failed amount of logins:"))
limit = float(input("enter total amounts of attempts:"))  


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = limit - value   
percent = (value / limit *100)
           
if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"
    print(status)
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

   # replace with your if / else (or if / elif / else)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" Failed logins: {value:>10.2f}")
print(f" Total attempts: {limit:>10.2f}")
print(f" Difference: {difference:>10.2f}")
print(f" Percentage: {percent:>10.2f}%")
print(f" Status: {status}")
print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ Run it three times with different numbers

# Failed logins:      50.00
# Total attempts:      90.00
# Difference:      40.00
# Percentage:      55.56%
# Status: OK

# Total attempts:      60.00
#Difference:      20.00
# Percentage:      66.67%
# Status: OK

#Failed logins:      80.00
#Total attempts:      80.00
# Difference:       0.00
# Percentage:     100.00%
# Status: OVER LIMIT









#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#percent = (value / limit *100)
#ZeroDivisionError: division by zero
# zero division error happens due to the limit being 0 and the percentage calculation trying to divide by zero.
#    [ ] Check every variable name says what it holds
#label, value, limit, difference, percent, status
