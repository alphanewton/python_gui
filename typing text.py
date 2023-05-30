from time import *
import random as r

def mistake(par, user):
    error = 0
    for i in range(len(par)):
        try:
            if par[i] != user[i]:
                error+=1
        except:
            error+=1
    return error

def speed_time(time_start, time_end, userInput):
    time_delay = time_end - time_start
    time_R = round(time_delay,2)
    speed = len(userInput)/time_R
    return round(speed)


while True:
    chk = input(" Ready to test - yes/no ")
    if chk == "yes":
        texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras erat dui, finibus vel lectus ac, pharetra dictum odio. Etiam risus sapien, auctor  eu volutpat sit amet, porta in nunc.", "First, you have to open Terminal (or any alternative you normally use). Press Command+Space to open Spotlight Search, type “terminal,” and then select it from the search results."]
        test = r.choice(texts)

        print("                 ***** typing speed *****")
        print(test)
        print()
        print()
        time_1 = time()
        testinput = input(" Enter : ")
        time_2 = time()

        print("Speed : ", speed_time(time_1,time_2,testinput)*60, "w/min")
        print("Error : ", mistake(test, testinput))

    elif chk == "no":
        print("Thank you!")
        break

    else:
        print("Wrong input")