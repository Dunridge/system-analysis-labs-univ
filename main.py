# Maksym Polinka, K - 34

import lab1.lab1 as lr1

lab1 = lr1.transcient_process()


#
# def say_no():  # testing
#     print("no")
#
#
# def say_yes():    #testing
#     print("yes")


def incorrect_method_number():
    print("Incorrect method number")


def not_yet_implemented():
    print("not yet implemented...")


def choose_lab(lab_number):
    if lab_number == 1:
        lab1.do_something()
        return
    if lab_number == 2:
        return

    else:
        incorrect_method_number()


def main():
    choose_lab(int(input("Please, enter the lab number: ")))


if __name__ == "__main__":
    main()
