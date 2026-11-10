# Finding the Area of a Polar Region
2026-11-03
Math Academy
Subject: Calculus II
Topics: Polar Coordinates Integrals

$$A=\frac12\int_{\theta_1}^{\theta_2}r^2\mathrm{d}\theta$$

## Q1
$$\displaylines{r=3\sin(2\theta),\pi\leq\theta\leq\dfrac{5\pi}{4}\\ \\ A=\frac92\int_{\pi}^{\frac{5\pi}{4}}\sin^2\left(2\theta\right)\mathrm{d}\theta=\frac92\int_{\pi}^{\frac{5\pi}{4}}\frac{1-\cos\left(4\theta\right)}{2}\mathrm{d}\theta=\left\lbrack\frac94\left(\theta-\frac14\sin\left(4\theta\right)\right)\right\rbrack_{\pi}^{\frac{5\pi}{4}}\\ \\ =\frac94\left(\frac{5\pi}{4}-0\right)-\frac{9\pi}{4}=\frac{45\pi}{16}-\frac{36\pi}{16}=\frac{9\pi}{16}}$$

## Q2
$$\displaylines{r=3\sin\theta,\dfrac{\pi}{6}\leq\theta\leq\dfrac{\pi}{3}.\\ \\ A=\frac92\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}\sin^2\theta\mathrm{d}\theta=\frac94\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}1-\cos\left(2\theta\right)\mathrm{d}\theta=\left\lbrack\frac94\theta-\frac98\sin\left(2\theta\right)\right\rbrack_{\frac{\pi}{6}}^{\frac{\pi}{3}}\\ \\ =\left(\frac{6\pi}{8}-\frac{9\sqrt3}{16}\right)-\left(\frac{3\pi}{8}-\frac{9\sqrt3}{16}\right)=\frac{3\pi}{8}}$$

## Q3
$$\displaylines{r=3-2\cos\theta,0\leq\theta\leq\pi\\ \\ A=\frac12\int_0^{\pi}9-12\cos\theta+4\cos^2\theta\mathrm{d}\theta\\ \\ =\frac92\int_0^{\pi}\mathrm{d}\theta-6\int_0^{\pi}\cos\theta\mathrm{d}\theta+\int_0^{\pi}\left(1+\cos\left(2\theta\right)\right)\mathrm{d}\theta\\ \\ =\left\lbrack\frac{11}{2}\theta-6\sin\theta+\frac12\sin\left(2\theta\right)\right\rbrack_0^{\pi}=\frac{11\pi}{2}}$$

## Q4
$$\displaylines{r=1-\sin\theta,-\dfrac{\pi}{2}\leq\theta\leq\dfrac{\pi}{2}\\ \\ A=\frac12\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\left(1-2\sin\theta+\frac{1-\cos\left(2\theta\right)}{2}\right)\mathrm{d}\theta\\ \\ =\frac12\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\mathrm{d}\theta-\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\sin\theta+\frac14\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\mathrm{d}\theta-\frac14\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\cos\left(2\theta\right)\mathrm{d}\theta\\ \\ =\left\lbrack\frac{3\theta}{4}+\cos\theta-\frac18\sin\left(2\theta\right)\right\rbrack_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\\ \\ =\left(\frac{3\pi}{8}\right)-\left(-\frac{3\pi}{8}\right)=\frac{3\pi}{4}}$$

## Q5
$$\displaylines{r=2\theta\Bigl(1+\sin(3\theta)\Bigr),0\leq\theta\leq\dfrac{\pi}{2}\\ \\ A=\frac12\int_0^{\frac{\pi}{2}}4\theta^2\left(1+2\sin\left(3\theta\right)+\frac{1-\cos\left(6\theta\right)}{2}\right)\mathrm{d}\theta\\ \\ =\frac12\int_0^{\frac{\pi}{2}}\left(6\theta^2+8\theta^2\sin\left(3\theta\right)-2\theta^2\cos\left(6\theta\right)\right)\mathrm{d}\theta\\ \\ =\theta^3\Biggr|_0^{\frac{\pi}{2}}+4\int_0^{\frac{\pi}{2}}\theta^2\sin\left(3\theta\right)\mathrm{d}\theta-\int_0^{\frac{\pi}{2}}\theta^2\cos\left(6\theta\right)\mathrm{d}\theta\\ \\ \int u\mathrm{d} v=uv-\int v\mathrm{d} u\\ \\ \theta^2\sin\left(3\theta\right),u=\theta^2\Rightarrow\mathrm{d} u=2\theta,v=-\frac13\cos\left(3\theta\right)\Rightarrow\mathrm{d} v=\sin\left(3\theta\right)\\ \\ \theta^2\cos\left(6\theta\right),u=\theta^2\Rightarrow\mathrm{d} u=2\theta,v=\frac16\sin\left(6\theta\right)\Rightarrow\mathrm{d} v=\cos\left(6\theta\right)\\ \\ =\theta^3\Biggr|_0^{\frac{\pi}{2}}-\frac43\cos\left(3\theta\right)\theta^2\Biggr|_0^{\frac{\pi}{2}}+\frac83\int_0^{\frac{\pi}{2}}\theta\cos\left(3\theta\right)\mathrm{d}\theta-\frac16\theta^2\sin\left(6\theta\right)\Biggr|_0^{\frac{\pi}{2}}+\frac13\int_0^{\frac{\pi}{2}}\theta\sin\left(6\theta\Biggr.\right)\mathrm{d}\theta\\ \\ \theta\cos\left(3\theta\right),u=\theta\Rightarrow\mathrm{d} u=1,v=\frac13\sin\left(3\theta\right)\Rightarrow\mathrm{d} v=\cos\left(3\theta\right)\\ \\ \theta\sin\left(6\theta\Biggr.\right),u=\theta\Rightarrow\mathrm{d} u=1,v=-\frac16\cos\left(6\theta\right)\Rightarrow\sin\left(6\theta\right)\\ \\ =\left\lbrack\theta^3-\frac43\cos\left(3\theta\right)\theta^2+\frac{8\theta}{9}\sin\left(3\theta\right)+\frac{8}{27}\cos\left(3\theta\right)-\frac16\theta^2\sin\left(6\theta\right)-\frac{\theta}{18}\cos\left(6\theta\right)+\frac{1}{108}\sin\left(6\theta\right)\right\rbrack_0^{\frac{\pi}{2}}\\ \\ =\frac{\pi^3}{2}-\frac{4\pi}{9}+\frac{\pi}{36}-\frac{8}{27}}$$

## Q6
$$\displaylines{r=4(3\theta^2+2\sin(2\theta)),\dfrac{\pi}{6}\leq\theta\leq\dfrac{\pi}{3}\\ \\ A=8\int_{\frac{\pi}{6}}^{\frac{\pi}{3}}(3\theta^2+2\sin(2\theta))^2\mathrm{d}\theta}$$


# Review
$$ A=\frac12\int_{\theta_1}^{\theta_2}r^2\mathrm{d}\theta $$
## Q1
$$\displaylines{r=\sin\theta+\cos\theta,0\leq\theta\leq\dfrac{\pi}{4}\\ \\ A=\frac12\int_0^{\frac{\pi}{4}}\left(\sin\theta+\cos\theta\right)^2\mathrm{d}\theta=\frac12\int_0^{\frac{\pi}{4}}\left(2\sin\theta\cos\theta+\mathrm{1}\right)\mathrm{d}\theta\\ \\ =\frac12\left\lbrack\theta-\frac12\cos\left(2\theta\right)\right\rbrack_0^{\frac{\pi}{4}}=\frac12\left(\frac{\pi}{4}\right)-\frac12\left(0-\frac12\right)=\frac{\pi}{8}+\frac14=\frac{\pi+2}{8}}$$

## Q2
$$\displaylines{r=1+\dfrac{\sin(\theta)}{3},\dfrac{\pi}{2}\leq\theta\leq{\pi}\\ \\ A=\frac12\int_{\frac{\pi}{2}}^{\pi}\left(1+\dfrac{\sin(\theta)}{3}\right)^2\mathrm{d}\theta}$$

## Q3
$$\displaylines{r=4-3\cos\theta,\dfrac{\pi}{2}\leq\theta\leq\pi\\ \\ A=\frac12\int_{\frac{\pi}{2}}^{\pi}\left(4-3\cos\theta\right)^2\mathrm{d}\theta=\frac12\int_{\frac{\pi}{2}}^{\pi}\left(16-24\cos\theta+9\cos^2\theta\right)\mathrm{d}\theta\\ \\ =\frac12\left\lbrack\frac{41}{2}\theta-24\sin\theta+\frac94\sin\left(2\theta\right)\right\rbrack_{\frac{\pi}{2}}^{\pi}\\ \\ =\left(\frac{41\pi}{4}-12\sin\pi+\frac98\sin\left(2\pi\right)\right)-\left(\frac{41\pi}{8}-12\sin\frac{\pi}{2}+\frac98\sin\left(\pi\right)\right)\\ \\ =\frac{41\pi}{4}-0+0-\frac{41\pi}{8}+12+0=\frac{41\pi}{8}+12}$$
