'''Wyestymować wartość liczby $\pi$ metodą Monte Carlo.

Pole kwadratu to $4r^2$, a pole koła wynosi $\pi r^2$. W takim razie stosunek:
$$
\frac{P_{kola}}{P_{kwadratu}} = \frac{\pi r^2}{4 r^2} = \frac{\pi}{4}.
$$
W konsekwencji:
$$
\pi = 4 \frac{P_{kola}}{P_{kwadratu}}.
$$

Jeżeli będziemy losować punkty o współrzędnych od $-2r$ do $2r$, to stosunek liczby punktów zawierających się w kole o środku w punkcie $(0,0)$ i promieniu $r$ do wszystkich wylosowanych punktów, będzie dążył w nieskończoności (z pewnym prawdopodobieństwem) do stosunku tego pola koła do koła kwadratu o boku $2r$.

Cała metoda sprowadza się więc do tego, by losować punkty i sprawdzać, czy mieszczą się w kole.
'''

import random

def monte_carlo_pi(n):
    inside = 0
    for i in range(n):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)
        if x**2 + y**2 <= 4:
            inside += 1
    return 4 * inside / n

print(monte_carlo_pi(1000000))
print(monte_carlo_pi(1000000))
print(monte_carlo_pi(1000000))