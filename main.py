from tkinter import *
import random
from outcomes import daytime, nighttime, events
confusion = 0
damages = 0
thinking = 0
choice = []
tie_stopper = False

def start_over():
    global confusion, damages, thinking, tie_stopper
    confusion = 0
    damages = 0
    thinking = 0
    story_label.config(text=f"Congratulations on your new mastodon.  What do those things do in their free time anyway?")
    next_button.config(text="Meet your mastodon", command=next_event)
    stats_label.config(text=f"Confusion: {confusion} Damages: {damages} Thinking: {thinking}")
    tie_stopper = False

def angery_bugger():
    sit_check = roll_die(events)
    if sit_check == 6:
        story_label.config(text=f"The mastodon sits on you.  You never emerge.")
        next_button.config(text="Leave your mastodon to your nearest relative.", command=start_over)
    else:
        story_label.config(text=f"You have defused the situation.")
        next_button.config(text="Phew", command=next_event)

def roll_die(event):
    return random.choice(event)


def next_event():
    day_or_night = roll_die(events)
    if day_or_night > 5:
        story_label.config(text="You have angered your mastodon!")
        next_button.config(text="Proceed with caution...", command=angery_bugger)
    elif day_or_night > 3:
        story_label.config(text="You spend an evening with your mastodon.")
        next_button.config(text="Proceed with caution...", command=next_night)
    else:
        story_label.config(text="You spend the day with your mastodon.")
        next_button.config(text="Proceed with caution...", command=next_day)

def next_night():
    global confusion, damages, thinking, tie_stopper
    big_pick = roll_die(nighttime)
    # print(big_pick)
    # print(big_pick["story"])
    confusion += big_pick["effect"]["confusion"]
    damages += big_pick["effect"]["damages"]
    thinking += big_pick["effect"]["thinking"]
    # print(confusion, damages, thinking)
    stats_label.config(text=f"Confusion: {confusion} Damages: {damages} Thinking: {thinking}")
    story_label.config(text=big_pick["story"])
    next_button.config(text="This effin thing...", command=next_event)
    if big_pick["effect"]["confusion"] > 0:
        choice = []
        for x in range(0, 3):
            choice.append(random.choice(events))
        if choice[0] == choice[1] and choice[0] == choice[2]:
            story_label.config(
                text=f"You have had a feverish moment of clarity.\n"
                     f"You finally have deciphered what the mastodon is saying\n"
                     f"You live the rest of your life in a state of blissful enlightenment\n"
                     f"in harmony with your new friend.\n "
                     f"\n \nAlso, you're vegan now.")
            next_button.config(text="Lets look in on another unfortunate sucker", command=start_over)
            tie_stopper = True
    stat_check()

def next_day():
    global confusion, damages, thinking, tie_stopper
    big_pick = roll_die(daytime)
    # print(big_pick)
    # print(big_pick["story"])
    confusion += big_pick["effect"]["confusion"]
    damages += big_pick["effect"]["damages"]
    thinking += big_pick["effect"]["thinking"]
    # print(confusion, damages, thinking)
    stats_label.config(text=f"Confusion: {confusion} Damages: {damages} Thinking: {thinking}")
    story_label.config(text=big_pick["story"])
    next_button.config(text="This thing is obnoxious", command=next_event)
    if big_pick["effect"]["confusion"] > 0:
        choice = []
        for x in range(0, 3):
            choice.append(random.choice(events))
        if choice[0] == choice[1] and choice[0] == choice[2]:
            story_label.config(
                text=f"You have had a feverish moment of clarity.\n"
                     f"You finally have deciphered what the mastodon is saying\n"
                     f"You live the rest of your life in a state of blissful enlightenment\n"
                     f"in harmony with your new friend.\n "
                     f"\n \nAlso, you're vegan now.")
            next_button.config(text="Lets look in on another unfortunate sucker", command=start_over)
    stat_check()


def stat_check():
    if tie_stopper:
        return
    global confusion, damages, thinking
    if confusion >= 6:
        endgame.config(text="You finally lose your temper with the wretched creature and confront it.\n"
                            "The argument is brief.\n"
                            "You have no idea what it is trying to tell you, and eventually\n"
                            "it crushes you to death using its trunk.")
        next_button.config(text="Leave your mastodon to your nearest relative.", command=start_over)
    if damages >= 6:
        endgame.config(text="You lose all your money\n"
                            "Your livelihood is destroyed\n"
                            "All reduced to gigantic footprints in the ashes\n"
                            "The mastodon abandons you in search of somone else to inconvenience."
                    )
        next_button.config(text="Lets look in on its next victim", command=start_over)
    if thinking >= 6:
        endgame.config(text="Mastodons are not for you.  You slip away into the night\n"
                            "with the last of your remaining savings, faking your death.\n"
                            "Perhaps you'll build a gigantic pillowfort.\n"
                            "Or collect tumblers?\n"
                            "Something quiet."
                            )
        next_button.config(text="Lets look in on another unfortunate sucker", command=start_over)

window = Tk()
window.title("Congratulations on your mastodon!")
window.config(width=200, height=100)
canvas = Canvas(background="White")
mastodonpic = PhotoImage(file="mastodon.png")
mastodon = canvas.create_image(50, 200, image=mastodonpic)
canvas.grid(row=0, column=0)
stats_label = Label(text=f"Confusion: {confusion} Damages: {damages} Thinking: {thinking}")
stats_label.grid(row=1, column=0, columnspan=2)
story_label = Label(text=f"Congratulations on your new mastodon.  What do those things do in their free time anyway?")
story_label.grid(row=2, column=0, columnspan=2)
next_button = Button(text="Meet your mastodon", command=next_event)
next_button.grid(row=3, column=0)
endgame = Label(text="")
endgame.grid(row=4, column=0)
placeholder = Label(text="")
placeholder.grid(row=4, column=2)

window.mainloop()