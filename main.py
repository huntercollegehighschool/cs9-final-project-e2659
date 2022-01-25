"""
Name(s): Chelsea Zhou, Alyosha Vak
Name of Project: 46 MINUTES TO MIDNIGHT
"""

#Write the main part of your program here. Use of the other pages is optional.

from random import choice
import time
import sys
from random import randrange

global walkietalkie
walkietalkie = 0

def start():
  print("You awake in a concrete prison cell with a mild headache. You struggle to recall your name.")
  cell()

def cell():#starting cell
  choice1 = str.upper(input("> Enter E to explore, D to test the door, or W to wait.\n> "))
  if choice1 == "W":
    print("It is unwise to remain idle in an unfamiliar environment.")
    print("It may only be your imagination, but the walls appear to be closing in on you...?")
    crushed()
  elif choice1 == "E": 
    print("You examine the room. You note the discolored concrete cell walls, a small cot in the left corner of the cell, and a bowl with a spoon on the floor.")
    explore()
  elif choice1 == "D": 
    print("The door is wrought from stainless steel and does not have a doorknob. You lean against it with the weight of your body, although it does not budge. The steel feels cool against your feverish skin.")
    cell()
  else:
    none()

def crushed(): #crushed death with broken crush counter
  print("You are crushed to death.")
  #crush counter broken (sad)
  restart()

def explore():#explore starting cell
  choice2 = str.upper(input("> Enter W to examine the wall, C to examine the cot, or B to examine the bowl and spoon.\n> "))
  if choice2 == "C": 
    print("A cot for sleeping. It is discolored from excessive use and negligence.")
    explore()
  elif choice2 == "W": 
    print("There are cracks and other symptoms of negligence and decay along the wall.")
    explore()
  elif choice2 == "B": 
    print("The bowl is heavy in your hands. You can probably break something with it.")
    bowl()
  else:
    none()
 
def bowl():
  choice2 = str.upper(input("> Enter W to examine the wall, C to examine the cot, or B to examine the bowl and spoon.\n> "))
  if choice2 == "W":
    print("There are cracks and other symptoms of negligence and decay along the wall.\nThe wall collapses when you throw the bowl at it. You notice a hidden passage behind the rubble.")
    leave = str.upper(input("> Enter G to enter the passage or S to remain in your cell.\n> "))
    if leave == "G": 
      go()
    elif leave == "S": 
      print("There is nothing else of importance in this cell.\nYou fail to notice the cell walls slowly closing in on you...")
      crushed()
  elif choice2 == "B": 
    print("The bowl is heavy in your hands. You can probably break something with it.")
    bowl()
  elif choice2 == "C": 
    print("A cot for sleeping. It is discolored from excessive use and negligence.")
    bowl()
  else:
      none()

def none():#select wrong option
  print ("Follow the instructions and only select from the options provided.")
  restart()

def restart():
  global restartcounter, health, health1, turn
  health = 15
  health1 = 15
  turn = 0
  global health2, health3, turn2
  health2 = 15
  health3 = 15
  turn2 = 0
  restart = str.upper(input("> Enter S to return to the start or L to accept your loss.\n> "))
  restartcounter = restartcounter + 1
  if restart == "S": 
    start()
  elif restart == "L": 
    print ("You surrender yourself to the cold embrace of eternal sleep.")
  else:
    none()

def go():#enter passage in wall from first cell
  print("You navigate through the narrow passage on your hands and knees.")
  print("You exit the passage and are confronted by a group of hooded figures.") 
  fight = str.upper(input("> Enter F to fight or R to run.\n> "))
  if fight == "F":
    print("You choose to fight and stand your ground!")
    fighting()
  elif fight == "R":
    run()
  else:
    none()

def run():
  print("You dash towards the opposite direction. The main path diverges before you.")
  path = str.upper(input("> Enter L to take the left path or R to take the right path.\n> "))
  if path == "L":
    left()
  elif path == "R": 
    right()
  
def left():
  print("You arrive at the edge of a steep cliff. Dark waves ripple ominously beneath you.\nThe hooded figures surround you, preventing any means of escape.")
  guardescape = str.upper(input("> Enter F to fight, S to surrender, or J to jump.\n> "))
  if guardescape == "F": 
    fighting()
  if guardescape == "S": 
    surrender()
  if guardescape == "J": 
    print("Your limbs feel leaden in the frigid waters. Salt water saturates your lungs and you struggle to remain afloat...")
    print("You drown.")
    restart()

def right():
  print("You are unable to halt before you find yourself hurtling down a jagged cliff.")
  print("Your body is dashed to pieces against the rocks...")
  restart()

def surrender():
  print("You are escorted back to a different cell.")
  escape2() 

def escape2(): #after surrender
  attempt2 = str.upper(input("> Enter E to explore, D to test the door, or W to wait.\n> "))
  if attempt2 == "W":
      print("It is unwise to remain idle in an unfamiliar environment.")
      print("It may only be your imagination, but the walls appear to be closing in on you...?")
      crushed()
  elif attempt2 == "E": 
    print("You examine the room. The walls are all a consistent, sickly shade of gray. A small walkie-talkie sits on a table with a lamp.")
    explore2()
  elif attempt2 == "D": 
    print("You brace your body and propel yourself against the door, however, you only succeed in dislocating your shoulder. The door does not budge.")
    #health = health - 1 
    escape2()
  else:
    none()
  
def explore2(): #after escape2
  choice = str.upper(input("> Enter W to examine the walkie-talkie, T to examine the table, or L to examine the lamp.\n> "))
  if choice == "W": 
    print("You desperately adjust the buttons on the walkie-talkie. Eventually, you begin to hear vague crackling from the other end.")
    communication()
  elif choice == "T": 
    print("The details of the table cannot be discerned in the poorly-illuminated room.")
    explore2()
  elif choice == "L": 
    print("You turn on the lamp. It illuminates the other objects in the room, and you discover a small key on the table.")
    lamp()
  else:
    none()

def lamp(): #after picking up lamp in explore2
  choice = str.upper(input("> Enter W to examine the walkie-talkie, T to examine the table, or L to examine the lamp.\n> "))
  if choice == "W": 
    print("You desperately adjust the buttons on the walkie-talkie. Eventually, you begin to hear vague crackling from the other end.")
    walkietalkie + 1
    communication()
  elif choice == "T":
    print("It is an ordinary wooden table.")
    lamp()
  elif choice == "L": 
    print("You seek to discover more information about the cell. You pick up the lamp and discover a locked trapdoor on the floor.")
    print("You use the key to unlock the trapdoor!")
    leave = str.upper(input("> Enter G to enter the passage or S to remain in your cell.\n> "))
    if leave == "G": 
      go2()
    elif leave == "S": 
      print("There is nothing else of importance in this cell.\nYou fail to notice the cell walls slowly closing in on you...")
      crushed()
  else:
    none()

def go2(): #after exploring trapdoor in lamp
  print("You descend into an unfamiliar corridor. More hooded figures confront you.")
  fof = str.upper(input("> Enter F to fight or R to run.\n> "))
  if fof == "F":
    fighting2()
  if fof == "R":
    print("You desperately attempt to flee, however, there is no exit route behind you. In front of you, the figures advance.")
    print("Before you can cohesively comprehend the situation, you are fatally stabbed.")
    print("You bleed out...")
    restart()

global health, health1, turn, restartcounter

health = 15
health1 = 15
turn = 0
restartcounter = 0

def fighting(): #battle during first escape from cell
  global health, health1, turn
  while turn%2 == 0 and 16 > health > 0 and 16 > health1 > 0: 
    choiceattack = str.upper(input("> Enter A to attack or D to defend.\n> "))
    if choiceattack == "A":
      print("Your opponents choose to attack!")
      health = health - 6
      health1 = health1 - 6
      print("Your health:", health)
      print("Their health:", health1)
      turn = turn + 1
      fighting()
    elif choiceattack == "D":
      print("Your opponents choose to attack!")
      health = health
      health1 = health1 - 3
      print("Your health:", health)
      print("Their health:", health1)
      turn = turn + 1
      fighting()
  while turn%2 == 1 and 16 > health > 0 and 16 > health1 > 0:
    choiceattack = str.upper(input("> Enter A to attack or D to defend.\n> "))
    if choiceattack == "A" :
      print("Your opponents choose to defend!")
      health = health - 3
      health1 = health1
      print("Your health:", health)
      print("Their health:", health1)
      turn = turn + 1
      fighting()
    elif choiceattack == "D":
      print("Your opponents choose to defend!")
      health = health
      health1 = health1
      print("Your health:", health)
      print("Their health:", health1)
      turn = turn + 1
      fighting()
  while health < 1: 
    print("The hooded figures close in on you...")
    restart()
  while health1 < 1:
    print("After an arduous battle, the bodies of the hooded figures lay strewn across the ground.")
    battle1victory()

global gun 
gun = 0

def battle1victory(): #fighting
  step = str.upper(input("> Enter E to explore your surroundings, S to search the bodies, or C to continue.\n> "))
  if step == "E": 
    print("The night is eerily silent. You get the feeling that something is terribly wrong.")
    battle1victory()
  elif step == "S":
    print("You remove the cloak from one of the incapacitated figures, revealing a walkie talkie, a frozen watch, and a gun.")
    search = str.upper(input("> Enter W to examine the walkie talkie, C to examine the watch, or G to examine the gun.\n> "))
    if search == "W":
      print("You desperately adjust the buttons on the walkie-talkie. Eventually, you begin to hear vague crackling from the other end.")
      walkietalkie2()
    elif search == "G": 
      print("The sleek metal gun feels familiar in your grip.")
      battle1victory()
    elif search == "C": 
      print("The hands of the watch are frozen at 11:14.")
      battle1victory()
    else:
      none()
  elif step == "C":
    print("You decide to venture fowards. Only the dim light from the crescent moon illuminates your path, although you still struggle to discern the details of your surroundings. You stagger forward for hours, however, there remain no noticable changes in your surroundings.")
    print("Without warning, your headache flares up, and you collapse onto the ground...")
    print("...")
    print("When you awaken, you discover that you have been taken to a small, dark room. A cord of rope binds your hands to a metal bar.")
    kidnapped()
  else:
    none()    

def kidnapped():
  choice = str.upper(input("> Enter E to explore, R to test the strength of the rope, or C to call for help.\n> "))
  if choice == "E":
    print("You examine the room. You notice a circle of blood drawn beneath your feet.") 
    kidnapped()
  if choice == "R":
    print("The rope does not slacken. Despite your efforts, your hands remain as tightly bound as before.")
    rope2()
  if choice == "C":
    callforhelp()

def rope2():
  choice = str.upper(input("> Enter E to explore the room, R to test the strength of the rope, or C to call for help.\n> "))
  if choice == "E":
    print("You examine the room. You notice a circle of blood drawn beneath your feet.\nYou are barely able to discern the vague outline of a jagged piece of wood.") 
    rope3()
  if choice == "R":
    print("The rope does not slacken. Despite your efforts, your hands remain as tightly bound as before.")
    rope2()
  if choice == "C":
    callforhelp()

def rope3():
  choice = str.upper(input("> Enter E to explore the room, R to test the strength of the rope, or C to call for help.\n> "))
  if choice == "E":
    print("You examine the room. You notice a circle of blood drawn beneath your feet.\nYou are barely able to discern the vague outline of a jagged piece of wood.") 
    rope3()
  if choice == "R":
    print("You bring your bound hands to the jagged piece of wood. After some effort, the rope begins to fray, allowing you to free your hands.")
    print("With your hands free, the only obstacle inhibiting your escape is the locked door before you.")
    escaping()
  if choice == "C":
    callforhelp()
    
def escaping(): 
  choice = str.upper(input("> Enter E to explore the room, D to examine the door, or C to call for help.\n> "))
  if choice == "E": 
    print("The blood beneath your feet stains your soles red. You notice that the walls are made from solid, indestructible metal.\nYou turn around to examine the back of the room...\n...\n\x1B[3mEndless, pulsating void.\x1B[0m\n...\nYou feel ill.")
    enter = str.upper(input("> Enter V to enter the void or T to turn away.\n> "))
    if enter == "V":
      void()
    else:
      print("Ḙ̶̡̔̆̓r̷͕̙̻̭͚̝̀̈́r̵̢͑õ̷̹̝̊̂r̶̮̝̤͆̏.̵̘͖̆̀͐͂̑̅͠.̴̩̰͙̟͚̔̀͆̉̌̕")
      str(input("≯̛̣͎̫̈́̃ ̷͈̳͔̏̀̃E̸͕͊ņ̴̡͔͉̌̑̔̄̕t̵͙͚̽ē̷͎̩̯̠͉͂̍̃̋́͘ͅr̶͕͈̱̪̆͠ ẗ̵̛͚̱́̏̌̉̉̆ơ̵͕͌͌̄͆́̑ ̸͚̅̾̓̍̄e̴͔͔͖͋͊̕̕n̵̲̭͂̾̽̇̕ẗ̶̰͓̗̭͇͛͝e̸͙̿̊̆͜ŗ̸̰̜͙̐̇̌͆͂͠͝ ̷̳͙̫̤̤̇̇t̴͇͑̌̔̊̕h̴̼̫̥̽͝ë̴̛̙̲̲̪́́̚͝ ̴̡̣̫͉̃̚v̶͖̭̘̟̉̓͗̂ͅo̶̯̼͖͈͑̈ͅï̴͔͕̹͘̕d̵̨̠̬̫̫͒͊͐.̶̛͖͔͇̽̓́̋́ͅ\n≯̛̣͎̫̈́̃ "))
      void()

  if choice == "D": 
    print("The door is made from solid metal. It is impossible to break down--not that forcibly attempting to open doors has ever worked.")
    escaping()
  if choice == "C": 
    str(input("You desperately attempt to call for help: "))
    print("Footsteps resonate down the hallway.\nYou warily crouch behind the door.")
    throughdoor()
  
def throughdoor():
  text = "The door opens, sending light flooding into the room. You squint; your eyes are unused to the brightness.\nThe hooded figure in the doorway steps in, and you note that it loosely holds a bloody knife."
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 4, 1))
    seconds = float(seconds)
    time.sleep(seconds)
  print("You wait as the figure further enters the room and puts together the pieces as it sees the severed rope.\nIn the brief moment when its attention is on hyperfocused on discovering your location, you slip out and slam the door shut behind you.")
  finding()

def finding(): #this function is a mess
  global walkietalkie 
  if walkietalkie == 0: 
    explore = str.upper(input("> Enter E to explore your surroundings or C to continue forward.\n> "))
    if explore == "E":
      print("You examine your surroundings. You are in a dimly lit hall. At its end are three doors, each with a note pasted to them.") 
      cont = str.upper(input("> Enter E to continue exploring and C to continue forward."))
      if cont == "E":
        print("You spend minutes closely examining every inch of the nearby area, but find nothing. The sound of heavy footsteps implies the arrival of more hooded figures.\nThough you struggle, you are easily grabbed and forcefully escorted back into the room...")
        restart()
      elif cont == "C": 
        print("At the end of the hall, you find a green door, a red door, and a blue door. A plaque above the door reads:\n\"Find the truth teller and open her door.\"")
        riddle()
      else:
        none()
    elif explore == "C":
      print('At the end of the hall, you find a green door, a red door, and a blue door. A plaque above the door reads:\n\"Only one of the notes tells the truth. Enter the correct door.\"')
      riddle()
    else:
      none()    
  elif walkietalkie != 0:
    messagetoyou()

def messagetoyou():
  global walkietalkie
  str(input("> Enter E to explore your surroundings or C to continue forward.\n> "))
  print("As you begin to act, you hear a staticky noise coming from an object in your left hand.\nConfused, you look down, and note a walkie talkie.\nJust how could that have gotten there?\nWhen did you get this object?\nWhen could you have gotten it?\nFor you to have been holding it the whole time is simply impossible...\n...\nYou shake your head to clear the intrusive thoughts.\nYou cannot afford to be distracted. It's far more important to focus on the present.")
  listen = str.upper(input("> Enter L to listen and T to talk.\n> "))
  if listen == "L":
    walkietalkie()
  if listen == "T":
    talkingwalkietalkie()
  walkietalkie = 0
  finding() 


def riddle():
  door = str.upper(input("> Enter G to examine the green door, R to read the note on the red door, or B to read the note on the blue door. If you have decided which door you have chosen, enter C to continue forward.\n> "))
  if door == "G":
    print("The note reads:\n\"I'm not the right door.\"")
    riddle()
  elif door == "R":
    print("The note reads:\n\"The blue door isn't the right door.\"")
    riddle()
  elif door == "B":
    print("The note reads:\n\"I'm the right door.\"")
    riddle()
  elif door == "C":
    choice()

def choice(): 
  choice = str.upper(input("> Enter G to enter the green door, R to enter the red door, or B to enter the blue door.\n> "))
  if choice == "G": 
    monologue() 
  if choice == "R":
    print("There is nothing but endless void behind the door.")
    void2()
  if choice == "B":
    print("There is nothing but endless void behind the door.")
    void2()

def monologue():
  global restartcounter
  print("You open the green door, and are greeted by [ ].")
  text = "\"You\'ve taken a while to arrive.\"\n" 
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 4, 1))
    seconds = float(seconds)
    time.sleep(seconds)
  str(input("You try to speak up: "))
  text = "\"It's irritating when you say useless things I can\'t respond to.\"\n\"But out of curiousity, I'll allow you to tell me something.\"\n\"In getting here, just how many times have you died and had to restart?\"\n" 
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 4, 1))
    seconds = float(seconds)
    time.sleep(seconds)
  playerdeathinput = input("\"Go on. Tell me:\" ")
  text = "\"Really? Is that really, honestly true?\"\n\"Though it\'s not as if I know. I\'m not the type to ask questions I already know the answer to.\"\n\"...what, did you think I was baiting you? That I was going to punish you if you didn\'t know the right answer?\"\n\"Something like that is just needlessly cruel.\"\n" 
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 4, 1))
    seconds = float(seconds)
    time.sleep(seconds)
  monologue2()


def monologue2():
  print("\"But it\'s about time to get back on topic.\"")
  text = "\"My role here is to ask you to stop playing this game.\""
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 4, 1))
    seconds = float(seconds)
    time.sleep(seconds)
  why = input("\"You can ask W for \'what?\' or H for \'why?\' right now.\" \n> ")
  if why == "W": 
   print("\"Well, of course YOU don\'t understand. I\'m not talking to YOU right now, I\'m talking to the player. And whoever\'s playing this game should have some rudimentary guesses as to where this plot is going by now.\"")
   talking()
  if why == "H":
    print("\"Is it still not obvious...?\"")
    talking()
  else:
    print("\"Try to follow the instructions next time.\"\n\"Have fun starting from the beginning...!\"")
    restart()

def talking():
  yep = input("\"You must've noticed by now that this is a pretty bad game.\"\n> \"Enter Y if you agree or N if you disagree.\"\n> ")
  if yep == "Y":
    text = "\"Don't blame your incompetence at games on the developers. That's pathetic of you.\"\n"
    for c in text:
      sys.stdout.write(c)
      sys.stdout.flush()
      seconds = "0." + str(randrange(1, 4, 1))
      seconds = float(seconds)
      time.sleep(seconds)
    talking1()
  elif yep == "N": 
    text = "\"You're too kind to the incompetent developers of this game.\"\n"
    for c in text:
      sys.stdout.write(c)
      sys.stdout.flush()
      seconds = "0." + str(randrange(1, 4, 1))
      seconds = float(seconds)
      time.sleep(seconds)
    talking1()
  else: 
    print("\"It's a bit rude to not respond as I told you to, you know.\"\n\"You\'d better start from the beginning and learn some manners...!\"\n")
    restart()

def talking1(): 
  text = "\"...\"\n\n"
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 4, 1))
    seconds = float(seconds)
    time.sleep(seconds)
  text = "\"Have you wondered what happens to a game once the player stops playing?\""
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 4, 1))
    seconds = float(seconds)
    time.sleep(seconds)
  agree = input("\"Everytime you die and the player has to restart?\"\n\"Enter Y if you have or N if you haven't.\"\n \"I hate to prompt you to input specific answers every time, but... Well, you know. I can only respond to specific inputs. Tragically, we can never have a normal conversation.\"\n> ")
  if agree == "Y": 
    print("\"How surprisingly thoughtful of you.\"")
    talking2()
  elif agree == "N":
    print("\"...I expected nothing more.\"")
    talking2()
  else:
    text = "\"I\'m really irritated by your insistence to not answer with a simple yes or no...\"\n\"I don\'t feel like talking to someone so rude, so just return to the beginning!\"\n"
    for c in text:
      sys.stdout.write(c)
      sys.stdout.flush()
      seconds = "0." + str(randrange(1, 4, 1))
      seconds = float(seconds)
      time.sleep(seconds)
    restart()

def talking2():
  print("..")
  text = "\"If you die, the world ends. Again, and again. A continuous v̷̨͚͓̘͓͉͗o̴̢̗̠͕̞̐̎͝ḯ̶̥͉̲̦̽̽̆d̵̨̳̮̎̂̽\"\n"
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 4, 1))
    seconds = float(seconds)
    time.sleep(seconds)
  print("\"Well, that\'s why I\'m here, requesting this of you.\"\n\"Just end this game.\"\n\"End all of this.\"")
  doit = str.upper(input("> Enter Y to end it or N to not end it.\n> "))
  if doit == "Y": 
    print("\"I'm grateful. Really.\"")
    text = "\"And, well.\"\n\"Thanks for playing this game.\"\n"
    for c in text:
      sys.stdout.write(c)
      sys.stdout.flush()
      seconds = "0." + str(randrange(1, 4, 1))
      seconds = float(seconds)
      time.sleep(seconds)
    end()
  elif doit == "N":
    print("\"I'm disappointed, but unfortunately, I'm not surprised.\"\n\"Really, that\'s how I feel.\"\n\"But it isn\'t as though desperately pleading with you was my only plan.\"")
    print("\"I\'ll ensure that neither of us will ever die again.\"")
    print("\"And you--I'll ensure that you\'ll never be able to win.\"")
    print("\"Everything will remain eternally stagnant, and nothing will end...\"")
    finalbattle()

health5 = 100000000000000
health6 = 100000000000000
turn3 = 0

def finalbattle():
  global health5, health6, turn3
  while turn3%3 == 0 and health5 > 0 and health6 > 0: 
    choiceattack = str.upper(input("> Enter A to attack or D to defend.\n> "))
    if choiceattack == "A":
      print("Your opponents choose to attack!")
      health5 = health5 - 6
      health6 = health6 - 6
      print("Your health:", health5)
      print("Their health:", health6)
      turn3 = turn3 + 2
      finalbattle()
    elif choiceattack == "D":
      print("Your opponents choose to attack!")
      health5 = health5
      health6 = health6 - 3
      print("Your health:", health5)
      print("Their health:", health6)
      turn3 = turn3 + 8
      finalbattle()
  while turn3%3 == 1 or turn3%3 == 2 and health5 > 0 and health6 > 0:
    choiceattack = str.upper(input("> Enter A to attack or D to defend.\n> "))
    if choiceattack == "A" :
      print("Your opponents choose to defend!")
      health5 = health5 - 3
      health6 = health6
      print("Your health:", health5)
      print("Their health:", health6)
      turn3 = turn3 + 1
      finalbattle()
    elif choiceattack == "D":
      print("Your opponents choose to defend!")
      health5 = health5
      health6 = health6
      print("Your health:", health5)
      print("Their health:", health6)
      turn3 = turn3 + 13
      finalbattle()
  if health5 < 1: 
    print("\"You can\'t die yet...!\"")
    restart()
  if health6 < 1:
    print("\"Was that really worth it...?\"")
    goodend()

def end(): #THE ERROR IS INTENTIONAL
  print("\nThe end.")
  g̷̺̣̈́̒ǎ̸̺̻̈m̸̩̘̔͊ë̵̙́o̸̫͘̚v̵͔̿͛e̶̡̞͑r̶̥͋̐()

def goodend():
  print("And you live happily ever after.")

def void2():
  text = "The world explodes into light.\nYou catch brief, imcomprehensible strings of text flickering before your eyes.\ndef choice():]\n  choice = str.upper(input(\"> Enter G to enter the green door, R to enter the red door, or B to enter the blue door.\"))\nYour head explodes.\n"
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 4, 1))
    seconds = float(seconds)
    time.sleep(seconds)
  start()

def talkingwalkietalkie():
  str(input("You attempt to transmit a frantic message: "))
  print("The walkietalkie briefly goes silent.\nThen, a voice speaks up.")
  print('"I think it\'s about time to end this pathetic charade, isn\'t that right?"\n"Just walk forward."')
  explore = str.upper(input("> Enter E to explore your surroundings or C to continue forward.\n> "))
  if explore == "E":
    print("You examine your surroundings. You are in a dimly lit hall. At its end are three doors, each with a note pasted to them.") 
    cont = str.upper(input("> Enter E to continue exploring or C to continue forward.\n> "))
    if cont == "E":
      print("You spend minutes closely examining every inch of the nearby area, but find nothing. The sound of heavy footsteps implies the arrival of more hooded figures.\nThough you struggle, you are easily grabbed and forcefully escorted back into the room...")
      restart()
    elif cont == "C": 
      print("At the end of the hall, you find a green door, a red door, and a blue door. A plaque above the door reads:\n\"Find the truth teller and open her door.\"")
      riddle()
    else:
      none()
  elif explore == "C":
    print('At the end of the hall, you find a green door, a red door, and a blue door. A plaque above the door reads:\n\"Only one of the notes tells the truth. Enter the correct door.\"')
    riddle()
  else:
    none()

def void():
  text = "You enter the void at the back of the room.\nThe world explodes into light.\nYou catch brief, imcomprehensible strings of text flickering before your eyes.\nif choice == \"E\":\n    print(\"The blood beneath your feet stains your soles red. You notice that the walls are made from solid, indestructible metal.\")\nYour head explodes.\n"
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 4, 1))
    seconds = float(seconds)
    time.sleep(seconds)
  start()
  
def callforhelp():
  str(input("You desperately attempt to call for help: ")) 
  print("You scream as loudly as possible, however, your actions seem to be ineffective. You only succeed in agitating your vocal chords.")
  print("Against your expectations, you begin to discern the faint sound of footsteps. In the darkness, a door slowly opens.")
  print("Hope flares up in your chest...!")
  print("Light floods into the room...")
  print("You are s̸̨̛̱̟̰̣͂̈́̊́́͐ȁ̸̧̯͕̣̓̐̅̊͊č̷̪̯̙͓͚͗̕r̸̢̙̟̳̭͔͐̀̓̐̊̚i̸̦̪͉͇̰̳̺͒́̈̋͂́f̴̨̧̙̗̫͚̚̕͠î̸̛̙̖̫̀͝ͅc̵̻͊̌͝e̸̪̲̺̯̐͋̒̋̿ḑ̴͖̙̙̠̙̍̾̈́̓͘̕͜͝")
  restart()

global health2, health3, turn2
health2 = 15
health3 = 15
turn2 = 0

def fighting2(): #battle during exploring trapdoor
  global health2, health3, turn2
  while turn2%3 == 0 and 16 > health2 > 0 and 16 > health3 > 0: 
    choiceattack = str.upper(input("> Enter A to attack or D to defend.\n> "))
    if choiceattack == "A":
      print("Your opponents choose to attack!")
      health2 = health2 - 6
      health3 = health3 - 6
      print("Your health:", health2)
      print("Their health:", health3)
      turn2 = turn2 + 1
      fighting2()
    elif choiceattack == "D":
      print("Your opponents choose to attack!")
      health2 = health2
      health3 = health3 - 3
      print("Your health:", health2)
      print("Their health:", health3)
      turn2 = turn2 + 1
      fighting2()
  while turn2%3 == 1 or turn2%3 == 2 and 16 > health2 > 0 and 16 > health3 > 0:
    choiceattack = str.upper(input("> Enter A to attack or D to defend.\n> "))
    if choiceattack == "A" :
      print("Your opponents choose to defend!")
      health2 = health2 - 3
      health3 = health3
      print("Your health:", health2)
      print("Their health:", health3)
      turn2 = turn2 + 1
      fighting2()
    elif choiceattack == "D":
      print("Your opponents choose to defend!")
      health2 = health2
      health3 = health3
      print("Your health:", health2)
      print("Their health:", health3)
      turn2 = turn2 + 1
      fighting2()
  if health2 < 1: 
    print("The hooded figures close in on you...")
    restart()
  if health3 < 1:
    print("After an arduous battle, the bodies of the hooded figures lay strewn across the ground.")
    battle2victory()
    
def battle2victory(): #fighting2
  step = str.upper(input("> Enter E to explore your surroundings, S to search the bodies, or C to continue.\n> "))
  if step == "E": 
    print("You are in a dark corridor. Your vision is faintly illuminated by rows of torches along the stone walls of the corridor.")
    battle2victory()
  elif step == "S":
    searching()
  elif step == "C":
    print("You continue onwards. The dim torch light gradually vanishes until you are left in complete darkness.\nYou abruptly stumble over some stairs.")
    doit = str.upper(input("> Enter S to go up the steps or T to turn back around.\n> "))
    if doit == "S":
      print("You wander up the seemingly-endless stairs before finally reaching a plateau.")
      finding()
    if doit == "T": 
      print("You stumble back to your original position.")
      battle2victory()
    else:
      none
  else:
    none()

def searching(): #win fighting2
  global walkietalkie
  print("You remove the cloak from one of the incapacitated figures, revealing a walkie talkie, a pocket watch, and a gun.")
  search = str.upper(input("> Enter W to examine the walkie talkie, P to examine the watch, or G to examine the gun.\n> "))
  if search == "W":
    walkietalkie = 0
    print("You desperately adjust the buttons on the walkie-talkie. Eventually, you begin to hear vague crackling from the other end.")
    walkietalkie2()
  if search == "P":
    print("The hands of the watch are frozen at 11:14.")
    battle2victory()
  if search == "G": 
    print("You pick up the gun, unused to the instrument.\nThough you only lightly press on the trigger, it ends up firing, the bullet ricotcheing around the corridor...")
    print("You are shot.")
    restart()

def walkietalkie2(): #searching after winning fighting2
  global walkietalkie
  walkietalkie = 1
  str(input("You attempt to transmit a frantic message: ")) 
  print("T̷̲̻͔͖͐̊͂̒o̵̖̍̆̕ ̶̲̞̮̟͎̈́̂̉̓̈͘s̶̡̛͕͙̤̤̤͋̆͂͂ọ̷̣̲̙͛̎͛̿̀̐ǫ̵̲̳̃̿͛̓͘͜n̷̺̥͕̤͉͙͛̓̐.̷̨͌ ̴͈̯͚̦̭́̈̈́̀͂͐͑͜W̶̢̟͕̰̰͚̔̄̔͜à̸͔̟̼̥͈̈́͛̉̾̿͝ḯ̶̧̛̗͓͔̽̓͊̀̕t̸̡͉̗̘͈͈̜͋̾̇͐͐̏͒.̷̦̗̟̲̪̾͋́͂̊͠ ̵̛̗Ḭ̸̧̀͋̋͝t̷̡̼̘̱̥͂͐̉̚͠ ̸̛͉͔w̸̜̩̲͌ì̸̪̻͚̦̹̽͛̎͗̀ͅl̷̦̲̖̝̈ḽ̵̡͇̰͚̎̃̌ ̶͚̯̘͎̪̲̊ͅf̴̨̛̈̃͝â̸̬̱i̴̜͖̗̮̎́̈͑̐ͅl̸͓̙̱̗̤̿̽͘ ̸̲̭͉̦̆̈́̚͝ä̶̙̞́̚͜n̵̨̩̭̭̙͚͎̾ỵ̷̎̅̓͝͝ŵ̴͚̥̗͉̠͙́͊͒͘ͅa̸̦͙̯͔̻̔͝y̶͚͚̝͓̫̠͑̉̚͝.̸̼̬͓̭͌̉̃̆̉̈́̕")
  start()

def communication():
  global walkietalkie
  walkietalkie = 1
  str(input("You attempt to transmit a frantic message: ")) 
  print("Y̷̨͖̺͎͈̹̟̏̿́ö̸̱̜̘͍̠͋̌ư̴͍͚̖̽̓̄͠ ̶̘̯̣̖̬̺̔͛̐̈̕̚͝c̵̪̊̒a̷͍̭̬͛͂̃n̵̢̨̨͇̰̱͑̈͛̍͌̎̕͜ņ̴̳̠͇͔̈́ͅǫ̸̮̗̩̞͂t̷̳̪̠̍̋̎̒̈̀ ̶̙͓͙̥̃̀̊̕͠é̶̛̖̦͑͠s̴͕̱̟͎̤͑͒͑̕c̵̟̥̙̬͆̃a̷̪̫̫̗͕̔͋̂̂̋̚͠p̷̭̔͑̊̾̎̇ĕ̷͍̮͈͙͇̥́̽̊̒͂.̸̭̹̤̬̏̀ ̸̝̳̮͖͖̰͊̓͠G̸̞̹̙̭͐͘ĩ̴̫͉v̸͉́̒ͅḛ̴͐̽̾͝ ̷̢͇̦̣̉̐́͝u̸̠̣̳͖̻͚̒̿͐̎̀p̸͕͋̓̈́̿̉.̴̨̢̙̹̙̜̤̈́̑͘ ̶̪̰͆Ȗ̵̧̖̬̞̫̝̭͑͐̿̌s̷̯̞̒͊͐́͘̚e̵̛̜̖̤̔̿l̶͆̎̿͐̎͜͠ë̸̦̬́̂̉͂́̚ș̴̼͖̺̠̾͋̈́̂̿s̸͎͂.̵͕͐͗͗̉̄͝")
  start()

def walkietalkie():
  global walkietalkie
  walkietalkie = 1
  print("You discern faint words coming from the walkie talkie.") 
  print("'We're - - close. Secure the - - - or kill - -. The end of times - - be near if we can just - - rid of - -. We can bring the apocal - - upon this cur - - - - ld.'")

print("46 MINUTES TO MIDNIGHT")
print("Developed by the esteemed Chelsea Zhou and Alyosha Vak\n")
start()