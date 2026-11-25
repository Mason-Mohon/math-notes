# Representing Functions as Power Series
2026-11-11
Math Academy
Subject: Calculus II
Topics: Power Series [Maclaurin Series](Maclaurin%20Series.md)

Function = expansion, interval of convergence

$$\displaylines{e^{x}=1+x+\frac{1}{2!}x^2+\frac{1}{3!}x^3+\cdots,x\in\left(-\infty,\infty\right)\\ \\ \sin\left(x\right)=x-\frac{1}{3!}x^3+\frac{1}{5!}x^5-\cdots,x\in\left(-\infty,\infty\right)\\ \\ \cos\left(x\right)=1-\frac{1}{2!}x^2+\frac{1}{4!}x^4-\cdots,x\in\left(-\infty,\infty\right)\\ \\ \ln\left(1+x\right)=x-\frac12x^2+\frac13x^3-\cdots,x\in\left(-1,1\right\rbrack\\ \\ \frac{1}{1-x}=1+x+x^2+x^3+\cdots,x\in\left(-1,1\right)\\ \\ \frac{1}{1+x}=1-x+x^2-x^3+\cdots,x\in\left(-1,1\right)}$$

## Q1
$$\displaylines{\ln(1-4x^2)=\ln\left(1+u\right)=u-\frac{u^2}{2}+\frac{u^3}{3}\\ \\ =-4x^2-8x^4-\frac{64}{3}x^6}$$

## Q2
$$\sin\left(x^3\right)=x^3-\dfrac{x^9}{6}+\dfrac{x^{15}}{120}-\cdots$$

## Q3
$$\sin(2x)+\sin(3x)=\left(2x-\frac{8x^3}{6}\right)+\left(3x-\frac{27x^3}{6}\right)=5x-\frac{35}{6}x^3+\cdots$$

## Q4
$$\displaylines{\dfrac{1}{1+2x}+\sin{x}\\ \\ =\left(1-2x+4x^2-8x^3\right)+\left(x-\frac{x^3}{6}\right)\\ \\ \dfrac{1}{1+2x}+\sin{x}=1-x+4x^2-\dfrac{49}{6}x^3+\cdots}$$

## Q5
$$\displaylines{\ln(1-x)=-x-\frac12\left(-x\right)^2+\frac13\left(-x\right)^3\\ \\ \ln(1-x)=-x-\dfrac12x^2-\dfrac13x^3-\cdots}$$

## Q6
$$\ln(1+2x)=2x - 2 x^2+\dfrac{8x^3}{3}-\cdots$$

## Q7
$$\displaylines{\dfrac{\ln(1-x)}{1+4x}=\left(-x-\dfrac12x^2-\dfrac13x^3\right)\left(1-4x+16x^2-64x^3\right)\\ \\ =-x+4x^2-16x^3+64x^4+2x^3-8x^4+32x^5-\frac12x^2-\frac13x^3\\ \\ =-x+\frac72x^2-\frac{43}{3}x^3+\cdots}$$

## Q8
$$\dfrac{\cos(x^2)-1}{x^2}=\frac{\left(\frac12x^4+\frac{1}{24}x^8-\frac{1}{720}x^{12}\right)}{x^2}=-\frac{x^2}{2}+\frac{x^6}{24}-\frac{x^{10}}{720}$$

# Review

$$\displaylines{e^{x}=1+x+\frac{1}{2!}x^2+\frac{1}{3!}x^3+\cdots,x\in\left(-\infty,\infty\right)\\ \\ \sin\left(x\right)=x-\frac{1}{3!}x^3+\frac{1}{5!}x^5-\cdots,x\in\left(-\infty,\infty\right)\\ \\ \cos\left(x\right)=1-\frac{1}{2!}x^2+\frac{1}{4!}x^4-\cdots,x\in\left(-\infty,\infty\right)\\ \\ \ln\left(1+x\right)=x-\frac12x^2+\frac13x^3-\cdots,x\in\left(-1,1\right\rbrack\\ \\ \frac{1}{1-x}=1+x+x^2+x^3+\cdots,x\in\left(-1,1\right)\\ \\ \frac{1}{1+x}=1-x+x^2-x^3+\cdots,x\in\left(-1,1\right)}$$

## Q1
$$\displaylines{\dfrac{e^x-e^{-x}}{2}=1+x+\frac{1}{2!}x^2+\frac{1}{3!}x^3-\left(1-x+\frac12x^2-\frac16x^3+\frac{1}{4!}x^4-\frac{1}{5!}x^5\right)\\ \\ \dfrac{e^{x}-e^{-x}}{2}=x+\dfrac{x^3}{6}+\dfrac{x^5}{120}+\cdots}$$

## Q2
$$\sqrt{x}\sin{\sqrt{x}}=\left(\sqrt{x}-\frac{1}{3!}x^{\frac32}+\frac{1}{5!}x^{\frac52}-\ldots\right)\left(\sqrt{x}\right)$$

## Q3
$$\displaylines{\ln\left(2+3x\right)=\ln2+\ln\left(\frac{3x}{2}\right)\\ \\ \ln\left(2+3x\right)=\ln{2}+\dfrac{3x}{2}-\dfrac{9x^2}{8}+\cdots}$$

# Review

## Q1
$$\displaylines{x\ln(1+x)\\ \\ x\ln(1+x)=x^2-\dfrac12x^3+\dfrac13x^4+\cdots}$$

## Q2
$$\displaylines{\cos(2x)+\cos\left(\sqrt{x}\right)\\ \\ \cos\left(2x\right)=1-2x^2+\frac{16}{24}x^4-\cdots\\ \\ \cos\left(\sqrt{x}\right)=1-\frac12x+\frac{1}{24}x^2-\cdots\\ \\ \cos(2x)+\cos\left(\sqrt{x}\right)=2-\dfrac{x}{2}-\dfrac{47x^2}{24}+\cdots}$$

## Q3
$$\displaylines{e^{-x}+\sin(4x).\\ \\ \sin\left(4x\right)=4x-\frac{32}{3}x^3+\frac{1}{5!}x^5-\cdots\\ \\ e^{-x}=1-x+\frac12x^2-\frac16x^3+\\ \\ e^{-x}+\sin(4x)=1+3x+\frac{x^2}{2}-\frac{65x^3}{6}}$$
