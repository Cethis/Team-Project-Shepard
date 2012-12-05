import random

intro_text = """You stand outside, the bright sunlight blidning you momentarily. After your eyes clear you look around, noing the debree and rubble you shake your head before noticng a sewer entrance in the distance.
"""

def run():
    print intro_text
    choice = input("What do you want to do (1->go left) (2->go right) (3->go staight) (4->go into sewer)")
    if choice == 1:
        print "You Go left, in the distance you see somthing interesting."
        choice = input("What is your course of action? (5->continue 6->kill yourself)")
        if choice == 5: 
            print "You continue tword the pretty pretty bright light and a zombie kills you with his crowbar"
            print "YOU LOSE, RESTART THE GAME LOSER"
        if choice == 6: 
            print "You take out your shotgun,realizing you have no hope, and blow off your head"
            print "YOU LOSE, RESTART THE GAME LOSER"
    if choice == 2:
        print "You Go right and are forced around the corner into a herd"
        print "YOU LOSE, RESTART THE GAME LOSER"
    if choice == 3:
        print "you go staight and in the distance you see a mechanics shop and hear gunfire"
        choice = input("What do you want to do? (7->run to help) (8->go back) (9->cautiously move forward)")
        if choice == 7:
            print "You run to help and the person inside shoots you in the head and your brain splatters all over the wall"
        if choice == 8:
            print "You go back to where you started, and throw yourself off a cliff"
        if choice == 9: 
            print "You get to a group of survivors losing people quickly, you help them push back the zombie. After a few minutes and once the people are healed, they decide to travel with you."
    if choice == 4:
        print "You find yourself in the dark without any scource of light. You 9are forced to commit suiside"
        print "GAME OVER"
        print "PLEASE RESTART THE GAME LOSER"
        print "P.S. DID YOU REALLY THINK THAT WOULD WORK?"
        








