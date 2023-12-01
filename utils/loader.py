import os

def load_day(day):
    # load day into an array line by line and return the array
    file = day + "/input"
    day = []
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', file), "r") as f:
        for line in f:
            day.append(line.strip())
    return day
