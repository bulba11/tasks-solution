import numpy  # импорт модуля для быстрой работы с массивами

epochs = 50000  # количество эпох

# сеть имеет три слоя - входной, один скрытый и выходной
inputLayerSize, hiddenLayerSize, outputLayerSize = 2, 3, 2  # количество входных, скрытых и выходных нейронов

X = numpy.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # набор входных данных для сети
Y = numpy.array([[0, 0], [1, 0], [1, 0], [0, 1]])  # набор выходных данных для сети для обучения xor и and


def sigmoid(x): return 1 / (1 + numpy.exp(-x))  # сигмоида - функция активации


def sigmoid_(x): return x * (1 - x)  # производная сигмоиды


# веса связей между нейронами

# массив связей между нейронами. Каждый элемент - массив - связи, входящие в один нейрон скрытого слоя
Wh = numpy.random.uniform(size=(inputLayerSize, hiddenLayerSize))  
Wz = numpy.random.uniform(size=(hiddenLayerSize, outputLayerSize))  # аналогично для нейронов выходного слоя

for i in range(epochs):  # по эпохам
    H = sigmoid(numpy.dot(X, Wh))  # результат работы скрытого слоя
    Z = sigmoid(numpy.dot(H, Wz))  # результат работы выходного слоя
    E = Y - Z  # расчёт ошибки
    dZ = E * sigmoid_(Z)  # раcчёт корректировки выходного слоя
    dH = dZ.dot(Wz.T) * sigmoid_(H)  # расчёт корректировки скрытого слоя
    Wz += H.T.dot(dZ)  # корректировка выходного слоя
    Wh += X.T.dot(dH)  # корректировка скрытого слоя

# вывод результатов
print(f"Обучение заняло {epochs} эпох.")
print("Результаты обучения:")
print(f"(0, 0) -> {numpy.round(Z[0], decimals=2)}")
print(f"(0, 1) -> {numpy.round(Z[1], decimals=2)}")
print(f"(1, 0) -> {numpy.round(Z[2], decimals=2)}")
print(f"(1, 1) -> {numpy.round(Z[3], decimals=2)}")