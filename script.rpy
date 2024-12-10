# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

$ import random

define mc = Character("[povname]")
default possible_outings = ['kitchen','backyard','living room','outside']

label start:
    default positive_identity_points = 0
    default negative_identity_points = 0

    $ povname = renpy.input("What is your name?", length=32)
    $ povname = povname.strip()

    if not povname:
        $ povname = "???"
        jump no_name_route
    
    scene pra_a1_day1

    "\*Complete slience\*"
    "An alarm goes off"
    "You've just woken up and you are surrounded by the view of your room as normal as can be."
    mc "Time to get ready for another day?"
    "You go to rub your eyes and try and get whatever is covering your eyes off but...."
    "your hands seem to go {u}straight through your face{/u} as if there was nothing there."
    mc "{b}AHHHHH{/b}"
    "You immediately pull your hands away and as you do a question comes to your mind..."
    mc "{i}Who am I?{/i}"
    "As you think of this and the mysterious \"disapperence\" of your face, emotions of deep emptiness consume you."
    "You know who you are. Right?"
    menu:
        "Yeah":
            mc "I'm [povname]"
            jump scene1
        "No, I think I had a different name.":
            jump choice1_a
    label choice1_a:
        $ povname = renpy.input("What is your name?", length=32)
        $ povname = povname.strip()
        if not povname:
            jump choice1_a
        else:
            mc "I remember now. Yeah, I'm [povname]."
            jump scene1

label scene1:

    scene pra_a1_day1

    "\*deep breaths\*"
    mc "Okay, everything is going to be fine"
    "As your emotions calm in a sense of morbid curiosity, you gingerly the edge of cavity in your face"
    "You shiver as you register the oddly smooth feeling as you trace the hole in your face"
    "You reach deeper putting your full finger in and further unsettle yourself but you quickly pull your hand out"
    mc "I need to focus up."
    "Despite the emptiness you feel, you feel if you can just find the things that make you...you"
    "You fee like you'll face back"
    mc "Okay lets am I going to go"
    call activity_select

label activity_select:

    menu:
        "Let's make some breakfast in the kitchen" if 'kitchen' in possible_outings:
            $ possible_outings.remove('kitchen')
            jump scene_kitchen

        "There's probably something in the backyard" if 'backyard' in possible_outings:
            $ possible_outings.remove('backyard')
            jump scene_backyard

        "Let's think about this further in the living room" if 'living room' in possible_outings:
            $ possible_outings.remove('living room')
            jump scene_livingroom

        "Maybe I can find something outside" if 'outside' in possible_outings:
            $ possible_outings.remove('outside')
            jump scene_outdoors


label scene_kitchen:
    if positive_identity_points == 0 or negative_identity_points == 0:
        jump scene_kitchen_day
    if positive_identity_points == 1 or positive_identity_points == 2 or negative_identity_points == 1 or negative_identity_points == 2:
        jump scene_kitchen_afternoon
    if positive_identity_points == 3 or negative_identity_points == 3:
        jump scene_kitchen_night

label scene_kitchen_day:

    scene kitchen_1_day

    "You head to the kitchen to make yourself some food"
    "You gather some ingredients to make your stuff some breakfast"
    $ foodname = renpy.input("What do you make?", length=32)
    $ foodname = povname.strip()
    $ possible_quality = ['bad','okay','good','amazing']
    $ quality = random.choice(possible_quality)
    "You made [quality] [foodname]"
    "You are wondering if you enjoyed this activity?"

    menu:
        "Yeah":
            mc "I like that"
            $ positive_identity_points += 1
            call activity_select
        "Not really":
            mc "This is not something I'll do again"
            $ negative_identity_points += 1
            call activity_select

label scene_kitchen_afternoon:

    scene kitchen_1_afternoon

    "You head to the kitchen to make yourself some food"
    "You gather some ingredients to make your stuff some lunch"
    $ foodname = renpy.input("What do you make?", length=32)
    $ foodname = povname.strip()
    $ possible_quality = ['bad','okay','good','amazing']
    $ quality = random.choice(possible_quality)
    "You made [quality] [foodname]"
    "You are wondering if you enjoyed this activity?"

    menu:
        "Yeah":
            mc "I like that"
            $ positive_identity_points += 1
            call activity_select
        "Not really":
            mc "This is not something I'll do again"
            $ negative_identity_points += 1
            call activity_select

label scene_kitchen_night:

    scene kitchen_1_night_light

    "You head to the kitchen to make yourself some food"
    "You gather some ingredients to make your stuff some dinner"
    $ foodname = renpy.input("What do you make?", length=32)
    $ foodname = povname.strip()
    $ possible_quality = ['bad','okay','good','amazing']
    $ quality = random.choice(possible_quality)
    "You made [quality] [foodname]"
    "You are wondering if you enjoyed this activity?"

    menu:
        "Yeah":
            mc "I like that"
            $ positive_identity_points += 1
            call finale1
        "Not really":
            mc "This is not something I'll do again"
            $ negative_identity_points += 1
            call finale1

label scene_backyard:
    if positive_identity_points == 0 or negative_identity_points == 0:
        jump scene_backyard_day
    if positive_identity_points == 1 or positive_identity_points == 2 or negative_identity_points == 1 or negative_identity_points == 2:
        jump scene_backyard_afternoon
    if positive_identity_points == 3 or negative_identity_points == 3:
        jump scene_backyard_night

label scene_backyard_day:

    scene backyard_2_day

    "You head to the backyard and swim some laps"
    $ possible_lap_amomunt = ['10km','1km','3km','40km']
    $ laps = random.choice(possible_lap_amomunt)
    "You did [laps]!"
    "Just don't think the amount of watewr that entered through the hole in your face"
    "You are wondering if you enjoyed this activity?"

    menu:
        "Yeah":
            mc "I like that"
            $ positive_identity_points += 1
            call activity_select
        "Not really":
            mc "This is not something I'll do again"
            mc "Why do I have this in my house"
            $ negative_identity_points += 1
            call activity_select

label scene_backyard_afternoon:

    scene backyard_2_afternoon

    "You head to the backyard and swim some laps"
    $ possible_lap_amomunt = ['10km','1km','3km','40km']
    $ laps = random.choice(possible_lap_amomunt)
    "You did [laps]!"
    "Just don't think the amount of watewr that entered through the hole in your face"
    "You are wondering if you enjoyed this activity?"

    menu:
        "Yeah":
            mc "I like that"
            $ positive_identity_points += 1
            call activity_select
        "Not really":
            mc "This is not something I'll do again"
            mc "Why do I have this in my house"
            $ negative_identity_points += 1
            call activity_select

label scene_backyard_night:

    scene backyard_2_night_light

    "You head to the backyard and swim some laps"
    $ possible_lap_amomunt = ['10km','1km','3km','40km']
    $ laps = random.choice(possible_lap_amomunt)
    "You did [laps]!"
    "Just don't think the amount of watewr that entered through the hole in your face"
    "You are wondering if you enjoyed this activity?"

    menu:
        "Yeah":
            mc "I like that"
            $ positive_identity_points += 1
            call finale1
        "Not really":
            mc "This is not something I'll do again"
            mc "Why do I have this in my house"
            $ negative_identity_points += 1
            call finale1

label scene_livingroom:
    if positive_identity_points == 0 or negative_identity_points == 0:
        jump scene_livingroom_day
    if positive_identity_points == 1 or positive_identity_points == 2 or negative_identity_points == 1 or negative_identity_points == 2:
        jump scene_livingroom_afternoon
    if positive_identity_points == 3 or negative_identity_points == 3:
        jump scene_livingroom_night

label scene_outdoors:
    if positive_identity_points == 0 or negative_identity_points == 0:
        jump scene_outdoors_day
    if positive_identity_points == 1 or positive_identity_points == 2 or negative_identity_points == 1 or negative_identity_points == 2:
        jump scene_outdoors_afternoon
    if positive_identity_points == 3 or negative_identity_points == 3:
        jump scene_outdoors_night

label no_name_route:
    "\*Complete slience\*"
    "An alarm goes off"
    "You awaken to find yourself in complete darkness" 
    mc "Why the hell is my alarm going of in the middle of the night?"
    "You've just woken up but you are surrounded by an absolute darkness where you can't see anything"
    mc "What the hell is going on?"
    "You sit up in your bed and look around but find yourself still devoured by this complete darkness"
    "You go to rub your eyes and try and get whatever is covering your eyes off but...."
    "your hands seem to go {u}straight through your face{/u} as if there was nothing there."
    mc "{b}AHHHHH{/b}"
    "You immediately pull your hands away and as you do a question comes to your mind..."
    mc "{i}Who am I?{/i}"
    "As you think of this and the mysterious \"disapperence\" of your face, emotions of deep emptiness consume you."
    "You know who you are. Right?"

    jump choice1_alt
    label choice1_alt:
        $ povname = renpy.input("What is your name?", length=32)
        $ povname = povname.strip()

        if not povname:
            $ povname = "Hollow"
            mc "I actually don't know. I guess I'm just hollow"
            jump altscene1
        else:
            mc "I remember now. Yeah, I'm [povname]."
            jump scene1

label altscene1:        
    "The feeling of emptiness flares to a degree, you don't even feel {i}human anymore{/i}."



label finale1:
    if positive_identity_points == 4 and negative_identity_points == 0:
        return
    elif positive_identity_points == 3 and negative_identity_points == 1:
        return
    elif positive_identity_points == 2 and negative_identity_points == 2:
        return
    elif positive_identity_points == 1 and negative_identity_points == 3:
        return
    elif positive_identity_points == 0 and negative_identity_points == 4:
        return
    else:
        return

