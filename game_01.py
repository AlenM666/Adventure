import time
import sys
import os
import keyboard

#if __name__ == '__main__':
   # playerName = input("Enter name")

playerName = input("Enter your name: ")

print(playerName + " Woke up in a dark room. You try to see, but the room is so dark that you can't see anything.")
time.sleep(2)
print("")
print("Press: -(a) you start crawling on the floor, feeling the are around you.")
print("Press: -(s) You stand up and try walking around, to get the felling of the area.")

choice1 = input("Enter choice: ")


if choice1 == 'a':
    os.system('clear')
    time.sleep(3)
    print("          ")
    print("          ")
    print("          ")
    print("You crawl on the floor and hit a smal steel object.")
    time.sleep(3)
    print("You try felling it with your hand and 'it fells like a pipe?' you think to your self.")
    time.sleep(3)
    print("You fell more fo the pipe and your hand hits a flaht surface.")
    time.sleep(4)
    print("You exhale from the joy you feel taht you found something in this darknes. You start draging your hand on the flat surface, and you hit something warm and sticky.")
    time.sleep(3)
elif choice1 == 's':
    print("You start walking around the room, with your arms streached out. You walk in a straight line and hit a wall.")
    time.sleep(3)
    print("When your hand touches the wall, your suprised and confuesd becouse, the material taht your fingers are felling is glass. You begin following the glass wall to see where it leads and how big is it.")
    time.sleep(3)
    print("You hiit a wall adn you emidetly, start going the other direction to mesure the glass wall.")
    time.sleep(3)
    print("When you reach the other end of the wall, your hand stops at a square shaped object inbeded in the wall. You fell ti around and realise it is a light swich.")










    
