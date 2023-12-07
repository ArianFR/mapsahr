from datetime import datetime

def get_user_input():
    try:

        user_input = input(" YYYY/MM/DD - HH:MM:SS: ")
        input_datetime = datetime.strptime(user_input, "%Y/%m/%d - %H:%M:%S")


        epoch_start = datetime(1970, 1, 1, 0, 0, 0)

        time_difference = input_datetime - epoch_start
        seconds_since_epoch = int(time_difference.total_seconds())

        print(seconds_since_epoch)

    except ValueError:
        print("value error, pls type right inputs")

get_user_input()
