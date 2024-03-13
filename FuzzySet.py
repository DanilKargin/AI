
class FuzzySet:
    def __init__(self, sets):
        if len(sets) <= 0:
            print("Ошибка!! Пустые данные.")
        self.sets = sets
        self.data_print()

        while True:
            print("Выберите действие(число):")
            print("1.Получить степень принадлежности для объекта.")
            print("2.Выйти из программы.")
            answer = input()
            if int(answer) == 1:
                number = input("Введите объект(число): ")
                for set in sets:
                    print(set[0] + " - " + str(self.accessory_function(float(number), set)))
            elif int(answer) == 2:
                break
            else:
                print("Ошибка ввода!!")

    def data_print(self):
        print("Дооступные множества:")
        for set in self.sets:
            print(set[0])
            print(self.fazification(set))
            #print("Левая граница: " + str(set[1]))
            #print("Правая граница: " + str(set[3]))
            #print("Вершина треугольника: " + str(set[2]))
            print()
    def fazification(self, set):
        item = set[1]
        accessory_list = list()
        while item <= set[3]:
            accessory_list.append(str(item) + "/" + str(self.accessory_function(item, set)))
            item += 1
        return accessory_list

    def accessory_function(self, number, set):
        if number >= set[1] and number <= set[2]:
            return (number - set[1])/(set[2] - set[1])
        elif number >= set[2] and number <= set[3]:
            return (set[3] - number)/(set[3] - set[2])
        elif number < set[1] or number > set[3]:
            return 0
