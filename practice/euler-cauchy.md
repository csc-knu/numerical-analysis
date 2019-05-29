{% include mathjax %}

### Задача

> Методом Ейлера-Коші $$h = 0.1$$ зробити $$1$$ крок, $$\frac{\diff u}{\diff x} = x^2 + u$$, $$u(1) = 1$$.

### Розв'язок

Нагадаємо, що метод Ейлера-Коші має вигляд 

\begin{align}
	\bar y_{i + 1} &= y_n + h \cdot f(x_i, y_i), \newline
	y_{n + 1} &= y_n + \frac{h}{2} \left( f(x_i, y_i) + f(x_{i + 1}, \bar y_{i + 1}) \right),
\end{align}

де початкові значення зрозуміло які, $$x_0 = 0$$, $$y_0 = u_0 = u(0) = 1$$.

Тобто маємо 

\begin{equation}
	\begin{aligned}
		\bar y_1 &= y_0 + h \cdot f(x_0, y_0) = \newline
		&= 1 + 0.1 \cdot f(0, 1) = \newline
		&= 1 + 0.1 \cdot (0^2 + 1) = 1.1,
	\end{aligned}
\end{equation}

і

\begin{equation}
	\begin{aligned}
		y_1 &= y_0 + \frac{h}{2} \left( f(x_0, y_0) + f(x_1, \bar y_1) \right) = \newline
		&= 1 + \frac{0.1}{2} ( f(0, 1) + f(0.1, 1.1) ) = \newline
		&= 1 + 0.05 ( (0^2 + 1) + (0.1^2 + 1.1) ) = \newline
		&= 1 + 0.05 ( 1 + 1.11 ) = 1.1055.
	\end{aligned}
\end{equation}

[Назад до задач](README.md)

[Назад на головну](../README.md)
