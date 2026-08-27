# Newton's Method for Optimizing Single-Variable Functions
2026-08-25
Math Academy
Subject: Calculus I
Topics: Optimization Newtonian Calculus

![](../assets/Pasted%20image%2020260825123452.png)
![](../assets/Pasted%20image%2020260825123513.png)

$$\displaylines{F\left(x\right)=f\left(x_{n}\right)+f^{\prime}\left(x_{n}\right)\left(x-x_{n}\right)+\frac12f^{\doubleprime}\left(x_{n}\right)\left(x-x_{n}\right)^2\\ \\ F^{\prime}\left(x\right)=f^{\prime}\left(x_{n}\right)+f^{\doubleprime}\left(x_{n}\right)\left(x-x_{n}\right)=0\\ \\ x_{n+1}=x_{n}-\frac{f^{\prime}\left(x_{n}\right)}{f^{\doubleprime}\left(x_{n}\right)}}$$


## Q1
$$\displaylines{f(x)=x^2\ln(x)-x+2,x\in\left\lbrack1,2\right\rbrack,x_0=1.2\\ \\ f^{\prime}\left(x\right)=x+2x\ln x-1\\ \\ f^{\doubleprime}\left(x\right)=3+2\ln x\\ \\ x_1=x-\frac{x+2x\ln x-1}{3+2\ln x}=1.2-\frac{1.2+2\left(1.2\right)\ln\left(1.2\right)-1}{3+2\ln\left(1.2\right)}=1.011}$$

## Q2
$$\displaylines{f(x)=x^3-4x+1,x_0=1,x\in\left\lbrack0,2\right\rbrack\\ \\ f^{\prime}\left(x\right)=3x^2-4\\ \\ f^{\doubleprime}\left(x\right)=6x\\ \\ x_1=1-\frac{3-4}{6}=\frac76=1.167}$$

## Q3
$$\displaylines{f(x)=\cos\left(3x+\dfrac{\pi}{4}\right),x\in\left\lbrack0,1\right\rbrack,x_0=1\\ \\ f^{\prime}\left(x\right)=-3\sin\left(3x+\frac{\pi}{4}\right)\\ \\ f^{\doubleprime}\left(x\right)=-9\cos\left(3x+\frac{\pi}{4}\right)\\ \\ x_1=x-\frac{-3\sin\left(3x+\frac{\pi}{4}\right)}{-9\cos\left(3x+\frac{\pi}{4}\right)}\\ \\ x_1=0.750\\ \\ x_2=0.786w}$$

## Q4
$$\displaylines{f(x)=x\sin x-4x^2,x\in\left\lbrack-2,2\right\rbrack,x_0=2\\ \\ f^{\prime}\left(x\right)=\sin x+x\cos x-8x\\ \\ f^{\doubleprime}\left(x\right)=2\cos x-x\sin x-8\\ \\ x_1=x-\frac{\sin x+x\cos x-8x}{2\cos x-x\sin x-8}\\ \\ x_2=0.025}$$

## Q5
$$\displaylines{f(x)=\sin(4x)-3x^2,x\in\left\lbrack0,0.5\right\rbrack,x_0=0.5\\ \\ f^{\prime}\left(x\right)=4\cos\left(4x\right)-6x\\ \\ f^{\doubleprime}\left(x\right)=-16\sin\left(4x\right)-6\\ \\ x_1=x-\frac{4\cos\left(4x\right)-6x}{-16\sin\left(4x\right)-6}\\ \\ \\ 0.283}$$

## Q6
$$\displaylines{f(x)=x^4+2x^2-x,x\in\left\lbrack0,1\right\rbrack,x_0=0.5\\ \\ f^{\prime}\left(x\right)=4x^3+4x-1\\ \\ f^{\doubleprime}\left(x\right)=12x^2+4\\ \\ x_1=x-\frac{4x^3+4x-1}{12x^2+4}}$$


# Review

## Q1
$$\displaylines{f(x)=x^3+x^2-3x+4,x_0=0\\ \\ f^{\prime}\left(x\right)=3x^2+2x-3\\ \\ f^{\doubleprime}\left(x\right)=6x+2\\ \\ x_1=x-\frac{3x^2+2x-3}{6x+2}}$$

## Q2
$$\displaylines{f(x)=x^4-4x^3+6x-2,x_0=3\\ \\ f^{\prime}\left(x\right)=4x^3-12x^2+6\\ \\ f^{\doubleprime}\left(x\right)=12x^2-24x\\ \\ x_1=x-\frac{4x^3-12x^2+6}{12x^2-24x}}$$

## Q3
$$\displaylines{f(x)=e^{2x}-4e^{x}+3,x_0=1\\ \\ f^{\prime}\left(x\right)=2e^{2x}-4e^{x}\\ \\ f^{\doubleprime}\left(x\right)=4e^{2x}-4e^{x}\\ \\ x_1=x-\frac{2e^{2x}-4e^{x}}{4e^{2x}-4e^{x}}}$$
