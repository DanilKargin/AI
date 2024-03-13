import matplotlib.pyplot as plt

class LinguisticScale:
    def __init__(self, sets, data):
        if len(sets) <= 0:
            print("Не заданы границы!!")
            return
        self.sets = sets
        self.data = data
        self.fuze_time_line = [None] * len(data)
        for index in range(len(data)):
            self.fuze_time_line[index] = self.fazification(data[index])
        self.create_graphics()


    def create_graphics(self):
        graph = plt.subplot()
        for set in self.sets:
            if len(set[1]) == 3:
                graph.plot(set[1], [0, 1, 0], label = set[0])
            else:
                graph.plot(set[1], [0, 1, 1, 0], label = set[0])
        graph.legend()
        for index in range(len(self.data)):
            y_val = self.triangular_accessory_function(self.data[index], self.fuze_time_line[index][1]) if len(self.fuze_time_line[index][1]) == 3 else self.trapezoidal_accessory_function(self.data[index], self.fuze_time_line[index][1])
            graph.plot(self.data[index], y_val, "b*")
        plt.show()

    def fazification(self, number):
        max_value = 0
        max_index = -1
        for index in range(len(self.sets)):
            value = 0
            if len(self.sets[index][1]) == 3:
                value = self.triangular_accessory_function(number, self.sets[index][1])
            else:
                value = self.trapezoidal_accessory_function(number, self.sets[index][1])
            if value > max_value:
                max_value = value
                max_index = index
        return self.sets[max_index]

    def triangular_accessory_function(self, number, set):
        if number >= set[0] and number <= set[1]:
            return (number - set[0])/(set[1] - set[0])
        elif number >= set[1] and number <= set[2]:
            return (set[2] - number)/(set[2] - set[1])
        elif number < set[0] or number > set[2]:
            return 0
    def trapezoidal_accessory_function(self, number, set):
            if number >= set[0] and number <= set[1]:
                return (number - set[0]) / (set[1] - set[0])
            elif number >= set[1] and number <= set[2]:
                return 1
            elif number >= set[2] and number <= set[3]:
                return (set[3] - number) / (set[3] - set[2])
            elif number < set[0] or number > set[3]:
                return 0