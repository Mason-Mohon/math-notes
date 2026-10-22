# The Arc Length of a Parametric Curve
2026-10-14
Math Academy
Subject: Calculus II
Topics: Parametric Equations Arc Length Integrals

$$\displaylines{x=x\left(t\right),y=y\left(t\right),t\in\left\lbrack t_1,t_2\right\rbrack\\ \\ L=\int_{t_1}^{t_2}\sqrt{\left(\frac{\differentialD x}{\differentialD t}\right)^2+\left(\frac{\differentialD y}{\differentialD t}\right)^2}\differentialD t}$$

## Q1
$$\displaylines{x=t^2+1,\,y=t^3+2t,t\in\left\lbrack-1,1\right\rbrack\\ \\ L=\int_{-1}^1\sqrt{\left(2t\right)^2+\left(3t^2+2\right)^2}\differentialD t=\int_{-1}^1\sqrt{9t^4+16t^2+4}\differentialD t}$$

## Q2
$$\displaylines{x=t^2+2t+1,\,y=\dfrac23t^3-2t,t\in\left\lbrack-3,2\right\rbrack\\ \\ L=\int_{-3}^2\sqrt{\left(2t+2\right)^2+\left(2t^2-2\right)^2}\differentialD t=\int_{-3}^2\sqrt{\left(4t^2+8t+4\right)+\left(4t^4-8t^2+4\right)}\differentialD t\\ \\ =\int_{-3}^2\sqrt4\cdot\sqrt{t^4-t^2+2t+2}\differentialD t={\displaystyle2\int_{-3}^2\sqrt{t^4-t^2+2t+2}\:\textrm{d}t}}$$

## Q3
$$\displaylines{x=\cos(5t),\,y=6\sin(t)\\ \\ {\displaystyle\int_0^{\pi/2}\sqrt{25\sin^2(5t)+36\cos^2(t)}\:\textrm{d}t}}$$

## Q4
$$\displaylines{x=e^{t},\,y=e^{t}\sin{t,y^{\prime}=e^{t}}\sin t+e^{t}\cos t\\ \\ L=\int_{-3}^1\sqrt{e^{2t}+\left(e^{t}\sin t+e^{t}\cos t\right)^2}=\int_{-3}^1\sqrt{e^{2t}+e^{2t}\sin^2t+e^{2t}\sin t\cos t+e^2\cos^2t}\\ \\ =\int_{-3}^1e^{t}\sqrt{2+\sin2t}}$$

## Q6
$$\displaylines{x=3\cos{t},\,y=8t+\cos{t}\\ \\ L=\int_{-1}^1\sqrt{\left(-3\sin t\right)^2+\left(8-\sin t\right)^2}\differentialD t=\int_{-1}^1\sqrt{9\sin^2t+\left(64-16\sin t+\sin^2t\right)}\differentialD t\\ \\ =\int_{-1}^1\sqrt{10\sin^2t-16\sin t+64}}$$

## Q7
$$\displaylines{x=1-\cos{t},\quad y=t-\sin{t},\quad t\in\left[0,\frac{\pi}{2}\right].\\ \\ L=\int_0^{\frac{\pi}{2}}\sqrt{\sin^2t^{}+\left(1-2\cos t+\cos^2t\right)}\differentialD t=\sqrt2\int_0^{\frac{\pi}{2}}\sqrt{1-\cos t}\differentialD t=\sqrt2\int_0^{\frac{\pi}{2}}\sqrt{2\sin^2\left(\frac{t}{2}\right)}\differentialD t\\ \\ =2\int_0^{\frac{\pi}{2}}\sin\left(\frac{t}{2}\right)\differentialD t,u=\frac{t}{2},\differentialD t=2du\\ \\ L=4\left\lbrack-\cos u\right\rbrack_0^{\frac{\pi}{4}}=-4\cos\left(\frac{\pi}{4}\right)+4\cos0=4-2\sqrt2}$$

## Q8
$$\displaylines{x=3\cos{t}-\cos(3t),\quad y=3\sin{t}-\sin(3t),\quad t\in\left[0,\pi\right]\\ \\ L=\int_0^{\pi}\sqrt{\left(3\sin\left(3t\right)-\sin t\right)^2+\left(3\cos t-3\cos\left(3t\right)\right)^2}\differentialD t=6\int_0^{\pi}\sin tdt\\ \\ =6\sin\pi-0=6}$$


# Review

$$\displaylines{x=x\left(t\right),y=y\left(t\right),t\in\left\lbrack t_1,t_2\right\rbrack\\ \\ L=\int_{t_1}^{t_2}\sqrt{\left(\frac{\differentialD x}{\differentialD t}\right)^2+\left(\frac{\differentialD y}{\differentialD t}\right)^2}\differentialD t}$$
## Q1
$$\displaylines{x=1+3t,\quad y=2t^{3/2},\quad t\in[0,1].\\ \\ L=\int_0^1\sqrt{9+9t}\differentialD t=3\int_0^1\sqrt{1+t}\differentialD t\\ \\ u=1+t\\ \\ 3\int_1^2\sqrt{u}\differentialD t=3\left\lbrack\frac23\sqrt{u^3}\right\rbrack_1^2=4\sqrt2-2}$$

## Q2
$$\displaylines{x=\cos(3t),\,y=3\sin(t)\\ \\ L=3\int_0^{\frac{\pi}{2}}\sqrt{\sin^2\left(3t\right)+\cos^2\left(t\right)}\mathrm{d}t}$$

## Q3
$$\displaylines{x=4\sin{t}+5,\quad y=4(\cos{t}+1),\quad t\in\left[0,\dfrac{\pi}{2}\right].\\ \\ L=\int_0^{\frac{\pi}{2}}\sqrt{\left(4\cos t\right)^2+\left(-4\sin t\right)^2}\mathrm{d}t=4\int_0^{\frac{\pi}{2}}dt=2\pi}$$
