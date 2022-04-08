

BONUS_RATE = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = show_bonus(gross_pay)
    print('Salary ${:,.2f},\nBonus: ${:,.2f}'.format(gross_pay, bonus))
    total_pay = gross_pay+bonus
    print("Total pay: ${:,.2f}".format(total_pay))
def show_bonus(gross):
    return gross*BONUS_RATE
    
if __name__ == "__main__":
    main()
    
    


