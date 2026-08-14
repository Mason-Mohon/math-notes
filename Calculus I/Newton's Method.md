# Newton's Method
2026-08-12
Math Academy
Subject: Calculus I
Topics: Roots Differentiation Linearization

![](../assets/Screenshot%202026-08-12%20at%207.44.49%20PM.png)
![](../assets/Screenshot%202026-08-12%20at%207.49.01%20PM.png)
![](../assets/Screenshot%202026-08-12%20at%207.49.29%20PM.png)
![](../assets/Screenshot%202026-08-12%20at%207.49.44%20PM.png)

$$\displaylines{L\left(x\right)=f\left(a\right)+f^{\prime}\left(a\right)\left(x-a\right)\\ \\ F\left(x\right)=f\left(x_0\right)+f^{\prime}\left(x_0\right)\left(x-x_0\right)}$$

Newton-Raphson method:
$$x_{n+1}=x_{n}-\frac{f\left(x_{n}\right)}{f^{\prime}\left(x_{n}\right)}$$

## Q1
$$\displaylines{f(x)=\ln(x+1)-x^2+2,x\in\left\lbrack1,2\right\rbrack,x_0=1.5\\ \\ f^{\prime}\left(x\right)=\frac{1}{x+1}-2x\\ \\ x_1=x_0-\frac{\ln(x+1)-x^2+2}{\frac{1}{x+1}-2x}\\ \\ x_1=1.5-\frac{\ln(1.5+1)-\left(1.5\right)^2+2}{\frac{1}{1.5+1}-2\left(1.5\right)}=1.756}$$

## Q2
$$\displaylines{f(x)=x^4+x^3-2,x\in\left\lbrack0,2\right\rbrack,x_0=0.5\\ \\ f^{\prime}\left(x\right)=4x^3+3x^2\\ \\ x_1=x_0-\frac{x^4+x^3-2}{4x^3+3x^2}\\ \\ x_1=0.5-\frac{0.5^4+0.5^3-2}{4\left(0.5\right)^3+3\left(0.5\right)^2}=1.95}$$
![](../assets/Screenshot%202026-08-12%20at%208.04.25%20PM.png)
## Q3
$$\displaylines{f(x)=x^4-10x^2+8,x\in\left\lbrack0,1\right\rbrack,x_0=0.5\\ \\ f^{\prime}\left(x\right)=4x^3-20x\\ \\ x_1=x_0-\frac{x^4-10x^2+8}{4x^3-20x}\\ \\ x_1=0.5-\frac{0.5^4-10\left(0.5\right)^2+8}{4\left(0.5\right)^3-20\left(0.5\right)}=1.085526316\\ \\ x_2=1.085526316-\frac{1.085526316^4-10\left(1.085526316\right)^2+8}{4\left(1.085526316\right)^3-20\left(1.085526316\right)}=0.9411889602}$$

## Q4
$$\displaylines{f(x)=2x^3-x^2+3x-1,x\in\left\lbrack0,1\right\rbrack,x_0=0.5\\ \\ f^{\prime}\left(x\right)=6x^2-2x+3\\ \\ x_1=x_0-\frac{2x^3-x^2+3x-1}{6x^2-2x+3}\\ \\ x_1=0.5-\frac{2\left(0.5\right)^3-0.5^2+3\left(0.5\right)-1}{6\left(0.5\right)^2-2\left(0.5\right)+3}=0.3571428571\\ \\ x_2=0.3571428571-\frac{2\left(0.3571428571\right)^3-0.3571428571^2+3\left(0.3571428571\right)-1}{6\left(0.3571428571\right)^2-2\left(0.3571428571\right)+3}=0.3456760631}$$
![](../assets/Screenshot%202026-08-12%20at%208.25.54%20PM.png)

## Q5
$$\displaylines{f(x)=x\ln x-2,x\in\left\lbrack1,3\right\rbrack,x_0=2\\ \\ f^{\prime}\left(x\right)=1+\ln x\\ \\ x_1=x-\frac{x\ln x-2}{1+\ln x}\\ \\ x_1=2-\frac{2\ln2-2}{1+\ln2}=2.362464437=2.36\\ \\ x_2=2.362464437-\frac{2.362464437\ln2.362464437-2}{1+\ln2.362464437}=2.345782621=2.35\\ \\ x_3=2.345764976=2.35}$$

## Q6
$$\displaylines{f(x)=x-\ln x-2,x\in\left\lbrack0,1\right\rbrack,x_0=0.1\\ \\ f^{\prime}\left(x\right)=1-\frac{1}{x}\\ \\ x_1=x-\frac{x-\ln x-2}{1-\frac{1}{x}}\\ \\ x_1=0.1-\frac{0.1-\ln0.1-2}{1-\frac{1}{0.1}}=0.144731677=0.14\\ \\ x_2=0.144731677-\frac{0.144731677-\ln0.144731677-2}{1-\frac{1}{0.144731677}}=0.1578643559=0.16\\ \\ x_3=0.1578643559-\frac{0.1578643559-\ln0.1578643559-2}{1-\frac{1}{0.1578643559}}=0.1585923416=0.16}$$


# Review
$$x_{n+1}=x_{n}-\frac{f\left(x_{n}\right)}{f^{\prime}\left(x_{n}\right)}$$


## Q1
$$\displaylines{f(x)=x^4-2x-1,x\in\left\lbrack1,2\right\rbrack,x_0=1.5\\ \\ f^{\prime}\left(x\right)=4x^3-2\\ \\ x_1=x-\frac{x^4-2x-1}{4x^3-2}=1.5-\frac{1.5^4-2\left(1.5\right)-1}{4\left(1.5\right)^3-2}=1.407608696\\ \\ x_2=1.407608696-\frac{1.407608696^{4}-2\left(1.407608696\right)-1}{4\left(1.407608696\right)^{3}-2}=1.395531394=1.396}$$

## Q2
$$\displaylines{f(x)=\tan(x^2)-x+1,x\in\left\lbrack1.8,2.2\right\rbrack,x_0=1.8\\ \\ f^{\prime}\left(x\right)=2x\sec^2\left(x^2\right)-1\\ \\ x_1=x-\frac{\tan(x^2)-x+1}{2x\sec^2\left(x^2\right)-1}=1.8-\frac{\tan(1.8^2)-1.8+1}{2\left(1.8\right)\sec^2\left(1.8^2\right)-1}=2.084656554=2.085\\ \\ x_2=2.084656554-\frac{\tan(2.084656554^{2})-2.084656554+1}{2\left(2.084656554\right)\left(\cos2.084656554^{2}\right)^{-2}-1}=2.400515856=2.401}$$

## Q3
$$\displaylines{f(x)=\cos x-x^3,x\in\left\lbrack0,2\right\rbrack,x_0=0.5\\ \\ f^{\prime}\left(x\right)=-\sin x-3x^2\\ \\ x_1=x-\frac{\cos x-x^3}{-\sin x-3x^2}=0.5-\frac{\cos0.5-0.5^3}{-\sin0.5-3\left(0.5\right)^2}=1.112141637\\ \\ x_2=1.112141637-\frac{\cos1.112141637-1.112141637^{3}}{-\sin1.112141637-3\left(1.112141637\right)^{2}}=0.9096726937\\ \\ x_3=0.9096726937-\frac{\cos0.9096726937-0.9096726937^{3}}{-\sin0.9096726937-3\left(0.9096726937\right)^{2}}=0.8672638182=0.87\\ \\ x_4=0.8672638182-\frac{\cos0.8672638182-0.8672638182^{3}}{-\sin0.8672638182-3\left(0.8672638182\right)^{2}}=0.8654771353=0.87}$$

## Q4
$$\displaylines{f(x)=2x^3-e^{x},x\in\left\lbrack1,2\right\rbrack,x_0=1\\ \\ f^{\prime}\left(x\right)=6x^2-e^{x}\\ \\ x_1=x-\frac{2x^3-e^{x}}{6x^2-e^{x}}=1-\frac{2^3-e^1}{6^2-e^1}=0.8413027193\\ \\ x_2=1.426796687\\ \\ x_3=1.222568572\\ \\ x_4=1.176126209\\ \\ x_5=1.173750671=1.174\\ \\ x_6=1.173744579=1.174}$$
