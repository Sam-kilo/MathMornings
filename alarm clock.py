
import time
import datetime
import pygame
from random_math_problems import add_problem

# %H=HOURS %M=MINUTES %p=AM or PM

def set_alarm(alarm_time):  # alarm was printing in military changed %H to %I to fix
    clock_alarm_time = datetime.datetime.strptime(alarm_time, "%I:%M:%S %p").strftime("%I:%M:%S")

    print(f"Your alarm is set for: {alarm_time}")
    sound_file = "alarm-clock-sound.mp3"
    pygame.init()
    pygame.mixer.init()

    #makes the alarm run
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%I:%M:%S")
        print(current_time)
        time.sleep(1) # Makes the clock count each second

        if current_time == clock_alarm_time:
            print("WAKE UP!")
            # pygame.mixer is a module for playing sounds
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.8)

            # Start the math problem-solving process
            solved_all_problems = add_problem()

            while pygame.mixer.music.get_busy() and not solved_all_problems:
                time.sleep(1)
            pygame.mixer.music.stop()
            print("Alarm stopped, dont go back to sleep!")
            is_running = False  # Exit the alarm loop once the problems are solve



if __name__ == '__main__':
    alarm_time = input("Enter alarm time (hh:mm:ss AM/PM): ")
    set_alarm(alarm_time)






