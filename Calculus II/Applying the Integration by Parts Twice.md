# Applying the Integration by Parts Twice
2026-09-24
Math Academy
Subject: Calculus II
Topics: Integrals Integration by Parts

![](../assets/Pasted%20image%2020260924102747.png)
![](../assets/Pasted%20image%2020260924102800.png)

$$\int_{}^{}uv^{\prime}dx=uv-\int_{}^{}vu^{\prime}dx$$

## Q1
$$\displaylines{{\displaystyle\int(3x^2+5)e^{x}\,\textrm{d}x}=\left(3x^2+5\right)e^{x}-\displaystyle\int\left(6x\right)e^{x}dx\\ }$$

## Q2
$$\displaylines{{\displaystyle\int(x^2-4)e^{x}\,\textrm{d}x=\left(x^2-4\right)e^{x}-2\int xe^{x}}dx\\ \\ =\left(x^2-4\right)e^{x}-2xe^{x}+\int e^{x}dx\\ \\ =e^{x}(x^2-2x-2)+C}$$

## Q3
$$\displaylines{{\displaystyle\int_0^{\pi}4x^2\sin\left(2x\right)dx=\left\lbrack-2x^2\cos\left(2x\right)\right\rbrack}_0^{\pi}+4\int_0^{\pi}x\cos\left(2x\right)\differentialD x\\ \\ =\left\lbrack-2x^2\cos\left(2x\right)+4x\sin\left(2x\right)\right\rbrack_0^{\pi}-4\int_0^{\pi}\sin\left(2x\right)\differentialD x\\ \\ =\left\lbrack-2x^2\cos\left(2x\right)+2x\sin\left(2x\right)+2\cos\left(2x\right)\right\rbrack_0^{\pi}\\ \\ =\left(-2\pi^2\cos\left(2\pi\right)+2\pi\sin\left(2\pi\right)+2\cos\left(2\pi\right)\right)-\left(2\cos\left(0\right)\right)\\ \\ =-2\pi^2+2-2=-2\pi^2}$$

## Q4
$$\displaylines{{\displaystyle{\int(7x^2+3)\sin x\,\textrm{d}x}}=-\left(7x^2+3\right)\cos x+14\int x\cos\left(x\right)\differentialD x\\ \\ =-\left(7x^2+3\right)\cos x+14x\sin x-14\int\sin xdx\\ \\ =-\left(7x^2+3\right)\cos x+14x\sin x+14\cos x\\ \\ =(11-7x^2)\cos{x}+14x\sin x+C}$$

## Logarithms

$$\displaylines{\int_1^{e}32x^3\left(\ln x\right)^2\differentialD x\\ \\ u=\left(\ln x\right)^2\Rightarrow\frac{du}{\differentialD x}=\frac{2\ln x}{x}\\ \\ \frac{dv}{\differentialD x}=32x^3\Rightarrow v=\int32x^3dx=8x^4\\ \\ uv-\int vu^{\prime}dx=\left(\ln x\right)^2\left(8x^4\right)-\int\left(8x^4\right)\left(\frac{2\ln x}{x}\right)\differentialD x=8x^4\left(\ln x\right)^2-16\int x^3\ln\left(x\right)\differentialD x\\ \\ u=\ln x\Rightarrow\frac{du}{\differentialD x}=\frac{1}{x}\\ \\ \frac{dv}{\differentialD x}=x^3\Rightarrow v=\int x^3dx=\frac{x^4}{4}\\ \\ =8x^4\left(\ln x\right)^2-16\left(\frac{x^4\ln x}{4}-\frac{x^4}{16}+C_1\right)\\ \\ =\left\lbrack x^4\left(8\left(\ln x\right)^2-4\ln x+1\right)\right\rbrack_1^{e}=5e^4-1}$$

## Q5
$$\displaylines{\int_1^{e}\left(\ln x\right)^2\cdot1\cdot\differentialD x\\ \\ u=\left(\ln x\right)^2\Rightarrow\frac{du}{\differentialD x}=\frac{2\ln x}{x}\\ \\ \frac{dv}{\differentialD x}=1\Rightarrow\int dx=x\\ \\ =x\left(\ln x\right)^2-\int x\cdot\frac{2\ln x}{x}\differentialD x=x\left(\ln x\right)^2-2\int\ln x\cdot1\cdot\differentialD x\\ \\ u=\ln x\Rightarrow\frac{du}{\differentialD x}=\frac{1}{x}\\ \\ \frac{dv}{\differentialD x}=1\Rightarrow v=\int dx=x\\ \\ =x\left(\ln x\right)^2-2x\ln x+2\int1\differentialD x\\ \\ =\left\lbrack x\left(\left(\ln x\right)^2-2\ln x+2\right)\right\rbrack_1^{e}\\ \\ =e\left(\left(\ln e\right)^2-2\ln e+2\right)-2=e-2}$$

## Q6
$$\displaylines{\int_1^{e}\ln^2\left(x^3\right)\cdot1\cdot\differentialD x\\ \\ u=\ln^2\left(x^3\right)\Rightarrow u^{\prime}=2\cdot\ln\left(x^3\right)\cdot\frac{1}{x^3}\cdot3x^2=\frac{6\ln\left(x^3\right)}{x}\\ \\ v^{\prime}=1\Rightarrow v=\int dx=x\\ \\ =x\ln^2\left(x^3\right)-6\int\ln\left(x^3\right)\cdot1\cdot\differentialD x\\ \\ u=\ln\left(x^3\right)\Rightarrow u^{\prime}=3x^2\cdot\frac{1}{x^3}=\frac{3}{x}\\ \\ v^{\prime}=1\Rightarrow v=x\\ \\ =x\ln^2\left(x^3\right)-6x\ln\left(x^3\right)+18\int dx\\ \\ =\left\lbrack x\left(\ln^2\left(x^3\right)-6\ln\left(x^3\right)+18\right)\right\rbrack_1^{e}\\ \\ =\left\lbrack e\left(\ln^2\left(e^3\right)-6\ln\left(e^3\right)+18\right)\right\rbrack-\left\lbrack\left(\ln^2\left(1^3\right)-6\ln\left(1^3\right)+18\right)\right\rbrack\\ \\ =e\left(9-18+18\right)-\left(0-0+18\right)=9e-18}$$


# Review

## Q1
$$$$

## Q2
$$$$

## Q3
$$$$
