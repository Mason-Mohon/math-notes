Math AcademyAlgebra II Riemann Sum
Want to find area A under graph of y=x^2 between x=1 and x=4
![](../assets/Pasted%20image%2020260625121321.png)
Find area of each rectangle and add them together to get 14, approximating the area under the curve.

Left sum means left corner of each box touches curve, meaning its an under-representation in this case, whereas right would be over. Converse if slope had been negative.

General formula:

$$A=\left(f\left(x_0\right)+f\left(x_1\right)+\cdots+f\left(x_{n-1}\right)\right)\cdot\Delta x$$

## Example

Estimate AUC for $$f\left(x\right)=\left(2x-4\right)^2$$
over \[0, 2]

![](../assets/Pasted%20image%2020260625201747.png)

Dx is width of each rectangle. Step size with a = 0, b = 2, 4 rectangles:
$$\Delta x=\frac{b-a}{n}=\frac{2-0}{4}=0.5$$
Area can be approximated with:
$$\char"391 =\left(f\left(0\right)+f\left(0.5\right)+f\left(1\right)+f\left(1.5\right)\right)\cdot\Delta x$$
Set up table with values f(x) at each point.

| x    | 0   | 0.5 | 1   | 1.5 |
| ---- | --- | --- | --- | --- |
| f(x) | 16  | 9   | 4   | 1   |
So we get:
$$\char"0391 =\left(16+9+4+1\right)\cdot0.5=15$$
## Question 1
Left Riemann sum for r(t) over interval \[2, 8] with three sub intervals

| t(hours)           | 2   | 4   | 6   | 8   |
| ------------------ | --- | --- | --- | --- |
| r(t) (liters/hour) | 1   | 3   | 4   | 7   |
$$\displaylines{\Delta x=\frac{8-2}{3}=2\\ \\ A=\left(1+3+4\right)\cdot2=16}$$
## Question 2
Interval \[0, 16], left sum with 4 sub-intervals

| x    | 0   | 4   | 8   | 12  | 16  |
| ---- | --- | --- | --- | --- | --- |
| f(x) | 2   | 3   | 3   | 1   | 4   |
$$\displaylines{\Delta x=\frac{16-0}{4}=4\\ \\ A=\left(2+3+3+1\right)\cdot4=36}$$
## Solving for unknown value
Interval is \[-4, 2], 3 sub-intervals, left Riemann sum is value of 28, what is k?

| x    | -4  | -2  | 0   | 2   |
| ---- | --- | --- | --- | --- |
| f(x) | 5   | 3   | k   | 2   |
$$\displaylines{A=\left(f\left(-4\right)+f\left(-2\right)+f\left(0\right)\right)\cdot\Delta x\\ \\ A=\left(5+3+k\right)\cdot2=16+2k\\ \\ 28=16+2k\\ \\ k=6}$$
## Question 3
Interval \[1, 13], 3 subintervals. Area is 20.

| x    | 1   | 5   | 9   | 13  |
| ---- | --- | --- | --- | --- |
| f(x) | -2  | 6   | k   | 3   |
$$\displaylines{\Delta x=\frac{13-1}{3}=4\\ \\ A=\left(-2+6+k\right)\cdot4=20\\ \\ 4+k=5\\ \\ k=1}$$
## Question 4
A = 46, 4 sub-intervals.

| t    | 0   | 1   | 2   | 3   | 4   |
| ---- | --- | --- | --- | --- | --- |
| r(t) | 10  | 12  | k   | 15  | 14  |

$$\displaylines{\Delta x=1\\ \\ 46=10+12+k+15\\ \\ k=46-12-10-15=36-27=9}$$
## Overestimates and Underestimates
If curve is increasing the left Riemann sum is an underestimate. If it is decreasing, the sum is an overestimate

![](../assets/Pasted%20image%2020260625215531.png)

This is an overestimate

## Question 6
Interval \[0, 1]
$$\displaylines{\Delta x=0.25\\ \\ y=4x+1\\ \\ A=\left(1+2+3+4\right)\cdot0.25=2.5}$$
## Left Riemann Sums with Irregular Step Size

Step size varies means irregular step size

| x    | 1   | 2   | 3.5 | 4   |
| ---- | --- | --- | --- | --- |
| f(x) | 1   | 4   | 6   | 12  |
Domain of f(x) is partitioned as
$$\left\lbrack1,4\right\rbrack=\left\lbrack1,2\right\rbrack\cup\left\lbrack2,3.5\right\rbrack\cup\left\lbrack3.5,4\right\rbrack$$
![](../assets/Pasted%20image%2020260625220442.png)
$$\displaylines{A=f\left(1\right)\cdot\Delta x_1+f\left(2\right)\cdot\Delta x_2+f\left(3.5\right)\cdot\Delta x_3\\ \\ A=1\cdot\left(2-1\right)+4\cdot\left(3.5-2\right)+6\cdot\left(4-3.5\right)=10}$$
## Example
Interval \[0, 2]

| x    | 0   | 0.8 | 1.6 | 2   |
| ---- | --- | --- | --- | --- |
| f(x) | 2   | 5   | 10  | 12  |
n = 3
$$\displaylines{A=f\left(0.0\right)\Delta x_1+f\left(0.8\right)\Delta x_2+f\left(1.6\right)\Delta x_3\\ \\ \Delta x_{i}=x_{i+1}-x_{i}\\ \\ \Delta x_1=0.8,\Delta x_2=0.8,\Delta x_3=0.4\\ \\ A=2\cdot0.8+5\cdot0.8+10\cdot0.4=9.6}$$
## Question 7
\[6, 18] interval

| x    | 6   | 8   | 11  | 15  | 18  |
| ---- | --- | --- | --- | --- | --- |
| f(x) | -1  | 2   | 4   | 3   | 1   |
$$\displaylines{A=f\left(6\right)\Delta x_1+f\left(8\right)\Delta x_2+f\left(11\right)\Delta x_3+f\left(15\right)\Delta x_4\\ \\ \Delta x_1=2,\Delta x_2=3,\Delta x_3=4,\Delta x_4=3\\ \\ A=-1\cdot2+2\cdot3+4\cdot4+3\cdot3=-2+6+16+9=29}$$
## Question 8
Interval \[0, 11]

| x    | 0   | 2   | 5   | 9   | 11  |
| ---- | --- | --- | --- | --- | --- |
| f(x) | 4   | 1   | 3   | 2   | 6   |
| Dx   | 2   | 3   | 4   | 2   | -   |
$$A=8+3+12+4=27$$
