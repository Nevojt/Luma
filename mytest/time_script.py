import time
import os

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for macOS and Linux
        os.system('clear')



def display_clock():
    # Display a real-time
    while True:
        # Clear the screen
        clear_screen()

        #     Get the current time
        _time_ = time.strftime("%H:%M:%S")

    #     Create a stylish clock
        print(f"""
            ========================
            ||  Real-Time Clock   ||
            ========================
            ||      {_time_}      ||
            ========================
        """)
        time.sleep(1)


# Start a timer
display_clock()
