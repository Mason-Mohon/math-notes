# Integration Using Basic Hyperbolic Identities
2026-11-02
Math Academy
Subject: Calculus II
Topics: Hyperbolic Functions Integrals

Osborn's ule:
1. Replace every trigonometric function with its corresponding hyperbolic function
2. For any product of two trigonometric sines, change the sign of the corresponding product of hyperbolic sines.

$$\displaylines{\cos^2x+\sin^2x=1\Rightarrow\cosh^2x-\sinh^2x=1\\ \\ 1+\tan^2x=\sec^2x\Rightarrow1-\tanh^2x=\operatorname{\mathrm{sech}}^2x}$$
## Q1
$$\cos^2x+\sin^2x=1\Rightarrow\cosh^2x-\sinh^2x=1$$

## Q2
$$\displaylines{\cos(x-y)=\cos{x}\cos{y}+\sin{x}\sin{y}\\ \\ \Rightarrow\cosh\left(x-y\right)=\cosh x\cosh y-\sinh x\sinh y}$$

## Q3
$$\int\operatorname{\mathrm{sech}}^2x\left(3-2\sinh x\right)\mathrm{d} x=3\int\operatorname{\mathrm{sech}}^2x\mathrm{d} x-2\int\operatorname{\mathrm{sech}}x\tanh x\mathrm{d} x$$

## Q4
$$\displaylines{{\displaystyle\int_0^{\ln3}\text{csch}{x}\sinh^3{x}\,\textrm{d}x=}\int_0^{\ln3}\sinh^2\left(x\right)\mathrm{d} x\\ \\ =\int_0^{\ln3}\frac{\cosh2x-1}{2}\mathrm{d} x=\left\lbrack\frac{\sinh\left(2x\right)}{4}-\frac{x}{2}\right\rbrack_0^{\ln3}=\frac{\left(\frac{e^{2\ln3}-e^{-2\ln3}}{2}\right)-2\ln3}{4}-0\\ \\ =\frac{\left(\frac{9-\frac19}{2}\right)-2\ln3}{4}=\frac{10}{9}-\frac{\ln3}{2}}$$

## Q5
$$\displaylines{{\displaystyle\int_0^{\ln4}\sech\text{sech}x\cosh^2x\,\textrm{d}x=\int_0^{\ln4}\cosh\left(x\right)\mathrm{d} x=}\sinh\left(\ln4\right)-\sinh\left(0\right)\\ \\ =\frac{e^{\ln4}-e^{-\ln4}}{2}=\frac{4-\frac14}{2}=\frac{15}{4}\cdot\frac12=\frac{15}{8}}$$

## Q6
$$\displaylines{{\displaystyle\int_0^{\ln4}\coth^2{x}\sinh^2{x}\text{sech}{x}\,\textrm{d}x=}\int_0^{\ln4}\frac{\cosh^2x}{\sinh^2x}\cdot\frac{\sinh^2x}{\cosh x}\mathrm{d} x=\int_0^{\ln4}\cosh\left(x\right)\mathrm{d} x\\ \\ =\frac{15}{8}}$$

## Q7
$$\displaylines{{\displaystyle\int_0^{\ln2}\coth{x}\sinh^2{x}\text{csch}{x}\,\textrm{d}x=}\int_0^{\ln2}\frac{\cosh x}{\sinh x}\cdot\sinh^2x\cdot\frac{1}{\sinh x}\mathrm{d} x\\ \\ =\int_0^{\ln2}\cosh\left(x\right)\mathrm{d} x=\frac{2-\frac12}{2}=\frac54}$$

## Q8
$$\displaylines{{\displaystyle\int_0^{\ln2}\dfrac{\tanh{x}}{\cosh^2x}\,\textrm{d}x=}\int_0^{\ln2}\operatorname{\mathrm{sech}}^2\left(x\right)\tanh\left(x\right)\mathrm{d} x\\ \\ u=\tanh x\Rightarrow du=\operatorname{\mathrm{sech}}^2\left(x\right)\mathrm{d} x\\ \\ \frac{e^{\ln2}-e^{-\ln2}}{e^{\ln2}+e^{-\ln2}}=\frac{\frac42-\frac12}{\frac42+\frac12}=\frac32\cdot\frac25=\frac35\\ \\ =\int_0^{\frac35}u\cdot\mathrm{d} u=\left\lbrack\frac12u^2\right\rbrack_0^{\frac35}=\frac{9}{50}}$$


# Review

## Q1
$$$$

## Q2
$$$$

## Q3
$$$$
