import pandas as pd
import numpy as np
import math
from random import randint
from keras.utils import to_categorical

class DataPreprocessor():
    def __init__(self):
        self.file = pd.read_csv('dataset/data.csv')
        self.data = self.file.values

    def fillMissingData(self, x):
        # Gender
        x[0] = x[0] - 1
        if x[0] != 0 and x[0] != 1:
            x[0] = randint(0, 1)

        # Age band of driver
        x[1] = x[1] - 1
        if x[1] == -2:
            x[1] = randint(0, 10)

        # Day of week
        x[3] = x[3] - 1
        if x[3] == -2:
            x[3] = randint(0, 6)

        # Road type
        if x[5] == 6:
            x[5] = 4
        elif x[5] == 7:
            x[5] = 5
        elif x[5] == 9:
            x[5] = 6
        elif x[5] == 12:
            x[5] = 7

        x[5] = x[5] - 1
        if x[5] == -2:
            x[5] = 6

        # Speed limit
        if x[6] == 0:
            x[6] == 40

        x[6] = int(x[6] / 10 - 1)

        # Junction detail
        if x[7] == -1:
            x[7] = 9

        # Weather conditions
        x[8] = x[8] - 1
        if x[8] == -2:
            x[8] = 8

        # Vehicle type
        elif x[9] == 1:
            x[9] = 0
        elif x[9] in [2, 3, 4, 5, 23, 97]:
            x[9] = 1
        elif x[9] in [8, 9, 90, -1]:
            x[9] = 2
        elif x[9] in [10, 11]:
            x[9] = 3
        elif x[9] == 19:
            x[9] = 4
        elif x[9] == 22:
            x[9] = 5
        elif x[9] in [20, 21, 98]:
            x[9] = 6
        elif x[9] in [16, 17]:
            x[9] = 7
        elif x[9] == 18:
            x[9] = 8
        else:
            x[9] = 2

    def oneHot(self):
        pass

    def setVehicleAgeBand(self, x):
        age = x[2]

        if age == -1:
            age = 4
        elif age >= 25:
            age = 12
        else:
            age = np.floor(age / 2)

        x[2] = int(age)

    def setTimeBand(self, x):
        time  = x[4]

        # If time is undefined
        if isinstance(time, float):
            hours = '12' # Assume midday
        else:
            hours = time[0:2]

        x[4] = int(hours)

    def preprocess(self):
        speeds = []

        for i in range(len(self.data)):
            self.setVehicleAgeBand(self.data[i])
            self.setTimeBand(self.data[i])

            self.fillMissingData(self.data[i])

        print(self.data[2387])

    def getData(self):
        return self.data