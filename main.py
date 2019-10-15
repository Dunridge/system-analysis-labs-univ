# Maksym Polinka, K - 34

import lab1.lab1 as lr1
import lab2.lab2 as lr2


def incorrect_method_number():
    print("Incorrect method number")


def not_yet_implemented():
    print("not yet implemented...")


def input_ko_for_lr1():
    print("input 1 for constant control")
    print("input 2 for change of control in the middle of the given interval")
    print("input 3 for dividing control into three parts")
    ko = int(input("please, input ko: "))
    return ko


def choose_lab(lab_number):
    if lab_number == 1:
        a1 = int(input("please, input a1 (a1 є [1, 10]): "))
        a2 = int(input("please, input a2 (a2 є [1, 10]): "))
        b = 1  # as given on the page 8
        q = int(input("please, input q (q є [2, 10]): "))
        t = float(input("please, input t (t є [0.001, 0.1]): "))
        # t might be float

        ko = input_ko_for_lr1()
        # ko = int(input("please, input ko: "))  # define a function for input of variant for change of control
        xo = int(input("please, input xo: "))
        # x0 must be int?
        lab1 = lr1.transcient_process(a1, a2, b, q, t, ko, xo)
        lab1.run_model()
        return
    if lab_number == 2:
        not_yet_implemented()
        return
    else:
        incorrect_method_number()


def main():
    choose_lab(int(input("Please, enter the lab number: ")))


if __name__ == "__main__":
    main()
