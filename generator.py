import random


def generate(count):
    """This module will generate values for requests and write them into a file
    Alternatively we can read from db or from file here.
    If we care about the memory, we can replace this with generator.
    :param count: how many values to generate
    :return: lst - list of values to send
    """
    lst = []
    with open('data.txt', 'w+') as f:
        for i in range(0, count):
            st = str(random.random())
            f.write(st+"\n")
            lst.append(st)
    return lst
