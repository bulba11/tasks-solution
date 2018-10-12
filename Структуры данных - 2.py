from __future__ import annotations  # для возможности использовать имя класса внутри его же объявления
from dataclasses import dataclass  # для удобного объявления класса


@dataclass  # удобное объявление класса с автоматической генерацией метода __init__ и __repr__
class Node:  # узел односвязного списка
	data: object = None  # поле класса - содержимое ячейки
	next: Node = None  # ссылка на следующий узел


@dataclass
class List:
	head: Node = None  # ссылка на голову списка

	def add(self, data):  # добавление объекта в список
		if self.head is None:  # если в списке нет элементов - создаём головной узел и сохраняем данные в этот узел
			self.head = Node(data)
		else:  # иначе ищем последний элемент списка и добавляем к нему узел с данными, что надо добавить
			itr = self.head  # узел списка
			while itr.next is not None:  # пока узел не последний - двигаемся по списку
				itr = itr.next
			itr.next = Node(data)

	def __iter__(self):
		return ListIterator(self.head)

@dataclass
class ListIterator:
	node: Node

	def __next__(self):
		if self.node is None:
			raise StopIteration
		data = self.node.data
		self.node = self.node.next
		return data


lst = List()

while True:  # повторять бесконечно
	ns = []
	try:
		inp = input()  # считываем строку со входного потока
		ns = [int(s) for s in inp.split()]  # пытаемся разделить строку на слова и распарсить числа
	except EOFError:  # если входной поток закончился - прекращаем цикл
		break
	except ValueError:  # если не удалось распарсить число
		print("Вводить можно только числа.")  # выводим сообщение об ошибке
		print("Эта строка не будет учтена.")
		continue

	for n in ns:
		lst.add(n)


count = 0
summ = 0
for n in filter(lambda x: x % 2 == 0, lst):
	count += 1
	summ += n

avg = round(summ / count)

print(f"Всего чётных чисел - {count}, их среднее - {avg}.")