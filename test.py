import sys
from atm_controller import Bank, Controller

if __name__ == "__main__":

    test_bank = Bank()
    test_bank.add_card(439967, 1234, "checking", 1000)
    test_bank.add_account(222444, "saving", 223)
    test_bank.add_card(95555, 7321, "checking", 24889)
    atm = Controller(test_bank, 100)
    action_list1 = [("Check Balance",0), ("Withdraw", 40), ("Withdraw", 1000), ("Deposit", 100)]

    ## Test Normal (valid)
    print (' Normal Test ')
    print (atm(95555, 7321, "checking", action_list1))

    # Test overdraft
    print (' Overdraft test ')
    print (atm(439967, 1234, "checking", action_list1))

    # Test incorrect PIN number
    print (' Incorrect PIN ')
    print (atm(95555, 1234, "checking", action_list1))
