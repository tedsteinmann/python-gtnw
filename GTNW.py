from datetime import datetime

now = datetime.now()

#string substitution
print "Today is %s/%s/%s" % (now.month, now.day, now.year)
print "The time is now %s:%s:%s" % (now.hour, now.minute, now.second)
print "\r"


print ("Hello Jousha")
print "\r"

#Control flow: gives us this ability to choose among outcomes based off what else is happening in the program.
def question1():
	answer1 = raw_input("SHALL WE PLAY A GAME?").lower()
	if answer1 == "how about global thermonuclear war?":
		question2()
	else:
		print "HOW ABOUT A NICE GAME OF CHESS?"

def question2():
	answer2 = raw_input("WOULDN'T YOU PREFER A GOOD GAME OF CHESS?").lower()
	if answer2 == "no, let's play global thermonuclear war.":
		print("FINE")
		question3()

def question3():
	answer3 = raw_input("NUMBER OF PLAYERS?").lower()
	if answer3 == "zero" or "0":
		print("A STRANGE GAME.")
		print("THE ONLY WINNING MOVE IS")
		print("NOT TO PLAY.")

question1()

quit()