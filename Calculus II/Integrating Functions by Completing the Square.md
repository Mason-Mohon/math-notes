# Integrating Functions by Completing the Square
2026-09-15
Math Academy
Subject: Calculus II
Topics: Integrals [Integration Using Inverse Trigonometric Functions](../Calculus%20I/Integration%20Using%20Inverse%20Trigonometric%20Functions.md)
![](../assets/Pasted%20image%2020260915095905.png)
## Q1
$$\displaylines{{\displaystyle\int\dfrac{1}{\sqrt{9-\left(6x-2\right)^2}}\,\textrm{d}x=}\frac13\frac{1}{\sqrt{1-\left(\frac{6x-2}{3}\right)^2}}\differentialD x\\ }$$

## Q2
$${\displaystyle\int\dfrac{1}{(x+1)^2+4}\,\textrm{d}x=}\frac14\frac{1}{1+\left(\frac{x+1}{2}\right)^2}\differentialD x$$

## Q3
$$\displaylines{{\displaystyle{\int_1^3\dfrac{6}{x^2-4x+5}\,\textrm{d}x}=}{\displaystyle{\int_1^3\dfrac{6}{x^2-4x+4-4+5}\,\textrm{d}x}=}{\displaystyle{6\int_1^3\dfrac{1}{\left(x-2\right)^2+1}\,\textrm{d}x}}\\ \\ u=x-2\\ \\ 6\int_{-1}^1\frac{1}{1+u^2}du=6\left\lbrack\arctan\left(u\right)\right\rbrack_{-1}^1=6\left(\frac{\pi}{4}-\left(-\frac{\pi}{4}\right)\right)=3\pi}$$

## Q4
$$\displaylines{{\displaystyle\int\dfrac{1}{x^2-8x+20}\textrm{d}x=}{\displaystyle\int\dfrac{1}{x^2-8x+16-16+20}\textrm{d}x=}{\displaystyle\int\dfrac{1}{\left(x-4\right)^2+4}\textrm{d}x}\\ \\ \frac14{\displaystyle\int\dfrac{1}{\left(\frac{x}{2}-2\right)^2+1}\textrm{d}x}\\ \\ u=\left(\frac{x}{2}-2\right),\frac{du}{\differentialD x}=\frac12,\differentialD x=2du\\ \\ {\displaystyle\frac12\int\dfrac{1}{u^2+1}\textrm{du}}=\dfrac12\arctan\left(\dfrac{x-4}{2}\right)+C}$$

## Q5
$$\displaylines{{\displaystyle{\int_{1-\sqrt3}^{1+\sqrt3}\dfrac{3}{\sqrt{-x^2+2x+3}}\,\textrm{d}x}=3}\int_{1-\sqrt3}^{1+\sqrt3}\dfrac{1}{\sqrt{-\left(x^2-2x+1-1-3\right)}}\,\textrm{d}x\\ \\ \frac32\int_{1-\sqrt3}^{1+\sqrt3}\dfrac{1}{\sqrt{1-\left(\frac{x-1}{2}\right)^2}}\,\textrm{d}x\\ \\ u=\left(\frac{x-1}{2}\right),\frac{du}{\differentialD x}=\frac12,\differentialD x=2du\\ \\ 3\int_{-\frac{\sqrt3}{2}}^{\frac{\sqrt3}{2}}\dfrac{1}{\sqrt{1-u^2}}\,\textrm{du}\\ \\ =3\left\lbrack\arcsin u\right\rbrack_{-\frac{\sqrt3}{2}}^{\frac{\sqrt3}{2}}=3\cdot\left(\frac{\pi}{3}+\frac{\pi}{3}\right)=2\pi}$$

## Q6
$$\displaylines{{\displaystyle{\int_{7/2}^{4+\sqrt3/2}\dfrac{1}{\sqrt{-x^2+8x-15}}\,\textrm{d}x}=}{\displaystyle{\int_{7/2}^{4+\sqrt3/2}\dfrac{1}{\sqrt{-\left(x^2-8x+16-16+15\right)}}\,\textrm{d}x}=}\\ \\ {\displaystyle{\int_{7/2}^{4+\sqrt3/2}\dfrac{1}{\sqrt{1-\left(x-4\right)^2}}\,\textrm{d}x},u=x-4}\\ \\ \int_{-1/2}^{\sqrt3/2}\dfrac{1}{\sqrt{1-u^2}}\,\textrm{du}=\left\lbrack\arcsin\left(u\right)\right\rbrack_{-\frac12}^{\frac{\sqrt3}{2}}=\frac{2\pi}{6}+\frac{\pi}{6}=\frac{\pi}{2}}$$

## Q7
$$\displaylines{{\displaystyle{\int_{-2+2/\sqrt3}^0\dfrac{3}{|x+2|\sqrt{x^2+4x+3}}\,\textrm{d}x}=}{\displaystyle{\int_{-2+2/\sqrt3}^0\dfrac{3}{|x+2|\sqrt{x^2+4x+4-4+3}}\,\textrm{d}x}=}\\ \\ {\displaystyle{3\int_{-2+2/\sqrt3}^0\dfrac{1}{|x+2|\sqrt{\left(x+2\right)^2-1}}\,\textrm{d}x}}\\ \\ u=x+2\\ \\ {\displaystyle{3\int_{2/\sqrt3}^2\dfrac{1}{|u|\sqrt{u^2-1}}\,\textrm{d}u=3\left(\operatorname{\mathrm{arcsec}}\left(2\right)-\operatorname{\mathrm{arcsec}}\left(\frac{2}{\sqrt3}\right)\right)}=3\cdot\frac{\pi}{6}=\frac{\pi}{2}}}$$

## Q8
$$\displaylines{{\displaystyle{\int_{-1+2/\sqrt3}^1\dfrac{5}{|x+1|\sqrt{x^2+2x}}\,\textrm{d}x}=}{\displaystyle{5\int_{2/\sqrt3}^2\dfrac{1}{|u|\sqrt{u-1}}\,\textrm{d}x}=}\\ \\ 5\left(\operatorname{\mathrm{arcsec}}\left(2\right)-\operatorname{\mathrm{arcsec}}\left(\frac{2}{\sqrt3}\right)\right)=5\cdot\frac{\pi}{6}=\frac{5\pi}{6}}$$



# Review

## Q2
$$\displaylines{{\displaystyle{\int_{-7/2}^{-5/2}\dfrac{1}{\sqrt{-x^2-6x-8}}\,\textrm{d}x}}={\displaystyle{\int_{-7/2}^{-5/2}\dfrac{1}{\sqrt{-\left(x^2+6x+9-9+8\right)}}\,\textrm{d}x}}\\ \\ =\int_{-\frac72}^{-\frac52}\frac{1}{\sqrt{-\left(x+3\right)^2+1}},u=\left(x+3\right)\\ \\ =\int_{-\frac12}^{\frac12}\frac{1}{\sqrt{1-u^2}}du=\arcsin\left(\frac12\right)-\arcsin\left(-\frac12\right)=\frac{\pi}{6}+\frac{\pi}{6}=\frac{\pi}{3}}$$

## Q3
$$\displaylines{{\displaystyle{\int_1^3\dfrac{8}{x^2-2x+5}\,\textrm{d}x},u=\left(x-1\right)}\\ \\ 8\int_0^2\frac{1}{u^2+4}du=\int\frac{1}{u^2+a^2}du=\frac{1}{a}\arctan\left(\frac{u}{a}\right)\\ \\ 8\left\lbrack\frac12\arctan\left(\frac{u}{2}\right)\right\rbrack_0^2=4\left(\arctan\left(1\right)-\arctan\left(0\right)\right)=\pi}$$

# Review

## Q1
$$\displaylines{{\displaystyle\int\dfrac{1}{\sqrt{21-4x-x^2}}\textrm{d}x=}\int\frac{1}{\sqrt{-\left(x^2+4x+4-4-21\right)}}\differentialD x=\int\frac{1}{\sqrt{25-\left(x+2\right)^2}}\differentialD x\\ \\ u=\left(\frac{x+2}{5}\right),\frac{du}{\differentialD x}=\frac15,\differentialD x=5du\\ \\ =\int\frac{1}{\sqrt{1-u^2}}du=\arcsin\left(\dfrac{x+2}{5}\right)+C}$$

## Q2
$$\displaylines{{\displaystyle\int\dfrac{1}{2x^2+12x+26}\,\textrm{d}x=}\frac12\int\frac{1}{x^2+6x+9-9+13}\differentialD x=\frac18\int\frac{1}{\left(\frac{x+3}{2}\right)^2+1}\differentialD x\\ \\ u=\left(\frac{x+3}{2}\right),\differentialD x=2du\\ \\ \frac14\int\frac{1}{u^2+1}du=\dfrac14\arctan\left(\dfrac{x+3}{2}\right)+C}$$

## Q3
$${\displaystyle{\int\dfrac{10}{|x-6|\sqrt{x^2-12x+35}}\,\textrm{d}x}=}10\int\frac{1}{\left|x-6\right|\sqrt{\left(x-6\right)^2-1}}\differentialD x=10\,\textrm{arcsec}{(x-6)}+C$$


# Review

## Q1
$$\displaylines{{\displaystyle{\int_4^5\dfrac{2}{x^2-8x+17}\,\textrm{d}x}}=2\int_4^5\dfrac{1}{1+\left(x-4\right)^2}\,\textrm{d}x=\left\lbrack2\arctan\left(x-4\right)\right\rbrack_4^5\\ \\ 2\arctan\left(1\right)-2\arctan\left(0\right)=\frac{\pi}{2}}$$

## Q2
$${\displaystyle\int\dfrac{1}{|x+3|\sqrt{x^2+6x+8}}\,\textrm{d}x=}\textrm{arcsec}(x+3)+C$$

## Q3
$$\displaylines{{\displaystyle{\int_{-3-\sqrt2}^{-3+\sqrt2}\dfrac{20}{\sqrt{-1-x(x+6)}}\,\textrm{d}x}=20{\displaystyle{\int_{-3-\sqrt2}^{-3+\sqrt2}\dfrac{1}{\sqrt{-1-\left(x^2+6x+9-9\right)}}\,\textrm{d}x}}}=\\ \\ \frac{10}{\sqrt2}{\displaystyle{\int_{-3-\sqrt2}^{-3+\sqrt2}\dfrac{1}{\sqrt{1-\left(\frac{x+3}{2\sqrt2}\right)^2}}\,\textrm{d}x}}\\ \\ u=\frac{x+3}{2\sqrt2}\Rightarrow\frac{du}{\differentialD x}=\frac{1}{2\sqrt2}\\ \\ 20\int_{-\frac12}^{\frac12}\frac{1}{\sqrt{1-u^2}}du=20\arcsin\left(\frac12\right)-20\arcsin\left(-\frac12\right)=\frac{20\pi}{3}}$$
