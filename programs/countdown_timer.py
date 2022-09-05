import sys
import time
import datetime


def usage():
    print("countdown.py <number>")

def countdown_timer():
    print(sys.argv)
    if len(sys.argv) == 2:
        try:
            countdown = int(sys.argv[1])
        except ValueError:
            print("Please enter a valid number")
            sys.exit(-1)
    else:
        usage()
        sys.exit(-1)
    
    while countdown > 0:
        # 00:00:00
        countdown_time = str(datetime.timedelta(seconds=countdown))
        print(countdown_time)
        time.sleep(1)
        countdown -= 1
    print("countdown finished")


def main():
    countdown_timer()


if __name__ == '__main__':
    main()