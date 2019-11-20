# Maksym Polinka, K - 34

import lab1.lab1 as lr1
import lab2.lab2 as lr2
import lab3.lab3 as lr3
import lab4.lab4 as lr4


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
        # input all of the variables:
        a1 = int(input("please, input a1 (a1 є [1, 10]): "))
        a2 = int(input("please, input a2 (a2 є [1, 10]): "))
        b = 1  # as given on the page 8
        q = int(input("please, input q (q є [2, 10]): "))
        t = float(input("please, input t (t є [0.001, 0.1]): "))
        # t might be float

        # ko = input_ko_for_lr1()
        ko = input("enter ko value for the lab: ")
        # ko = int(input("please, input ko: "))  # define a function for input of variant for change of control
        xo = int(input("please, input xo: "))
        # x0 must be int?

        l2 = float(input("please, input the l2 value: "))
        l3 = float(input("please, input the l3 value: "))
        # chosen_mode = input("enter the variant for the work of this lab (1 - l=(0,l2,0); 2 - l=(0,0,l3), or input"
        #                     " anything else to input custom l values)")
        # # add an if statement here to check the input
        # if chosen_mode == 1:
        #     l2 = 0.0
        #     l3 = float(input("please, input the l3 value: "))
        # if chosen_mode == 2:
        #     l2 = float(input("please, input the l2 value: "))
        #     l3 = 0.0
        # else:
        #     l2 = float(input("please, input the l2 value: "))
        #     l3 = float(input("please, input the l3 value: "))
        # l2 = float(input("please, input the l2 value: "))
        # l3 = float(input("please, input the l3 value: "))
        # create the object
        lab2 = lr2.DynamicModel(a1, a2, b, q, t, ko, xo, l2, l3)
        # run the lab
        lab2.runModel()
        # not_yet_implemented()
        return
    if lab_number == 3:
        # def calculate(self, a_0, a_1, b, q, T_0, x_1, x_2, x_3, special_coordinate):
        a, b, c, z = lr3.program_management(100).calculate(1, 3, 1, 3, 0.05, 0, 0, 0, 5)
        lr3.draw_four_parameters(a, c, z, ['x1', 'x2', 'x3', 'u'])

    if lab_number == 4:
        # returns only seven pictures because we call
        # lr4.compare_observations(a, [b1, b], ['without', 'with'])
        # that compares the results
        # 1.1
        # a, b1, c = lr4.study_of_transients(1, 100).calculate(1, 3, 1, 10, 0.05, 0, 0, 0)
        # lr4.draw_management(a, c, ['x1', 'x2', 'x3'])
        # # 1.2
        # a, b, c = lr4.study_of_transients(2, 100).calculate(1, 3, 1, 10, 0.05, 0, 0, 0)
        # lr4.draw_management(a, c, ['x1', 'x2', 'x3'])
        # # 1.3
        # a, b, c = lr4.study_of_transients(3, 100).calculate(1, 3, 1, 10, 0.05, 0, 0, 0)
        # lr4.draw_management(a, c, ['x1', 'x2', 'x3'])
        # # 2
        # a, b, c = lr4.study_of_transients_with_callback(1, 100).calculate(1, 3, 1, 10, 0.05, 0, 0, 0, 1, 0.05)
        # lr4.compare_observations(a, [b1, b], ['without', 'with'])
        # # 3
        # a, b, c, z = lr4.program_management(110).calculate(1, 3, 1, 10, 0.05, 0, 0, 0, 2)
        # lr4.draw_four_parameters(a, c, z, ['x1', 'x2', 'x3', 'u'])
        # # 4.1
        a, b, c, z = lr4.reconstruct_the_state(1, 200).calculate(1, 3, 1, 10, 0.05, 0, 0, 0, 2, 2, 2)
        lr4.draw_observation_first(a, [b, c, z], ['original', 'recreated', 'error'])
        # 4.2
        a, b, c, z = lr4.reconstruct_the_state(2, 200).calculate(1, 3, 1, 10, 0.05, 0, 0, 0, 2, 2, 2)
        lr4.draw_observation_first(a, [b, c, z], ['original', 'recreated', 'error'])
        # 4.3
        a, b, c, z = lr4.reconstruct_the_state(3, 200).calculate(1, 3, 1, 10, 0.05, 0, 0, 0, 2, 2, 2)
        lr4.draw_observation_first(a, [b, c, z], ['original', 'recreated', 'error'])

        return

    else:
        incorrect_method_number()


def main():
    choose_lab(int(input("Please, enter the lab number: ")))


if __name__ == "__main__":
    main()
