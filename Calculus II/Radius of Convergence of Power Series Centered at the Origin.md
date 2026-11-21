# Radius of Convergence of Power Series Centered at the Origin
2026-11-17
Math Academy
Subject: Calculus II
Topics: Series Convergence and Divergence


$$\displaylines{\sum_{n=1}^{\infty}\frac{x^{n}}{n^2}=x+\frac{x^2}{2^2}+\frac{x^3}{3^2}+\frac{x^4}{4^2}+\cdots\\ \\ \text{Ratio test}\\ \\ L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=1,\text{inconclusive}\\ \\ x=1\text{ converges by p series test}\\ \\ x=-1\text{ converges by alternating series test}\\ \\ x\in\left\lbrack-1,1\right\rbrack\text{ interval of convergenct}\\ \\ \text{Radius of convergence }\\ \\ R=\frac{1-\left(-1\right)}{2}=1\\ \hline\\ \\ \\ \hline}$$


## Q1
$$\displaylines{\sum_{n=1}^{\infty}\dfrac{(-1)^{n-1}x^{n}}{2^{n}\sqrt{n}}=\dfrac{x}{2}-\dfrac{x^2}{2^2\cdot\sqrt2}+\dfrac{x^3}{2^3\cdot\sqrt3}-\dfrac{x^4}{2^4\cdot\sqrt4}+\cdots\,?\\ \\ L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=\left(\dfrac{(-1)^{n}x^{n+1}}{2^{n+1}\sqrt{n+1}}\right)\cdot\left(\frac{2^{n}\sqrt{n}}{(-1)^{n-1}x^{n}}\right)\\ \\ =\left(\dfrac{(-1)^{n-1}\left(-1\right)x^{n}\cdot x}{2\cdot2^{n}\sqrt{n+1}}\right)\cdot\left(\frac{2^{n}\sqrt{n}}{(-1)^{n-1}x^{n}}\right)\\ \\ =\lim_{n\to\infty}\left|\frac{-x\sqrt{n}}{2\sqrt{n+1}}\right|=\frac{\left|x\right|}{2}\cdot1\Rightarrow\left|x\right|<2,R=2}$$

## Q2
$$\displaylines{\sum_{n=0}^{\infty}(-1)^{n+1}5^{n}x^{n+2}=-x^2+5x^3-5^2x^4+5^3x^5+\cdots\,.\\ \\ L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=\frac{(-1)^{n+2}5^{n+1}x^{n+3}}{(-1)^{n+1}5^{n}x^{n+2}}=\left|-5x\right|\Rightarrow\left|x\right|<\frac15}$$

## Q3
$$\displaylines{\sum_{n=1}^{\infty}\frac{(-1)^{\,n-1}x^{n}}{n}=x-\frac{x^2}{2}+\frac{x^3}{3}-\frac{x^4}{4}+\cdots\,.\\ \\ L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=\frac{-x(-1)^{\,n-1}x^{n}}{n+1}\cdot\frac{n}{\left(-1\right)^{n-1}x^{n}}=\left|x\right|\lim_{n\to\infty}\left|\frac{n}{n+1}\right|\Rightarrow\left|x\right|<1\\ \\ x=1\Rightarrow1-\frac12+\frac13-\frac14}$$

## Q4
$$\displaylines{\sum_{n=1}^{\infty}\dfrac{x^{n}}{4^{n}(5n-2)}=\dfrac{x}{4\cdot3}+\dfrac{x^2}{4^2\cdot8}+\dfrac{x^3}{4^3\cdot13}+\cdots\\ \\ L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=\left(\dfrac{x\cdot x^{n}}{4\cdot4^{n}(5n+3)}\right)\cdot\left(\frac{4^{n}\left(5n-2\right)}{x^{n}}\right)\Rightarrow\frac{\left|x\right|}{4}<1,\left|x\right|<4\\ \\ x=4\Rightarrow\sum_{n=1}^{\infty}\dfrac{4^{n}}{4^{n}(5n-2)}=\sum_{n=1}^{\infty}\dfrac{1}{5n-2}=\frac13+\frac18+\frac{1}{13}+\cdots\text{ diverges by comparison with harmonic series}\\ \\ x=-4\Rightarrow-\frac13-\frac18-\frac{1}{13}\text{ converges by alternating series test}\\ \\ \left\lbrack-4,4\right)}$$

## Q5
$$\displaylines{\sum_{n=0}^{\infty}\frac{3^{n}x^{n}}{n^2+1}=1+\dfrac{3x}{2}+\frac{3^2x^2}{5}+\frac{3^3x^3}{10}+\cdots\,.\\ \\ L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=\left(\frac{3x\cdot3^{n}x^{n}}{\left(n+1\right)^2+1}\right)\cdot\left(\frac{n^2+1}{3^{n}x^{n}}\right)=3\left|x\right|\lim_{n\to\infty}\frac{n^2+1}{\left(n+1\right)^2+1}\\ \\ R=\frac13\\ \\ x=\frac13\Rightarrow\sum_{n=0}^{\infty}\frac{3^{n}\cdot\frac13^{n}}{n^2+1}=\sum_{n=0}^{\infty}\frac{1}{n^2+1}\le\frac{1}{n^2}\text{ compare wiht p series},\text{ }p=2>1,\text{ converges}\\ \\ x=-\frac13\Rightarrow\sum_{n=0}^{\infty}\frac{\left(-1\right)^{n}}{n^2+1}\le\frac{1}{n^2}\text{, same as above}\\ \\ x\in\left[-\dfrac13,\dfrac13\right]}$$

## Q6
$$\displaylines{\sum_{n=0}^{\infty}\frac{x^{n}}{(2n+1)!}=1+\frac{x}{3!}+\frac{x^2}{5!}+\frac{x^3}{7!}+\cdots\,.\\ \\ L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=\left(\frac{x\cdot x^{n}}{(2n+3)!}\right)\cdot\frac{\left(2n+1\right)!}{x^{n}}\\ \\ =\left|x\right|\lim_{n\to\infty}\frac{\left(2n+1\right)!}{\left(2n+3\right)\left(2n+2\right)\left(2n+1\right)!}\\ \\ R=\infty}$$


# Review

## Q1
$$\displaylines{{\displaystyle\sum_{n=0}^{\infty}\frac{n^2 x^{n}}{n!}}\\ \\ L=\lim_{n\to\infty}\left(\frac{\left(n+1\right)^2x\cdot x^{n}}{\left(n+1\right)\cdot n!}\cdot\frac{n!}{n^2x^{n}}\right)=\left|x\right|\lim_{n\to\infty}\left(\frac{n+1}{n^2}\right)=0\\ \\ x\in\left(-\infty,\infty\right)}$$

## Q2
$$\displaylines{\sum_{n=0}^{\infty}\frac{x^{n}}{(n+1)!}=1+\frac{x}{2!}+\frac{x^2}{3!}+\frac{x^3}{4!}+\cdots\,\\ \\ L=\lim_{n\to\infty}\left|\frac{x\cdot x^{n}}{\left(n+2\right)\left(n+1\right)!}\cdot\frac{\left(n+1\right)!}{x^{n}}\right|=\left|x\right|\lim_{n\to\infty}\left(\frac{1}{n+2}\right)\to0\\ \\ R=\infty}$$

## Q3
$$\displaylines{{\displaystyle\sum_{n=1}^{\infty}\frac{x^{n}}{n^3}=x+\dfrac{x^2}{2^3}+\dfrac{x^3}{3^3}+\dfrac{x^4}{4^3}+\cdots\,}\\ \\ L=\lim_{n\to\infty}\left|\frac{x\cdot x^{n}}{\left(n+1\right)^3}\cdot\frac{n^3}{x^{n}}\right|=\left|x\right|\lim_{n\to\infty}\frac{n^3}{\left(n+1\right)^3}\Rightarrow\left|x\right|<1\\ \\ R=1\\ \\ \frac{1}{n^3},p=3>1,\text{ both converge}\\ \\ x\in\left\lbrack-1,1\right\rbrack\\ \\ \\ \\ \hline}$$
