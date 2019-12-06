import random
import time

class Error(Exception):
  pass

class BadWordError(Error):
  pass

class DablyError(Error):
  pass

u_file = open("UserPy.txt", "a")
r_file = open("UserPy.txt", "r")
scram = False
createUser = False
correctPass = False
hang = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
verCode = ['DanieldDably', 'EOF','SOP','GFD','NIGA','DOG','MON','NIG','SOA','IGL','CHA','KRA','JOE','NOA','KYL','RAM']
badWord = ['nigger','faggot','fuck','bitch', 'nigga', 'fucker']
dably = 'dably'
words = words = ['chakra','joe','noah','dably','python','eshaan','zeroparticipation','monkey','horrible','danielddably', 'chicken','minecraft','krunker','god','sellpoints','dablymad','spritecranberry','ghost','ransom','biology','computerscience','man','sam','ashfuahisaojhahjfhafjsdhnjkncvskudhgtoeuashfoehawifhsihawofihiwhafoihajghkjashbghagaowf']

print "HANGMAN."
print "With saved usernames and scores!"
print ""
print "Type Username to Start! "
names = r_file.read().split(",")
# print "INVALID --> ",names

# GIVING USERNAME TO ACCESS POINTS
while scram != True:
  try:
    time.sleep(0.1)
    name = raw_input("Username: ")
    name = name.lower()
    cf = name
    if name in names:
      print "Hi "+name+"! Welcome back."
      print ""
      time.sleep(1)
      scram = True
    elif cf == badWord[0]:
      raise BadWordError
    elif cf == badWord[1]: # BADWORD FILTER
      raise BadWordError
    elif cf == badWord[2]:
      raise BadWordError
    elif cf == badWord[3]:
      raise BadWordError
    elif cf == badWord[4]:
      raise BadWordError
    elif cf == badWord[5]:
      raise BadWordError
    elif cf == dably: # DABLY FILTER
      raise DablyError
    else:
      bame = name+","
      u_file.write(bame)
      u_file.close()
      createUser = True     
      scram = True
  except BadWordError:
    print "BadWordError --> True Dably Army men don't use curse words."
    print ""
  except DablyError:
    print "DablyError --> Mr.Dably has rejected your name."
    print ""


      
# CREATING THE NAME OF FILE
gameRecord = name+".txt"
Password = name+"pass.txt"
userPass = open(Password, "a")
checkPass = open(Password, "r")
iPass = checkPass.read()
userFile = open(gameRecord, "a")
pFile = open(gameRecord, "r")
score = pFile.read()

# IF NEW USER, CREATE A PASSWORD.
if createUser == True:
  print
  print "New User!"
  while createUser == True:
    print ""
    time.sleep(1)
    newPass = raw_input("Create Password: ")
    confirmation = raw_input("Confirm Password: ")
    if confirmation == newPass:
      userPass.write(newPass)
      print "Password Created!"
      break
    else:
      print "Your input doesn't match your password!"
else:
  while correctPass == False:
    passw = raw_input("Password: ")
    if passw == iPass:
      print "Login Successful!"
      correctPass == True
      break
    else:
      print "Incorrect Password. If you typed the wrong username, please restart module."
      print "We cannot recover passwords if lost."
      print ""
  
# FILE PROPERTIES
if score != '':
  score_int = int(score)
else:
  score = '0'
  score_int = int(score)
OldScore = score
print name+"'s score is: "+score
print

# HANGMAN BEGINS HERE
guess = ""
word = ""
guesses = ""
print "Hello, " + name+". Everything here are from computer science class."
print "                   and the stuff that happen are sure to be funny."
print "     Lets start!"
print ""
def hangman():
  global word, guesses, guess, score_int
  time.sleep(1)
  print "Loading..."
  print ""
  time.sleep(0.5)
  word = random.choice(words)
  guesses = ''
  turns = 6
  guest = 0
  print "You Guessed: ", guest
  print hang[0]
  while turns > 0:
    try:
      failed = 0             
      for i in word:      
          if i in guesses:     
              print i,    

          else:    
              print "-",     
              failed = failed+1     
      if failed == 0:        
          print ""
          print "You got it!"
          percent = guest/2
          prize = 100/percent
          score_int += prize
          print "You guessed",guest,"times and recieved a prize of", prize,"points!!" 
          break              
      print
      guess = raw_input("guess a character:")
      print 
      guest += 1
      guesses += guess.lower()
      print "You Guessed: ", guest
      if guess not in word:

        turns -= 1
        if turns == 6:
          print hang[0]
        if turns == 5:
          print hang[1]
        if turns == 4:
          print hang[2]
        if turns == 3:
          print hang[3]
        if turns == 2:
          print hang[4]
        if turns == 1:
          print hang[5]

        print "Nope!"    
        print "You have", + turns, 'more guesses' 
        if turns == 0:
          print hang[6]
          print "The phrase was", word
      else:
        if turns == 6:
          print hang[0]
        if turns == 5:
          print hang[1]
        if turns == 4:
          print hang[2]
        if turns == 3:
          print hang[3]
        if turns == 2:
          print hang[4]
        if turns == 1:
          print hang[5]
    except KeyboardInterrupt:
      print "KeyboardInterrupt --> Sorry, we denied this interruption."
    except EOFError:
      print "EOFError --> Sorry, we denied this interruption."
  print "Type 'yes' to play again!"
  a = raw_input(">>> ")
  if a == 'yes':
    print
    hangman()
  else: # SAVING SCORE IF YOU QUIT.
    print "Your Score: ", score_int
    time.sleep(1)
    print "Saving your score..."
    time.sleep(1)
    print ""
    print "SAVED!"

hangman()

score = str(score_int)
  
# DELETE PREVIOUS SCORE 
with open(gameRecord, "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != OldScore:
            f.write(i)
    f.truncate()
# REPLACE NEW SCORE
userFile.write(score)
    
