import os #imports os module allowing user to directly enter commands into the host console (cmd, terminal, ect-)
import random #imports random module allowing random generated numbers and selections from list or sorts

name = "" #global variables called for the export of names to score.txt
name2 = "" 

p1 = [] #list storing player 1's information
p2 = [] #list storing player 2's information

roundc = [] #list storing the round value so 1-5 @ 5 game will end
names = ["", "Liam", "Nium", "Zachmolony", "kiddo", "bean", "grill"] #list storing usernames for authentication func
os.system("clear") #"clear" function for linux terminal use // for windows command line (cmd) use "cls"
                   #os module allows use of direct input into command line or terminal in linux based machines

def auth(): #authentication function 
    global name  #calling names from line 4,5 as a global variable so that they can be accessed and used later for read and write
    global name2
    
    print("ENTER LOGIN INFO BELOW: ") 
    name = input("USERNAME: ") #User input for "player 1" and "player 2" this username will be stored in score.txt
    name2 = input("USERNAME: ")
    if name in names and name2 in names: #decision asking if both usernames are in names which is the list made before with allowed users
        print("YOU ARE AUTHORISED!")
        os.system("clear")
        main() #running main function {not yet mentioned}
    else:
        print("INCORRECT INFORMATION")
        os.system("clear")
        auth() #if the user is not recognised then it runs authentication again 
               #this is because the user may have got the information wrong

def switch(): #switch function used to switch from main function that is called inside authentication function 
    ui = input("Press enter when ready: ") #a user input that responds to both responses of either nothing or just text (if and else)
    if ui == "": #Decision 
        os.system("clear")
        main2() #calling main2 function
    else:
        os.system("clear")
        main2() #calling main2 function


def txtdoc(name, name2): #function for text document that imports name and name2 so that it can be written to score.txt 
    if p1 > p2: #Decides if player1 (p1), is greater than player2 (p2) and if so it will output appropriate values to score.txt
        ab = sum(p1) #sum of p1 to convert it into a use-able value
        a = str(ab)  #converting p1 in the form of ab into a string(str) behind the var 
        text_file = open("score.txt", "a") #use of the "a" funtion to append to the given document in this case it is score.txt
        text_file.write(name + "'s score: " + a + "\n") #writing to the text file in order of username to "score"string and a "\n" used as newline
        text_file.close()                               #closing the file so the machine knows that it is no longer needed in this instance
    if p2 > p1: #Similar to p1>p2 exept the values are round the other way so it decides if player2 (p2) is higher than player1 (p1)
        abc = sum(p2)
        b = str(abc)
        text_file2 = open("score.txt", "a")
        text_file2.write(name2 + "'s score: " + b + "\n")
        text_file2.close()
    exit() #exit ending the process, this is one of the last functions to be called before termination
        
   
def main(): #main function used to run the first part of the game for player 1
    heythere = """
█▀▀▄ ░▀░ █▀▀▀ █▀▀▀ █▀▀█ █▀▄▀█ █▀▀
█▀▀▄ ▀█▀ █░▀█ █░▀█ █▄▄█ █░▀░█ █▀▀
▀▀▀░ ▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀░░▀ ▀░░░▀ ▀▀▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░
░█░░░░░░░░▀▄░░░░░░▄░
█░░▀░░▀░░░░░▀▄▄░░█░█
█░▄░█▀░▄░░░░░░░▀▀░░█
█░░▀▀▀▀░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
░█░░▄▄░░▄▄▄▄░░▄▄░░█░
░█░▄▀█░▄▀░░█░▄▀█░▄▀░
░░▀░░░▀░░░░░▀░░░▀░░░
    """
    roundc.append(1) #Appending to roundc which is inturn the roundcounter variable
    sumor = sum(roundc) #sumor is interpreting "roundc" and getting its sum in order to print it at the start of each round
    
    if sumor >= 5:   #If the rounds exceed the value of 5 then it will refer to the txtdoc() function to import a set of values into score.txt
        print("game over!") 
        txtdoc() #runs the text document function
    welcome = """
 █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
 █Welcome to the b1g game all you gotta do is roll█
 █A dice until you reach round five and the person█
 █with the highest score wins!                    █
 ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"""
    print(heythere, welcome) #outputting welcome string
    op = open("score.txt", "r") #opens score.txt for read purposes
    listing = op.readlines() #from score.txt reads all lines without output
    op.close #close score.txt to prevent futher changes
    lines = "▀" * 40 #string of hyphens multiplied by 40 to create a long line (for visual purposes only)
    print(" Top scores: \n", lines, "\n",listing[len(listing)-5], "\n", listing[len(listing)-4], "\n", listing[len(listing)-3], "\n", listing[len(listing)-2], "\n", listing[len(listing)-1]) #from listing variable opened before this reads given lines using len and int values

    
    g1 = random.randint(1,6) #g1, g2, g3 are all randomly generated numbers within the parameters given (1,6)
    g2 = random.randint(1,6) #on loop these values will be regenerated so it doesnt require more instances
    g3 = random.randint(1,6)
    
    print("", lines) #prints lines which is the visual created above using strings
    check = input("Press enter when ready: ")
    os.system("clear")
    print("You have rolled", g1, "and", g2, "\n") #displays what initial numbers have been rolled from g1 and g2 integers
    
    
    if g1 == g2:
        os.system("clear")
        print("ROUND: ", sumor)
        print("You have rolled a double roll again \n You have rolled: ", g3, "\n") #rolling two of the same numbers will output this  
        
    gadd = g1+g2 #"gadd" is a variable created for the sum of g1 and g2
    oe = gadd % 2 #oe is the sum of g1+g2 %2 "%" is the modulus operator // % acts as a division only checking the remainder so if its %2 has a     remainder of 0 then it is even anything else so for example 0.23 this would indicate odd.
    
    txtof = "The sum of your two numbers is:" #string values for later output 
    txtsc = "Your new score is: "
    if oe > 0: #decision if the remainder of the sum %2 is > 0 then the number has to be odd
        print(txtof, "ODD -5pt") #using string value to connect the statement, and the result loosing 5 points
        odsum = gadd - 5 #subtracting five becuase odd result
        p1.append(odsum) #appending to p1 the variable odsum
        sc = sum(p1) #sum of p1 is stored in sc variable
        print(txtsc, sc) #sc variable is now called to display to the user the current score
        switch() #running the switch function which will allow player2 to take over
    else: #this will indicate even result because the remainder must be 0 from this decision
        print(txtof, "EVEN +10pt") 
        odsum2 = gadd + 10
        p1.append(odsum2) #appending to p1 the variable odsum2
        sc2 = sum(p1) #sum of p1 is found
        print(txtsc, sc2) #output the current scores to the user
        switch() #switch function
        
def main2(): #same function as main1 with modified values to make it compatible with player2's game
    roundc.append(1)
    sumor = sum(roundc)
    print("ROUND: ", sumor)
    if sumor >= 5:
        print("game over!")
        txtdoc(name, name2)
    g1 = random.randint(1,6)
    g2 = random.randint(1,6)
    g3 = random.randint(1,6)
    print("You have rolled", g1, "and", g2, "\n")
    if g1 == g2:
        print("You have rolled a double roll again \n You have rolled: ", g3, "\n")
        
    gadd = g1+g2
    oe = gadd % 2
    
    txtof = "The sum of your two numbers is:"
    txtsc = "Your new score is: "
    if oe > 0:
        print(txtof, "ODD -5pt")
        odsumb = gadd - 5
        p2.append(odsumb)
        sc = sum(p2)
        print(txtsc, sc)
        switch()
    else:
        print(txtof, "EVEN +10pt")
        odsum2b = gadd + 10
        p2.append(odsum2b)
        sc2 = sum(p2)
        print(txtsc, sc2)
        switch()


auth() #authentication will be run first as the computer skips over all functions before they are called and auth() function is called before anything else.

#Code by "Liam Debell", Holcombe Grammar School 

