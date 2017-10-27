def selfish():
    print('\n\n   You say, "Ehh... It\'s only a room away. I\'m sure you can do it." The man replies with a brash tone, \n'
          '\n"I disapprove your selfishness." He gets his motel key out of his pocket. "You should be careful when talking \n'
          '\nto strangers," he says, "and learn how to respect your elders!" He swiftly shoves his key into your throat. \n'
          '\nYou fall to the ground. Blood squirts out of your neck. It\'s deeply stuck inside. As you\'re lying on the \n'
          '\nfloor, gasping for air, the old man looks down on you and says, "That\'ll teach you a lesson. How about you \n'
          '\nchoose better next time, huh? Maybe you\'ll get a less bitter end." \n\n')

    print('\nYou got: Selfish End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def accompany():
    print('\n\n   You say, "Sure thing. It\'s only one room away." "Oh, thank you so much," says the man. "Here\'s the key," \n'
          '\nhe says as he gives you his room key. You accompany him to Room 11. You get there and unlock the door. \n'
          '\nIt\'s dark in there, so you can\'t see much. "Sorry, it\'s a little messy," the man says as he turns on the \n'
          '\nlights. \n')

    print('\n\n   You notice that there\'s nothing but a duffel bag in the room. You get a little creeped out. How is \n'
          '\nthere literally nothing but a bag in this room? What happened to the bed? What motel provides nothing but an \n'
          '\nempty room? You snap out of the little monologue going on inside your head as you see the old man go for his \n'
          '\nbag. He\'s looking for something inside his bag. "I can\'t find it," he says a little frustrated, "Would you \n'
          '\nmind helping me look for my medication?" he asks, "I don\'t think my eyes are what they used to be." \n')

    print('\n\n   You go over to help him and look down into his bag. The next thing you know, you feel a little sting \n'
          '\non your neck. You feel a little drowsy then stumble onto the floor. Your vision is a little blurry, but you \n'
          '\nsee the man looking down on you. You can barely make out the words his saying, but you think he said something \n'
          '\nabout never wanting to leave, or being in paradise forever... \n\n')

    print('\nYou got: Paradise End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def decision_escort():
    invalid = True
    while invalid:
        print('\n\n   You\'re only in front of Room 10. He\'s just that close to his room. You\'re only a few rooms near \n'
              '\nyour room, Room 8. It\'s already late, and you\'re really tired, but the old man must be tired as well. \n\n')

        print('\n\n   1. "Sure thing. It\'s only one room away." [Accompany him to his room] \n'
              '\n\n   2. "Ehh... It\'s only a room away. I\'m sure you can do it." [Let him go by himself] \n\n')

        choice = input('You tell the man...\n\n\n')

        if choice == 1:
            accompany()
            invalid = False
        elif choice == 2:
            selfish()
            invalid = False
        # loop back to start of decision_escort()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def room8_sleep():
    print('\n\n   It\'s late. You want to get as much sleep as possible, so you decide to go to bed. You fall straight down \n'
          '\ninto your bed but eventually fixed yourself to your preferred position, then you slowly went to sleep. \n')

    print('\n\n   A few hours later... \n')

    print('\n\n   You feel like you\'re being dragged on the floor, so you open your eyes. Everything looks a little hazy, \n'
          '\nso you don\'t really know what\'s happening. However, you can barely see the figure of what looks like a guy \n'
          '\nwho\'s pulling you by the leg. You try to focus your vision and then see that the man is the one you saw \n'
          '\nmumbling to himself in the hallway last night! You try moving to get out of his grip, but you can\'t seem \n'
          '\nto move! The man notices you and brings out a syringe containing a purple liquid. Then he injects the fluid \n'
          '\nthrough your neck, and you fall back to sleep. \n\n')

    print('\nYou got: Abducted End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def room8_check():
    print('\n\n   You check the bed to see if there are any stains or bed bugs under the bed sheets or on the mattress. \n'
          '\nYou go into the bathroom and find it to be surprisingly squeaky clean. You check the toilet and test it out, \n'
          '\nand it remarkably works. The receptionist sure gave you one of the good rooms, or maybe this motel is really \n'
          '\ngood. Eventually, you decide to go to sleep. You get to the bed, then suddenly remembered something -- you \n'
          '\nneed to lock the door. You get to the door and lock it. You want to be safe from whatever happens here, like \n'
          '\nthe old man or the hooded guy. After locking the door, you go to bed and sleep. \n')

    print('\n\n   You wake up, and you\'re perfectly fine. You use the toilet and get your luggage. Then, you leave the \n'
          '\nroom and go to the reception office to give back the keys and to pay for staying. You enter your car and \n'
          '\nleave the motel. \n\n')

    print('\nYou got: Safe End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def decision_room8():
    invalid = True
    while invalid:
        print('\n\n   You unlock the door and enter into a fairly decent room. You put down your luggage and take a look \n'
              'of the room. You don\'t see any visible dirt or dust. \n\n')

        print('\n\n   1. [Go to sleep] \n'
              '\n\n   2. [Check the room] \n\n')

        choice = input('You decide to... \n\n\n')

        if choice == 1:
            room8_sleep()
            invalid = False
        elif choice == 2:
            room8_check()
            invalid = False
        # loop back to start of decision_room8()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def ignore():
    print('\n\n   You look away from him to not make any eye contact with him and continued to walk to your room. When you \n'
          '\npassed by him, you noticed that he kept talking about a paradise of some sort. "He must be crazy or something," \n'
          '\nyou think to yourself. You get the thought out of your mind and resume to get to your room. Room 10, Room 9, \n'
          '\nand finally, Room 8 -- your room. \n')

    # decision ring-no_money_ignore-4
    decision_room8()


def ask():
    print('\n\n   You say to the man, "Hey, mister. Are you alright?" He loses his balance and falls forward. You catch \n'
          '\nhim. "Oh, why thank you," he says, "I was just going to my room. Would you kindly bring me to Room 11. It\'s \n'
          '\njust nearby."')

    # decision ring-no_money-ask-4
    decision_escort()


def decision_mumbling():
    invalid = True
    while invalid:
        print('\n\n   You walk toward the other side of the motel. As you\'re walking, you see an old man mumbling to \n'
              '\nhimself walking opposite of your direction. \n\n')

        print('\n\n   1. "Hey, mister. Are you alright? [Show concern] \n'
              '\n\n   2. Nothing. [Ignore him] \n\n')

        choice = input('You say... \n\n\n')

        if choice == 1:
            ask()
            invalid = False
        elif choice == 2:
            ignore()
            invalid = False
        # loop back to start of decision_mumbling()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def suggest():
    print('\n\n   "I might know somebody," you tell them, "but I still get money for this right?" One of the scientists \n'
          '\nsays, "Of course! Certainly! Your contribution is essential to us." You gave the name of someone you knew \n'
          '\nwho you considered as your rival. "Thanks for the suggestion," another scientist says, "We\'ll send this name \n'
          '\nto the team back at HQ to find this person." The man you followed suggests to you, "Would you mind joining us? \n'
          '\nWe need you to get us more people to participate in our experiment." You agree and go into their van. This is \n'
          '\nthe start of your new life in riches. \n\n')

    print('\nYou got: Riches End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def retreat():
    print('\n\n   You tell them you needed to go somewhere. One of the scientists says, "You can\'t go. We\'ve already told \n'
          '\nyou too much." You reply, "I won\'t tell anybody! I promise!" They refuse to comply. They take you in the van \n'
          '\nby force and cover your face with a bag. You hear one of them say, "If you refuse to cooperate, then you\'ll \n'
          '\nbe our lab rat!" Another voice says, "You could\'ve made millions, you know." \n\n')

    print('\nYou got: Lab Rat End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def decision_lab():
    invalid = True
    while invalid:
        print('\n\n   Another says, "What we\'re doing is kinda confidential, but if you get us some subjects, then we\'ll tell \n'
              '\nyou." Someone else says, "So do you know anybody in particular who would be willing to help?" The man who \n'
              '\nbrought you here says, "You don\'t know much about what we\'re doing, but the less you know, the better." \n\n')

        print('\n     1. "I might know somebody..." [Suggest someone] \n'
              '\n     2. "Uh... I think I need to go..." [Retreat] \n')

        choice = input('You tell them... \n\n\n')

        if choice == 1:
            suggest()
            invalid = False
        elif choice == 2:
            retreat()
            invalid = False
        # loop back to start of decision_lab()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def yes_money():
    print('\n\n   You accept his offer and say, "Sure! I\'m down with anything as long as I get money." "Good," he say, \n'
          '\n"Now follow me." He leads you to the back of the motel, and you notice a black van. You get a little cautious \n'
          '\nbut still followed him. The van\'s door opens, and you see a group of three people inside. The man leading \n'
          '\nyou says, "Don\'t worry. We\'re not some gang of thugs." He removes his hood and reveals himself wearing a \n'
          '\nlabcoat. He says, "We\'re just a bunch of scientists in need of test subjects." They each show their I.D. \n'
          '\nto prove it to you. One of them says, "If our experiment comes to a success, we\'ll make millions!" \n')

    # decision ring-yes_money-3
    decision_lab()


def no_money():
    print('\n\n   You tell the man, "No thank you. I\'m good for now." He replies, "Hey, it\'s your loss." He moves \n'
          '\nout of the way and lets you go up the stairwell. You reach the second floor and check your room key. \n'
          '\n"08" is labeled on the key. Room 20 is the first one you see, so Room 8 must be somewhere on the other side \n'
          '\nof the motel. \n')

    # decision ring-no_money-3
    decision_mumbling()


def decision_money():
    invalid = True
    while invalid:
        print('\n\n   The man finally meets you eye to eye. He doesn\'t look harmful, but he doesn\'t look trustworthy either. \n'
              '\nHe then gives you an offer. He asks, "You want to make some easy money?" \n\n')

        print('\n     1. "No thank you. I\'m good for now. [No] \n'
              '\n     2. "Sure! I\'m down with anything as long as I get money. [Yes] \n\n')

        choice = input('You respond... \n\n\n')

        if choice == 1:
            no_money()
            invalid = False
        elif choice == 2:
            yes_money()
            invalid = False
        # loop back to start of decision_money()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def yes_brownie():
    print('\n\n   "Sure," you tell him, "I\'m good with brownies." "Wonderful," he says, "You won\'t be disappointed." \n'
          '\nHe gives you a brownie, and you take a bite. "Not bad," you say, and you really mean it. He grins and responds, \n'
          '\n"Glad you like it. Enjoy your stay in the party." You really like the brownie, so you finish it. \n')

    print('\n\n   After a few minutes, you feel a little trippy. Everything looks psychedelic. You start to think that the \n'
          '\nbrownie was more than you anticipated. You sit down on the floor and close your eyes to stabilize yourself.')

    # go back to decision_party()
    decision_party()


def no_brownie():
    print('\n\n   You tell him, "I think I\'ll stick to the chips." The man responds, "Okay. It\'s your choice, and I respect \n'
          '\nit. Maybe you\'ll reconsider the choice next time." He leaves, and you decide to eat chips and whatever else \n'
          '\nthey had on the table. You continued to party until you passed out. \n')

    print('\n\n   You wake up feeling groggy. You noticed you\'re still in the room and see nobody else there. Your clothes \n'
          '\nare slighty torn, probably from whatever happened in the party. You exit the room and try to find your luggage. \n'
          '\nYou can\'t. You\'ve been robbed! Guess you shouldn\'t have come to the party then. \n\n')

    print('\nYou got: Robbed End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def decision_brownie():
    invalid = True
    while invalid:
        print('\n\n   "Hey," someone says. You turn to see who it is. "Would you like a brownie instead?" some guy says. \n'
              '\nHe looks like one of the hosts here. "What\'s in it?" you ask. He replies, "Oh, just regular brownie stuff." \n'
              '\n"So do you want one?" he asks again. \n\n')

        print('\n     1. "I think I\'ll stick to the chips." [Refuse offer] \n'
              '\n     2. "Sure, I\'m good with brownies" [Accept offer] \n\n')

        choice = input('You answer... \n\n\n')

        if choice == 1:
            no_brownie()
            invalid = False
        elif choice == 2:
            yes_brownie()
            invalid = False
        # loop back to start of decision_brownie()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def bat():
    print('\n\n   You remember about the baseball bat! You go to the closet and grab it. You grip the bat and place your \n'
          '\nhands and bat behind your neck and above your shoulder. You\'re ready for whatever comes at you. Both of you \n'
          '\nstared at each other for a few seconds. Then finally, you decided to attack first. You charge at him and swing \n'
          '\nthe bat as hard as you can. You were so quick that he didn\'t have enough time to dodge the attack. You were \n'
          '\nable to knock him in the head, and he fell to the floor. \n')

    print('\n\n   Angered by the service of the motel, you decide to leave immediately. Lazy receptionist, dirty rooms, \n'
          '\nand lousy security. This has been one of the worst motel experience you\'ve ever had. You get your luggage \n'
          '\nand leave the room. You don\'t even want to return the keys. You get to your car and put your stuff in the \n'
          '\ntrunk. Annoyed, you get in the car and leave the motel. \n\n')

    print('\nYou got: Annoyed End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def fight():
    print('\n\n   Angered due to an interruption in sleep, you get up and charge at the intruder. You were able to grab \n'
          '\nhim at his stomach and ram him to the wall. He groans in pain but still pushes you away from him. He swings \n'
          '\nhis knife at you, but since you don\'t have anything to defend yourself, you block his attack using your hand. \n'
          '\nIt pierces your hand and stings like hell. The intruder pulls the knife out and swings it at you again. Distracted \n'
          '\nfrom pain, you didn\'t block or dodge his attack, so he got you in the stomach and pushed it in further. You \n'
          '\nstart crying in pain, and you slowly lose consciousness. \n\n')

    print('\nYou got: Stabbed End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def run():
    print('\n\n   You get overwhelmed by fear that by instinct, you run to the door. You unlock it and then run as fast \n'
          '\nas you can out of the motel. You left your luggage, wallet, phone, everything. The only things you have are \n'
          '\nyourself and whatever clothes you\'re wearing. \n\n')

    print('\nYou got: Coward End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def decision_intruder(n): ###
    print('\n\n   You arrive in front of your bed and lift up the bedsheets. Surprisingly, it\'s not stained, so you lie \n'
          '\ndown on the bed and fall to sleep. \n\n')

    print('\n\n   A few hours later... \n')

    invalid = True
    while invalid:
        print('\n\n   You\'re lying down on your bed and suddenly start to hear footsteps. You open your eyes a little and see \n'
              '\nthat there\'s someone else in the room! You\'re not entirely sure if there really is someone inside, so you \n'
              '\nfully open your eyes. You notice that there really is someone inside! He notices you, and then he threatens you \n'
              '\nwith a knife! \n\n')

        if n == 0:
            print('\n     1. [Run away] \n'
                  '\n     2. [Fight him] \n\n')
        elif n == 1:
            print('\n     1. [Run away] \n'
                  '\n     2. [Fight him] \n'
                  '\n     3. [Get bat] \n')

        choice = input('You decide to... \n\n\n')

        if choice == 1:
            run()
            invalid = False
        elif choice == 2:
            fight()
            invalid = False
        elif choice == 3 and n == 1:
            bat()
            invalid = False
        # loop back to start of decision_intruder()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def party_stay():
    print('\n\n   You decide to continue partying. You\'re a little hungry, so you go to the food table. There are chips, \n'
          '\ndonuts, burgers, tacos, and a bunch more. You get overwhelmed by how much food they have in the party. ')

    # decision steal-yes_party-party_stay-4
    decision_brownie()


def room13_late():
    print('\n\n   You pick up your luggage and head out of the party to go to your room. The key says, "13," so that\'s \n'
          '\nmost likely the room number. You get to your room and unlock it. You notice it stinks in the room but don\'t \n'
          '\ncare because you\'re too tired from the party. You place down your luggae and immediately decide to go for \n'
          '\nthe bed. \n')

    # decision-steal-yes_party-room13_late-4
    decision_intruder(0)


def decision_stay():
    invalid = True
    while invalid:
        print('\n\n   You check the time and notice you\'ve been in the party for at least an hour. You think on whether you \n'
              '\nshould go to your room or just continue partying. \n\n')

        print('\n     1. "I should probably go to my room now." [Leave] \n'
              '\n     2. "I\'ll just stay for a few more minutes." [Stay] \n\n')

        choice = input('You say to yourself... \n\n\n')

        if choice == 1:
            room13_late()
            invalid = False
        elif choice == 2:
            party_stay()
            invalid = False
        # loop back to start of decision_stay()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def closet(): ###
    print('\n\n   You go to the closet and find out that there\'s a baseball bat inside. There\'s nothing else interesting \n'
          '\nin there, so you go to bed. \n')

    # decision-steal-no_party-closet-4
    decision_intruder(1)


def bathroom():
    print('\n\n   You go to the bathroom and see that the whole bathroom is color brown. You can\'t tell if its the design \n'
          '\nor if it\'s something... You don\'t want to think about it. It also reeks of... yeah it\'s probably that. \n'
          '\nMhm, it\'s most likely and definitely that thing. You can\'t understand why someone would put that all over \n'
          '\nthe bathroom. It\'s just a waste of coffee! Anyway, you get the thought out of your mind and go to the bed. \n')

    # decision-steal-no_party-bathroom-4
    decision_intruder(0)

def decision_room13():
    invalid = True
    while invalid:
        print('\n\n   The room has huge stains everywhere, but you still put down your luggage anyway. You\'re unsure if \n'
              '\nit\'s even safe to be in here, so you decide to check out as much as you can about the room. \n\n')

        print('\n     1. [Check bathroom] \n'
              '\n     2. [Check closet] \n\n')

        choice = input('You decide to... \n\n\n')

        if choice == 1:
            bathroom()
            invalid = False
        elif choice == 2:
            closet()
            invalid = False
        # loop back to start of decision_room13()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def yes_party():
    print('\n\n   "Yeah, definitely!" you say, " I haven\'t partied in days!" "Then I\'m sure this\'ll be a blast," \n'
          '\nshe says. She lets you in the room. You place your luggage near the entrance of the room and go inside. \n '
          '\nThe room is filled with people. There are snacks and drinks. They even have strove lights and a fog machine. \n'
          '\nYou wonder how they were able to fit all of this in, but you just want to party, so you don\'t mind the \n'
          '\nnonsense of this. You dance and party like an animal. \n')

    # decision steal-yes_party-3
    decision_stay()


def no_party(): ###
    print('\n\n   "No, I\'m good," you reply, "I\'m not really much of a party person." She says, "That\'s fine. It\'s \n'
          '\nyour loss for missing a good opportunity." She goes back inside the room, and you continue to find your room. \n'
          '\nYour key has the number "13" on it, so that must be your room. You\'re in front of Room 15, so it\'s just a \n'
          '\nfew steps away. You continue to walk until you reached your room. You unlocked the door, and immediately you \n'
          '\nget a good whiff of the room. It stinks and rots of dead rats or something. They probably haven\'t cleaned this \n'
          '\nroom yet. You begin to regret about stealing one of the room keys, but you persist anyway.')

    # decision steal-no_party-3
    decision_room13()


def decision_party():
    print('\nYou hear music in front of you. It sounds like a party. You open your eyes, look up and see there\'s \n'
          '\na lady in front of a room. The person notices you. \n')

    invalid = True
    while invalid:
        print('\n\n   "Hey, wanna join the party?" she says, "We have plenty of space for one more guest. We\'ve also \n'
              '\ngot a DJ and tons of food." You go to her and take a look inside the room. She wasn\'t joking. \n'
              '\nThere\'s really a huge party with a bunch of people inside. \n\n')

        print('\n      1. "No, I\'m good. I\'m not really much of a party person." [No] \n'
              '\n      2. "Yeah, definitely! I haven\'t partied in days!" [Yes] \n\n')

        choice = input('You tell her... \n\n\n')

        if choice == 1:
            no_party()
            invalid = False
        elif choice == 2:
            yes_party()
            invalid = False
        # loop back to decision_party()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def steal():
    print('\n\n   You stealthily move to the desk and constantly check your surroundings to make sure nobody sees your act.  \n'
          '\nYou get close to the key rack and then successfully grab a motel key. You rush out of the office with your  \n'
          '\nluggage. Nobody saw you, or that\'s what you think to yourself. You get the thought out of your mind and \n'
          '\ndecide to go to your room. You run up the staircase and reach your floor. You ran so fast you tired yourself. \n'
          '\nYou look down with your eyes closed, bend down with your hands on your knees and try to catch your breath.')

    # decision steal-2
    decision_party()


def ring():
    print('\n\n    You go to the counter and ring the bell. It gives a resonating and hollow sound. You wait a while \n'
          '\nfor someone to come. Two minutes pass, and you decide to check your phone. You go to your contacts and \n'
          '\ndecide whether to check up on your family or not. \n')

    print('\n\n    Before you could call someone, you look up. The receptionist appears in front of you. You didn\'t even \n'
          '\nhear the person enter. You talk to the receptionist for a while and eventually got the keys for your room. \n')

    print('\n\n    You head out of the office and go to the stairway that leads to the motel rooms. You see a hooded\n'
          '\nman leaning on the stairway, somewhat blocking the path to your room. As you get closer to the staircase, \n'
          '\nthe man begins to raise his head up. \n')

    # decision ring-2
    decision_money()


def leave():
    print('\n\n   You get upset about the service of the motel for not having a person on duty, so you decide to leave \n'
          '\nand go elsewhere. You go back to your car and put back your luggage. You enter your car, start the engine, \n'
          '\nand move out of the motel. You never went back to place ever again. \n\n')

    print('\nYou got: Depart End \n'
          '\n\nPlay again and see if you get a different ending.\n')


def decision_office():
    invalid = True
    while invalid:
        print('\n\n   You enter the reception office and see nobody on the desk. However, you see that the key rack is  \n'
              '\nopen and within reach from the table. You also notice that there\'s a call bell on the counter. \n\n')

        print('\n     1.    "Luck is on my side today!" [Steal a key from the rack.] \n'
              '\n     2.    "I wonder where the receptionist could be..." [Ring the bell.] \n'
              '\n     3.    "What a lousy service!" [Leave the motel.] \n\n')

        choice = input("You say to yourself... \n\n\n")

        if choice == 1:
            steal()
            invalid = False
        elif choice == 2:
            ring()
            invalid = False
        elif choice == 3:
            leave()
            invalid = False
        # loop back to start of decision_office()
        else:
            print('\n\n   That\'s not one of the choices. Please read the text carefully and choose correctly next time. \n'
                  '\nAhem... \n\n')

###############################################################################################################################


def main():
    # title
    print('                                 The Motel: A Choose Your Own Adventure')

    print('\n\n   You finished college and decided to take some time alone before starting work. You\'ve just left your \n '
          '\ncollege dorm, but you don\'t have that much money to afford to stay somewhere luxurious, so you decide to  \n'
          '\nstay in a motel for a while. You get out of your car and bring out your luggage. You then head over to the \n'
          '\nreception office to rent a room. \n')

    # decision 1
    decision_office()

main()