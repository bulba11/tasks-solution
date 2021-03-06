import math

print("Введите два числа через пробел:", end=" ")

m = None
n = None
while n is None and m is None:  # пока n и m равны None, делаем:
	try:
		n, m = [int(s) for s in input().split()]  # попытка считать и распарсить числа
	except ValueError as e:
		print("Необходимо ввести два числа через пробел.")  # вывод сообщения об ошибке

# Реализация обобщённого алгоритма Евклида. Прочесть о нём можно в книге
# "Искусство программирования", часть 1, раздел 1.2.1, страница 33.

# инициализация переменных алгоритма
aa = 1
b = 1
a = 0
bb = 0
c = m
d = n

while True:  # выполнять бесконечно

	# основной цикл обобщённого алгоритма Евклида
	q = c // d
	r = c - d * q

	if r == 0:  # Если остаток от деления равен 0, алгоритм завершает работу
		break

	# Иначе цикл продолжает выполняться
	c = d
	d = r
	t = aa
	aa = a
	a = t - q * a
	t = bb
	bb = b
	b = t - q*b

# вывод результатов
print(f"НОД чисел {m} и {n} равен {d}.")
print(f"Числа a и b равны {a} и {b} соответственно.")
print("Уравнение:")
print(f"{a} * {m} + {b} * {n} = {d}.")