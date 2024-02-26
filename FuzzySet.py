class FuzzySet:
    def __init__(self, sets):
        if len(sets) <= 0:
            print("Error!!! Empty data!")
        self.sets = sets
