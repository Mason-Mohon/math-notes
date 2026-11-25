# Further Integration of Algebraic Functions Using Substitution
2026-11-18
Math Academy
Subject: Calculus II
Topics: Integrals


$$\displaylines{\int x\sqrt{x+2}\mathrm{d} x\\ \\ u=x+2\Rightarrow\mathrm{d} u=\mathrm{d} x\Rightarrow x=u-2\\ \\ \int\left(u-2\right)\sqrt{u}\mathrm{d} u=\int\left(u^{\frac32}-2u^{\frac12}\right)\mathrm{d} u\\ \\ =\frac25\sqrt{\left(x+2\right)^5}-\frac43\sqrt{\left(x+2\right)^3}+C}$$

## Q1
$$\displaylines{{\displaystyle\int x^2\sqrt{1-x}\,\textrm{d}x}\\ \\ u=1-x\Rightarrow\mathrm{d} u=-\mathrm{d} x\Rightarrow x=1-u\\ \\ \int\left(1-u\right)^2\sqrt{u}\mathrm{d} u=-\int\left(u^{\frac12}-2u^{\frac32}+u^{\frac52}\right)\mathrm{d} u\\ \\ =-\frac23\left(1-x\right)^{\frac32}+\frac45\left(1-x\right)^{\frac52}-\frac27\left(1-x\right)^{\frac72}+C}$$

## Q2
$$\displaylines{{\displaystyle\int x\sqrt[3]{2x+1}\,\textrm{d}x}\\ \\ u=2x+1\Rightarrow\frac{\mathrm{d} u}{\mathrm{d} x}=2,\mathrm{d} x=\frac12\mathrm{d} u\Rightarrow x=\frac{u-1}{2}\\ \\ {\displaystyle\dfrac14\int\left(u^{4/3}-u^{1/3}\right)\textrm{d}u}}$$

## Q3
$$\displaylines{{\displaystyle\int_0^2x^7\sqrt{5+x^2}\,\textrm{d}x}\\ \\ u=5+x^2\Rightarrow\frac{\mathrm{d} u}{\mathrm{d} x}=2x,x\mathrm{d} x=\frac12\mathrm{d} u\Rightarrow x=\sqrt{u-5}\\ \\ \frac12\int_5^9\left(\sqrt{u-5}\right)^6\sqrt{u}\mathrm{d} u\\ \\ ={\displaystyle\dfrac12\int_5^9(u-5)^3\sqrt{u}\,\textrm{d}u}}$$

## Q4
$$\displaylines{{\displaystyle{\int_0^{\sqrt8}3x\sqrt{x^2+1}\,\textrm{d}x},u=x^2+1\Rightarrow x=\sqrt{u-1}}\\ \\ \frac{\mathrm{d} u}{\mathrm{d} x}=2x\Rightarrow x\mathrm{d} x=\frac12\mathrm{d} u\\ \\ \frac32\int_1^9\sqrt{u}\mathrm{d} u=\frac32\cdot\left\lbrack\frac23u^{\frac32}\right\rbrack_1^9=26}$$


# Review

## Q1
$$\displaylines{\int\dfrac{z+5}{\sqrt{z+4}}\mathrm{d} z,u=z+4\Rightarrow z=u-4\\ \\ \int\frac{u+1}{\sqrt{u}}\mathrm{d} u=2\sqrt{u}\left(u+1\right)-2\int\sqrt{u}\mathrm{d} u\\ \\ =2\sqrt{u}\left(u+1\right)-\frac43u^{\frac32}\\ \\ f\left(u\right)=u+1\Rightarrow f^{\prime}\left(u\right)=1\\ \\ v=2\sqrt{u}\Rightarrow v^{\prime}=u^{-\frac12}\\ \\ =\frac63u^{\frac32}-\frac43u^{\frac32}+2\sqrt{u}\\ \\ =\dfrac{2\sqrt{(z+4)^3}}{3}+2\sqrt{z+4}+C}$$

## Q2
$$\displaylines{{\displaystyle{\int_{-2}^0x\left(x+2\right)^3\,\textrm{d}x,u=x+2,x=u-2}}\\ \\ \int_0^2\left(u^4-2u^3\right)\mathrm{d} u=\left\lbrack\frac15u^5-\frac12u^4\right\rbrack_0^2\\ \\ \frac{32}{5}-\frac{40}{5}=-\frac85}$$

## Q3
$$\displaylines{{\displaystyle\int x\sqrt[5]{x-1}\,\textrm{d}x,u=x-1,x=u+1}\\ \\ \int u^{\frac15}\left(u+1\right)\mathrm{d} u\\ \\ {\displaystyle\int\left(u^{6/5}+u^{1/5}\right)\textrm{d}u}}$$

# Review

## Q1
$$\displaylines{{\displaystyle\int(x^2+1)\sqrt{x-2}\,\textrm{d}x}\\ \\ u=x-2\Rightarrow x=u+2\\ \\ \int\left(u^2+4u+5\right)\left(u^{\frac12}\right)\mathrm{d} u=\int\left(u^{\frac52}+4u^{\frac32}+5u^{\frac12}\right)\mathrm{d} u\\ \\ =\frac27\left(x-2\right)^{\frac72}+\frac85\left(x-2\right)^{\frac52}+\frac{10}{3}\left(x-2\right)^{\frac32}+C}$$

## Q2
$$\displaylines{{\displaystyle{\int_0^2x\sqrt{\left(2-x\right)^3}\,\textrm{d}x}}\\ \\ u=2-x\Rightarrow x=2-u\\ \\ \int_0^2\left(2-u\right)\left(u^{\frac32}\right)\mathrm{d} u=\left\lbrack\frac45u^{\frac52}-\frac27u^{\frac72}\right\rbrack_0^2\\ \\ \left(\frac45\sqrt{2^5}-\frac27\sqrt{2^7}\right)=\dfrac{\sqrt{2^{11}}}{35}}$$

## Q3
$$\displaylines{{\displaystyle\int\dfrac{x^3\,\textrm{d}x}{\sqrt{1+x^2}},u=1+x^2\Rightarrow x=\sqrt{u-1}},\frac{\mathrm{d} u}{\mathrm{d} x}=2x\Rightarrow x\cdot\mathrm{d} x=\frac12\mathrm{d} u\\ \\ \frac12\int\left(u-1\right)\left(u^{-\frac12}\right)\mathrm{d} u={\displaystyle\dfrac12\int\left(u^{1/2}-u^{-1/2}\right){\textrm{d}u}}}$$
