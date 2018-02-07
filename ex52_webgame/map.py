class Scene(object):

    def __init__(self, title, urlname, description, m_choice):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}
        self.m_choice = m_choice

    def go(self, direction):
        default_direction = None

        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

waking_up = Scene("Waking Up", "waking_up",
"""
You slowly open your eyes, blinking against the bright light shining straight into your face.
It takes a few seconds for you to fully open your eyes, straining them to focus on your surroundings.
Your head is pounding, like you have been partying for a week straight. You sit up and look around.

Wait a second. Where the fuck are you? You're definitely not hungover in your bedroom.

You turn and look around when suddenly you stare into two big brown curious eyes. It takes a second until you realize
the pair belongs to a huge tiger.
""",True)

the_boulder = Scene("Behind the boulder", "the_boulder",
"""
You silently crawl away, never losing eye contact with the huge animal.
Your foot crashes into a big boulder, behind which you hide. Hopefully this will allow you a moment
to think about what is happening.
You take a moment to look around and suddenly you remember what has happened.

You went to the zoo on a class trip. Everything went great until you tried to catch a young child that was about to
fall into the tiger enclosure. Well shit, the child seems to be fine but you must have fallen instead.
That would also explain the huge headache. Probably a nice concussion...
But how are you supposed to get out of here alive and why is noone coming to save you?
No time to contemplate your life choices anymore, the tiger is moving towards you.
What do you do?
""", True)

the_crawl = Scene("The Crawl", "the_crawl",
"""
Crawling around the jungle-like enclosure, you desperately look for someway to escape.
You assume that you have to find the fencing to find some door out but you have yet to see the fence.
You are now faced with a forest on one side, a big rock wall on the other and the two tigers you know of behind you.
""", True)



the_forest = Scene("The Forest", "the_forest",
"""
You make it to the forest and after walking a few meters you suddenly are faced with another tiger.
Oh man, how many tigers live here?!
You react instantenously and climb up a large tree. The tiger scratches and shakes the whole tree.
You better not fall! Slowly you make your way up the tree and once at the top you where the
rock wall ends. It's about a 2 meter jump but if you make it, you'll be able to run towards the enclosures
fencing. There surely must be a way out somewhere around there.
""", True)


the_landing = Scene("The Landing", "the_landing",
"""
Quickly you just go for it and jump of the tree. You barely make it to the landing, but you make it.
Below you you can see the three tigers trying to climb up the tree. Those three seem occupied for a
little bit. Let's hope there isn't anymore tigers around!
""", True)


the_gate = Scene("The Gate", "the_gate",
"""
You walk around and finally find the gate you have been searching for. Your head is still pounding and
a gut feeling tells you that the tigers have realized that you are no longer in the tree and are searching for you.
Slowly you sneak towards the gate that leads to the inside enclosure. You hope it's open, but you're not in luck,
it's locked. Looking around you find a keypad. But what could the code be? After some further inspection
you find three different 4-digit-numbers scribbled next to the lock.
Which one do you type in?
""", True)

the_end_winner = Scene("You Made It!", "the_end_winner",
"""
Congratulations, you have entered the correct pin! The door buzzes open and you quickly slide inside before the tigers,
that are now running at you full speed, catch up with you. They jump up the metal bars of the gate and you almost get hit
by one of the gigantic paws. But the door is now between you and the killer animal. You are save!

Finally a zookeeper comes running to the cages and let's you out. After being treated in the hospital
for a concussion and some minor injuries, you are being honored in a ceremony for your brave action
to save the child and getting yourself into danger.
""", False)

# the deaths:
run_death = Scene("Too slow.", "run_death",
"""
You try to run away, but how on earth would you outrun a tiger?! Ofcourse he immediately catches you...
And eats you.
""", False)

right_death = Scene("Oh Crap", "right_death",
"""
You crawl right into the arms of another tiger, a hungry one, too. He chomped you down within seconds...
""", False)

stay_death = Scene("Stupid you", "stay_death",
"""
You sit still, not daring to take a breath. But the tiger can smell your fear, possibly because you wet yourself...
You smell terrified, but apparently tigers love the smell of terrified humans. One big pounce and he takes you down.
""", False)

rock_wall_death = Scene("Rock Wall", "rock_wall_death",
"""
You start climbing up the rock wall, but the higher you get, the steeper the wall gets.
Soon you are struggling to get a good grip to climb higher. You are almost at the top and you can
see the enclosures wall, but then your foot slips of the wall and you plummeth down.
By now the tigers have realized where you were going and they decide that you are today's lunch...
""", False)

tree_death = Scene("Too late", "tree_death",
"""
You stay in the trees thinking about the jump, a second too long. The moment you jump,
the tigers on the ground shake the tree in such a way that you can't properly jump off.
You slip and fall down to the ground. Luckily you pass out, so you don't really feel the tigers
eating your face off.
""", False)

left_landing_death = Scene("Oops", "left_landing_death",
"""
You wander around and find an opening in a rock. Maybe that's the passage to the cages?
Through the inside cages is your only way out of here. You slowly enter the dark cave but instead of
finding a gate you find a mother tiger with her cubs. She immediately takes the initiative to teach
her cubs how to hunt for food. You were great help but also dinner.
""", False)

the_end_death = Scene("Oh no...", "the_end_death",
"""
Desperately you try a pin. The door buzzes when suddenly the keypad starts to smoke and spark.
A second later the the whole thing explodes with a loud bang. You are startled but ok. The door on the other hand
is not open and without a keypad it probably won't. But look! The bang has finally attracked a zoo keeper!
You start crying out of joy, but as soon as you see the zoo keepers shocked expression you can feel the presence
of the tigers behind you. The explosion attracted them as well. You look in the zoo keepers traumatized eyes
when you feel the jaw of a tiger locking in around you're neck.

So close and yet so far...
""", False)

# Define the action commands available in each scene
waking_up.add_paths({
    'crawl':the_boulder,
    'run':run_death
})
the_boulder.add_paths({
    'left': the_crawl,
    'stay': stay_death,
    'right': right_death
})
the_crawl.add_paths({
    'climb the rock wall': rock_wall_death,
    'crawl in the forest': the_forest
})
the_forest.add_paths({
    'jump':the_landing,
    'hesitate':tree_death
})
the_landing.add_paths({
    'left':left_landing_death,
    'right':the_gate
})
the_gate.add_paths({
    '9692': the_end_winner,
    '1589': the_end_death,
    '4628': the_end_death
})





# Make some useful variables to be used in the web application
SCENES = {
    waking_up.urlname : waking_up,
    the_boulder.urlname : the_boulder,
    run_death.urlname : run_death,
    stay_death.urlname : stay_death,
    right_death.urlname : right_death,
    the_crawl.urlname : the_crawl,
    the_forest.urlname : the_forest,
    rock_wall_death.urlname : rock_wall_death,
    tree_death.urlname : tree_death,
    the_landing.urlname : the_landing,
    left_landing_death.urlname : left_landing_death,
    the_end_winner.urlname : the_end_winner,
    the_end_death.urlname : the_end_death





}
START = waking_up
