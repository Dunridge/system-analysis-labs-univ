import matplotlib.pyplot as mpl
import numpy as np
import math

class study_of_transients :
    __type = 0
    __time = 0;
    __iterations = 0
    def __init__(self, type = 0, time = 0) :
        self.__type = type
        self.__time = time
    def calculate(self, a_0, a_1, b, q, T_0, x_1, x_2, x_3) :
        u = 1
        self.__iterations = int(self.__time / T_0)
        A = np.matrix([
                [0, 1, 0],
                [0, 0, 1],
                [-1, -a_0, -a_1]
        ], dtype = float)
        B = np.matrix([
                [0],
                [0],
                [b]
        ])
        C = np.matrix([
                [1, 0, 0]
        ], dtype = float)
        F = np.identity(3)
        for index in range(1, q + 1) :
            F += np.linalg.matrix_power(A * T_0, index) / float(math.factorial(index))
        vector = np.matrix([
            [x_1],
            [x_2],
            [x_3]
        ], dtype = float)
        G = np.dot(np.dot((F - np.identity(3)), np.linalg.inv(A)), B)
        x_next = np.dot(F, vector) + (G * u)
        array_of_vectors = []
        array_X = []
        array_Y = []
        for index in range(self.__iterations) :
            if self.__type == 1 :
                u = 1
            if self.__type == 2 :
                if index == int(self.__iterations / 2) :
                    u = -1
            if self.__type == 3 :
                if index == int(self.__iterations / 3) :
                    u = -1
                if index == int(self.__iterations - int(self.__iterations / 3)) :
                    u = 1
            x_previous = x_next
            x_next = np.dot(F, x_previous) + (G * u)
            array_Y.append(float(np.dot(C, x_next)))
            array_of_vectors.append(x_next)
            array_X.append(index * T_0)
        return array_X, array_Y, array_of_vectors
class study_of_transients_with_callback :
    __type = 0
    __time = 0
    __iterations = 0
    def __init__(self, type = 0, time = 0) :
        self.__type = type
        self.__time = time
    def J(self, x_vectors, T_0) :
        value = 0
        for index in range(self.__iterations) :
            value += np.absolute(x_vectors[index][0] - 1) * T_0
        return value
    def calculate_next(self, F, G, l_vector, vector, u_dash) :
        array_of_vectors = []
        x_next = np.dot(F - np.dot(G, l_vector), vector) + (G * u_dash)
        for index in range(self.__iterations) :
            x_previous = x_next
            x_next = np.dot(F - np.dot(G, l_vector), x_previous) + (G * u_dash)
            array_of_vectors.append(x_next)
        return array_of_vectors
    def calculate(self, a_0, a_1, b, q, T_0, x_1, x_2, x_3, l, delta_l) :
        self.__iterations = int(self.__time / T_0)
        u_dash = 1
        A = np.matrix([
                [0, 1, 0],
                [0, 0, 1],
                [-1, -a_0, -a_1]
        ], dtype = float)
        B = np.matrix([
                [0],
                [0],
                [b]
        ])
        C = np.matrix([
                [1, 0, 0]
        ], dtype = float)
        l_vector = np.matrix([0, 0, 0], dtype = float)
        if self.__type == 1 :
            l_vector = np.matrix([0, l, 0], dtype = float)
        if self.__type == 2 :
            l_vector = np.matrix([0, 0, l], dtype = float)
        F = np.identity(3)
        for index in range(1, q + 1) :
            F += np.linalg.matrix_power(A * T_0, index) / float(math.factorial(index))
        vector = np.matrix([
            [x_1],
            [x_2],
            [x_3]
        ], dtype = float)
        G = np.dot(np.dot((F - np.identity(3)), np.linalg.inv(A)), B)
        array_of_vectors = []
        array_X = []
        array_Y = []
        J_previous = self.J(self.calculate_next(F, G, l_vector, vector, u_dash), T_0)
        if self.__type == 1 :
            l_vector[0, 1] += delta_l
        if self.__type == 2 :
            l_vector[0, 2] += delta_l
        J_next = self.J(self.calculate_next(F, G, l_vector, vector, u_dash), T_0)
        while J_previous > J_next :
            J_previous = J_next
            if self.__type == 1 :
                l_vector[0, 1] += delta_l
            if self.__type == 2 :
                l_vector[0, 2] += delta_l
            J_next = self.J(self.calculate_next(F, G, l_vector, vector, u_dash), T_0)
        array_of_vectors = self.calculate_next(F, G, l_vector, vector, u_dash)
        array_Y = self.calculate_next(F, G, l_vector, vector, u_dash)
        for index in range(self.__iterations) :
            array_Y[index] = (float(np.dot(C, array_Y[index])))
            array_X.append(index * T_0)
        return array_X, array_Y, array_of_vectors
class program_management :
    __iterations = 0
    def __init__(self, iterations = 0) :
        self.__iterations = iterations
    def P(self, F) :
        P_next = np.identity(3)
        for index in range(self.__iterations) :
            P_previous = P_next
            P_next = np.dot(F, P_previous)
        return P_next
    def S(self, F, F_Inverse, G, collection) :
        P_next = np.identity(3)
        for index in range(self.__iterations) :
            P_previous = P_next
            P_next = np.dot(F_Inverse, P_previous)
            collection.append(np.dot(P_next, G))
        sum_next = np.zeros((3, 3))
        for index in range(1, self.__iterations) :
            sum_previous = sum_next
            sum_next = sum_previous + np.dot(collection[index], collection[index].transpose())
        return sum_next
    def calculate(self, a_0, a_1, b, q, T_0, x_1, x_2, x_3, special_coordinate) :
        A = np.matrix([
                [0, 1, 0],
                [0, 0, 1],
                [-1, -a_0, -a_1]
        ], dtype = float)
        B = np.matrix([
                [0],
                [0],
                [b]
        ])
        C = np.matrix([
                [1, 0, 0]
        ], dtype = float)
        F = np.identity(3)
        F_Inverse = np.identity(3)
        for index in range(1, q + 1) :
            F += np.linalg.matrix_power(A * T_0, index) / float(math.factorial(index))
        for index in range(1, q + 1) :
            if index % 2 != 0 :
                F_Inverse -= np.linalg.matrix_power(A * T_0, index) / float(math.factorial(index))
            else :
                F_Inverse += np.linalg.matrix_power(A * T_0, index) / float(math.factorial(index))
        vector = np.matrix([
            [x_1],
            [x_2],
            [x_3]
        ], dtype = float)
        collection = []
        x_special = np.matrix([
            [special_coordinate],
            [0],
            [0]
        ], dtype = float)
        G = np.dot(np.dot((F - np.identity(3)), np.linalg.inv(A)), B)
        L = np.dot(self.P(F), self.S(F, F_Inverse, G, collection))
        L_Inverse = np.linalg.inv(L)
        l_0 = np.dot(L_Inverse, x_special)
        x_next = np.dot(F, vector) + (G * 0)
        array_of_vectors = []
        array_of_vectors.append(x_next)
        u_next = np.dot(collection[0].transpose(), l_0)
        array_X = []
        array_Y = []
        array_Z = []
        for index in range(self.__iterations) :
            u_previous = u_next
            x_previous = x_next
            x_next = np.dot(F, x_previous) + (G * u_previous)
            u_next = np.dot(collection[index].transpose(), l_0)
            array_Y.append(float(np.dot(C, x_next)))
            array_of_vectors.append(x_next)
            array_X.append(index)
            array_Z.append(u_next)
        return array_X, array_Y, array_of_vectors, array_Z
class reconstruct_the_state :
    __iterations = 0
    __type = 0
    def __init__(self, type = 0, iterations = 0) :
        self.__iterations = iterations
        self.__type = type
    def calculate(self, a_0, a_1, b, q, T_0, x_1, x_2, x_3, x_cup_1, x_cup_2, x_cup_3) :
        u = 1
        A = np.matrix([
                [0, 1, 0],
                [0, 0, 1],
                [-1, -a_0, -a_1]
        ], dtype = float)
        B = np.matrix([
                [0],
                [0],
                [b]
        ])
        C = np.matrix([
                [1, 0, 0]
        ], dtype = float)
        F = np.identity(3)
        for index in range(1, q + 1) :
            F += np.linalg.matrix_power(A * T_0, index) / float(math.factorial(index))
        vector = np.matrix([
            [x_1],
            [x_2],
            [x_3]
        ], dtype = float)
        vector_cup = np.matrix([
            [x_cup_1],
            [x_cup_2],
            [x_cup_3]
        ])
        G = np.dot(np.dot((F - np.identity(3)), np.linalg.inv(A)), B)
        q = np.matrix([
            [2 * T_0],
            [2 * T_0],
            [T_0]
        ])
        collection_of_u = []
        collection_of_y = []
        x_next = np.dot(F, vector) + (G * u)
        y_next = float(np.dot(C, x_next))
        x_cup_next = np.dot(F, vector_cup) + np.dot(q, y_next - np.dot(C, vector_cup)) + np.dot(G, u)
        y_cup_next = float(np.dot(C, x_cup_next))
        collection_of_u.append(u)
        collection_of_y.append(y_next)
        array_of_rates = []
        array_of_vectors = []
        array_Y_cup = []
        array_X = []
        array_Y = []
        for index in range(self.__iterations) :
            if self.__type == 1 :
                u = 1
            if self.__type == 2 :
                u = 3 * math.sin(2 * math.pi * T_0  * index / 5)
            if self.__type == 3 :
                if index % 2 == 0 :
                        u = 2
                else :
                        u = -2
            x_cup_previous = x_cup_next
            y_previous = y_next
            x_previous = x_next
            x_next = np.dot(F, x_previous) + np.dot(G, u)
            y_next = float(np.dot(C, x_next))
            x_cup_next = np.dot(F, x_cup_previous) + np.dot(q, y_previous - np.dot(C, x_cup_previous)) + np.dot(G, u)
            y_cup_next = float(np.dot(C, x_cup_next))
            collection_of_u.append(u)
            collection_of_y.append(y_next)
            array_of_rates.append(np.linalg.norm(x_cup_next - x_next))
            array_X.append(index)
            array_Y.append(y_next)
            array_Y_cup.append(y_cup_next)
        array_Y_cup[0] = float(vector_cup[0])
        return array_X, array_Y, array_Y_cup, array_of_rates
def draw_management(array_X, arrays_Y, names) :
    plots = [[], [], []]
    for index in range(len(array_X)) :
        plots[0].append(float(arrays_Y[index][0]))
        plots[1].append(float(arrays_Y[index][1]))
        plots[2].append(float(arrays_Y[index][2]))
    mpl.plot(array_X, plots[0], label=names[0])
    mpl.plot(array_X, plots[1], label=names[1])
    mpl.plot(array_X, plots[2], label=names[2])
    mpl.legend()
    mpl.show()
    return
def draw_observation_first(array_X, arrays_Y, names) :
    mpl.plot(array_X, arrays_Y[0], label=names[0])
    mpl.plot(array_X, arrays_Y[1], label=names[1])
    mpl.plot(array_X, arrays_Y[2], label=names[2])
    mpl.legend()
    mpl.show()
    return
def compare_observations(array_X, arrays_Y, names) :
    plots = [[], []]
    for index in range(len(array_X)) :
        plots[0].append(float(arrays_Y[0][index]))
        plots[1].append(float(arrays_Y[1][index]))
    mpl.plot(array_X, plots[0], label=names[0])
    mpl.plot(array_X, plots[1], label=names[1])
    mpl.legend()
    mpl.show()
    return
def draw_four_parameters(array_X, arrays_Y, management, names) :
    plots = [[], [], [], []]
    for index in range(len(array_X)) :
        plots[0].append(float(arrays_Y[index][0]))
        plots[1].append(float(arrays_Y[index][1]))
        plots[2].append(float(arrays_Y[index][2]))
        plots[3].append(float(management[index]))
    mpl.plot(array_X, plots[0], label=names[0])
    mpl.plot(array_X, plots[1], label=names[1])
    mpl.plot(array_X, plots[2], label=names[2])
    mpl.plot(array_X, plots[3], label=names[3])
    mpl.legend()
    mpl.show()
    return

# if __name__ == "__main__" :
#     #1.1
#     a, b1, c = study_of_transients(1, 100).calculate(1, 3, 1, 10, 0.05, 0, 0, 0)
#     draw_management(a, c, ['x1', 'x2', 'x3'])
#     #1.2
#     a, b, c = study_of_transients(2, 100).calculate(1, 3, 1, 10, 0.05, 0, 0, 0)
#     draw_management(a, c, ['x1', 'x2', 'x3'])
#     #1.3
#     a, b, c = study_of_transients(3, 100).calculate(1, 3, 1, 10, 0.05, 0, 0, 0)
#     draw_management(a, c, ['x1', 'x2', 'x3'])
#     #2
#     a, b, c = study_of_transients_with_callback(1, 100).calculate(1, 3, 1, 10, 0.05, 0, 0, 0, 1, 0.05)
#     compare_observations(a, [b1, b], ['without', 'with'])
#     #3
#     a, b, c, z = program_management(110).calculate(1, 3, 1, 10, 0.05, 0, 0, 0, 2)
#     draw_four_parameters(a, c, z, ['x1', 'x2', 'x3', 'u'])
#     #4.1
#     a, b, c, z = reconstruct_the_state(1, 200).calculate(1, 3, 1, 10, 0.05, 0, 0, 0, 2, 2, 2)
#     draw_observation_first(a, [b, c, z], ['original', 'recreated', 'error'])
#     #4.2
#     a, b, c, z = reconstruct_the_state(2, 200).calculate(1, 3, 1, 10, 0.05, 0, 0, 0, 2, 2, 2)
#     draw_observation_first(a, [b, c, z], ['original', 'recreated', 'error'])
#     #4.3
#     a, b, c, z = reconstruct_the_state(3, 200).calculate(1, 3, 1, 10, 0.05, 0, 0, 0, 2, 2, 2)
#     draw_observation_first(a, [b, c, z], ['original', 'recreated', 'error'])