from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "not configured yet"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "Christmas is dead. Thanks a lot!",
        "Have fun explaining to the kids why Santa didn't bring any presents this year!",
        "Oh come on, it wasn't that hard! You're an elf making sure Christmas happens is your job! ",
        "Seriously, how do you even survive the real world?"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class StartingPoint(Scene):

    def enter(self):
        print """
        Imagine this:
        Everything around you is coated in wonderous, white snow.
        All the houses have sparkling lights all around their roofs and they
        twinkle golden in the night. In the air is a marvellous smell you can't
        quite distinguish. It smells of cinnamon, pine, baked apples and all
        kinds of sweets. You hear church bells ringing in the distance and from
        somewhere you hear joyous melodies.

        You can probably guess where you are. You're at the North Pole - to be
        precise, you're in Santa's Village!

        Why you are here you're asking? Well, you're an elf and it's the night
        before Christmas - where else would you be?

        In the distance you hear a loud roar. When you turn around you see a
        herd of polarbears approaching.
        Behind them they are pulling a large black sleigh.


        Oh no! It's Santas evil twin brother Ranta!
        He's here to ruin Christmas, he has tried it before.
        Santa is sleeping so that he is fit tomorrow to deliver all the presents,
        but if you don't stop Ranta there won't be any presents to deliver!
        Quick, it's up to you, you need to do something!
        """

        return 'hallway'

class Hallway(Scene):

    def enter(self):
        print "You run into Santas Workshop where you just saw Ranta enter."
        print "He is making his way to the gift storage."
        print "You need to do something, "
        print "do you 'yell' at him to stop?"
        print "Or do you 'run' after him?"
        print "Or do you try and take a 'shortcut' to get there earlier?"

        action = raw_input("> ")

        if action == "yell":
            print "You shout out Rantas name as loud as you can, "
            print "he turns around with a diabolical grin on his face and shouts back: "
            print "'Not this year smurf! This year I'm going to win! Christmas will DIE!!!'"
            print "He then whistles loudly and you see a huge polar bear running toward you at full speed."
            print "You try to run but the bear lunges at you and swallows you whole."
            print "\n"
            return 'death'

        elif action == "run":
            print "You run after Ranta, but you are small and he is tall,"
            print "it seems that you need to come up with a new idea to stop him from ruining the holidays."
            print "When Ranta looks over his shoulder, you quickly slide into the room to your right."
            print "\n"
            return 'office'

        elif action == "shortcut":
            print "You run down a corridor to the right, "
            print "hoping you can still remember the shortcut through the hole in the wall"
            print "that was the result of a mice infestation earlier in the year."
            print "After a few more meters you can spot the table under which the hole is"
            print "But to you're surprise someone has finally gotten around to plastering it shut."
            print "You're shortcut is gone and you have now lost valuable time."
            print "When you finally make it to the gift storage room, you can see all of the presents"
            print "in flames. Next to them stands Ranta laughing and dancing of joy."
            print "\n"
            return 'death'
        else:
            print "Type only one of the given answers and type correctly!"
            print "\n"
            return 'hallway'


class Office(Scene):

    def enter(self):
        print "\n"
        print "Lucky for you it is Santas office you have entered."
        print "On his desk you see his computer with its multiple security camera screens."
        print "You know that from there you can lock and unlock all of the doors in the building,"
        print "you quickly climb on to the desk chair and open the security program."
        print "On the camera you can see Ranta has almost reached the storage room."
        print "When you try to lock the door to the storage room the computer asks for a code."
        print "\n"
        print "The code is 4 digits, but if you get it wrong 3 times the computer"
        print "will think you are an intruder and lock the office door from the outside"
        print "so that you can't get out unless someone unlocks it from outside."
        code = "%d%d%d%d" % (2,4,1,2)


        guesses = 0

        while guesses < 3:
            guess = raw_input("[type code here]> ")
            if guess == code:
                break
            print "unlocked"
            guesses += 1

        if guess == code:
            print "\n"
            print "The security program unlocks and you are able to"
            print "lock any door in the building."
            print "You quickly find the gift storage room door and click on 'lock'."
            print "\n"
            return 'junk_room'
        else:
            print "The computer buzzes and shuts itself down."
            print "Behind you you can hear the door lock itself - you are trapped."
            print "All you can do now is hope that someone will find you in the morning and unlock the door."
            print "You sit and watch on the security cameras as Ranta enters the storage room"
            print "and sets fire to all of the presents that were so lovingly"
            print "wrapped by you and all your fellow elves."
            print "\n"
            return 'death'

class JunkRoom(Scene):

    def enter(self):
        print "\n"
        print "On the cameras you can see Ranta failing to open the door to the"
        print "storage room."
        print "Angrily he tries to force it open. He kicks it and smashes it,"
        print "but the door won't budge."
        print "You think he is about to give up when he grabs a flame thrower"
        print "from his backpack. While the door doesn't give in yet"
        print "you know that the metal won't hold up for too long."
        print "You need to do something to stop him!"
        print "\n"
        print "You leave the office and sneak down the hall."
        print "A few doors down you see the door to the junk room, you enter."
        print "\n\n"
        print "Surely you must be able to find something in here to defeat Ranta with."
        print "But you need to be quick, and you're small so can only grab a few things."
        print "In the distance you hear Ranta's triumphant laugh."
        print "Oh no, he must have succeeded in burning down that door, hurry!"
        print "YOu quickly shove some things in your backpack, hoping they'll be helpful"
        backpack = ['fire extinguisher', 'marbles', 'rope']
        print "And run to the storage room."

        return 'storage_room'


class StorageRoom(Scene):

    def enter(self):
        print "\n"
        print "In the storage room you see Ranta standing by the wrapped presents"
        print "turning his flame thrower on and pointing it at the gifts."
        print "You yell out 'STOP!' and Ranta turns to face you. He drops the"
        print "flame thrower and runs towards you. Quickly you open your bag to"
        print "see what's inside:"
        backpack = ['fire extinguisher', 'marbles', 'rope']
        print backpack
        print "\n"
        print "What do you use first?"

        action = raw_input("> ")

        if action == "marbles":
            print "You pour out the jar of marbles that you packed and Ranta"
            print "runs right into them, stumbling and falling to the ground."
            print "\n"
            print "What do you use next?"
            actionb = raw_input("> ")
            if actionb == "rope":
                print "You run to Ranta and tie him up with the rope you brought."
                print "You then run towards the presents that have caught on fire"
                print "and extinguish them with the fire extinguisher you brought"
                print "along as well."
                return 'finished'
            elif actionb == "fire extinguisher":
                print "You activate the fire extinguisher and point it at Ranta."
                print "He rolls around growling but then gets up and catches you."
                print "The foam doesn't bother him the tiniest bit. He throws"
                print "you into the burning present pile and walks away laughing."
                return 'death'
            else:
                print "Type only one of the given answers and type correctly!"
                print "\n"
                return 'storage_room'

        elif action == "fire extinguisher":
            print "You blast your fire extinguisher at Ranta but he just keeps"
            print "running toward you. You turn to run from him but he quickly"
            print "catches you and throws you into the pile of presents"
            print "that have caught on fire from the flame thrower that he dropped."
            print "\n"
            return 'death'
        elif action == "rope":
            print "You grab your rope, which is conveniently tied into a lasso"
            print "and swing it at Ranta. You miss and try again and miss."
            print "You try one more time and miss once more. Ranta runs to you"
            print "and catches you. He then throws you into the flames that"
            print "are the christmas presents for kids all over the globe."
            print "They must have caught on fire from the flame thrower on the ground."
            print "Your last thought was that you should've taken that lasso"
            print "workshop for elves Santa organized in the summer."
            print "\n"
            return 'death'
        else:
            print "Type only one of the given answers and type correctly!"
            print "\n"
            return 'storage_room'


class Finished(Scene):

    def enter(self):
        print "\n"
        print "You have made it! Ranta is defeated and Santa has taken care of him!"
        print "Christmas is saved, you have literally saved the jolliest holiday!"
        print "Saved it all by yourself, you little elf."
        print "Congratulations, elf."
        print "\n"
        print "When Santa wakes up and realizes your heroism he rewards"
        print "you with a big ceremonious party where he nominates you as"
        print "master elf."
        print "\n"
        print "Merry Christmas, master elf!"

        exit(0)

class Map(object):

    scenes = {
        'starting_point': StartingPoint(),
        'hallway': Hallway(),
        'office': Office(),
        'junk_room': JunkRoom(),
        'storage_room': StorageRoom(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('starting_point')
a_game = Engine(a_map)
a_game.play()
