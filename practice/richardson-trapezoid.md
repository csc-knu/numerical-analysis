{% include mathjax %}

### Задача

> З-ти явний вигляд кв. ф-ми, яка отримується з кв. ф-ли трапеції за ф-лою Річардсона.

### Розв'язок

Нагадаємо формулу Річардсона:

\begin{equation}
	\tilde I_{h/2} = \frac{2^m I_{h/2} - I_h}{2^m - 1},
\end{equation}

де для формули трапеції $$m = 2$$.

Далі, за формулою трапеції,

\begin{equation}
	I_h = h \left( \frac{f(0)}{2} + \Sum_{k = 1}^{n - 1} f(k h) + \frac{f(n h)}{2} \right),
\end{equation}

а також

\begin{equation}
	I_{h/2} = \frac{h}{2} \left( \frac{f(0)}{2} + \Sum_{k = 1}^{2 n - 1} f \left( \frac{k h}{2} \right) + \frac{f(n h)}{2} \right),
\end{equation}

або

\begin{equation}
	I_{h/2} = \frac{h}{2} \left( \frac{f(0)}{2} + \Sum_{k = 1}^{n - 1} f \left( \frac{(2 k - 1) h}{2} \right) + \Sum_{k = 1}^{n - 1} f(k h) + \frac{f(n h)}{2} \right).
\end{equation}

Підставляючи ці значення у формулу Річардсона, знаходимо

\begin{equation}
	\tilde I_{h/2} = \frac{h}{6} \left( f(0) + 4 \Sum_{k = 1}^{n - 1} f \left( \frac{(2 k - 1) h}{2} \right) + 2 \Sum_{k = 1}^{n - 1} f(k h) + f(n h) \right).
\end{equation}

[Назад до задач](README.md)

[Назад на головну](../README.md)
