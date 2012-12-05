print " Begin level 3"

print "You wake up quickly, at first scared beyond belief. You are in an RV, and it's moving."
print " It has been some time since you have had people around you. after recovering from the mild heart attack you feel you have just had, you get up and walk to the passenger seat. As you walk through the RV you pass some other survivors (asleep of course). You stop for a moment and see a man that looks very familiar, but you can't place him. You continue on to the front only to find a kind elderly lady driving. You sit down."
print "Hey! Who said you could sit there?!"
print "Oh I'm sorry I didn't....."
print "You start to stand back up"
print "Now, Now I'm only kidding dear, sit back down. I could use the company"
print "Oh alright."
print "It must have been some time since you were around the living. huh? Well Maybe your dog..."
print "Uh... well I've only just met him a few minutes before you."
print "Oh I see, well never the less he is in the van with the children behind us."
print "I'm sure they enjoy that"
print "Well they need what they can get. After all this has become a pretty scary world."
print "Yeah....Hey, What happened? I remember meeting up with you, and fighting. However I do not recall getting in the RV."
print "Well you sustained a concussion, After you showed up...... What the hell is that?!?!"
print "Stop the car!"

print "A sea of the undead lay before you, And you can't just push through because the road is blocked by a military checkpoint that was there before the infection got bad."

print "There might be some useful things in there, like ammo and guns. Maybe even a bunch of M.R.E.'s. We should see what there is."
print "Maybe we should focus on not gettin eaten!"
print "The man from earlier stands up. EVERYBODY UP!"
print "He wakes everyone up and starts passing out guns."
print "Everybody get on the the vehicle. It'll be safe up there."
print "Good Idea there boy"
print "I've had some experience with this sort of thing"
print "Ha! Prove it."


choice = input ("(1-> Go up to the top)(2-> Run out on your own)")
if choice == 1:
    print "You climb onto the roof"
if choice == 2: 
    print "You jump out of the vehicle and almost immediately get attacked by a zombie. You manage to fight it off and get back in the RV. Then climb to the roof."


import random

zombies = 100
hero = 1
shotgun_rounds = 20
armor = 50
progress_start = 0
progress_end = 100
progress = progress_start
while hero>0 and zombies>0 and progress<progress_end:
    print zombies,hero,armor,shotgun_rounds,progress
    progress = 3 + progress
    choice = input("What do you want to do (1->Nothing?) (2->shoot) (3->Melee)")
    if choice == 1:
        print "You did nothing"
    if choice == 2:
       shotgun_rounds -= 1
       number_shot = int(random.random()*12)
       zombies = zombies-number_shot 
       print "You just shot",number_shot,"zombies!"
       print "there are",zombies,"zombies left."
    if choice == 3: 
       print "you hit a zombie"
       print "there are fewer zombies"
       armor -= 4
       zombies -= int(random.random()*7)
    if zombies == 0:
       print "YOU WIN!"
    if armor < 1:
       print "You lost"
       break
   
print "You realize that the RV has moved up to the checkpoint. Without a word you jump off onto the roof of the checkpoint and open the gates for the RV"

choice = input ("(1-> Check around for food and weapons) (2-> Get back on the RV)")
if choice ==1:
    print "you come upon a T in the corridor, The sight says Left for Armory Right for Mess Hall"
    choice = input ("(1-> Left) (2-> Right)")
    if choice == 1:
        print "You run down the hall and into the armory. Kill a zombie and notice that your choice is rewarded. Along with the guns and ammo two boxes of M.R.E.s sit next to the Assault rifle ammo."
    if choice == 2:
        print " You run into the mess hall. Low and behold 15 boxes of M.R.E.s and on top sits an Assault rifle and a box of ammo."
        print "You run back to the RV"
import random

zombies = 100
hero = 1
shotgun_rounds = 20
armor = 50
progress_start = 0
progress_end = 100
progress = progress_start
while hero>0 and zombies>0 and progress<progress_end:
    print zombies,hero,armor,shotgun_rounds,progress
    progress = 3 + progress
    choice = input("What do you want to do (1->Nothing?) (2->shoot) (3->Melee)")
    if choice == 1:
        print "You did nothing"
    if choice == 2:
       shotgun_rounds -= 1
       number_shot = int(random.random()*25)
       zombies = zombies-number_shot 
       print "You just shot",number_shot,"zombies!"
       print "there are",zombies,"zombies left."
    if choice == 3: 
       print "you hit a zombie"
       print "there are fewer zombies"
       armor -= 4
       zombies -= int(random.random()*7)
    if zombies == 0:
       print "YOU WIN!"
    if armor < 1:
       print "You lost"
       break
   
if choice == 2: 
     import random

zombies = 100
hero = 1
shotgun_rounds = 20
armor = 50
progress_start = 0
progress_end = 100
progress = progress_start
while hero>0 and zombies>0 and progress<progress_end:
    print zombies,hero,armor,shotgun_rounds,progress
    progress = 3 + progress
    choice = input("What do you want to do (1->Nothing?) (2->shoot) (3->Melee)")
    if choice == 1:
        print "You did nothing"
    if choice == 2:
       shotgun_rounds -= 1
       number_shot = int(random.random()*15)
       zombies = zombies-number_shot 
       print "You just shot",number_shot,"zombies!"
       print "there are",zombies,"zombies left."
    if choice == 3: 
       print "you hit a zombie"
       print "there are fewer zombies"
       armor -= 4
       zombies -= int(random.random()*7)
    if zombies == 0:
       print "YOU WIN!"
    if armor < 1:
       print "You lost"
       break
   
print "After you finally get down the road and through the hoard of zombies, Your new group does a headcount and find that everyone is accounted for. "
print "Good job boy. Everyone is still here, Thank you"
print "I didnt do anything you couldnt have."
print "No you managed to make sure my group got through that. Take whatever small victories you can get. Otherwise this life will consume the humanity you have left."
print "Then you are very welcome sir."
print "Carter, James Carter. Everybody just calls me Carter though."
print "Well then....."
print "Now...Let's introduce you to your new family. I know they are eager to meet you..... What it your name?"
print "I am ____"
print "Nice to meet you ____"
noun = raw_input ("Enter your name")
text = text.replace ("____",noun)
print "The lady from before, Thats Jane"
print "Jane: Hey were about to get moving but there is someone who want to see you"
print "The door to the RV swings open and your dog comes running in, knocks you over onto the floor and starts licking you again. It seems you have finally found a place for yourself."
print "End"