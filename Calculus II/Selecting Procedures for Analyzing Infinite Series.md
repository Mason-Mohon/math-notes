# Selecting Procedures for Analyzing Infinite Series
2026-11-16
Math Academy
Subject: Calculus II
Topics: Infinite Series Series Convergence and Divergence

![](../assets/Pasted%20image%2020261116062436.png)

convergence tests.png
## Q1
$$\displaylines{{\displaystyle\sum_{n=1}^{\infty}\left(\dfrac{\cos{n}}{n}\right)^2}\\ \\ a_{n}=\frac{\cos^2n}{n^2}\le\frac{1}{n^2},\text{ comparable to known, then p series. converges}\\ \\ {\displaystyle\sum_{n=1}^{\infty}\dfrac{3n+4n^4}{n^4+2n^2}}\\ \\ a_{n}=\dfrac{3n+4n^4}{n^4+2n^2}\Rightarrow\lim_{n\to\infty}\dfrac{\frac{3}{n^3}+4}{1+\frac{2}{n^2}},\text{ diverges by divergence test}\\ \\ {\displaystyle\sum_{n=1}^{\infty}\dfrac{\sqrt{n}}{n+2}}\\ \\ a_{n}=\dfrac{\sqrt{n}}{n+2},b_{n}=\frac{1}{\sqrt{n}},\frac{a_{n}}{b_{n}}=\frac{1}{1+\frac{2}{n}}=1,\text{ }\\ \\ \text{compare to known and then p series. diverges}}$$

## Q2
$$\displaylines{{\displaystyle\sum_{n=1}^{\infty}\dfrac{(-1)^{n+1}}{n^2\sqrt{n}}}\text{, alternating series test}\\ \\ b_{n}=\frac{1}{n^{\frac52}},\text{ converges because }b_{n}\to0\\ \\ {\displaystyle\sum_{n=1}^{\infty}\dfrac{1}{\sqrt[7]{n^6}}},p=\frac67,\text{ diverges}\\ \\ {\displaystyle\sum_{n=1}^{\infty}\dfrac{n!}{(2n)!}}\text{ ratio test}\\ \\ \left|\frac{a_{n+1}}{a_{n}}\right|=\frac{\left(n+1\right)!}{\left(2n+2\right)!}\cdot\frac{\left(2n\right)!}{n!}=\frac{1}{2\left(2n+1\right)}\to0\text{, converges}}$$

## Q3
$${\displaystyle\sum_{n=1}^{\infty}a_{n}},0<a_{n}\leq b_{n},n\geq1,a_{n}\text{ diverges}$$


# Review

## Q1
$$\displaylines{{\displaystyle\sum_{n=1}^{\infty}\dfrac{\sqrt[3]{n}}{\sqrt{n^3}}},\frac96-\frac26,a_{n}=\frac{1}{n^{\frac76}},p=\frac76>1,\text{ converges}\\ \\ {\displaystyle\sum_{n=1}^{\infty}\ln\left(\dfrac{n}{3n+1}\right)}\Rightarrow f\left(x\right)=\ln\left(\frac{x}{3x+1}\right)\Rightarrow\lim_{a\to\infty}\int_1^{a}\ln\left(\frac{x}{3x+1}\right)\mathrm{d} x\\ \\ u=\ln\left(\frac{x}{3x+1}\right)\Rightarrow\mathrm{d} u=\frac{3x+1}{x}\cdot\frac{3x+1-\left(3x\right)}{\left(3x+1\right)^2}=\frac{1}{3x^2+x}\\ \\ v=x\Rightarrow\mathrm{d} v=\mathrm{d} x\\ \\ x\ln\left(\frac{x}{3x+1}\right)-\frac13\ln\left(3x+1\right)\\ \\ L=\ln\left(\frac13\right)\text{ divergence test, it diverges because }L\ne0\\ \\ {\displaystyle\sum_{n=2}^{\infty}\dfrac{n}{\sqrt{n}(n-1)}}\Rightarrow a_{n}=\frac{n}{n^{\frac32}-\sqrt{n}},L=0\\ \\ b_{n}=\frac{1}{\sqrt{n}},p=-\frac12<1\\ \\ a_{n}>b_{n}\text{, both diverge}}$$

## Q2
$$\displaylines{{\displaystyle\sum_{n=1}^{\infty}\dfrac{1}{n^2+4}=a_{n},}b_{n}=\frac{1}{n^2},p=2,a_{n}<b_{n},\text{ converge}\\ \\ {\displaystyle\sum_{n=1}^{\infty}\dfrac{1}{n^2\sqrt[3]{n}}\Rightarrow a_{n}=\frac{1}{n^{\frac53}},p=\frac53>1,\text{ converge}}\\ \\ {\displaystyle\sum_{n=1}^{\infty}\dfrac{n+1}{n-3}}}$$

## Q3
$$\displaylines{{\displaystyle\sum_{n=1}^{\infty}\dfrac{2n}{\sqrt{n^2+4}}\Rightarrow f\left(x\right)=\frac{2x}{\sqrt{x^2+4}}\Rightarrow\lim_{a\to\infty}\int_5^{a}\frac{1}{\sqrt{u}}\mathrm{d} x=2\sqrt{a}-2\sqrt5=\infty\text{,  diverges}}\\ \\ {\displaystyle\sum_{n=1}^{\infty}\dfrac{5^{n-1}}{4^{n+1}}}\\ \\ L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=\lim_{n\to\infty}\frac{5\cdot5^{n-1}}{4\cdot4^{n+1}}\cdot\frac{4^{n+1}}{5^{n-1}}=\frac54>1,\text{ diverges}\\ \\ {\displaystyle\sum_{n=1}^{\infty}\dfrac{n!}{5^{n}}}\\ \\ L=\lim_{n\to\infty}\frac{\left(n+1\right)n!}{5\cdot5^{n}}\cdot\frac{5^{n}}{n!}=\lim_{n\to\infty}\left|\frac{n+1}{5}\right|=\infty\text{ diverges}}$$
