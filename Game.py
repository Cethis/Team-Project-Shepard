import random

sparkling_vampires = 100
you = 1
armor = 50
wooden_bullets = 35
progress_start = 0
progress_end = 100
progress = progress_start

while you > 0 and sparkling_vampires > 0 and progress < progress_end:
    print sparkling_vampires,you,armor,wooden_bullets,progress
    choice = input("What do you want to do (1->Run!) (2->Shoot?) (3->Stake?)")
    if choice == 1:
        progress = progress+int(random.random()*10)
        print"You have run ",progress," percent to saftey!"
    if choice == 2:
        wooden_bullets -= 1
        number_shot = int(random.random()*3)
        sparkling_vampires -= number_shot
        print "You just shot",number_shot,"Sparkling Vampires in the heart!"
        print "there are",sparkling_vampires,"Sparkling Vampires left."
    if choice == 3:
        sparkling_vampires -= 1
        print"You have staked one vampire in the heart!"
    if sparkling_vampires<0:
        print"You have killed them all!"
    if progress>100:
        print"You have made it to saftey!"
    if wooden_bullets<0:
        print"You run out of bullets, and are left with no hope! You lose the game!"
        