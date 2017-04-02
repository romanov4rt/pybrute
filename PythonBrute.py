import itertools
import time

Password = input("kakoB Pincode, Dpy)|(ok?\n")

start = time.time()

counter = 1

CharLength = 1

Pin = ("1234567890")

for CharLength in range(25):
    
    passwords = (itertools.product(Pin, repeat = CharLength))

    print("\n \n")
    print("currently working on passwords with ", CharLength, " chars")
    print("We are currently at ", (counter / (time.time() - start)), "attempts per seconds")
    print("It has been ", time.time() - start, " seconds!")
    print("We have tried ", counter, " possible passwords!")

    for i in passwords:

        counter +=1
        
        i = str(i)

        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")

        if i == Password:

            end = time.time()

            timetaken = end - start

            print("Found it in ", timetaken, " seconds and ", counter, "attempts")

            print("That is ", counter / timetaken, " attempts per second!")

            print(i)

            input("Press enter when you have finished")

            exit()
