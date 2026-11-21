# The Tabular Method of Integration by Parts
2026-11-20
Math Academy
Subject: Calculus II
Topics: Integrals Integration by Parts


$$\displaylines{\int x^3e^{\frac{x}{2}}\mathrm{d} x\\ \\ u=x^3,\frac{\mathrm{d} v}{\mathrm{d} x}=e^{\frac{x}{2}}}$$

| Derivates | Integrals | Sign | Products                  |
| --------- | --------- | ---- | ------------------------- |
| x^3       | e^x/2     |      | diaganol and to the right |
| 3x^2      | 2e^x/2    | +    | 2x^3e^x/2                 |
| 6x        | 4e^x/2    | -    | -12x^2e^x/2               |
| 6         | 8e^x/2    | +    | 48xe^x/2                  |
| 0         | 16e^x/2   | -    | -96e^x/2                  |
![](../assets/Pasted%20image%2020261120053419.png)

Add up all terms from last column to get the answer

$$\int x^3e^{\frac{x}{2}}\mathrm{d} x=2x^3e^{\frac{x}{2}}-12x^2e^{\frac{x}{2}}+48xe^{\frac{x}{2}}-96e^{\frac{x}{2}}+C$$


## Q1
$$\displaylines{{\displaystyle\int x^3\cos(3x)\,\textrm{d}x}\\ \\ u=x^3,v^{\prime}=\cos\left(3x\right)\\ \\ \begin{pmatrix}x^3 & \cos\left(3x\right) &  & \\ 3x^2 & \frac13\sin\left(3x\right) & + & \frac{x^3}{3}\sin\left(3x\right)\\ 6x & -\frac19\cos\left(3x\right) & - & \frac{x^2}{3}\cos\left(3x\right)\\ 6 & -\frac{1}{27}\sin\left(3x\right) & + & -\frac{2x}{9}\sin\left(3x\right)\\ 0 & \frac{1}{81}\cos\left(3x\right) & - & -\frac{2}{27}\cos\left(3x\right)\\  &  &  & \end{pmatrix}\\ \\ =\left(\frac13x^3-\frac29x\right)\sin\left(3x\right)+\left(\frac13x^2-\frac{2}{27}\right)\cos\left(3x\right)\\ \\ =(3x^3-2x)\dfrac{\sin(3x)}{9}+(9x^2-2)\dfrac{\cos(3x)}{27}+C}$$

## Q2
$$\displaylines{{\displaystyle\int x^3\sin(x)\,\textrm{d}x}\\ \\ u=x^3,v^{\prime}=\sin x\\ \\ \begin{pmatrix}x^3 & \sin x &  & \\ 3x^2 & -\cos x & + & -x^3\cos x\\ 6x & -\sin x & - & 3x^2\sin x\\ 6 & \cos x & + & 6x\cos x\\ 0 & \sin x & - & 6\sin x\end{pmatrix}\\ \\ =\left(6x-x^3\right)\cos x+\left(3x^2-6\right)\sin x+C}$$

## Q3
$$\displaylines{{\displaystyle\int(2x^3+3x^2+5)e^{2x}\,\textrm{d}x}\\ \\ \begin{pmatrix}2x^3+3x^2+5 & e^{2x} &  & \\ 6x^2+6x & \frac12e^{2x} & + & \frac12e^{2x}\left(2x^3+3x^2+5\right)\\ 12x+6 & \frac14e^{2x} & - & -\frac14e^{2x}\left(6x^2+6x\right)\\ 12 & \frac18e^{2x} & + & \frac18e^{2x}\left(12x+6\right)\\ 0 & \frac{1}{16}e^{2x} & - & -\frac34e^{2x}\end{pmatrix}\\ \\ =\frac12e^{2x}\left(2x^3+3x^2+5-3x^2-3x+3x+\frac64-\frac32\right)\\ \\ =\dfrac{e^{2x}}{2}(2x^3+5)+C}$$

## Q4
$$\displaylines{{\displaystyle{\int(2x^3-1)e^{x}\,\textrm{d}x}}\\ \\ \begin{pmatrix}2x^3-1 & e^{x} &  & \\ 6x^2 & e^{x} & + & e^{x}\left(2x^3-1\right)\\ 12x & e^{x} & - & e^{x}6x^2\\ 12 & e^{x} & + & 12xe^{x}\\ 0 & e^{x} & - & 12e^{x}\end{pmatrix}\\ \\ =e^{x}(2x^3-6x^2+12x-13)+C}$$


# Review

## Q1
$$$$

## Q2
$$$$

## Q3
$$$$
