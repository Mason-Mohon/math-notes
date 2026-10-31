# Improper Integrals Over the Real Line
2026-10-20
Math Academy
Subject: Calculus II
Topics: [Improper Integrals](Improper%20Integrals.md) Integrals

$$\displaylines{\int_{-\infty}^{\infty}f\left(x\right)\mathrm{d} x=\int_{-\infty}^0f\left(x\right)\mathrm{d} x+\int_0^{\infty}f\left(x\right)\mathrm{d} x\\ \\ \int_1^{\infty}\frac{1}{x^{p}}\mathrm{d} x,p>1\text{ Converges},p\le1\text{ Diverges}}$$

## Q1
$$f(x)=\dfrac{1}{1+4x^2}$$
![](../assets/Pasted%20image%2020261020101701.png)
## Q6
$$\displaylines{{\displaystyle\int_{-\infty}^{\infty}\dfrac{4x^3}{\left(2+x^4\right)^2}\,\textrm{d}x}\\ \\ \lim_{a\to\infty}\int_0^{a}\frac{1}{u^2}du=\lim_{a\to\infty}\left\lbrack-\frac{1}{u}\right\rbrack_0^{a}\\ \\ \int_{-\infty}^0\dfrac{4x^3}{\left(2+x^4\right)^2}\,\textrm{d}x=+\frac{1}{u}}$$

## Q7
$${\displaystyle\int_{-\infty}^{\infty}e^{-|x|+2}\,\textrm{d}x}=2\lim_{a\to\infty}\int_0^{a}e^{-x+2}dx=2\lim_{a\to\infty}\left\lbrack-e^{-x+2}\right\rbrack_0^{a}=2e^2$$

## Q8
$$\displaylines{\int_{-\infty}^{\infty}\dfrac{e^{x}}{1+3e^{2x}}\mathrm{d} x\\ \\ u=\sqrt3e^{x}\Rightarrow\frac{du}{\sqrt3}=e^{x}dx}$$

# Review

## Q1
$$\displaylines{\displaystyle\int_{-\infty}^\infty\dfrac{x}{\left(3+x^2\right)^2}\,\textrm{d}x.\\ \\ u=3+x^2\Rightarrow\frac{du}{\mathrm{d} x}2x\\ \\ \lim_{a\to\infty}\frac12\int_3^{a}\frac{1}{u^2}du=\lim_{a\to\infty}\left\lbrack-\frac{1}{2u}\right\rbrack_0^{a}=0+\frac16\\ \\ \frac16-\frac16}$$

## Q2
$$\int_{-\infty}^{\infty}2e^{-|x|+3}dx$$

## Q3
$$y =  \dfrac{3x^2}{1+2x^6}$$

# Review

## Q1
$$\int_{-\infty}^{\infty}\dfrac{4}{36+x^2}=\frac29\lim_{a\to\infty}\int_0^{a}\frac{1}{1+\left(\frac{x}{6}\right)^2}=\frac43\left\lbrack\arctan\left(\frac{x}{6}\right)\right\rbrack_0^{a}=\frac43\cdot\frac{\pi}{2}=\frac{2\pi}{3}$$

## Q2
$${\displaystyle\int_{-\infty}^{\infty}\dfrac{1}{4+x^2}\,\textrm{d}x=\frac12\lim_{a\to\infty}\int_0^{a}\frac{1}{1+\left(\frac{x}{2}\right)^2}}dx=\frac{\pi}{2}$$

## Q3
$$\displaylines{{\displaystyle\int_{-\infty}^{\infty}\dfrac{3}{9+2x^2}\,\textrm{d}x}\\ \\ \frac23\lim_{a\to\infty}\int_0^{a}\frac{1}{1+\left(\frac{\sqrt2}{3}x\right)^2}\mathrm{d} x=\lim_{a\to\infty}\frac23\left\lbrack\frac{3}{\sqrt2}\arctan\left(\frac{\sqrt2}{3}x\right)\right\rbrack_0^{a}=\frac{\pi}{\sqrt2}}$$
