# Taylor Series
2026-10-22
Math Academy
Subject: Calculus II
Topics: Infinite Series [Maclaurin Series](Maclaurin%20Series.md) Taylor Polynomials Series

$$\displaylines{f\left(x\right)=f\left(a\right)+f^{\prime}\left(a\right)\left(x-a\right)+\frac{f^{\doubleprime}\left(a\right)}{2!}\left(x-a\right)^2+\frac{f^{\prime\prime\prime}\left(a\right)}{3!}\left(x-a\right)^3+\cdots\\ \\ =\sum_{k=0}^{\infty}\frac{f^{\left(k\right)}\left(a\right)}{k!}\left(x-a\right)^{k}}$$

## Q1
$$\displaylines{\ln(x),x=1\\ \\ f\left(x\right)=0+\left(x-1\right)-\frac{\left(x-1\right)^2}{2}+\frac{\left(x-1\right)^3}{3}+\cdots}$$

## Q2
$$\displaylines{\dfrac{1}{\sqrt{x}},x=9\\ \\ f^{\prime}\left(x\right)=-\frac{1}{2\sqrt{x^3}}\Rightarrow-\frac{1}{54}\\ \\ f^{\doubleprime}\left(x\right)=\frac{3}{4\sqrt{x^5}}\Rightarrow\frac{1}{324}\\ \\ \dfrac{1}{\sqrt{x}}=\dfrac13-\dfrac{1}{54}(x-9)+\dfrac{1}{648}(x-9)^2-\cdots}$$

## Q3
$$\displaylines{f(x)=2^{x},x=2,2^{2.1}=?\\ \\ f^{\prime}\left(x\right)=2^{x}\ln2\Rightarrow4\ln2\\ \\ f^{\doubleprime}\left(x\right)=4\ln^22\\ \\ f\left(x\right)=4+4\ln\left(2\right)\left(x-2\right)+2\ln^2\left(2\right)\left(x-2\right)^2\\ \\ f\left(2.1\right)=4+0.4\ln\left(2\right)+0.02\ln^2\left(2\right)=4.286867933}$$

## Q4
$$\displaylines{f(x)=\cos{x},x=2\pi,\cos(5)=?\\ \\ f^{\prime}\left(x\right)=-\sin x\\ \\ f^{\doubleprime}\left(x\right)=-\cos x\\ \\ f^{\prime\prime\prime}\left(x\right)=\sin x\\ \\ f^{\prime\prime\prime\prime}\left(x\right)=\cos x\\ \\ f\left(x\right)=1-\frac12\left(x-2\pi\right)^2+\frac{1}{24}\left(x-2\pi\right)^4\\ \\ f\left(5\right)=1-\frac12\left(5-2\pi\right)^2+\frac{1}{24}\left(5-2\pi\right)^4=0.2896833}$$

## Q5
$$\displaylines{f(x)=\cos{x},x=\pi,\cos{4}\\ \\ f\left(x\right)=-1+\frac{\left(x-\pi\right)^2}{2}-\frac{\left(x-\pi\right)^4}{24}}$$

## Q6
$$f(x)=x^{-1/2},x=4,\frac{1}{\sqrt3}$$


# Review

$$\displaylines{f\left(x\right)=f\left(a\right)+f^{\prime}\left(a\right)\left(x-a\right)+\frac{f^{\doubleprime}\left(a\right)}{2!}\left(x-a\right)^2+\frac{f^{\prime\prime\prime}\left(a\right)}{3!}\left(x-a\right)^3+\cdots\\ \\ =\sum_{k=0}^{\infty}\frac{f^{\left(k\right)}\left(a\right)}{k!}\left(x-a\right)^{k}}$$


## Q1
$$\displaylines{f(x)=\ln{x},x=e^2,\ln8=?\\ \\ f\left(e^2\right)=2\\ \\ f^{\prime}\left(x\right)=\frac{1}{x}\Rightarrow f^{\prime}\left(e^2\right)=\frac{1}{e^2}\\ \\ f^{\doubleprime}\left(x\right)=-\frac{1}{x^2}\Rightarrow f^{\doubleprime}\left(e^2\right)=-\frac{1}{e^4}\\ \\ \ln8=2+\frac{1}{e^2}\left(8-e^2\right)-\frac{1}{2e^4}\left(8-e^2\right)^2\\ \\ =2.079264087}$$

## Q2
$$\displaylines{f\left(x\right)=xe^{x}\Rightarrow f\left(-1\right)=-\frac{1}{e}\\ \\ f^{\prime}\left(x\right)=xe^{x}+e^{x}\Rightarrow f^{\prime}\left(-1\right)=-\frac{1}{e}+\frac{1}{e}=0\\ \\ f^{\doubleprime}\left(x\right)=xe^{x}+2e^{x}\Rightarrow f^{\doubleprime}\left(-1\right)-\frac{1}{e}+\frac{2}{e}=\frac{1}{e}\\ \\ f^{\prime\prime\prime}\left(x\right)=xe^{x}+3e^{x}\Rightarrow f^{\prime\prime\prime}\left(-1\right)=\frac{2}{e}\\ \\ xe^{x}=-\dfrac{1}{e}+\dfrac{1}{2e}(x+1)^2+\dfrac{1}{3e}(x+1)^3\cdots}$$

## Q3
$$\displaylines{\sec(\pi+0.2)=?\\ \\ f\left(x\right)=\sec x\Rightarrow f\left(\pi\right)=-1\\ \\ f^{\prime}\left(x\right)=\sec x\tan x\Rightarrow f^{\prime}\left(\pi\right)=0\\ \\ f^{\doubleprime}\left(x\right)=\sec x\tan^2x+\sec^3x\Rightarrow f^{\doubleprime}\left(\pi\right)=-1\\ \\ f\left(x\right)=-1-\frac12\left(x-\pi\right)^2\\ \\ \sec(\pi+0.2)\approx-1-\frac12\left(0.2\right)^2=-1.02}$$

# Review

$$\displaylines{f\left(x\right)=f\left(a\right)+f^{\prime}\left(a\right)\left(x-a\right)+\frac{f^{\doubleprime}\left(a\right)}{2!}\left(x-a\right)^2+\frac{f^{\prime\prime\prime}\left(a\right)}{3!}\left(x-a\right)^3+\cdots\\ \\ =\sum_{k=0}^{\infty}\frac{f^{\left(k\right)}\left(a\right)}{k!}\left(x-a\right)^{k}}$$

## Q1
$$\displaylines{x^{-1/3},x=8\\ \\ f\left(x\right)=x^{-1/3}\Rightarrow f\left(8\right)=\frac12\\ \\ f^{\prime}\left(x\right)=-\frac13x^{-\frac43}\Rightarrow f^{\prime}\left(8\right)=-\frac13\cdot\frac{1}{16}\\ \\ x^{-1/3}=\dfrac12-\dfrac{1}{48}(x-8)+\dfrac{1}{576}(x-8)^2+\cdots}$$

## Q2
$$\displaylines{f\left(x\right)=\sin{x}\Rightarrow\sin\left(\pi\right)=0\\ \\ f^{\prime}\left(x\right)=\cos x\Rightarrow f^{\prime}\left(\pi\right)=-1\\ \\ f^{\prime\prime}\left(\pi\right)=0\\ \\ f^{\prime\prime\prime}\left(\pi\right)=1\\ \\ \sin{x}=-\left(x-\pi\right)+\dfrac16\left(x-\pi\right)^3-\dfrac{1}{120}\cdot\left(x-\pi\right)^5+\cdots}$$

## Q3
$$\displaylines{x^{-\frac12}=\frac13-\frac{1}{54}\left(x-9\right)\\ \\ 8^{-\frac12}=\frac{19}{54}}$$

# Review

$$\displaylines{f\left(x\right)=f\left(a\right)+f^{\prime}\left(a\right)\left(x-a\right)+\frac{f^{\doubleprime}\left(a\right)}{2!}\left(x-a\right)^2+\frac{f^{\prime\prime\prime}\left(a\right)}{3!}\left(x-a\right)^3+\cdots\\ \\ =\sum_{k=0}^{\infty}\frac{f^{\left(k\right)}\left(a\right)}{k!}\left(x-a\right)^{k}}$$

## Q1
$$\displaylines{f(x)=\sqrt{x},x=9\\ \\ \sqrt{x}=3+\frac16\left(x-9\right)-\frac{1}{216}\left(x-9\right)^2\\ \\ \sqrt{10}=3+\frac16-\frac{1}{216}=3.16204}$$

## Q2
$$\cos{x} = -\left(x-\dfrac{\pi}{2}\right) + \dfrac{1}{6} \left(x-\dfrac{\pi}{2}\right)^3 - \dfrac{1}{120} \left(x-\dfrac{\pi}{2}\right)^5 + \cdots$$

## Q3
$$\displaylines{x^{1/4},x=16\\ \\ f^{\prime}\left(x\right)=\frac14x^{-\frac34}\Rightarrow f^{\prime}\left(16\right)=\frac{1}{32}\\ \\ x^{\frac14}=2+\frac{1}{32}\left(x-16\right)\\ \\ 12^{\frac14}=2-\frac18=\frac{15}{8}}$$
