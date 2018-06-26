# Median Computation of Large Data Problem

## Description

Calculating the median requires all the data to be in memory at once. This is an issue in typical astrophysics calculations, which may use hundreds of thousands of exoplanets' dictionaries.

Even with a machine with lots of RAM, it's not going to be possible to find the median of billions of billions of real numbers.

This isn’t an issue for calculating the mean, since the sum only requires one real number to be added at a time. You can load a batch of real numbers, add them to the sum, and then reuse the memory. Since the sum is only ever the size of a single real number, you’ll never run out of memory.

If there were a way to calculate a "running median" you could save space by only having a batch of real numbers loaded at a time. Unfortunately, there’s no way to do an exact running median, but there are ways to do it approximately.

The [binapprox algorithm](http://www.stat.cmu.edu/~ryantibs/papers/median.pdf) does just this. The idea behind it is to find the median from the data's histogram.


## The binapprox algorithm

In order to find approximately the median, this algorithm uses a very interesting property of the median

### The range existance of the median;

If X is a random variable having mean µ, variance σ^2, and median m, then:
m ∈ [µ − σ, µ + σ]

## Example

Say we have a list of 30 numbers between 7 and 16 and its histogram is:

<p align="center">
  <img src="./images/bin_approx_diagram.png" width="520" height="410">
</p>

The median is the average of the 15th and 16th numbers in the ordered list (we can think of this as the 15.5th number). So, starting from the left, if we sum up the counts in the histogram bins until we get to just over 15.5 then we know the last bin we added must have contained the median.

In our example, the first 3 bins sum to 9 and the first 4 bins sum to 18, so we know that the median falls into the 4th bin (marked in red), and so it must be between 10 and 11.

We choose the middle (or midpoint) giving an estimate of 10.5.
