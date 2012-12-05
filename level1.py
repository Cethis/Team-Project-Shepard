import random

intro_text = """It had been a long night. Your boss had not let you off until far later than normal. You realized that the only thing you got to look forward to, was your nice, warm bed back home. You took the time to get some water and a quick bite to eat from the fridge before heading to bed. It was some time later, you could not tell when due to the lack of a clock. You checked your phone and realized it was far to early to be up. You raise your head as a noise starts to come from the door, rising from the bed you look to the door. A growling from behind the door causes you to jump. looking around for the nearest item. You know there is a knife under your pillow, and a shotgun in the closet.
"""

def run():
    print intro_text
    choice = input("What do you want to do (1->Grab knife) (2->Grab Shotgun) (3->open door with nothing)")
    if choice == 1:
            print "You rush for the knife, grasping it in your hand you turn to face the door. Your footsteps slow and sure as you grip the doorknob. Turning it slightly you scream out in shock and horror to see a fiendish creature. The head has been nearly severed in half and its eyes remain dull. It rushes in the room once the door had been opened, running straight for you. You grasp the knife and in a last ditch effort, stab the creature in the head. It watches you for a moment before falling back, making a large thud on the ground."
    if choice == 2:
            print "You hold the shotgun with on hand as you throw the door open. You remain at a loss for words as something rushes in, not bothering to check what it is you squeeze the trigger, the shell firing out of the barrel and striking the beast. You fire again, not sure if you hit it the first time. As the creature falls to the floor you shudder as you look down upon it. It is something from your worst nightmares, the eyes are dull, and half the face is missing. The body looks beyond repair with several bullets lodged into it. You raise your head as hear more growling in the distance"
    if choice == 3: 
           print "You open the door, not thinking much of it. A creature rushes in, trying to grab at you as you stumble back. Landing on top of you, you barely have time to raise your hands in defense. You realize this was a mistake as the creature bites into your hand. You scream out in anguish as you lower your hand. The beast dives for your throat, latching on to it. You eyes dull as your body ceases to breath."
           print "GAME OVER!"
    if choice == 1:
        print "you continue through the apartment, having already dressed you try the tv and realize the power it off. Walking out of the door you look around before continuing. "
    if choice == 2: 
        print "You rush to the door, poking your head out you look down the hall. You notice your door has been broken off the hinges and several zombies are starting to rush through the door. Holding your gun up to your shoulder you look down the sights, aiming and firing. Some time later you pant heavily as the horde has stopped, leaning against the door you let out a low sigh before pushing off the door and continue on your way."
    print "You move down the hallway of the apartment building. You hear a shuffling behind you, when you turn your head to look back, you see nothing."
    choice = input ("What do you do? (4-> Continue walking) (5-> Go back) (6-> Knock on the door next to you)")
    if choice == 4:
        print "You continue down the hall, looking around warily as you keep your guard up."
    if choice == 5:
        print "You walk back into your apparment, looking around you realize you should grab a few items. Walking into your closet you take the shotgun, and a medkit from the bathroom."
    if choice == 6:
        print "As you knock on the door you cringe as you hear something move behind it. Taking the shotgun you point it at the door before opening it. A short black and white blur tackles you to the ground before you feel warm breath upon your face. Saying your final prayers you open your eyes, only to be greeted by the sight of a dog. You push it off of you and get up, shaking your head as you continue down on your way. You realize the dog is following you after several yards of walking. You realize that it will follow you for awhile, and you decide to let it."
    print "You continue on your way through the apartment. Your eyes warily searching for more dnager as your dog sniffs around.You continue down the stairs, cringing as your footsteps echo through it. Keeping the shotgun close to your shoulder you move floor by floor. As you make it to the lobby you look around. Blood stains the floor and the lobby seems half destroyed. You look out the glass door to realize it is broken. Stepping to it you push it open, stepping outside."


