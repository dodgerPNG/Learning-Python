import time
import random
## DICE ROLLER ##
# A simple dice roller program
# made on July 29, 2024 as a 
# script to learn Python

# Welcome and menu
print("Welcome to Dice Roller! Need some RNG help? I'm here for you!")
# Roll menu
print("\nChoose from one of the options below:\n")
print("1. Flip coin (d2)")
print("2. Roll d4")
print("3. Roll d6")
print("4. Roll d8")
print("5. Roll d10")
print("6. Roll d12")
print("7. Roll d20")
print("8. See more options")
print("To exit, type 'exit'")

while True:
  #Menu prompt
  nav = input("\nEnter your main menu selection: ")
  #Menu check
  if nav in ('1', '2', '3', '4', '5', '6', '7', '8', 'menu','exit'):
    ## ROLLING DICE ##
    # Flip coin (d2)
    if nav == '1':
      print("\nReady to take a chance? Let's go!")
      time.sleep(1)
      print("Flipping your coin...\n")
      time.sleep(1)
      flip = random.randint(1,2)
      if flip == 1:
        print("You landed on Heads! Or 1, if you were looking for a number.")
      else:
        print("You landed on Tails! Or 2, if you were looking for a number.")
    # Roll d4
    if nav == '2':
      print("\nReady to take a chance? Let's go!")
      time.sleep(1)
      print("Rolling your d4...\n")
      time.sleep(1)
      roll = random.randint(1,4)
      print("Your d4 landed on", roll,"!")
    # Roll d6
    if nav == '3':
      print("\nReady to take a chance? Let's go!")
      time.sleep(1)
      print("Rolling your d6...\n")
      time.sleep(1)
      roll = random.randint(1,6)
      print("Your d6 landed on", roll,"!")
    # Roll d8
    if nav == '4':
      print("\nReady to take a chance? Let's go!")
      time.sleep(1)
      print("Rolling your d8...\n")
      time.sleep(1)
      roll = random.randint(1,8)
      print("Your d8 landed on", roll,"!")
    # Roll d10
    if nav == '5':
      print("\nReady to take a chance? Let's go!")
      time.sleep(1)
      print("Rolling your d10...\n")
      time.sleep(1)
      roll = random.randint(1,10)
      print("Your d10 landed on", roll,"!")
    # Roll d12
    if nav == '6':
      print("\nReady to take a chance? Let's go!")
      time.sleep(1)
      print("Rolling your d12...\n")
      time.sleep(1)
      roll = random.randint(1,12)
      print("Your d12 landed on", roll,"!")
    # Roll d20
    if nav == '7':
      print("\nReady to take a chance? Let's go!")
      time.sleep(1)
      print("Rolling your d20...\n")
      time.sleep(1)
      roll = random.randint(1,20)
      if roll == 1:
        print("Critical failure! Your d20 landed on", roll,"! Better luck next time.")
      if roll == 2:
        print("Your d20 landed on", roll,"! Could have been worse!")
      if 3<= roll <=9:
        print("Your d20 landed on", roll,"!")
      if roll == 10:
        print("Your d20 landed on", roll,"! Right in the middle!")
      if 11<= roll <=18:
        print("Your d20 landed on", roll,"!")
      if roll == 19:
        print("Your d20 landed on", roll,"! So close!")
      if roll == 20:
        print("Critical success! Your d20 landed on", roll,"! Well done!")
    # See more options // Expanded menu
    if nav == '8':
      print("\nMoving to the expanded menu...")
      time.sleep(2)
      print("\n----- EXPANDED MENU -----")
      print("\nWelcome to the bonus menu! Please choose from one of the options below:\n")
      print("1. Roll for percentage (d00)")
      print("2. Roll d3")
      print("3. Roll d5")
      print("4. Roll d7")
      print("5. Roll d16")
      print("6. Roll d24")
      print("7. Roll d30")
      print("8. Roll d60")
      print("9. Roll d100")
      print("0. Roll within a custom range")
      print("To return to the main menu, type 'return'")
      while True:
        # Expanded menu prompt
        expnav = input("\nEnter your menu selection: ")
        # Expanded menu check
        if expnav in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'menu','return','exit'):
          ## EXPANDED DICE ROLLING ##
          # Roll percent (d00)
          if expnav == '1':
            print("\nReady to take a chance? Let's go!")
            time.sleep(1)
            print("Calculating percent...\n")
            time.sleep(1)
            roll = random.randint(1,9)
            print("Your percentage is", roll*10,"% !")
          # Roll d3
          if expnav == '2':
            print("\nReady to take a chance? Let's go!")
            time.sleep(1)
            print("Rolling your d3...\n")
            time.sleep(1)
            roll = random.randint(1,3)
            print("Your d3 landed on", roll,"!")
          # Roll d5
          if expnav == '3':
            print("\nReady to take a chance? Let's go!")
            time.sleep(1)
            print("Rolling your d5...\n")
            time.sleep(1)
            roll = random.randint(1,5)
            print("Your d5 landed on", roll,"!")
          # Roll d7
          if expnav == '4':
            print("\nReady to take a chance? Let's go!")
            time.sleep(1)
            print("Rolling your d7...\n")
            time.sleep(1)
            roll = random.randint(1,7)
            print("Your d7 landed on", roll,"!")
          # Roll d16
          if expnav == '5':
            print("\nReady to take a chance? Let's go!")
            time.sleep(1)
            print("Rolling your d16...\n")
            time.sleep(1)
            roll = random.randint(1,16)
            print("Your d16 landed on", roll,"!")
          # Roll d24
          if expnav == '6':
            print("\nReady to take a chance? Let's go!")
            time.sleep(1)
            print("Rolling your d24...\n")
            time.sleep(1)
            roll = random.randint(1,24)
            print("Your d24 landed on", roll,"!")
          # Roll d30
          if expnav == '7':
            print("\nReady to take a chance? Let's go!")
            time.sleep(1)
            print("Rolling your d30...\n")
            time.sleep(1)
            roll = random.randint(1,30)
            print("Your d30 landed on", roll,"!")
          # Roll d60
          if expnav == '8':
            print("\nReady to take a chance? Let's go!")
            time.sleep(1)
            print("Rolling your d60...\n")
            time.sleep(1)
            roll = random.randint(1,60)
            print("Your d60 landed on", roll,"!")
          # Roll d100
          if expnav == '9':
            print("\nReady to take a chance? Let's go!")
            time.sleep(1)
            print("Rolling your d100...")
            time.sleep(2)
            print("Hold on...")
            time.sleep(2)
            print("It's really big...")
            time.sleep(2)
            roll = random.randint(1,100)
            print("\nFinally! Your d100 landed on", roll,"!")
          # Custom roll
          if expnav == '0':
            time.sleep(0.5)
            print("\nOur options aren't good enough for you, huh?")
            time.sleep(1)
            print("Alright wise guy...\n")
            time.sleep(1)
            try:
              cus1 = int(input("Enter the value of the beginning of your range: "))
              cus2 = int(input("Enter the value of the ending of your range: "))
            except ValueError:
              print("Invalid input. Please enter a valid number.")
              continue
            print("Thank you. Let's get rolling!")
            time.sleep(1)
            print("Your range is", cus1,"to",cus2)
            time.sleep(0.5)
            print("Rolling your custom range...")
            time.sleep(1)
            roll = random.randint(cus1,cus2)
            print("\nYour roll landed on", roll,"!")
          # Reprint menu
          if expnav == 'menu':
            print("Need to see the menu again? No problem!")
            time.sleep(0.5)
            print("Reloading menu...")
            time.sleep(1)
            print("Please choose from one of the options below:\n")
            print("1. Roll for percentage (d00)")
            print("2. Roll d3")
            print("3. Roll d5")
            print("4. Roll d7")
            print("5. Roll d16")
            print("6. Roll d24")
            print("7. Roll d30")
            print("8. Roll d60")
            print("9. Roll d100")
            print("0. Roll within a custom range")
            print("To return to the main menu, type 'return'")
          # Return
          if expnav == 'return':
            print("\nReturning to main menu...")
            time.sleep(2)
            # Displays main menu again before breaking
            print("\nChoose from one of the options below:\n")
            print("1. Flip coin (d2)")
            print("2. Roll d4")
            print("3. Roll d6")
            print("4. Roll d8")
            print("5. Roll d10")
            print("6. Roll d12")
            print("7. Roll d20")
            print("8. See more options")
            print("To exit, type 'exit'")
            break
          # Attempt to exit
          if expnav == 'exit':
            print("\nCannot exit from expanded menu.\nTo leave expanded menu, please type 'return'")
        else:
          print("\nInvalid input. Please try again.")    
    # Reprint menu
    if nav == 'menu':
      print("Need to see the menu again? No problem!")
      time.sleep(0.5)
      print("Reloading menu...")
      time.sleep(1)
      print("\nChoose from one of the options below:\n")
      print("1. Flip coin (d2)")
      print("2. Roll d4")
      print("3. Roll d6")
      print("4. Roll d8")
      print("5. Roll d10")
      print("6. Roll d12")
      print("7. Roll d20")
      print("8. See more options")
      print("To exit, type 'exit'")
    # Exit program
    if nav == 'exit':
      print("\nUnderstood. Exiting program in 3 seconds...\n")
      time.sleep(3)
      break
  else:
    print("\nInvalid input. Please try again.")