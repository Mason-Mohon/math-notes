Math Academy Algebra II Exponentiation Limits
## Power Rule
Power rule - limit of a power is the power of the limit.

If n is any positive integer and

$$\lim_{x\to a}f\left(x\right)=L$$
THEN
$$\lim_{x\to a}\left(f\left(x\right)^{}\right)^{n}=\left(\lim_{x\to a}f\left(x\right)\right)^{n}=L^{n}$$

Evaluate the limit of the expression within the parenthesis and take the power of the result.

Example:
$$\displaylines{\lim_{x\to2}\left(3x-4\right)^8\\ \\ =\left(\lim_{x\to2}\left(3x-4\right)\right)^8\\ \\ =\left(3\cdot2-4\right)^8=2^8=256}$$

### Example: Applying Power Rule to Compute a Limit

$$\displaylines{\lim_{x\to3}\left\lbrack\left(2x-1\right)^3\left(x-2\right)^9\right\rbrack=\lim_{x\to3}\left(2x-1\right)^3\cdot\lim_{x\to3}\left(x-2\right)^9\\ \\ =\left(\lim_{x\to3}\left(2x-1\right)\right)^3\cdot\left(\lim_{x\to3}\left(x-2\right)\right)^9\\ \\ =\left(2\cdot3-1\right)^3\cdot\left(3-2\right)^9=5^3\cdot1^9=125}$$
### Question 1
$$\displaylines{\displaystyle{\lim_{x \to-1} \dfrac{(x^3+x^2+x+3)^2}{(3x+5)^6}} =\\ \\ =\left(\lim_{x\to-1}\left(x^3+x^2+x+3)\right.\right)^2\cdot\left(\lim_{x\to-1}\left(\frac{1}{3x+5}\right)\right)^6\\ \\ =\left(-1+1-1+3\right)^2\cdot\left(\frac{1}{-3+5}\right)^6\\ \\ =4\cdot\left(\frac12\right)^6=0.0625}$$

### Question 2
$$\displaylines{\displaystyle{\lim_{x \to3} \left(2x-7 \right)^4(x-5)^{4}}=\\ \\ =\left(-1\right)^4\cdot-2^4=16}$$

### Example - Applying the Power Rule to Compute a Limit Given a Graph

f(x) is
![](../assets/Pasted%20image%2020260624170950.png)

Determine:
$$\displaylines{\lim_{x\to2}\left(\frac{2-7x}{xf\left(x\right)+2}\right)^3\\ \\ \lim_{x\to2}f\left(x\right)=3\\ \\ =\left(\frac{2-7\left(2\right)}{\left(2\cdot3\right)+2}\right)^3=\left(-\frac{12}{8}\right)^3=-\frac{27}{8}}$$

### Question 3
f(x) is
![](../assets/Pasted%20image%2020260624171246.png)

$$\displaylines{\displaystyle{\lim_{x\rightarrow-1} (x^2+1)^3(3- f(x))^4} =\\ \\ =\left(2\right)^3\cdot2^4=8\cdot16=128}$$

### Question 4

![](../assets/Pasted%20image%2020260624171456.png)

$$\displaylines{\displaystyle{\lim_{x\rightarrow-2} (x^3+4)^2(4-2f(x))^5}\\ \\ f\left(-2\right)=2\\ \\ =16\cdot0=0}$$

### Question 5

![](../assets/Pasted%20image%2020260624171634.png)

$$\displaylines{\displaystyle{\lim_{x\rightarrow\,\pi/2} (4x)^2(f(x)-2)^4}\\ f\left(\frac{\pi}{2}\right)=1\\ \\ =\left(2\pi\right)^2\cdot\left(1-2\right)^4=4\pi^2}$$

## The Root Rule for Limits
The limit of a root is the root of the limit, provided root exists.

If n is any position integer and $$\lim_{x\to a}f\left(x\right)=L$$
THEN
$$\lim_{x\to a}\sqrt[n]{f\left(x\right)}=\sqrt[n]{\lim_{x\to a}f\left(x\right)}=\sqrt[n]{L}$$

For example
$$\displaylines{\lim_{x\to2}\sqrt{3x-2}\\ \\ =\sqrt{\lim_{x\to2}3x-2}=\sqrt{3\cdot2-2}=\sqrt4=2}$$

### Example - Applying the Root Rule to Compute a Limit

$$\displaylines{\lim_{x\to1}\frac{\sqrt{x+8}}{x-2}\\ \\ =\frac{\sqrt{\lim_{x\to1}x+8}}{\lim_{x\to1}\left(x-2\right)}=\frac{3}{-1}=-3}$$
### Question 6
$$\displaylines{{\displaystyle{\lim_{x \to-2} \sqrt{(2x^2+3x+2)^3}}}\\ \\ =\sqrt{\left(8-6+2\right)^3}=\sqrt{64}=8}$$

### Question 7

$$\displaylines{{\displaystyle{\lim_{x \to4} \left(\sqrt[3]{(x^2-3x-5)^5}-\sqrt{(2x-7)^3}\right)}}\\ \\ =\left(\sqrt[3]{(16-12-5)^5}-\sqrt{(8-7)^3}\right)\\ \\ =\left(\sqrt[3]{(-1)^5}-\sqrt{(1)^3}\right)=-1-1=-2}$$
### Question 8
$$\displaystyle{\lim_{x\rightarrow25} x^{-1/2}}=\frac15$$

# Revisited

## Question 1
$$\displaystyle{\lim_{x \to2} \dfrac{(x^3-4x^2+5x-1)^6}{(x-1)^2}} =\frac{\left(8-16+10-1\right)^6}{1}=1$$

## Question 2
$$\displaystyle{\lim_{x \to0} \dfrac{(2x^3-x+1)^4}{(3x+2)^5}} =\frac{1}{2^5}=\frac{1}{32}$$

## Question 3
f(0)=2
$${\displaystyle{\lim_{x\rightarrow0}\dfrac{(f(x)+2)^4}{(f(x)-5)^3}}=}\frac{4^4}{-3^3}=\frac{256}{-27}$$

## Question 4
f(0)=2
$$\displaystyle{\lim_{x\rightarrow0} \dfrac{(f(x)-3)^5}{(2f(x)+1)^3}}=DNE$$
![](../assets/Pasted%20image%2020260627231631.png)

## Question 5
$$\lim_{x\to2}\sqrt[3]{\dfrac{x^3}{x^2-4x+5}}=\sqrt[3]{\frac{8}{4-8+5}}=\sqrt[3{}]{\frac81}=2$$

## Question 6
$$\displaystyle{\lim_{x \to-1} \sqrt{(x^2+4x+6)^4}}=\sqrt{\left(1-4+6\right)^4}=9$$

## Question 7
$$\displaylines{\displaystyle{\lim_{x \to1} \left(\sqrt[3]{(x^2+2x-4)^3}-\sqrt[5]{(3x+2)^5}\right)}=\\ \\ \left(\sqrt[3]{(1+2-4)^3}-\sqrt[5]{(3+2)^5}\right)=\left(\sqrt[3]{(-1)^3}-\sqrt[5]{(5)^5}\right)\\ \\ =\left(-1-5\right)=-6}$$

## Question 8
$$\lim_{x\to4}\dfrac{\sqrt{x^2+9}-1}{3x-2}=\frac{4}{10}=\frac25$$

## Question 9
f(4)=7
$${\displaystyle\lim_{x\to4}\frac{f(x)-2}{\sqrt{f(x)-1}}}=\frac{7-2}{\sqrt6}=\frac{5}{\sqrt6}$$

## Question 10
f(3)=-1
$$\lim_{x\to3}\sqrt[3]{2f(x)+3}=\sqrt[3]{-2+3}=1$$
