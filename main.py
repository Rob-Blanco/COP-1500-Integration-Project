#Robert Blanco Integration Project COP 1500 CRN 80597
#Last edit as of 25SEP2020
#This is a simple 'Choose Your Own Adventure' style game meant to demonstrate SE fundamentals.

import time
#The first keyword, 'import', is used to import a module. The next word, 'time' is a pre-built module within Python
#According to w3schools.com, a module is a file containing a set of functions.
#The idea to utilize this module for suspense building, and aid in reading, was in Doug McNally's YouTube channel: https://www.youtube.com/watch?v=miuHrP2O7Jw&t=622s

print("Welcome and thank you for your participation!")
#Print is a function within Python that prints a message, within those parentheses and double quotes, once the program is run.
#The text within the parentheses and double quotes (those quotes can also be single quotes) is called a 'string', or string literal.
#This is the first line of text that the user will see, so I'm greeting them. And thanking them for their participation.

time.sleep(1)
#This line utilizes the time module to suspend execution for a given number of seconds. That given number being specified within the parentheses of 'time.sleep()'.

print("This is an early version of a text based 'Choose Your Own Adventure' game. Set in space and aboard a spacecraft of....currently unspecified size.")
time.sleep(1)
print("First, let's pick a name and title for your character")
time.sleep(1)

game_start = True
#I'm assigning the variable 'game_start' the boolean value of 'True'
#This will be in order to start a 'while loop' which will keep returning to an input function, which I'll specify below.

while game_start:
#This starts the loop command of 'while' which means that while 'game_start' is equal to 'True', the program will continue 'returning' here.
#Until the user completes an action which results in 'game_start' being assigned to 'False'.
#https://www.w3schools.com/python/python_while_loops.asp
#https://sites.google.com/site/profvanselow/programming/languages/python/loops?authuser=0

    introduction_choice = input("Ready to get started? Enter 1 for 'Yes' or 2 for 'No'\n")
#The '=' symbol is an assignment operator that assigns the variable of 'introduction_choice' to whatever the user inputs through the function input().
#The function 'input()', contains a prompt. Which is a string representing a default message before the input. Basically, instructions for the user.

    if introduction_choice != "1" and introduction_choice != "2":
        #AND is a python logical/boolean operator. Here, the IF conditional statement is checked both conditions of whether 'introduction_choice' is NOT equal-
        #-to BOTH (due to the AND) "1" and "2"
        print("")
        print("Sorry! That was an invalid entry. Just enter a 1 or 2. Nothing else besides the number.")
        time.sleep(1)
        print("Let's try again.")
        time.sleep(1)
        print("")
    #This is an 'if' logical condition statement that tests conditions based around the terms within it.
    # != is a comparison operator that compares whether two values are NOT equal to each other.
    #Additionally, the logical operator of 'and' is testing whether both conditions are evaluated as 'true'.
    #So, from the top. While game_start remains True, which it still is, since nothing here has changed that.
    #These lines of code are going to run these print statements and loop back.
    #Because it's 'True' that introduction_choice is not assigend 1 and 2. Meaning neither valid choice was selected and the code will loop.

    else:
    #'Else' is often paired with 'if' conditional statements, to catch any other conditions not already specified by a prior 'if' or 'elif' statement.
    #So provided the user enters a 1 or 2....

        if introduction_choice == "1":
            #Relational/conditional operator. Used in conjunction with the IF conditional statement, this is checked if the user's input is equal to "1"
            print("Great! Let's get started...")
            time.sleep(1)
            game_start = False
            #The 'if' conditional statement here gets a 'True' when it evalutes introduction_choice
            #Since a prior assignment operation assigned a 1 to introdcution_choice
            #It now runs the next three lines of code from top to bottom. Right to left.
            #Most importantly, it assigns game_start to 'False'
            #And now the 'game_start' loop is broken and the rest of the code can run.

        else:
            if introduction_choice == "2":
                print("Understood! No worries, come back any time. Should you change your mind.")
                time.sleep(1)
            quit()
            #Here, the user decides to not play.
            #I thank them for their time and the function quit() runs.
            #https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
            #There appear to be SystemExit concerns with using this function, but for now, I'll use it. And change it a further date when it becomes a concern.
            #https://stackoverflow.com/questions/73663/how-to-terminate-a-python-script

name_choice = True
while name_choice:
    user_name = input("\nPlease type a fictional last name for your character. Such as \"Williams\" but without quotes.\nType it here: ")
    #Nothing new here, except that I utilize the escape character  \n to create a new line.
    #And \" to allow for double quotes within a string, which would cause an error otherwise.

    answer_verify = input("You selected \"" + user_name + "\" as your character's last name. Is this correct? Type 1 for Yes, or 2 for No: ")
    #Within the above input function, I conduct a string operation.
    #I combine the literal string of 'You selected' with the variable 'user_name' using '+'. And then 'user_name' to the second portion of the text.
    #An input function already produces a string, so there is no need to format 'user_name'
    #More on that later.

    if answer_verify == "1":
        print("Great!")
        time.sleep(1)
        print("\"" + user_name + "\"" + " it is, then.")
        time.sleep(1)
        name_choice=False
        #Again, same 'while' to 'if' loop format as above. The user accepts their fictional last name and the loop breaks.
        #'user_name' can now be used throughout the program.
    else:
        if answer_verify == "2":
            print("Understood, let's try again.")
            time.sleep(1)
            #Python sees that name_choice still is assigned 'True' and loops back to the user_name input function.
        else:
            print("I'm sorry, that wasn't an input the program understood. Let's try again.")
            time.sleep(1)
            #Following the tree of decision making, this would be printed if the user chose something ELSE other than 1 or 2.
            #' name_choice ' is still true, and Python loops back.
            #Ideally, the program would loop back without the user having to reinput their last name.
            #Will be implemented in a future Sprint.

rank_choice = True
print("Moving on, you are playing a pilot in space.")
time.sleep(2)
print("So let's decide on a pseudo-military rank, or title.")
time.sleep(2)
#Nothing new introduced here. Just more variable assignments and print functions.

while rank_choice:
    answer_verify = input("Which sounds good?\n1. Commander\n2. Chief Warrant Officer (addressed as 'Chief')\n3. Captain\nEnter your selection here: ")
    if answer_verify != "1" and answer_verify != "2" and answer_verify != "3":
        print("")
        time.sleep(1)
        print("Sorry, that wasn't a valid input. Enter only a 1, 2, or 3 to select the rank you prefer.")
        print("")
    else:
        if answer_verify == "1":
            rank = "Commander"
            answer_verify = input("Alright, " + rank + " " + user_name + ". Does that sound good? Enter 1 for Yes or 2 for No:")
            if answer_verify != "1" and answer_verify != "2":
                print("Sorry, that wasn't a valid input. Enter just the number 1 to accept " + rank + ", or 2 to start again with rank selection.")
                print("")
                time.sleep(1)
            else:
                if answer_verify == "2":
                    print("Alright, let's go over the rank choices again.")
                    print("")
                    time.sleep(1)
                else:
                    if answer_verify == "1":
                        print("Great! " + rank + " " + user_name + " it is.")
                        rank_choice = False
                        print("")
                        time.sleep(1)

        else:
            if answer_verify == "2":
                rank = "Chief"
                answer_verify = input("Alright, " + rank + " " + user_name + ". Does that sound good? Enter 1 for Yes or 2 for No:")
                if answer_verify != "1" and answer_verify != "2":
                    print("Sorry, that wasn't a valid input. Enter just the number 1 to accept " + rank + ", or 2 to start again with rank selection.")
                    print("")
                    time.sleep(1)
                else:
                    if answer_verify == "2":
                        print("Alright, let's go over the rank choices again.")
                        print("")
                        time.sleep(1)
                    else:
                        if answer_verify == "1":
                            print("Great! " + rank + " " + user_name + " it is.")
                            rank_choice = False
                            print("")
                            time.sleep(1)
            else:
                if answer_verify == "3":
                    rank = "Captain"
                    answer_verify = input("Alright, " + rank + " " + user_name + ". Does that sound good? Enter 1 for Yes or 2 for No:")
                    if answer_verify != "1" and answer_verify != "2":
                        print("Sorry, that wasn't a valid input. Enter just the number 1 to accept " + rank + ", or 2 to start again with rank selection.")
                        print("")
                        time.sleep(1)
                    else:
                        if answer_verify == "2":
                            print("Alright, let's go over the rank choices again.")
                            print("")
                            time.sleep(1)
                        else:
                            if answer_verify == "1":
                                print("Great! " + rank + " " + user_name + " it is.")
                                rank_choice = False
                                print("")
                                time.sleep(1)

#This entire block of code is essentially a second 'while loop'. Similar to the first depicted above.
#Also, I try to utlize trailing "if" statements, so I catch all possiblities of what the user could input.
#In the hopes of preventing the program from crashing due to an invalid input.

print("And with that, " + rank + " " + user_name + ", let's take a brief step forward into the story.")
#It bears mentioning that if the variables in the above print function contained integers, they would need a str() function to format them into strings.
#As only strings can be concatonated through a string operation of '+'.

time.sleep(2)
print("The silence of space and the calm din of the cockpit surrounds you, as you're seated in the single occupant 'bridge' of the Endeavor.")
time.sleep(2)
print("The amount of human intellectual, and financial capital, that it took to bring twelve generations of your ancestors to finally crest Alpha Centauri can't be understated.")
time.sleep(2)
print("Even as you rub your eyes and shrug off any lingering drowsiness from your sleep, you look forward to another day of travel and data collection....")
time.sleep(2)
print("Even if some of the first daily tasks aren't exactly thrilling....")
time.sleep(2)
print("A screen in front of you lights up, as the ship’s AI ‘Abby’ greets you.")
#A future sprint might allow the user to specify whether 'Abby' could be an 'Arthur'. Or something unspecific.
time.sleep(2)
print("A calm feminine voice reaches out to you from a nearby display panel...")
print("")
time.sleep(2)
print("Abby: Good morning, and welcome back to the bridge, " + rank,user_name + ". The daily SITREP is due to the ISS~")
#Here I utilize a 'comma' to space the variables of 'rank' and 'user_name'
time.sleep(1)
#This stack of print functions and time.sleep functions act as a brief introduction.
print("")
print("")

dialogue_1 = True

while dialogue_1:
    dialogue_1_answer = input("Please select a dialogue option:\n1. Sure!\n2. Uh.....what's a SITREP?\n3. Abby, could we wait like....5 more minutes before you start bossing me around?\n")
    if dialogue_1_answer == "1":
        print("")
        time.sleep(1)
        print("Abby: That's the spirit " + rank + " " + user_name + "! Positivity is key during long periods of space isolation!")
        dialogue_1= False
        print("")
        time.sleep(2)
    elif dialogue_1_answer == "2":
        print("")
        time.sleep(1)
        print("Abby: Oh very funny, " + rank + "....you know all too well that SITREP stands for situational report. No procrastinating! Let's get to it~")
        dialogue_1 = False
        print("")
        time.sleep(2)
    elif dialogue_1_answer == "3" :
        print("")
        time.sleep(1)
        print("Abby: Nope! I waited until the completion of your morning coffee, as per your directives, " + rank + ". Now....the SITREP will only take a few moments....")
        dialogue_1 = False
        print("")
        time.sleep(2)
    else:
        print("")
        print("Sorry! Invalid input! Enter only a 1, 2, or 3")
        print("")
        time.sleep(2)

#The above section of code is a much simpler version of the prior two 'while' loops
#Here, this combines IF, ELIF, and ELSE conditional statements together. IF has already been defined
#ELIF is another conditional statement. And is short of ELSE IF. ELIF, when used between a IF and ELSE -
#- conditional statement, is essentially the bridge that connects their logic. The initial IF statement is the-
#- first premise. The ELIF's have all subsequential arguements/conditions. Ideally, the ELSE will take care of any
#- remaining outlying possibilities.


#I utilized the 'Elif' keyword which is Pythons way of saying "if the previous condition(s) were not true, then try this condition.
#I finish it off with an 'Else' statement, which isn't required. But since Else statements can only go at the end of the logical condition branch,
# I put it there because it's easier for me to proofread/debug. Knowing that this is the end of that section.


print("You rotate your chair to a nearby computer console and log into it.....")
time.sleep(2)
print("")

#The below variable assignments are important for the next function that the user will have to perform

days_abroad = 256
#Simply an assignment for the ship's period of 'days abroad. As of yesterday, in the fictional storyline.

days_abroad_n_plus_one = days_abroad + 1
#An assignment which performs an addition of '1' via the addition operator '+' which will display total days abroad, as of today, in the storyline.

current_julian_date = 210
current_julian_date += 1
#Similar as the prior addition operation, but demonstrates the += addition shortcut operator.
#Certain organizations utilize julian dates, particularly in the goverment sector. So I figured I would try implementing it's usage.

prior_day_fuel = 490320
prior_day_fuel_usage = 320
current_day_fuel = prior_day_fuel - prior_day_fuel_usage
#Two lines of assignment into a subtraction operation via the subtraction operator '-'.
#This is intended to display today's current fuel level (490000) after 'prior_day_fuel_usage' 320 has been subtracted from prior_day_fuel level '490320'.

fuel_percent_usage = ((current_day_fuel - prior_day_fuel) / prior_day_fuel)
#This is a calculation for percentage change in fuel levels via a subtraction operator. There is also a division operator '/', or back slash, used in this line of code.
#The formula is (new amount - old amount) / old amount. Don't forget the parenthesis
#The same rules of order of operations, as within mathematics, apply here.

days_fuel_remaining = current_day_fuel // prior_day_fuel_usage
#Here, I use a floor division arithmetic operator '//' as I only want to know the integer amount result of the division.
#Not the remainder
#Basically, we're not interested in knowing a number like 30.2345 days of fuel remaining.
#We just want to know there's 30 days of fuel remaining, for the sake of brevity.

prior_day_expendables_level = 12984
prior_day_expendables_level_usage = 984
current_expendables_level = prior_day_expendables_level - prior_day_expendables_level_usage
organic_storage_percentage_change = (current_expendables_level - prior_day_expendables_level ) / prior_day_expendables_level
approx_expendables_remaining = current_expendables_level // prior_day_expendables_level_usage
#Similar to the prior block of variables, assignments, and arithmetic operators.
#This does the same except for expendables. Or a generic term for food.


current_year = 2116
current_solar_battery_levels=10
gamma_ray_shielding=25
#Assignments which are utilized to show the modulus and multiplication operator
#More on that further in the code


SITREP = True
while SITREP:
    print("")
    print("The panel reads as follows....")
    print("")
    time.sleep(2)
    print("Reconnaissance and Science Vessel Endeavor - Logistics and Communications Panel")
    print("Main Menu:")
    time.sleep(2)
    print("1. Send automated SITREP and recharge daily defensive measures.")
    time.sleep(2)
    print("2. Display a brief summary of yesterday's expendable metrics.")
    time.sleep(2)
    print("3. Log out.")
    time.sleep(2)
    #All of this is my attempt to help the player visualize what the computer panel is listing off
    log_computer_input = input("\nPlease select an option: ")
    if log_computer_input != "1" and log_computer_input != "2" and log_computer_input != "3":
        #An example of a relational/comparison operator. "!=" means not equal to. Here, if the user enters anything other than input that's NOT EQUAL to-
        #- "1" "2" or "3", there are given a response to re-enter a valid input.
        print("The console gives an error tone and asks for a valid input....")
        #A more "narrative driven" user input validation. The character in game receives an error tone, and subsequently the player.
        time.sleep(1)
        print("")
        #input validation
    else:
        if log_computer_input == "3":
            print("")
            time.sleep(1)
            print("As you try to log out of the computer, you hear Abby chime in.....")
            time.sleep(2)
            print("Abby: " +rank + ", I've already automated the metrics for the SITREP. Just log back in and select the first option....please?")
            time.sleep(2)
            print("")
            #Basically, the ship's AI is nagging you back into sending the SITREP.
        else:
            if log_computer_input == "2":
                print("")
                print("Now compiling summary....")
                time.sleep(2)
                print("Days Abroad: " + str(days_abroad_n_plus_one) + "\nCurrent Fuel Levels: " + str(current_day_fuel) + "\nCurrent Food Storage Amount: " + str(current_expendables_level))
                print("")
                time.sleep(2)
                #Just a much simpler version of the report
            else:
                if log_computer_input == "1":
                    print("SITREP " * 5)
                    time.sleep(2)
                    #An example of string multiplication. The literal string 'SITREP' is displayed five times. The scrolling SITREP is meant to simulate a report banner.
                    print("Current Julian Date: " + str(current_julian_date))
                    #I have to format the interger value of 'current_julian_date' to be a string. In order to before the string operation of '+'
                    print("Days Abroad: " + str(days_abroad_n_plus_one) + "\nCurrent Fissile Fuel Levels: " + str(current_day_fuel))
                    print("Current Fissile Percentage Change From Last Report: ", format(fuel_percent_usage, '.4f'), "%" )
                    #Here, I utilize the format function to force the percentage value to only read off 4 decimal places
                    time.sleep(2)
                    print("Days of fuel remaining: " + str(days_fuel_remaining))
                    print("Current Food Expendable Levels: " + str(current_expendables_level))
                    print("Current Expendable Percentage Change From Last Report: ", format(organic_storage_percentage_change, '4f'), "%")
                    print("Diverting solar energy capacitance. Total energy reserves: " + str(current_solar_battery_levels**2))
                    #An example of the exponential multiplication arithmetic operator '**'.
                    time.sleep(2)
                    print("Gamma Ray Shielding Levels: " + str(gamma_ray_shielding *4))
                    #An example of a multiplication arithmetic operator '*'.
                    print("Current year is: " + str(current_year))
                    print("Current year divided by 4 has a remainder of...." + str(current_year % 4))
                    #An example of a modulus arithmetic operator '%' in use.
                    #When the program is executed, Python will divide the current year by 4.
                    #There are no logical conditions evaluating this.
                    #This is simply meant to read, when the program is executed.
                    #That the current year, divided by 4, has no remainder. And will be printed out as 'zero'
                    print("Thus, ISS, congratulations on making it to a Leap Year!")
                    #This is just the main character putting a random bit of flair into their report.
                    #A more creative and novel use of modulus will be used in a future sprint.
                    time.sleep(2)
                    print("Nothing else significant to report.")
                    print(rank + " " + user_name + " out.")
                    time.sleep(1)
                    print("Now returning to main menu...")
                    time.sleep(1)
                    SITREP=False


def communications_array(num):
    access_card = num
    leave_room = False
    print("You step into the communication's array")
    while not leave_room:
    #The usage of the "Not" operator means the while loop will continue while the operand is false
        user_choice = int(input("Please make a selection:\n1.Start pinging the drones, as Abby requested. 2. Head back to the cockpit\n"))
        if access_card == 1 and user_choice == 1:
            list_elements = open('elements.txt')
            for index in range(1,7):
            #From left to right, in this statement. The FOR loop will iterate over a sequence, which is a list called 'elements.txt'
            #The IN statement specifies that the FOR loop pertains to the range function, where I know the list ends at entry six
            #The range() function will return a sequence of numbers, within the specified parameters. Here, it will start at 1. And run until 7.
                list_off= list_elements.readline()
                print(str(index) + ". ",list_off)
                leave_room = True


        elif access_card == 2 and user_choice ==1:
            print("Wait, you don't have the access card. Head back to the cockpit and retrieve it")

        elif user_choice == 2:
            leave_room = True
            cockpit()
        else:
            print("Invalid input")



def cockpit():
    access_card = 0
    leave_room = True
    obtain_card = False
    while leave_room:
        user_choice=int(input("Make a selection:\n1. Head to the communications array\n2. Grab your common access card\n"))
        if user_choice < 1 or user_choice > 2:
        #The '>' and '<' comparison operators are greater than and less than, respectively . Both those conditions are identifying any user input that isn't "1" or "2"
        #The Boolean operator "or" is used to state that either of those prior statements will result in the while loop.
            print("That isn't an option. Please select either 1 or 2")
        elif user_choice == 2 and obtain_card == False :
            print("Obtained common access card!")
            obtain_card = True
        elif user_choice == 2 and obtain_card == True:
            print("You already did that!")
        elif user_choice == 1 and obtain_card == True:
            print("You head to the communication's room")
            leave_room = False
            communications_array(1)
        elif user_choice == 1 and obtain_card == False:
            print("You head to the communication's room")
            leave_room = False
            communications_array(2)



print("Abby: Great job! Alright " + rank + " " + user_name + " , let's move on. Today's an exciting day! We're finally within communication's reach of the drone package that was fired to Proxima B almost 20 years ago!")
print("Make sure to grab your Common Access Card and head to the communications array. I'll see you there!")
print("And with that, the AI disappeared from your display. Most likely to check some other systems while you head to the communications room")
print("Select your next choice:")
cockpit()


print("That's it for now...more to come! Thank you for playing!")
#Ideas for improvement:
#Creating input validation during the rank choice segment that doesn't have to loop all the way back through the program given invalid input
#Trying to find a better and more streamlined way to not have repetitive blank print statements.
#Finding a better way to have scrolling text with loops. So that the scrolling text doesn't become TOO repetitive given mistaken input