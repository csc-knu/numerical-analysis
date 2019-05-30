{% include mathjax %}

## Чисельне інтегрування

_Необхідними умовами здачі лабораторної роботи є наявність звіту, студента, викладача, і ноутбука._

### Постановка задачі

Ообчислити невласний інтеграл $$\Int_a^b f(x) \diff x$$ 

Вивести наближене значення інтегралу $$I_h$$, похибку $$R_h^\circ$$, та кінцевий крок розбиття інтервалу $$h$$.

Для обчислень використати певну формулу, принцип Рунге, формулу Річардсона, та апріорні оцінки похибки для квадратурних формул.

Параметрами варінту є:

- функція $$f(x)$$;

- проміжок $$[a, b]$$;

- формула яку потрібно використати.

<!-- ### Варіанти -->

### Приклади звітів

<!-- - Нікіта Скибицький, 2019&nbsp;р.: [pdf](tex/report.pdf) -->

- Ілля Бабієнко, 2019&nbsp;р.: [pdf](tex/report-babienko-2019.pdf)

_Можливо з часом тут будуть розміщені ще звіти._

### Нотатки по моєму варіанту, тимчасово будуть тут

Необхідно обчислити інтеграл 

\begin{equation}
	\Int_{-1}^{1} \frac{\ln \left(2 + \sqrt[3]{x} \right)}{\sqrt[3]{x}} \diff x.
\end{equation}

#### Мультиплікативний метод:

Спочатку обмежимося проміжком $$[0, 1]$$.

Запишемо

\begin{equation}
	\Int_{0}^{1} \frac{\ln \left(2 + \sqrt[3]{x} \right)}{\sqrt[3]{x}} = \Int_{0}^{1} \underset{\rho(x)}{\underbrace{\frac{1}{\sqrt[3]{x}}}} \cdot \underset{f(x)}{\underbrace{\ln \left(2 + \sqrt[3]{x}\right)}} \diff x
\end{equation}

Знайдемо сім'ю багаточленів які ортогональні з вагою $$\rho(x) = \sqrt[3]{x}$$.

Для цього візьмемо сім'ю $$1, x, x^2, \ldots$$ і &laquo;пропустимо&raquo; її через процес ортогоналізації Грама-Шмідта:

- $$P_0 = {\bf 1}$$;

- $$P_1 = x - \frac{\langle {\bf 1}, x\rangle}{\langle {\bf 1}, {\bf 1} \rangle} \cdot {\bf 1}$$. 

	Враховуючи визначення скалярного добутку маємо:

	\begin{equation}
		P_1 = x - \frac{\Int_{0}^{1} x^{4/3} \diff x}{\Int_{0}^{1} x^{1/3} \diff x} \cdot x = x - \frac{3/7}{3/4} \cdot {\bf 1} = x - \frac{4}{7}.
	\end{equation}

- $$P_2 = x^2 - \frac{\langle {\bf 1}, x^2\rangle}{\langle {\bf 1}, {\bf 1} \rangle} \cdot {\bf 1} - \frac{\langle x - 4/7, x^2\rangle}{\langle x - 4/7, x - 4/7 \rangle} \cdot (x - 4/7)$$. 

	Враховуючи визначення скалярного добутку маємо:

	\begin{equation}
		\begin{aligned}
			P_2 &= x^2 - \frac{\Int_{0}^{1} x^{7/3} \diff x}{\Int_{0}^{1} x^{1/3} \diff x} \cdot {\bf 1} - \frac{\Int_{0}^{1} x^{7/3} \left(x - \frac{4}{7} \right) \diff x}{\Int_{0}^{1} x^{1/3} \left(x - \frac{4}{7} \right)^2 \diff x} \cdot \left(x - \frac{4}{7} \right) = \newline
			&= x^2 - \frac{3/10}{3/4} \cdot {\bf 1} - \frac{27/455}{27/490} \cdot \left(x - \frac{4}{7} \right) = x^2 - \frac{2}{5} - \frac{14}{13} \cdot \left(x - \frac{4}{7} \right) = x^2 - \frac{14 x}{13} + \frac{14}{65}.
		\end{aligned}
	\end{equation}

<!-- \frac{15}{2} \cdot \ln 3 - 6  -->

- метод обрізання границі
- метод виділення особливостей


[Назад до лаб](../README.md)

[Назад на головну](../../README.md)