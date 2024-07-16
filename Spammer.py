# Author = Jone Santhanaraj#

import pyautogui as pt
import time

max = 1000  # Sets The Max Number Of Messages That Can Be Sent.

wait = 10  # Time In Seconds - Stops The Program While Placing The Insertion Point In The Required Position.

# --------------------------------------------------------------------------#


def return_func():
    import keyboard

    print("\nPress CTRL To Try Again, Or Press ENTER To Exit.\n")

    while True:
        if keyboard.read_key() == "ctrl":
            print(
                "\n\n------------------------------------------------------------------------\n"
            )
            spammer(max, wait)
        elif keyboard.read_key() == "enter":
            print("\nThank You!\n")
            time.sleep(2)
            pt.typewrite("exit")
            pt.press("enter")
        else:
            return_func()
        break


# -------------------------------------------------------------------------#


def spammer(max_message, wait_time):
    mm = max_message
    wt = wait_time

    print("\n")
    print("=================================================")
    print("Welcome To The Spam Bot!")
    print("*Use It Only For Fun, Please Don't Misuse This*")
    print("=================================================")
    time.sleep(1)

    valid = False

    while not valid:
        try:
            limit = int(input("\nEnter Message Count: \n"))
            valid = True
        except ValueError:
            print("Please Enter Only A Valid Number...\n")

    if limit > max:
        print(
            "\nSorry, For Safety Reasons The Maximum Message Count Allowed Is",
            mm,
            "!!!\n",
        )
        return_func()
    else:
        message = input("\nEnter Your Message: \n")

    print(
        "\nPlace The Insertion Point Where You Want To Spam, Within", wt, "Seconds!!!\n"
    )
    time.sleep(2)

    print("\nSpamming Starts In,\n")

    print(f"{wt}", end="")

    t = 0

    while wt >= t:
        print(f"\r{wt} ", end="")
        time.sleep(1)
        wt -= 1

    print("\rSpamming Now!...\n")

    i = 1
    bar = 50

    while i <= limit:
        pt.typewrite(
            message
        )  # The Message Is Written Where The Insertion Point - [ I ] Is Placed...
        pt.press("enter")

        if i == limit:
            print(f"\r{str(i)} Messages sent.\n\nSpamming Completed! \n", end="")
            break

        print(f"\r{str(i)} Messages sent.", end="")
        i += 1

    return_func()


# ----------------#
spammer(max, wait)
# ----------------#
