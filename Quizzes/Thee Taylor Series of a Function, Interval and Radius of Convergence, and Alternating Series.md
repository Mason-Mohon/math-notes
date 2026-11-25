# Thee Taylor Series of a Function, Interval and Radius of Convergence, and Alternating Series
2026-11-24
Math Academy
Subject: Calculus II Multistep
Topics: [Taylor Series](../Calculus%20II/Taylor%20Series.md) Convergence and Divergence


$$f(x)=\sum\limits_{n=1}^{\infty}\dfrac{(-5)^{n+1}}{n}(x+1)^{n}$$

## Q1
$$\displaylines{L=\lim_{n\to\infty}\left|\frac{\left(-5\right)\left(x+1\right)n}{\left(n+1\right)}\right|=\left|-5x-5\right|\lim_{n\to\infty}\left(\frac{1}{n+1}\right)\\ \\ L=5\left|x+1\right|<1\Rightarrow R=\frac15}$$

## Q2
$$\displaylines{x=-\dfrac45,{\displaystyle\lim\limits_{n\to\infty}a_{n}=c}\\ \\ a_{n}=\dfrac{(-5)^{n+1}}{n\left(5\right)^{n}}=\frac{-5}{n}\cdot\left(-\frac55\right)^{n}=\frac{5\left(-1\right)^{n+1}}{n}}$$

## Q3
$$\displaylines{{\displaystyle f\left(-\dfrac65\right)=-\sum_{n=1}^{\infty}a_{n},}b_{n}=\dfrac{1}{n}\\ \\ a_{n}=\dfrac{(-5)^{n+1}}{n}(-\frac65+1)^{n}=-\frac{5}{n}\Rightarrow\frac{5}{n}\\ \\ {\displaystyle L=\lim_{n\to\infty}\dfrac{a_{n}}{b_{n}}}=5}$$

## Q4
$$\displaylines{f(x)=\sum\limits_{n=1}^{\infty}\dfrac{(-5)^{n+1}}{n}(x+1)^{n}\\ \\ f^{\prime}(x)=\sum\limits_{n=1}^{\infty}(-5)^{n+1}(x+1)^{n-1}\\ \\ =25-125\left(x+1\right)+625\left(x+1\right)^2}$$

## Q5
$$\displaylines{x=-1\\ \\ f^{\prime}(x)=\sum\limits_{n=1}^{\infty}(-5)^{n+1}(x+1)^{n-1}}$$

## Q6
$$\displaylines{S_{\infty}=\dfrac{a_1}{1-r},\qquad|r|\lt1,a_1=25\\ \\ r=\dfrac{a_2}{a_1}=\dfrac{25(-5x-5)^{2-1}}{25(-5x-5)^{1-1}}=-5x-5.\\ \\ \begin{align*}\sum_{n=1}^{\infty}25(-5x-5)^{n-1} & =\dfrac{a_1}{1-r}\\  & =\dfrac{25}{1-(-5x-5)}\\[5 pt]  & =\dfrac{25}{5x+6}\end{align*}}$$

## Q7
$$f\left(x\right)=25\int\left(5x+6\right)^{-1}\mathrm{d} x=5\ln\left(5x+6\right)$$
