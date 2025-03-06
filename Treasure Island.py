print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /______________|_______
|                   | |o ;    `"-.o`"=._`` '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /_
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print('''
Despite just stepping out of a convenience store nearby your house, you suddenly
find yourself surrounded by dense woods of tropical trees.

       ****                        ****                         ****                 
     ********                     ********                     ********               
    **  ******                   **  ******                   **  ******              
     *   ******     ******        *   ******     ******        *   ******     ******  
         ******   *********           ******   *********           ******   ********* 
          ****  *****   ***            ****  *****   ***            ****  *****   *** 
          ***  ***     **              ***  ***     **              ***  ***     **    
    *************       *        *************       *        *************       *   
  ******************           ******************           ******************        
*****   H*****H*******       *****   H*****H*******       *****   H*****H*******      
***     H-___-H  *********   ***     H-___-H  *********   ***     H-___-H  *********  
 ***    H     H      *******  ***    H     H      *******  ***    H     H      *******
  **    H-___-H        *****   **    H-___-H        *****   **    H-___-H        *****
    *   H     H         ****     *   H     H         ****     *   H     H         ****
        H     H         ***          H     H         ***          H     H         *** 
        H-___-H         **           H-___-H         **           H-___-H         **  
        H     H         *            H     H         *            H     H         *   
        H-___-H                      H-___-H                      H-___-H             

However, you see that, to your left, the woods ar a bit different, less dense. At
this point, despite making no sense, you can notice you're at a coastline. Still,
despite the smell of salty water, you see no ocean. You can hear it but you can't
make out where it is. You only know it's no good to stay still.
''')

path = ""
while path != "forward" and path != "backwards" and path != "right" and path != "left":
    path = input("To which direction will you go?\n        Type \"forward\", \"backwards\", \"right\" or \"left\" in lowercase.\nYour choice: ")

    if path == "forward":
        print('''
After some time delving forward in the dense woods, you sense a burning pain in your
chest. Something hit you really hard and it's impact even staggered you. As you look
down, there is an arrow piercing you through your shirt and blood starts to stain it
and it drips to the ground. You drop to your knees. the strength of your body slowly
vanishing. You can still hear nearby cries from voices unknown approaching. You lose
consciousness before you could even feel when your face dropped against the dirt.
        ''')
        print("        GAME OVER!")
        input("\nPress the Enter key to exit.")
    elif path == "backwards":
        print('''
As you move a step backwards before turning around, you slip on a small rock. It was
just bad luck. You fall backwards and hits your head against something very hard. It
immediately made you unconscious. The last thing you remember before passing out are
the palm trees leaves against the blue sky. Unfortunately, you never wake up again.
        ''')
        print("        GAME OVER!")
        input("\nPress the Enter key to exit")
    elif path == "right":
        print('''
You turn right and delve into progressively dense woods. The tree types slowly begin
change from a clearly tropical flora to resemble a forest, though still tropical. As
time passes, bushes appear. When you notice you no longer can smell or hear the sea,
you reach a treeline. A bush prevents you to see there is no more ground ahead. Your
next step finds nothing but air and you fall from a cliff. Maybe it was for the best
that the shock of hitting the bottom instantly shut down your brain.    
        ''')
        print("        GAME OVER!")
        input("\nPress the Enter key to exit.")
    elif path == "left":
        print('''
You turn left and goes towards the less dense woods. It feels like you are descending
to lower terrain and the sound and smell of salty water grows stronger. It takes only
a few minutes for you to find yourself at a peaceful, almost empty beach. There was a
small boat ashore. It made you wonder where it came from and who left it there. Would
someone mind if you borrowed it? But to go where? You looked around the sea and, much
to yur surprise, you did see what seemed to be a very tiny rocky island, almost if it
was the flattened tip of a cliff. There was something there you couldn't make out the
shape, but it was almost certainly man-made. You decided you had to go there. So, you
looked at the boat. Should you take it even though you didn't know if the owner would
come after you or should you swim to the island? Maybe you should wait for the owner?
        ''')

        crossing = ""
        while crossing != "wait" and crossing != "swim" and crossing != "steal":
            crossing = input("Will you swim or wait for the boat owner? Maybe you want to steal it?\n        Type \"swim\", \"wait\" or \"steal\" in lowercase.\nYour choice: ")

            if crossing == "wait":
                print('''
Struck by a feeling of uneasiness from unknown waters and not really wanting to taint
your soul by stealing what could be the difference between life and death for someone
else, you sit at the beach and wait. You don't have to wait too long, however. Soon a
man dressed in pirate clothes comes out of the woods. You ask him if he is the boat's
owner and, though warily, he confirms. As you ask him to go to the island, he gives a
grim look and tells you it's cursed. You explain to him your story and he nods saying
maybe the curse and your circumstances are related. He invites you to take you to the
island and it doesn't take long for you to reach there. The man would not stay and he
left immediately after delivering you. At the flat top of the rocky island, there are
three closed doors with nothing behind them, floating close to the ground. They emmit
a very strange pressure despite looking like made of wood. They stand proud and their
only difference is their color: one is red, one is blue and one is yellow. Though the
doors are still, you feel like they are calling to you. 
                ''')

                color = ""
                while color != "red" and color != "blue" and color != "yellow":
                    color = input("Choose a door to open first.\n        Type \"red\", \"blue\" or \"yellow\" in lowercase.\nYour choice: ")

                    if color == "red":
                        print('''
You decide to open the red door first. You touch the handler and feel it's gentle and
inviting warmth. It reminds you of the sunny days at your hometown. Sure, you weren't
really a good kid back then, but you had much, much fun. With those thoughts in mind,
you open it wide without hesitation. You meet a dragon's fire breath that reduces you
to ashes before you even realize you were being burned alive.  
                        ''')
                        print("        GAME OVER!")
                        input("\nPress the Enter key to exit.")
                    elif color == "blue":
                        print('''
You decide to open the blue door first. The handler feels like it's sweating just like
a cold beer would. The memories your youth comes to mind. Back then, you wanted almost
everything that fancied you, and a lot did. Friends, lovers, large apartments, all the
most desired cars, very expensive furniture and luxury goods. Really good times. Times
when you felt like the king of the world. With eyes shining with greed, you pulled the
door wide open. Without giving you time to react, several large tentacles emerged from
it and constrained you. You were pulled inside while having your bones broken, several
teeth of a kraken being your destination. 
                        ''')
                        print("        GAME OVER!")
                        input("\nPress the Enter key to exit.")
                    elif color == "yellow":
                        print('''
When you approached the yellow door, you felt uneasy. It was giving off coldness and a
feeling too familiar of being back at home. But since going back home was exactly what
you were trying to do, you didn't changed your mind. Shyly, you held the doorknob. The
thoughts of guilt over all the very poorly made decisions through your life that ended
up leading you to lose all your wealth and become just one more in the crowd made your
eyes teary. You remembered all those you had wronged and manipulated. You wished to go
back in time and do it all differently, but you knew it was impossible. And amidst all
the sorrow, it also came to you two very familiar voices. The voices of those still in
this world that greeted you with love at home after every single day of hard work. The
most precious jewels for you in the whole world. And you smiled. Because now you would
be going back to them. So you opened the yellow door of reality and stepped through it
without looking back, as a new man. And went straight from that convenience store that
you were teleported from to your modest house. To meet these two persons that were the
very reasons that kept you going: your wife and daughter, your true treasure.
                        ''')
                        print("        YOU WON THE GAME!")
                        input("\nPress the Enter key to exit.")
                    else:
                        print('''
(You typed the wrong word to proceed. Maybe a misspelling, maybe trying to find a
hidden solution, maybe as a joke, out of boredom, or who knows what else.

So, please, try again.)
                        ''')

            elif crossing == "swim":
                print('''
You decide that you don't want to wait around but it also doesn't feel right to just
take what could be the lifeline of someone else. Then, you start to stretch yourself
to swin to that island. You run into the water and it takes some time, but, you have
crossed enough distance to see it more clearly. You were just about forty yards away
when you felt the first bite. Your leg was gone and soon other limbs. It was violent
and painful, and you couldn't even make up what was it that attacked you.
                ''')
                print("        GAME OVER!")
                input("\nPress the Enter key to exit.")
            elif crossing == "steal":
                print('''
You decide you don't want to wait around and swimming is just too much work when the
boat is just sitting there, with no owner in sight, so you take it. You push it into
the water and jump inside. You progress smoothly. However, soon you see a man run to
the beach. He shouts and points something at you. The loud noise of powder exploding
reach your ears, and, though he keeps missing, he also keeps firing. It's enough for
making you lose your balance and fall from the boat into the sea. But you are closer
now. You start swimming, but soon you feel the searing pain of your leg being ripped
out of your body by a ferocious bite. You notice you are surrounded by sharks and it
only takes a few moments for they to devour you.
                ''')
                print("        GAME OVER!")
                input("\nPress the Enter key to exit.")
            else:
                print('''
(You typed the wrong word to proceed. Maybe a misspelling, maybe trying to find a
hidden solution, maybe as a joke, out of boredom, or who knows what else.

So, please, try again.)
                ''')
    else:
        print('''
(You typed the wrong word to proceed. Maybe a misspelling, maybe trying to find a
hidden solution, maybe as a joke, out of boredom, or who knows what else.

So, please, try again.)
        ''')
