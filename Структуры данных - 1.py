nums = []  # список для хранения чисел со входного потока

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

	if -42 in ns:  # если встретилось число -42
		ns = ns[:ns.index(-42)+1]  # убираем все числа после -42
		nums = nums + ns  # добавляем числа  в основной список
		for n in reversed(nums):  # выводим все числа в обратном порядке
			print(n, end=" ")
		break

	nums = nums + ns  # сохраняем числа в основной список

	if len(nums) > 100:  # если чисел больше 100 - прекращаем цикл
		break