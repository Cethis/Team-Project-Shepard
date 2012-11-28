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












