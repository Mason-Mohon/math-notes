# Integrating Functions Using Polynomial Division
2026-11-20
Math Academy
Subject: Calculus II
Topics: Integrals Polynomial Division Synthetic Division


$$\displaylines{\int\frac{3x+2}{x+2}\mathrm{d} x\\ \\ \begin{pmatrix} & x^1 & x^0\\ -2 & 3 & 2\\  & \downarrow & -6\\  & 3 & -4\end{pmatrix}\\ \\ 3-\frac{4}{x+2}\Rightarrow\int3\mathrm{d} x-4\int\left(\frac{1}{x+2}\right)\mathrm{d} x=3x-4\ln\left|x+2\right|+C}$$

## Q1
$$\displaylines{{\displaystyle\int\dfrac{5x+7}{x+2}\,\textrm{d}x}\\ \\ \begin{pmatrix} & x^1 & x^0\\ -2 & 5 & 7\\  & \downarrow & -10\\  & 5 & -3\end{pmatrix}\to5-\frac{3}{x+2}\\ \\ =5x-3\ln\left|x+2\right|+C}$$

## Q2
$$\displaylines{{\displaystyle\int_1^5\dfrac{15x+4}{x+6}\,\textrm{d}x}\\ \\ \begin{array}{c|rrr} & x^1 & x^0\\ {\textcolor{red}{-6}} & 15 & 4\\  & \downarrow & -90\\  & 15 & -86\end{array}\\ \\ =\int_1^515-\frac{86}{x+6}\mathrm{d} x=\left\lbrack15x-86\ln\left|x+6\right|\right\rbrack_1^5\\ \\ =60-86\ln\left(\frac{11}{7}\right)}$$

## Q3
$$\displaylines{{\displaystyle\int_0^3\dfrac{x^2+4x+1}{x+2}\,\textrm{d}x}\\ \\ \begin{array}{c|rrr} & x^2 & x^1 & x^0\\ -2 & 1 & 4 & 1\\  & \downarrow & -2 & -4\\ \hline & 1 & 2 & -3\end{array}\\ \\ \int_0^3\left(x^{}+2-\frac{3}{x+2}\right)\mathrm{d} x\Rightarrow\left\lbrack\frac12x^2+2x-3\ln\left(x+2\right)\right\rbrack_0^3\\ \\ =\frac92+\frac{12}{2}-3\ln5-\left(-3\ln2\right)=\frac{21}{2}-3\ln\left(\frac52\right)}$$

## Q4
$$\displaylines{{\displaystyle\int_1^4\dfrac{x^2+5x+3}{x+1}\,\textrm{d}x}\\ \\ \begin{array}{c|rrr} & x^2 & x^1 & x^0\\ -1 & 1 & 5 & 3\\  & \downarrow & -1 & -4\\ \hline & 1 & 4 & -1\end{array}\\ \\ \int_1^4x+4-\frac{1}{x+1}\mathrm{d} x=\left\lbrack\frac12x^2+4x-\ln\left(x+1\right)\right\rbrack_1^4\\ \\ =24-\ln5-\frac12-4+\ln2\\ \\ \frac{39}{2}-\ln\left(\frac52\right)}$$

## Q5
$$\displaylines{{\displaystyle\int_0^1\dfrac{5x-3}{2x+1}\,\textrm{d}x=}\frac12\int_0^1\frac{5x-3}{x+\frac12}\mathrm{d} x\\ \\ \begin{array}{c|rr} & x^1 & x^0\\ -\frac12 & 5 & -3\\  & \downarrow & -\frac52\\ \hline & 5 & -\frac{11}{2}\end{array}\\ \\ =\frac12\int_0^15-\frac{11}{2}\left(\frac{1}{x+\frac12}\right)\mathrm{d} x=\left\lbrack\frac{5x}{2}-\frac{11}{4}\ln\left(x+\frac12\right)\right\rbrack_0^1\\ \\ =\frac52-\frac{11}{4}\ln\left(\frac32\right)+\frac{11}{4}\ln\left(\frac12\right)=\frac52-\frac{11}{4}\ln\left(3\right)}$$

## Q6
$$\displaylines{{\displaystyle\int_0^2\dfrac{4x-5}{3x+1}\,\textrm{d}x=}\frac13\int_0^2\frac{4x-5}{x+\frac13}\mathrm{d}x\\ \\ \begin{array}{c|rr}-\frac13 & x^1 & x^0\\ {} & 4{} & -5{}\\  & \downarrow & -\frac43{}\\ \hline & {}4 & {}-\frac{19}{3}\end{array}\\ \\ \int_0^24-\frac{19}{3}\left(\frac{1}{x+\frac13}\right)\mathrm{d} x=\left\lbrack\frac43x-\frac{19}{9}\ln\left(x+\frac13\right)\right\rbrack_0^2\\ \\ \frac83-\frac{19}{9}\ln7}$$


# Review

## Q1
$$$$

## Q2
$$$$

## Q3
$$$$
