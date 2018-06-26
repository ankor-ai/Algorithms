import time
import numpy as np

def get_mean(numbers):
    mean = sum(numbers)/len(numbers)
    return mean

def get_median(numbers):
  n = len(numbers)
  if n % 2 == 1:
    median = sorted(numbers)[n//2]
  else:
    median = sum(sorted(numbers)[n//2-1:n//2+1])/2.0
  return median

def time_stat(func, size, ntrials):
  total_time = 0
  for _ in range(ntrials):
    # the time to generate the random array should not be included
    data = np.random.rand(size)
    # modify this function to time func with ntrials times using a new random array each time
    start = time.time()
    res = func(data)
    end = time.time()
    # return the average run time
    total_time += (end - start)
  return 1.0 * total_time / ntrials


def median_bins(values, nbins):

    values = np.array(values)

    # Compute the mean and standard deviation
    mu = np.mean(values)
    sigma = np.std(values)

    # Compute the interval in which the median should exist
    minval = mu - sigma
    maxval = mu + sigma

    # Get the number of values smaller than minval:
    values_smaller_than_minval = values[ values < minval ]

    # Ignore all values less than minval or greater than maxval since the median will always be in [minval, maxval] only
    values = values[(minval <= values)&(values < maxval)]

    # Define the bin width
    bin_width = 2.0 * sigma / nbins

    # Discretized the original interval into nbins intervals
    bins_intervals = np.linspace(minval, maxval, num=nbins+1)

    # Count the number of element in each bin
    #bin_counts = np.zeros(nbins, dtype=int)

    bin_counts, bin_edges = np.histogram(values, bins=bins_intervals)

    return (mu, sigma, len(values_smaller_than_minval), bin_counts, bin_edges)

def median_approx(values, nbins):
    mu, sigma, length_values_smaller_than_minval, bin_counts, bin_edges = median_bins(values, nbins)

    N = len(values)

    counter = 0
    total = length_values_smaller_than_minval

    # Get the midpoint of the bin that exceeded (N+1)/2
    while total < (N+1)/2 and counter < len(bin_counts):
        total += bin_counts[counter]
        counter += 1

    counter -= 1

    midpoint = (bin_edges[counter] + bin_edges[counter+1])/2

    # Return the midpoint of bin b
    return midpoint

if __name__ == '__main__':
    numbers = [1.3, 2.4, 20.6, 0.95, 3.1, 2.7]
    mean = get_mean(numbers)

    numbers = [1.3, 2.4, 20.6, 0.95, 3.1, 2.7]
    median = get_median(numbers)

    mean_function_average_time = time_stat(get_mean, 10**5, 10)
    median_function_average_time = time_stat(get_median, 10**5, 10)

    numpy_mean_function_average_time = time_stat(np.mean, 10**5, 10)
    numpy_median_function_average_time = time_stat(np.median, 10**5, 10)

    print('{:.6f}s for mean'.format(mean_function_average_time))
    print('{:.6f}s for median'.format(median_function_average_time))

    print('{:.6f}s for mean with numpy'.format(numpy_mean_function_average_time))
    print('{:.6f}s for median with numpy'.format(numpy_median_function_average_time))

    numbers1 = [1, 5, 7, 7, 3, 6, 1, 1]
    median_approximation1 = median_approx(numbers1, 4)
    print('the median_approximation of {} is {} '.format(numbers1, median_approximation1))

    numbers2 = [1, 1, 3, 2, 2, 6]
    median_approximation2 = median_approx(numbers2, 3)
    print('the median_approximation of {} is {} '.format(numbers2, median_approximation2))

