{% include mathjax %}

### Задача

> За принципом Рунге оцінити пох. чисельн. інтегрув. за формулою трапецій 
> 
> \begin{equation}
> I(f) = \Int_0^1 \frac{\diff x}{1 + x^2}
> \end{equation}
>
> для кроку $$0.25$$.
>
> За Річардсона уточними обчислене значення.

### Розв'язок

Принцип Рунге каже, що 

\begin{equation}
	\overset{\circ} R_{h/2} = \frac{I_{h/2} - I_h}{2^m - 1}.
\end{equation}

У нас $$0.25 = h/2$$, $$m = 2$$ бо формула трапецій.

Далі за формулою трапецій обчислюємо:

\begin{equation}
	I_{0.5} = 0.5 \cdot \left( \frac{f(0)}{2} + f(0.5) + \frac{f(1)}{2} \right) = \frac{41}{30}
\end{equation}

і

\begin{equation}
	I_{0.25} = 0.25 \cdot \left( \frac{f(0)}{2} + f(0.25) + f(0.5) + f(0.75) + \frac{f(1)}{2} \right) = \frac{5323}{6800}.
\end{equation}

Тоді

\begin{equation}
	\overset{\circ} R_{h/2} = \frac{\frac{5323}{6800} - \frac{31}{40}}{2^2 - 1} = \frac{53}{20400} \approx 0.0025980.
\end{equation}

Уточнимо знайдене значення за формулою Річардсона:

\begin{equation}
	\tilde I_{h/2} = \frac{4}{3} \cdot I_{h/2} - \frac{1}{3} \cdot I_h.
\end{equation}

Підсвляючи наші значення маємо:

\begin{equation}
	\tilde I_{h/2} = \frac{4}{3} \cdot \frac{5323}{6800} - \frac{1}{3} \cdot \frac{31}{40} = \frac{8011}{10200} \approx 0.7853922.
\end{equation}

Зауважимо, що це значення відхиляється від справжнього значення $$\pi / 4$$ всього лише на $$6.00653 \times 10^{-6}$$.

[Назад до задач](README.md)

[Назад на головну](../README.md)
