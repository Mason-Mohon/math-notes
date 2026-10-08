# Solving First-Order IVPs Using Separation of Variables
2026-09-28
Math Academy
Subject: Calculus II
Topics: [Solving First-Order ODEs Using Separation of Variables](Solving%20First-Order%20ODEs%20Using%20Separation%20of%20Variables.md) IVPs

$$\displaylines{y^{\prime}=\left(1-2x\right)y^2,y\left(0\right)=1\\ \\ \text{the second is a boundary condition}\\ \\ \frac{1}{y^2}\cdot\frac{\differentialD y}{\differentialD x}=1-2x\\ \\ \int\frac{1}{y^2}\cdot\frac{\differentialD y}{\differentialD x}\differentialD x=\int1-2xdx\\ \\ -\frac{1}{y}=x-x^2+C\\ \\ y=\frac{1}{x^2-x-C},y\left(0\right)=\frac{1}{-C}=1,C=-1}$$

$$\displaylines{\frac{\differentialD y}{\differentialD x}=5y\\ \\ \int\frac{1}{y}\frac{\differentialD y}{\differentialD x}\differentialD x=5\int dx\\ \\ \ln\left|y\right|=5x+C\\ \\ y=\pm e^{5x+C}=Ke^{5x}}$$


## Q1
$$\displaylines{\dfrac{\textrm{d}y}{\textrm{d}x}=y^2+1,y\left(\dfrac{\pi}{2}\right)=1\\ \\ \int\frac{1}{y^2+1}\differentialD y=x\\ \\ \arctan y=x+C\\ \\ y=\tan\left(x+C\right),y\left(\frac{\pi}{2}\right)=\tan\left(\frac{\pi}{2}+C\right)=1,C=-\frac{\pi}{4}\\ \\ y=\tan\left(x-\dfrac{\pi}{4}\right)}$$

## Q2
$$\displaylines{\dfrac{\textrm{d}y}{\textrm{d}x}=\dfrac{3x^2}{y},y\left(1\right)=2\\ \\ \frac12y^2=x^3+C\\ \\ y=\sqrt{2x^3+C}\\ \\ 2=\sqrt{2+C},C=2\\ \\ y=\sqrt{2x^3+2}}$$

## Q3
$$\displaylines{\dfrac{\textrm{d}y}{\textrm{d}x}=\dfrac{y^2}{2x^2}-3xy^2\\ \\ -\frac{1}{y}=-\frac{1}{2x}-\frac{3x^3}{2x}\\ \\ y=\dfrac{2x}{3x^3+1}}$$

## Q4
$$\displaylines{e^{x}\dfrac{\textrm{d}y}{\textrm{d}x}-6xe^{x}=2,y\left(0\right)=5\\ \\ y=\int6x+2e^{-x}\differentialD x\\ \\ y=3x^2+2e^{-x}+C\\ \\ C=7\\ \\ y=3x^2-2e^{-x}+7}$$

## Q5
$$\displaylines{\dfrac{\textrm{d}y}{\textrm{d}x}=e^{4x-y},y\left(0\right)=5\\ \\ e^{y}=\frac14e^{4x}+C\\ \\ y=\ln\left(\dfrac{e^{4x}}{4}+C\right)\\ \\ 5=\ln\left(\frac14+C\right)\\ \\ e^5-\frac14=C\\ \\ y=\ln\left(\dfrac{e^{4x}+4e^5-1}{4}\right)}$$

## Q6
$$\displaylines{\left(\dfrac{1}{xy}-\dfrac{1}{x}\right)\dfrac{\textrm{d}y}{\textrm{d}x}=2,y\left(1\right)=1\\ \\ \int\frac{1}{y}-1\differentialD y=x^2+C\\ \\ \ln\left|y\right|-y=x^2+C\\ \\ -1=1+C,C=-2\\ \\ }$$


# Review

## Q1
$$\displaylines{\dfrac{\textrm{d}y}{\textrm{d}x}=\dfrac{y^2}{x^2+1},y\left(1\right)=1\\ \\ -\frac{1}{y^{}}=\arctan x+C\\ \\ y=-\frac{1}{\arctan x}+C,C=-1-\frac{\pi}{4}\\ \\ y=\dfrac{4}{{\pi}+4-4\arctan(x)}}$$

## Q2
$$\displaylines{3y^2\dfrac{\textrm{d}y}{\textrm{d}x}=4x+2xy^3=2x\left(2+y^3\right)\\ \\ \int\frac{3y^2}{2+y^3}\differentialD y=\int2xdx\\ \\ =3\int\frac{1}{u}du=x^2+C\\ \\ \ln\left|2+y^3\right|=x^2+C\\ \\ y=\sqrt[3]{Ke^{x^2}-2},y\left(0\right)=1\\ \\ 1=K-2,K=3}$$

## Q3
$$\displaylines{\dfrac{\textrm{d}y}{\textrm{d}x}=3y^2x^2-4y^2x^3\\ \\ \int\frac{1}{y^2}\differentialD y=\int3x^2-4x^3dx\\ \\ -\frac{1}{y}=x^3-x^4+C\\ \\ y=-\frac{1}{x^3-x^4+C}\\ \\ \frac18=-\frac{1}{8-16+C}=\frac{1}{8+C},C=0}$$
