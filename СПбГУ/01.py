# cd Desktop\numerical-analysis\СПбГУ
# cls && python 1.py
import numpy as np
import matplotlib.pyplot as plt


def f(x):
	return np.power(x, 2) - 20 * np.sin(x)


def f_1(x):
	return 2 * x - 20 * np.cos(x)


def f_2(x):
	return 2 + 20 * np.sin(x)


if input("[I] Бажаєте побудувати графік функції f(x) на якомусь інтервалі? [Y/n]: ") == 'Y':
	a, b = map(float, input("[I] Введіть інтервал на якому бажаєте зобразити графік "
		"(у форматі [a, b] або (a, b)): "
		).lstrip('[').lstrip('(').rstrip(']').rstrip(')').split(', '))

	x = np.arange(a, b, 0.01)
	plt.grid(True)
	plt.plot(x, f(x), 'k', label='$f(x)$')
	plt.xlabel('$x$')
	plt.ylabel('$f(x)$')
	plt.legend(loc='best')
	plt.show()


while True:
	if input("[I] Бажаєте знайти корінь на якомусь інтервалі? [Y/n]: ") != 'Y':
		break

	a, b = map(float, input("[I] Введіть інтервал на якому бажаєте знайти нуль функції f(x) "
		"(у форматі [a, b]  або (a, b)): "
		).lstrip('[').lstrip('(').rstrip(']').rstrip(')').split(', '))

	if input("[I] Бажаєте звузити проміжок у кілька разів методом бісекції? [Y/n]: ") == 'Y':
		i = int(input("[I] Скільки разів бажаєте звузити проміжок: "))

		for _ in range(i):
			c = (a + b) / 2
			if f(a) * f(c) < 0:
				b = c
			if f(c) * f(b) < 0:
				a = c

		print(f"Новий проміжок [{a}, {b}].\n")
	
	if a > b:
		print("[E] Проміжок [a, b] не валідний, a > b. "
			"Програма не буде шукати корінь на цьому порміжку.")
		continue

	if f(a) * f(b) > 0:
		print("[W] Проміжок не задовольняє умовам теореми про збіжність, f(a) * f(b) > 0.")

	if any(f_1(np.arange(a, b, 0.01)) > 0) and any(f_1(np.arange(a, b, 0.01)) < 0):
		print("[W] Проміжок не задовольняє умовам теореми про збіжність, f' змінює знак.")

	if any(f_2(np.arange(a, b, 0.01)) > 0) and any(f_2(np.arange(a, b, 0.01)) < 0):
		print("[W] Проміжок не задовольняє умовам теореми про збіжність, f'' змінює знак.")

	x0 = float(input("[I] Введіть початкове наближення x0 з [a, b]: "))

	if a > x0 or x0 > b:
		print("[E] Початкове наближення x0 не з [a, b]. "
		 	"Програма не буде шукати корінь з таким початковим наближенням.")
		continue

	if f(x0) * f_2(x0) < 0:
		print("[W] Початкове наближення не задовольняє умовам теореми про збіжність, "
			"f(x0) * f''(x0) < 0. ")

	kmax = int(input("[I] Введіть максимальну кількість ітерацій: "))

	epsilon = 1e-6  # epsilon = float(input("Введіть бажану точність: "))

	x, k = [x0, x0 - f(x0) / f_1(x0)], 1
	while k < kmax and (abs(x[k] - x[k - 1]) >= epsilon or f(x[k]) >= epsilon):
		print(k, x[k], x[k] - x[k - 1], f(x[k]))
		x.append(x[-1] - f(x[-1]) / f_1(x[-1]))
		k += 1

	print(k, x[k], x[k] - x[k - 1], f(x[k]))
