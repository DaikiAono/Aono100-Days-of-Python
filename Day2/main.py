# The main function that asks the user for the total bill, tip percentage and displays the calculated tip
def main():
    print("Welcome to the tip calculator!")

    bill = float(input("What was the total bill? "))
    tip = int(input("How much tip would you like to give? 10, 12, or 15: "))
    final_bill = tip_calc(tip, bill)
    print(f'Your final bill is {final_bill:.2f}')


# This function calculates the tip and return the total bill

def tip_calc(tip, bill):
    tip_amt = 0

    if tip == 10:
       tip_amt = bill * 10 / 100

    elif tip == 12:
        tip_amt = bill * 12 / 100

    elif tip == 15:
        tip_amt = bill * 15 / 100

    calc_tip = tip_amt + bill

    return calc_tip


main()