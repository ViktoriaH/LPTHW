from sys import exit


def landing():
    print """
    After wandering a little more you end up on a big landing.
    Now that the trees have cleared you can see that the moon has already risen.
    It's a huge beautiful full moon. Suddenly you hear a loud growl to your right.
    When you turn around you stare into the eyes of five big wolves.
    You begin to panic, what do you do?
    """
    print "Do you run, climb a tree or drop dead?"
    choice = raw_input("> ")

    if choice == "run":
        print "Good try, but wolves are usually faster than humans. The wolves catch up with you instantly."
        print "They eat you alive. Sucks to be you!"
        dead()
    elif choice == "climb a tree":
        tree()
    elif choice == "drop dead":
        print "\tYou drop to the ground, hoping the wolves will think you're dead."
        print "\tThe wolves aren't as stupid as you, though. They enjoy you as their late dinner."
        print "\nYou have horrible instincts, you should've never entered the wodds in the first place!"
        dead()

def tree():
    print """
    You climb onto the nearest tree.
    You are lucky that wolves can't climb, or they would've eaten you right up.
    You make it to the top of the tree and wait. After what feels like hours the wolves finally disappear.
    """
    print "\nDo you climb back down, yes or no?"
    choice = raw_input("> ")

    if choice == "yes":
        print """You climb down and find your way back to the WEGGABELUNG."""
        print "\nDo you now want to try to go the other path?"

        choice = raw_input("> ")
        if "yes" in choice:
                hut()
        elif "no" in choice:
                print """
                You sit down, cry and cry some more.
                Eventually you fall asleep.
                When you wake up a man is standing in front of you.
                He offers you his help and takes you home!
                """
                print "\nCongratulations, you have survided!!!"
                exit()
    elif choice == "no":
        print "You stay up in the tree and fall asleep. Sadly you fall off the tree in your sleep and die."
        dead()

def room():
    print """
    Inside the hut you find a table with some food.
    You decide that the owner can't be too mad if you eat a little bit."""
    print "\nHow much percent of the food do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)

    if how_much < 30:
        print """
        You eat a little bit of the food and then lie down on the couch to rest.
        You wake up when you hear the creaking of the door. You realize too late that you just got caught
        breaking into the house of a stranger.
        An old man walks into the room and stares at you.
        You explain your situation to him and apologize profoundly.
        He accepts your apology and takes you home after making you breakfast with the rest of the food you left."""
        print "\nCongratulations, you have survived!"
        exit(0)
    else:
        print """
        You eat so much of the food that you don't even realize the door opening behind you.
        A man walks in with a shotgun yelling 'Hey, get away from my food!
        That's the last I have and it needs to feed me and my kids for the rest of the week!"""

        print "\nHe then procedes to shoot at you. If only you hadn't been so greedy..."
        dead()

def hut():
    print """
    You make it to an old little hut.
    The door seems to be unlocked.
    """
    print "Do you enter, yes or no?"
    choice = raw_input("> ")
    if choice == "yes":
        room()
    elif choice == "no":
        print "\tYou don't enter the hut and continue wandering around. You eventually get so hungry \n\tthat you eat some berries you find. They were poisonous, you die."
        dead()


def start():
    print """
    You are walking through a forest.
    The sun is beginning to set but it turns out that you can't find your wack back home.
    You wander around aimlessly, hoping for a miracle.
    You make it to a fork in the road, you can either go right, or go left.
    """
    print "\nWhich one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        hut()
    elif choice == "right":
        landing()

def dead():
    print "\nToo bad, but at least you tried!"
    exit(0)

start()
