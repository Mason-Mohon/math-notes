# Areas Under Curves and the Fundamental Theorem of Calculus
2026-11-21
Math Academy
Subject: Calculus II Multistep
Topics: [The Fundamental Theorem of Calculus](../Calculus%20I/The%20Fundamental%20Theorem%20of%20Calculus.md) Integrals Synthetic Division


$$x(t)=\dfrac{-3t^2+11t+4}{t-1}$$

## **Q1**
$$\displaylines{\int x\left(t\right)\mathrm{d}t\\ \\ \begin{array}{c|rrr} & x^2 & x^1 & x^0\\ 1 & -3 & 11 & 4\\  & \downarrow & -3 & 8\\ \hline & -3 & 8 & 12\end{array}\\ \\ \int-3t+8+\frac{12}{t-1}\mathrm{d} t=-\frac32t^2+8t+12\ln\left|t-1\right|}$$

## Q2
$$\displaylines{-3t^2+11t+4=0\\ \\ t=\frac{-11\pm\sqrt{121+48}}{-6}=\frac{11\pm13}{6}\\ \\ t=-\frac13,4}$$

## Q3
$$\displaylines{A_1=\left\lbrack-\frac32t^2+8t+12\ln\left|t-1\right|\right\rbrack_3^4\\ \\ =8+12\ln3-\left(-\frac{27}{2}+24+12\ln2\right)=-\frac52+12\ln\left(\frac32\right)\\ \\ A_2=\left\lbrack-\frac32t^2+8t+12\ln\left|t-1\right|\right\rbrack_4^5\\ \\ =-\frac{75}{2}+\frac{80}{2}+12\ln4-\left(\frac{16}{2}+12\ln3\right)=-\frac{11}{2}+12\ln\left(\frac43\right)\\ \\ 3+12\ln\left(\frac43\right)+12\ln\left(\frac32\right)=3+12\ln\left(\frac98\right)}$$

## Q4
$${\displaystyle\int_3^5x(t)\,\textrm{d}t=}-\frac52+12\ln\left(\frac32\right)-\frac{11}{2}+12\ln\left(\frac43\right)=-8+12\ln2$$

## Q5
$$\displaylines{{\displaystyle\int_{a}^5\dfrac{x(t)}{4}\,\textrm{d}t=5+3\ln{2}-3\ln{3=5+3\ln\left(\frac23\right)}}\\ \\ {\displaystyle\int_3^{a}x(t)\,\textrm{d}t=}\int_3^5x\left(t\right)\mathrm{d} t+\int_5^{a}x\left(t\right)\mathrm{d} t\\ \\ \\ =-8+12\ln2+\left(-20-12\ln\left(\frac23\right)\right)\\ \\ =-28+12\ln3}$$

## Q6
$$\displaylines{x(t)=\dfrac{-3t^2+11t+4}{t-1}=-3t+8+\frac{12}{t-1}\\ \\ x^{\prime}\left(t\right)=-3-\frac{12}{\left(t-1\right)^2}}$$

## Q7
$$\displaylines{\mathbf{r}=\left\langle x(t),1-\dfrac{t^2}{2}\right\rangle,\quad t\in[0,\infty).\\ \\ \mathbf{r}=\left\langle-3t+8+\frac{12}{t-1},1-\dfrac{t^2}{2}\right\rangle\\ \\ \mathbf{v\left(t\right)}=\left\langle-3-\frac{12}{\left(t-1\right)^2},-t\right\rangle}$$

## Q8
$$\mathbf{v\left(0\right)}=\left\langle-3-\frac{12}{\left(0-1\right)^2},-0\right\rangle=\left\langle-15,0\right\rangle$$

## Q9
$$\displaylines{\mathbf{v\left(t\right)}=\left\langle-3-\frac{12}{\left(t-1\right)^2},-t\right\rangle\\ \\ \mathbf{a\left(t\right)}=\left\langle\frac{24}{\left(t-1\right)^3},-1\right\rangle}$$

## Q10
$$\displaylines{\mathbf{a\left(0\right)}=\left\langle\frac{24}{\left(-1\right)^3},-1\right\rangle=\left\langle-24,-1\right\rangle\\ \\ \left|\mathbf{a}\left(0\right)\right|=\sqrt{\left(-24\right)^2+\left(-1\right)^2}=\sqrt{577}}$$
