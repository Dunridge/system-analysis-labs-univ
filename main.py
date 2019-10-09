# Maksym Polinka, K - 34

import lab1.lab1 as lr1
import lab2.lab2 as lr2


def incorrect_method_number():
    print("Incorrect method number")


def not_yet_implemented():
    print("not yet implemented...")


def choose_lab(lab_number):
    if lab_number == 1:
        a1 = int(input("please, input a1 (a1 є [1, 10]): "))
        a2 = int(input("please, input a2 (a2 є [1, 10]): "))
        b = 1  # as given on the page 8
        q = int(input("please, input q (q є [2, 10]): "))
        t = float(input("please, input t (t є [0.001, 0.1]): "))
        # t might be float
        ko = int(input("please, input ko: "))
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
