import time
import sys
import os
import keyboard

#if __name__ == '__main__':
    #main()

playerName = input("Enter your name: ")

print(playerName + " Woke up in a dark room. You try to see, but the room is so dark that you can't see anything.")
time.sleep(2)
print("")
print("Press: -(a) you start crawling on the floor")
print("Press: -(s) You stand up and try walking around")
print("Press: -(d) You stay STILL!!") 

choice1 = input("Enter choice: ")


if choice1 == 'a':
    os.system('clear')
    time.sleep(3)
    print("          ")
    print("          ")
    print("          ")
    print("You crawl on the floor and hit a smal steel object.")
    time.sleep(4)
    print("You try felling it with your hand and 'it fells like a pipe?' you think to your self.")
    time.sleep(4)
    print("You fell more fo the pipe and your hand hits a flaht surface.")
    time.sleep(4)
    print("You exhale from the joy you feel taht you found something in this darknes. You start draging your hand on the flat surface, and you hit something warm and sticky.")
    time.sleep(3)
elif choice1 == 's':
    print("You start walking around the room, with your arms streached out. You walk in a straight line and hit a wall.")
    time.sleep(4)
    print("When your hand touches the wall, your suprised and confuesd becouse, the material taht your fingers are felling is glass. You begin following the glass wall to see where it leads and how big is it.")
    time.sleep(4)
    print("You hiit a wall adn you emidetly, start going the other direction to mesure the glass wall.")
    time.sleep(3)
    print("When you reach the other end of the wall, your hand stops at a square shaped object inbeded in the wall. You fell ti around and realise it is a light swich.")
elif choice1 == 'd':
    print("You stay still and wait")
    time.sleep(2)
    print("Then you start hearing footsteps, you quickly turn around and BAM!!! you her a gun shot. You try to get up but you start felling pain in your chest.")
    time.sleep(6)
    print("The pain starts growing more and more until you fall on your back. The lights turn on and you see that your in a white room.")
    time.sleep(6)
    print("And next to you is a masked man with a gun and an axe. Last thing you se is a swing of an axe and every thing goes black")
    time.sleep(2)
    print("YOU DIED!!!!,   GAME OVER")
    time.sleep(3)










    
