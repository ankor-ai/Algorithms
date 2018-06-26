# Median Computation of Large Data Problem

## Description

Calculating the median requires all the data to be in memory at once. This is an issue in typical astrophysics calculations, which may use hundreds of thousands of exoplanets' dictionaries.

Even with a machine with lots of RAM, it's not going to be possible to find the median of billions of billions of real numbers.

This isn’t an issue for calculating the mean, since the sum only requires one real number to be added at a time. You can load a batch of real numbers, add them to the sum, and then reuse the memory. Since the sum is only ever the size of a single real number, you’ll never run out of memory.

If there were a way to calculate a "running median" you could save space by only having a batch of real numbers loaded at a time. Unfortunately, there’s no way to do an exact running median, but there are ways to do it approximately.

The [binapprox algorithm](http://www.stat.cmu.edu/~ryantibs/papers/median.pdf) does just this. The idea behind it is to find the median from the data's histogram.


## The binapprox algorithm

In order to find approximately the median, this algorithm uses two interesting properties of the median

### Property 1:

Firmally speaking, the median <img src="https://latex.codecogs.com/gif.latex?m"> of a random variable <img src="https://latex.codecogs.com/gif.latex?X"> is defined as any number such that:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20P%28X%20%5Cgeq%20m%29%20%5Cgeq%20%5Cfrac%7B1%7D%7B2%7D%20%5C%3B%20%5Ctext%7Band%7D%20%5C%3B%20P%28X%20%5Cleq%20m%29%20%5Cgeq%20%5Cfrac%7B1%7D%7B2%7D">
</p>

The median <img src="https://latex.codecogs.com/gif.latex?m"> minimizes the following function:
<!--
m = \min\limits_{c} \;f(c) = \min\limits_{c}\; E(|X-c|)
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20m%20%3D%20%5Cmin%5Climits_%7Bc%7D%20%5C%3Bf%28c%29%20%3D%20%5Cmin%5Climits_%7Bc%7D%5C%3B%20E%28%7CX-c%7C%29">
</p>

Why it is the case? Well, that's simply compute the derivative of this function to 0 and see which value solve it :)
<!--
\begin{align*}
0 = \frac{d}{dc}\;f(c)&=\frac{d}{dc}\;E(|X-c|)\\&= E(\frac{d}{dc}\,|X-c|) \\
&= E ( \;\mathbb{I} (X < c) - \mathbb{I} (X > c) \;)
\end{align*}
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cbegin%7Balign*%7D%200%20%3D%20%5Cfrac%7Bd%7D%7Bdc%7D%5C%3Bf%28c%29%26%3D%5Cfrac%7Bd%7D%7Bdc%7D%5C%3BE%28%7CX-c%7C%29%5C%5C%26%3D%20E%28%5Cfrac%7Bd%7D%7Bdc%7D%5C%2C%7CX-c%7C%29%20%5C%5C%20%26%3D%20E%20%28%20%5C%3B%5Cmathbb%7BI%7D%20%28X%20%3C%20c%29%20-%20%5Cmathbb%7BI%7D%20%28X%20%3E%20c%29%20%5C%3B%29%20%5Cend%7Balign*%7D">
</p>
where 𝟙 is the indicator function. To see why this is true, note that the derivative of |X-c| with respect to c equals +1 if x < c and -1 if x > c.  We can ignore the case x = c, since this single event has zero probability in the continuous space of events. Therefore, since:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20E%28%5C%3B%5Cmathbb%7BI%7D%28%5Ctext%7Bcondition%7D%29%5C%3B%29%20%3D%20P%28condition%29">
</p>
thus, the derivative is 0 if and only if:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20P%28X%3Cc%20%29%20%3D%20P%28%20X%20%3E%20c%20%29">
</p>

If we compare the definition of the median <img src="https://latex.codecogs.com/gif.latex?m"> and the last inequation, we automatically have:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20m%20%3D%20c">
</p>

<!--
\blacksquare 
-->
<p align="right">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cblacksquare">
</p>

Now that we proved this first property, let's check another interesting property of the median.

### Property 2: The range existance of the median

If <img src="https://latex.codecogs.com/gif.latex?X"> is a random variable having mean <img src="https://latex.codecogs.com/gif.latex?%5Cmu">, variance <img src="https://latex.codecogs.com/gif.latex?%5Csigma%5E2">, and median <img src="https://latex.codecogs.com/gif.latex?m">, then:

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20m%20%5Cin%20%5B%5Cmu%20-%5Csigma%2C%20%5Cmu%20&plus;%20%5Csigma%5D">
</p>

This is an interesting property, but why it is true ? 

First of all, we know that:  
<!--
m \in [\mu-\sigma, \mu + \sigma] \iff |\mu - m | \leq \sigma
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20m%20%5Cin%20%5B%5Cmu-%5Csigma%2C%20%5Cmu%20&plus;%20%5Csigma%5D%20%5Ciff%20%7C%5Cmu%20-%20m%20%7C%20%5Cleq%20%5Csigma">
</p>

So let's show the second inequality:
<p align="center">
<img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%7C%5Cmu%20-%20m%20%7C%20%5Cleq%20%5Csigma">
</p>

Let's start by rewriting step by step what  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%7C%5Cmu%20-%20m%20%7C">  is.
<!--
\begin{align*}
|\mu - m| &= |E(X) - m|\\
&=|E(X) - E(m)|\\
&=|E(X - m)|
\end{align*}
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cbegin%7Balign*%7D%20%7C%5Cmu%20-%20m%7C%20%26%3D%20%7CE%28X%29%20-%20m%7C%5C%5C%20%26%3D%7CE%28X%29%20-%20E%28m%29%7C%5C%5C%20%26%3D%7CE%28X%20-%20m%29%7C%20%5Cend%7Balign*%7D">
</p>

Now, since the absolute value function on the real numbers is convex, then we can apply the [Jensen's inequality](https://en.wikipedia.org/wiki/Jensen%27s_inequality) which stipulates that:
<!--
\text{f is convex} \iff f(E(X)) \leq E(f(X))
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Ctext%7Bf%20is%20convex%7D%20%5Ciff%20f%28E%28X%29%29%20%5Cleq%20E%28f%28X%29%29">
</p>
 Thus, by taking f as the absolute value function, we have:
 <!--
\begin{align*}
|\mu - m| &= |E(X - m)|\\
&\leq E(|X - m|)
\end{align*}
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cbegin%7Balign*%7D%20%7C%5Cmu%20-%20m%7C%20%26%3D%20%7CE%28X%20-%20m%29%7C%5C%5C%20%26%5Cleq%20E%28%7CX%20-%20m%7C%29%20%5Cend%7Balign*%7D">
</p>

In the property 1 of this tutorial, we showed that the median <img src="https://latex.codecogs.com/gif.latex?m"> minimizes the following function:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20m%20%3D%20%5Cmin%5Climits_%7Bc%7D%20%5C%3Bf%28c%29%20%3D%20%5Cmin%5Climits_%7Bc%7D%5C%3B%20E%28%7CX-c%7C%29">
</p>

Thus, we can write:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cbegin%7Balign*%7D%20%7C%5Cmu%20-%20m%7C%20%26%5Cleq%20E%28%7CX%20-%20m%7C%29%5C%5C%20%26%5Cleq%20E%28%7CX%20-%20%5Cmu%7C%29%20%5Cend%7Balign*%7D">
</p>

Additionally, since we have:
<!--
E(|X-\mu|) = E(\sqrt{  (X-\mu)^2})
-->
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20E%28%7CX-%5Cmu%7C%29%20%3D%20E%28%5Csqrt%7B%20%28X-%5Cmu%29%5E2%7D%29">
</p>

then the previous inequality becomes:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cbegin%7Balign*%7D%20%7C%5Cmu%20-%20m%7C%20%26%5Cleq%20E%28%7CX%20-%20%5Cmu%7C%29%5C%5C%20%26%3D%20E%28%5Csqrt%7B%20%28X-%5Cmu%29%5E2%7D%29%20%5Cend%7Balign*%7D">
</p>

At this stage, we apply again the Jensen's inequality for the concave function f, the root square function:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cbegin%7Balign*%7D%20%7C%5Cmu%20-%20m%7C%20%26%3D%20E%28%5Csqrt%7B%20%28X-%5Cmu%29%5E2%7D%29%5C%5C%20%26%5Cleq%20%5Csqrt%7BE%28X-%5Cmu%29%5E2%7D%20%5Cend%7Balign*%7D">
</p>

Finally we have, just by the definition of the standart deviation:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cbegin%7Balign*%7D%20%7C%5Cmu%20-%20m%7C%20%26%3D%20%5Cleq%20%5Csqrt%7BE%28X-%5Cmu%29%5E2%7D%5C%5C%20%26%3D%20%5Csigma%20%5Cend%7Balign*%7D">
</p>
<p align="right">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%5Cblacksquare">
</p>

Great! We have just shown that:
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20m%20%5Cin%20%5B%5Cmu%20-%5Csigma%2C%20%5Cmu%20&plus;%20%5Csigma%5D">
</p
  
But wait a minute. Why this is useful ?

## The binapprox algorithm using Property 2

Well, since we want to approximate the median of large data, we can use the property 2 to narrow the scope of the median search. In other words, if we compute the mean and the standard deviation

## Example

Say we have a list of 30 numbers between 7 and 16 and its histogram is:

<p align="center">
  <img src="./images/bin_approx_diagram.png" width="520" height="410">
</p>

The median is the average of the 15th and 16th numbers in the ordered list (we can think of this as the 15.5th number). So, starting from the left, if we sum up the counts in the histogram bins until we get to just over 15.5 then we know the last bin we added must have contained the median.

In our example, the first 3 bins sum to 9 and the first 4 bins sum to 18, so we know that the median falls into the 4th bin (marked in red), and so it must be between 10 and 11.

We choose the middle (or midpoint) giving an estimate of 10.5.

##  Strengths and weaknesses of binapprox algorithm
* *Strength*: the runtime of binapprox doesn’t depend on the data’s distribution. It requires O(1) space, and doesn’t perturb the input. The algorithm has O(n) worst-case computational complexity, as it only needs 3 passes through the data:
  1. one pass to compute the mean and the standard deviation
  2. one pass to add each data point to its corresponding bin
  3. one pass to find the median
* *Weakness*: if the standard deviation is extremely large, the median approximation could be significantly different from the actual median.


# References
* [Ryan J. Tibshirani's paper](http://www.stat.cmu.edu/~ryantibs/papers/median.pdf)

