from time import *
import random as r
from tkinter import *


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


def calc():
    end_time = time()
    INPUT = datatxt.get("1.0", "end-1c")
    error = mistake(test, INPUT)
    speed = speed_time(start_time, end_time, INPUT)

    popup = Toplevel(window)
    popup.geometry("400x100")
    popup.title("Results!")
    result_text = f"Your Typing Speed -> {speed} words/sec\nNumber of Errors -> {error}"
    result_label = Label(popup, text=result_text)
    result_label.pack()

    popup.mainloop()



texts = ["Scolding is something common in student life. Being a naughty boy, I am always scolded by my parents. But one day I was severely scolded by my English teacher. She infect teaches well. But that day, I could not resist the temptation that an adventure of Nancy Drew offered. While she was teaching, I was completely engrossed in reading that book. Nancy Drew was caught in the trap laid by some smugglers and it was then when I felt a light tap on my bent head. The teacher had caught me red handed. She scolded me then and there and insulted me in front of the whole class. I was embarrassed. My cheeks burned being guilty conscious. When the class was over, I went to the teacher to apologize. When she saw that I had realized my mistake, she cooled down and then told me in a very kind manner how disheartening it was when she found any student not paying attention. I was genuinely sorry and promised to myself never to commit such a mistake again.", "Days are not of equal value in one’s life. Some bring happiness while others bring sadness. Sadness and happiness both are equally important to man’s life, since they are the two sides of a coin. As we cannot forget the happiest day, we are unable to forget the saddest day of our life too. The saddest day of my life was the Diwali Day. Diwali is considered to be a happy festival and till last Diwali, it was my favorite festival. On last Diwali, my sister, my brother and I were busy lighting the fireworks. I was holding a ‘fuljhari’ in my hand and unfortunately my younger brother, who was standing just beside me, had a cracker in his hand. This cracker caught fire and a very loud explosion was heard which shook my sister and me. After that, we all could think of nothing else than blood stained cotton, bandage, dettol etc. My cousin took my brother to the doctor where he got 14 stitches in his forefinger and thumb. But at home, everybody kept cursing and blaming me for the mishap. That night, I could not sleep and I cried a lot. For next few days, I bore the burden of this blame for being responsible for this unfortunate incident. I felt deeply guilty conscious which I was able to overcome after a long time.", "Studying is the main source of knowledge. Books are indeed never failing friends of man. For a mature mind, reading is the greatest source of pleasure and solace to distressed minds. The study of good books ennobles us and broadens our outlook. Therefore, the habit of reading should be cultivated. A student should never confine himself to his schoolbooks only. He should not miss the pleasure locked in the classics, poetry, drama, history, philosophy etc. We can derive benefit from other’s experiences with the help of books. The various sufferings, endurance and joy described in books enable us to have a closer look at human life. They also inspire us to face the hardships of life courageously. Nowadays there are innumerable books and time is scarce. So we should read only the best and the greatest among them. With the help of books we shall be able to make our thinking mature and our life more meaningful and worthwhile."]
test = r.choice(texts)


window = Tk()
window.title('Typing Test by Newton')
window.geometry("800x600")
window.config(padx=30, pady=30)

text = Label(text=test, wraplength=700).pack()
start_time = time()
datatxt = Text(width=90)
datatxt.pack()
calculate = Button(text='Check WPM!', command=calc).pack()
window.mainloop()
