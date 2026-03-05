from datetime import datetime
balance = 100
log = list()

def deposit(balance):
  depositAmount = float(input('Enter amount to deposit\nBWP'))
  balance += depositAmount
  print(f"BWP{depositAmount:.2f} has been successfully depositted into your account.")
  now = datetime.now()
  log.append(f"BWP{depositAmount:.2f} deposited on {now.strftime('%A %d %B %Y')} at {now.strftime('%H:%M')}")
  return balance

def withdraw(balance):
  checkBalance(balance)
  if balance <= 100:
    print('Insufficient funds to withdraw cash')
  else:
    approveWithdrawal = False
    while approveWithdrawal is False:
      print(f"Enter an amount to withdraw between 0 and {(balance - 100):.2f}")
      withdrawAmount = float(input())
      if balance - withdrawAmount >= 100:
        approveWithdrawal = True
        balance -= withdrawAmount
        print(f"BWP{withdrawAmount:.2f} has been successfully withdrawn from your account.")
        now = datetime.now()
        log.append(f"BWP{withdrawAmount:.2f} withdrawn on {now.strftime('%A %d %B %Y')} at {now.strftime('%H:%M')}")
        return balance
      else:
        print('Insufficient funds. Please try again\n')


def checkBalance(balance):
  print(f"Current balance: BWP{(balance):.2f}")
  print(f"Available balance: BWP{(balance - 100):.2f}")

if datetime.now().hour < 12:
  greeting = 'Good Morning'
elif datetime.now().hour > 17:
  greeting = 'Good Evening'
else:
  greeting = 'Good Afternoon'

while True:
  print(f"{greeting}. Please enter one of the following options:")
  print('1) Check Balance')
  print('2) Deposit Cash')
  print('3) Withdraw Cash')
  print('4) View transaction history')
  print('5) Exit')
  action = int(input())


  if action == 1:
    checkBalance(balance)
  elif action == 2:
    balance = deposit(balance)
  elif action == 3:
    balance = withdraw(balance)
  elif action == 4:
    if not log:
      print('No transactional history')
    else:
      for i in log:
        print(i)
  elif action == 5:
    print('Thank you for banking with ClintBanks™')
    break
  else:
    print('Invalid option. Please try again.')

  print('\n')
