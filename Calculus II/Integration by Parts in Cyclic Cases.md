# Integration by Parts in Cyclic Cases
2026-11-25
Math Academy
Subject: Calculus II
Topics: Integrals Integration by Parts


$$\displaylines{I=\int\frac{\ln^2x}{x}\mathrm{d}x\\ u=\ln^2x\Rightarrow\frac{\mathrm{d} u}{\mathrm{d} x}=\frac{2\ln x}{x}\\ \\ \frac{\mathrm{d} v}{\mathrm{d} x}=\frac{1}{x}\Rightarrow v=\ln x\\ \\ uv-\int_{}^{}vu^{\prime}dx=\ln^3x-2\int\frac{\ln^2x}{x}\mathrm{d} x\\ \\ =\ln^3x-2I\\ \\ I=\frac{\ln^3x}{3}+C}$$

## Q1
$$\displaylines{{\displaystyle\int_1^{e^3}\dfrac{\ln^5{x}}{4x}\,\textrm{d}x=}\frac14\int_1^{e^3}\frac{\ln^5x}{x}\mathrm{d} x=I\\ \\ u=\ln^5x\Rightarrow u^{\prime}=\frac{5\ln^4x}{x}\\ \\ v^{\prime}=\frac{1}{x}\Rightarrow v=\ln x\\ \\ I=\frac14\left(\ln^6x-5\int\frac{\ln^5x}{x}\mathrm{d} x\right)=\frac{\ln^6x}{4}-5I\\ \\ =\left\lbrack\frac{\ln^6x}{24}\right\rbrack_1^{e^3}=\left(\frac{3^6}{24}\right)-0=\frac{243}{8}}$$

## Q2
$$\displaylines{{\displaystyle\int_1^{e}\dfrac{\ln^6x}{x}\,\textrm{d}x}=I\\ \\ =\left\lbrack\frac{\ln^7x}{7}\right\rbrack_1^{e}=\frac17}$$


$$\displaylines{I=\int\left(e^{x}\sin x\right)\mathrm{d} x\\ \\ u=\mathrm{e}^{x}\Rightarrow u^{\prime}=e^{x}\\ \\ v^{\prime}=\sin x\Rightarrow v=-\cos x\\ \\ I=-e^{x}\cos x+J\\ \\ J=\int\left(e^{x}\cos x\right)\mathrm{d} x\\ \\ u=e^{x}\Rightarrow u^{\prime}=e^{x}\\ \\ v^{\prime}=\cos x\Rightarrow v=\sin x\\ \\ J=e^{x}\sin x-I\\ \\ I=-e^{x}\cos x+J\\ I=-e^{x}\cos x+e^{x}\sin x-I\\ 2I=-e^{x}\cos x+e^{x}\sin x\\ \\ I=\frac{e^{x}}{2}\left(\sin x-\cos x\right)+C}$$

## Q3
$$\displaylines{{\displaystyle I=\int e^{-2x}\cos(3x)\,\textrm{d}x}\\ \\ u=e^{-2x}\Rightarrow u^{\prime}=-2e^{-2x}\\ v^{\prime}=\cos\left(3x\right)\Rightarrow v=\frac13\sin\left(3x\right)\\ \\ I=\frac{e^{-2x}}{3}\sin\left(3x\right)+\int\frac{2e^{-2x}}{3}\sin\left(3x\right)\mathrm{d} x\\ \\ J=\int\frac{2e^{-2x}}{3}\sin\left(3x\right)\mathrm{d} x\\ \\ u=\frac23e^{-2x}\Rightarrow u^{\prime}=-\frac43e^{-2x}\\ v^{\prime}=\sin\left(3x\right)\Rightarrow v=-\frac13\cos3x\\ \\ J=-\frac29e^{-2x}\cos\left(3x\right)-\frac49\int e^{-2x}\cos\left(3x\right)\mathrm{d} x\\ \\ J=-\frac29e^{-2x}\cos\left(3x\right)-\frac49I\\ \\ I=\frac{e^{-2x}}{3}\sin\left(3x\right)-\frac29e^{-2x}\cos\left(3x\right)-\frac49I\\ \\ I=\frac{9}{13}\left(\frac{e^{-2x}}{3}\sin\left(3x\right)-\frac29e^{-2x}\cos\left(3x\right)\right)\\ \\ =\dfrac{e^{-2x}(3\sin(3x)-2\cos(3x))}{13}+C}$$

## Q4
$$\displaylines{I={\displaystyle\int e^{2x}\cos(3x)\,\textrm{d}x}\\ \\ u=e^{2x}\Rightarrow u^{\prime}=2e^{2x}\\ v^{\prime}=\cos\left(3x\right)\Rightarrow v=\frac13\sin\left(3x\right)\\ \\ I=\frac{e^{2x}}{3}\sin\left(3x\right)-\int\frac23e^{2x}\sin\left(3x\right)\\ \\ J=\int\frac23e^{2x}\sin\left(3x\right)\\ \\ u=\frac23e^{2x}\Rightarrow u^{\prime}=\frac43e^{2x}\\ v^{\prime}=\sin\left(3x\right)\Rightarrow v=-\frac13\cos\left(3x\right)\\ \\ J=-\frac29e^{2x}\cos\left(3x\right)+\frac49I\\ \\ I=\frac{9}{13}\left(\frac{e^{2x}}{3}\sin\left(3x\right)+\frac29e^{2x}\cos\left(3x\right)\right)=\dfrac{e^{2x}(3\sin(3x)+2\cos(3x))}{13}+C}$$

## Q5
$$\displaylines{{\displaystyle I=\int_0^{2\pi}e^{3x}\cos{x}\,\textrm{d}x}\\ \\ u=e^{3x}\Rightarrow u^{\prime}=3e^{3x}\\ v^{\prime}=\cos x\Rightarrow v=\sin x\\ \\ I=e^{3x}\sin x-\int3e^{3x}\sin\left(x\right)\mathrm{d} x\\ \\ J=\int3e^{3x}\sin\left(x\right)\mathrm{d} x\\ \\ u=3e^{3x}\Rightarrow u^{\prime}=9e^{3x}\\ v^{\prime}=^{}\sin x\Rightarrow v=-\cos x\\ \\ J=-3e^{3x}\cos x+9\int e^{3x}\cos\left(x\right)\mathrm{d} x\\ \\ I=\left\lbrack\frac{e^{3x}\left(\sin x+3\cos x\right)}{10}\right\rbrack_0^{2\pi}\\ \\ \left(\frac{e^{6\pi}\left(3\right)}{10}\right)-\left(\frac{3}{10}\right)=\dfrac{3}{10}(e^{6\pi}-1)}$$

## Q6
$$\displaylines{I={\displaystyle\int_0^{\pi}e^{-x}\cos(3x)\,\textrm{d}x}\\ \\ u=e^{-x}\Rightarrow u^{\prime}=-e^{-x}\\ v^{\prime}=\cos\left(3x\right)\Rightarrow v=\frac13\sin\left(3x\right)\\ \\ I=\frac{\mathrm{e}^{-x}}{3}\sin\left(3x\right)+\int\frac{e^{-x}}{3}\sin\left(3x\right)\mathrm{d}x\\ \\ J=\int\frac{e^{-x}}{3}\sin\left(3x\right)\mathrm{d}x\\ \\ u=\frac{e^{-x}}{3}\Rightarrow u^{\prime}=-\frac{e^{-x}}{3}\\ v^{\prime}=\sin\left(3x\right)\Rightarrow v=-\frac13\cos\left(3x\right)\\ \\ J=-\frac{e^{-x}}{9}\cos\left(3x\right)-\frac19I\\ \\ I=\left\lbrack\frac{\mathrm{3e}^{-x}}{10}\sin\left(3x\right)-\frac{e^{-x}}{10}\cos\left(3x\right)\right\rbrack_0^{\pi}\\ \\ =\frac{1+e^{-\pi}}{10}}$$


# Review

## Q1
$$$$

## Q2
$$$$

## Q3
$$$$
