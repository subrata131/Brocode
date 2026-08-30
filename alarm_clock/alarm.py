import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file1= r"S:\pogramming\python\Brocode\my_music.mp3"
    sound_file2=r"S:\pogramming\python\Brocode\my_music2.mp3"

    while True:
        current=datetime.datetime.now().strftime("%H:%M:%S")
        print(current)

        if current==alarm_time:
            print("WAKE UP BRO!!")
            print("Press Enter to stop the alarm")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file1)
            pygame.mixer.music.play(-1)
            
            input()

            pygame.mixer.music.stop()
            print("Alarm stopped!!")

            break
        time.sleep(1)

        

if __name__=="__main__":
    alarm_time=input("Enter the alarm time (HH:MM:SS):")
    set_alarm(alarm_time)
