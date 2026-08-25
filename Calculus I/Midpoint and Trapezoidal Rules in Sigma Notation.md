# Midpoint and Trapezoidal Rules in Sigma Notation
2026-08-21
Math Academy
Subject: Calculus I
Topics: Sigma Notation [Approximating Areas With the Trapezoidal Rule](Approximating%20Areas%20With%20the%20Trapezoidal%20Rule.md) [Approximating Areas With the Midpoint Riemann Sum](Approximating%20Areas%20With%20the%20Midpoint%20Riemann%20Sum.md) Riemann Sum

![](../assets/Pasted%20image%2020260821101233.png)
$$\displaylines{\left(f\left(x_1^{\text{\textasteriskcentered}}\right)+f\left(x_2^{\text{\textasteriskcentered}}\right)+\cdots+f\left(x_{m}^{\text{\textasteriskcentered}}\right)\right)\cdot\Delta x\\ \\ m\text{ is the number of rectangles}\\ \\ x_{i}^{\text{\textasteriskcentered}}\text{ is the midpoint of the }i\text{th subinterval}\\ \\ \sum_{i=1}^{m}f\left(x_{i}^{\text{\textasteriskcentered}}\right)\Delta x\\ \\ x_{i}^{\text{\textasteriskcentered}}=a+\left(i-\frac12\right)\Delta x,\Delta x=\frac{b-a}{m}}$$
![](../assets/Pasted%20image%2020260821101551.png)
![](../assets/Pasted%20image%2020260821101603.png)
## Q1
![](../assets/Pasted%20image%2020260821101613.png)
$$\displaylines{y=x^2-2x+2,a=1.5,b=4.5\\ \\ x_{i}=1.5+\left(k-\frac12\right)=1+k\\ \\ \Delta x=\frac{4.5-1.5}{3}=1\\ \\ S_{M}=\sum_{k=1}^3\left(\left(1+k\right)^2-2-2k+2\right)=k^2+2k+1-2k=k^2+1\\ \\ S_{M}=\sum_{k=1}^3\left(k^2+1\right)\cdot1}$$

$$\displaylines{x_{i}^{\text{\textasteriskcentered}}=a+\left(i-\frac12\right)\Delta x\\ \\ \Delta x=\frac{b-a}{m}\\ \\ \sum_{i=1}^{m}f\left(x_{i}^{\text{\textasteriskcentered}}\right)\Delta x}$$

## Q2
$$\displaylines{y=\cos^2(x+1),a=-\frac12,b=\frac72,m=4\\ \\ \Delta x=\frac{\frac72+\frac12}{4}=1\\ \\ x_{i}=k-1\\ \\ S_{M}={\displaystyle\sum_{k=1}^4}\left(\cos^2(k)\right)}$$

## Q3
$$\displaylines{y=(x+1)^3,a=-1,b=0,m=n\\ \\ \Delta x=\frac{1}{n}\\ \\ x_{i}=-1-\left(j-\frac12\right)\left(\frac{1}{n}\right)=-1-\frac{j}{n}+\frac{1}{2n}=-1-\frac{2j-1}{2n}\\ \\ \sum_{j=1}^{n}\left(1-1-\frac{2j-1}{2n}\right)^3\left(\frac{1}{n}\right)={\displaystyle\sum_{j=1}^{n}\dfrac{(2j-1)^3}{8n^4}}}$$

## Q4
$$\displaylines{y=\ln(x+1),a=0,b=2,m=n\\ \\ \Delta x=\frac{2}{n}\\ \\ x_{i}=0+\left(k-\frac12\right)\frac{2}{n}=\left(\frac{2k-1}{n}\right)=\frac{2k-1}{n}\\ \\ S_{M}={\displaystyle\sum_{k=1}^{n}\dfrac{2}{n}\cdot\ln\left(1+\frac{2k-1}{n}\right)}}$$

![](../assets/Pasted%20image%2020260821104936.png)

$$\displaylines{\frac{\Delta x}{2}\left\lbrack f\left(a\right)+2\left(\sum_{j=1}^{n-1}f\left(x_{j}\right)\right)+f\left(b\right)\right\rbrack\\ \\ x_{j}=a+j\Delta x,\Delta x=\frac{b-a}{n}}$$

## Q5
$$\displaylines{y=e^{x},a=1,b=5,n=4\\ \\ \Delta x=\frac44=1\\ \\ x_{k}=1+k\\ \\ \frac12\left\lbrack e+2\left(\sum_{k=1}^3e^{1+j}\right)+e^5\right\rbrack=\frac{e^1+e^5}{2}+\sum_{k=1}^3e^{1+k}}$$

## Q6
$$\displaylines{y=x^3+1,a=0,b=4,n=4,j\\ \\ \Delta x=\frac44=1\\ \\ x_{j}=j\\ \\ \frac12\left\lbrack f\left(0\right)+2\left(\sum_{j=1}^{n-1}f\left(j\right)\right)+f\left(4\right)\right\rbrack=\frac12\left\lbrack1+2\left(\sum_{j=1}^{n-1}f\left(j\right)\right)+65\right\rbrack\\ \\ =33+{\displaystyle\sum_{j=1}^3(j^3+1)}}$$

## Q7
$$\displaylines{y=2^{x},a=0,b=2,n=n,i\\ \\ \Delta x=\frac{2}{n}\\ \\ x_{i}=\frac{2i}{n}\\ \\ \frac{1}{n}\left\lbrack1+2\left(\sum_{i=1}^{n-1}2^{\left(\frac{2i}{n}\right)}\right)+4\right\rbrack=\frac{5}{n}+\frac{2}{n}{\displaystyle\sum_{i=1}^{n-1}2^{2i/n}}}$$

## Q9
$$\displaylines{y=4^{x},a=0,b=1,n=n,i\\ \\ \Delta x=\frac{1}{n}\\ \\ x_{i}=\frac{i}{n}\\ \\ \frac{1}{2n}\left\lbrack1+2\left(\sum_{j=1}^{n-1}f\left(\frac{i}{n}\right)\right)+4\right\rbrack={\displaystyle\dfrac{1}{2n}\left(5+2\sum_{i=1}^{n-1}4^{i/n}\right)}}$$

## Q10
$$\displaylines{y=4-x^2,a=-2,b=2,n=n,j\\ \\ \Delta x=\frac{4}{n},x_{j}=-2+\frac{4j}{n}\\ \\ \frac{4}{2n}\left\lbrack0+2\left(\sum_{j=1}^{n-1}f\left(-2+\frac{4j}{n}\right)\right)+0\right\rbrack}$$



# Review

## Q1
$$\displaylines{y=\frac{1}{x},a=1,b=3\\ \\ x_{i}^{\text{\textasteriskcentered}}=1+\left(i-\frac12\right)\frac{2}{m}=1+\frac{2i-1}{m}\\ \\ \Delta x=\frac{2}{m}\\ \\ \sum_{i=1}^{m}f\left(x_{i}^{\text{\textasteriskcentered}}\right)\Delta x=\left(\frac{m}{m+2i-1}\right)\cdot\frac{2}{m}={\displaystyle\sum_{i=1}^{m}\dfrac{2}{2i-1+m}}}$$

## Q2
$$\displaylines{y=\dfrac{x+1}{2},a=-1,b=1\\ \\ \Delta x=\frac{2}{n}\\ \\ x_{i}=-1+\frac{2i}{n}\\ \\ \frac{1}{n}\left\lbrack0+2\left(\sum_{j=1}^{n-1}\frac{i}{n}\right)+1\right\rbrack=\dfrac{1}{n}\left[1+2{\displaystyle\sum_{i=1}^{n-1}\dfrac{i}{n}}\right]}$$

## Q3
$$\displaylines{y=\dfrac{1}{x+2},a=1,b=7,n=6\\ \\ \Delta x=1\\ \\ x_{k}=1+k\\ \\ \frac12\left\lbrack f\left(1\right)+2\left(\sum_{k=1}^5f\left(1+k\right)\right)+f\left(7\right)\right\rbrack\\ \\ \frac12\left\lbrack\frac13+2\left(\sum_{k=1}^5f\left(1+k\right)\right)+\frac19\right\rbrack=\frac29+\sum_{k=1}^5\left(\frac{1}{3+k}\right)}$$
