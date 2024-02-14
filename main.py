import numpy as np
from random import randint
import itertools
class GenericAlgorithm:


    def __init__(self, products, medical_standards, population_count, iteration_number):
        self.products = products
        self.medical_standards = medical_standards

        if self.check_first_data() == False:
            print("Data error!! Check the arguments")
            return

        self.population = np.array([[randint(0, 1) for _ in range(len(products))]
                               for _ in range(population_count)])

        index = 0
        while index <= iteration_number or self.find_best_decision()[1] < 100:
            self.ranking_method(int(population_count / 2))
            new_genereation = [None] * population_count

            for i in range(population_count):
                first_index = randint(0, int(population_count) / 2 - 1)
                second_index = randint(0, int(population_count) / 2 - 1)

                new_child = np.array(0 for _ in range(len(self.products)))
                new_genereation[i] =[*self.population[first_index][:int(len(self.population)/2)],*self.population[second_index][int(len(self.population)/2):]]
            index += 1
            self.population = new_genereation

            for i in range(int(population_count / 4)):
                obj_index = randint(0, int(population_count) - 1)
                product_index = randint(0, len(self.products) - 1)
                old_number = self.population[obj_index][product_index]
                if old_number == 0:
                    self.population[obj_index][product_index] = 1
                else:
                    self.population[obj_index][product_index] = 0

        result = self.find_best_decision()
        print("Наиболее лучший вариант:")
        print(self.population[result[0]])
        print("Входящие продукты:")
        for i in range(len(self.products)):
            if self.population[result[0]][i] != 0:
                print('-' + self.products[i][0])


    def find_best_decision(self):
        adaptability = self.find_adaptability_func()
        index = -1
        min_value = float('inf')
        for i in range(len(adaptability)):
            if adaptability[i] < min_value:
                min_value = adaptability[i]
                index = i
        return [index, adaptability[index]]
    def ranking_method(self, number_obj):
        adaptability = self.find_adaptability_func()
        new_generation_index = np.array(number_obj)
        old_population = self.population
        self.population = [None] * number_obj

        for i in range(number_obj):
            min_value = float('inf')
            index = -1
            for j in range(len(adaptability)):
                if adaptability[j] < min_value:
                    min_value = adaptability[j]
                    index = j
            if index != -1:
                self.population[i] = old_population[index]
                adaptability[index] = float('inf')

    def find_adaptability_func(self):
        adaptability = np.array([float('inf') for _ in range(len(self.population))])
        for i in range(len(self.population)):
            sum_parameter = np.array(self.medical_standards)*-1
            for j in range(len(self.population[i])):
                sum_parameter[0] += self.population[i][j] * self.products[j][1][0]
                sum_parameter[1] += self.population[i][j] * self.products[j][1][1]
                sum_parameter[2] += self.population[i][j] * self.products[j][1][2]
                sum_parameter[3] += self.population[i][j] * self.products[j][1][3]
                sum_parameter[4] += self.population[i][j] * self.products[j][1][4]
            sum_parameter = [x ** 2 for x in sum_parameter]
            adaptability[i] = (sum(sum_parameter)) ** 1/2

        return adaptability

    def check_first_data(self):
        if len(self.products[0][1]) != len(self.medical_standards):
            return False
        return True

class BruteForceAlgorithm:
    def __init__(self, products, medical_standards):
        self.products = products
        self.medical_standards = medical_standards
        for numbers in itertools.product([0, 1], repeat=len(products)):
            if self.check_standards(numbers) == True:
                print("Наиболее лучший вариант:")
                print(numbers)
                print("Входящие продукты:")
                for i in range(len(self.products)):
                    if numbers[i] != 0:
                        print('-' + self.products[i][0])
                break

    def check_standards(self, variant):
        adaptability = float('inf')
        sum_parameter = np.array(self.medical_standards) * -1
        for j in range(len(variant)):
            sum_parameter[0] += variant[j] * self.products[j][1][0]
            sum_parameter[1] += variant[j] * self.products[j][1][1]
            sum_parameter[2] += variant[j] * self.products[j][1][2]
            sum_parameter[3] += variant[j] * self.products[j][1][3]
            sum_parameter[4] += variant[j] * self.products[j][1][4]
        sum_parameter = [x ** 2 for x in sum_parameter]
        adaptability = (sum(sum_parameter)) ** 1 / 2
        if adaptability < 2500:
            return True
        else:
            return False


if __name__ == "__main__":
    #GenericAlgorithm([["Яблоко", [0.40, 0.40, 9.80, 47, 10]], ["Вареное яйцо", [6.3, 5.31, 0.56, 78, 11]], ["Овсянка 50г", [6.5, 3.1, 33, 178, 6.45]], ["Сок аплеьсиновый 150мл", [0, 0, 12, 48, 19.5]], ["Йогурт", [4, 2.7, 6.8, 75, 50]], ["Бекон 100г", [16, 40, 0, 420, 90]], ["Хлеб 100г", [8.5, 3.3, 48.3, 259, 14]]], [34, 25, 60, 600, 0], 100, 100)
    BruteForceAlgorithm([["Яблоко", [0.40, 0.40, 9.80, 47, 10]], ["Вареное яйцо", [6.3, 5.31, 0.56, 78, 11]], ["Овсянка 50г", [6.5, 3.1, 33, 178, 6.45]], ["Сок аплеьсиновый 150мл", [0, 0, 12, 48, 19.5]], ["Йогурт", [4, 2.7, 6.8, 75, 50]], ["Бекон 100г", [16, 40, 0, 420, 90]], ["Хлеб 100г", [8.5, 3.3, 48.3, 259, 14]]], [34, 25, 60, 600, 0])