# Importing the libraries
import math
import random
import matplotlib.pyplot as plt
import pandas as pd


# importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
n_users, n_ads = dataset.shape

# Implementing Upper Confidence Bound (UCB)
ads_selected = []
numbers_of_selections = [0] * n_ads
sums_of_rewards = [0] * n_ads
total_reward = 0


for user_id in range(0, n_users):

    ad = 0
    max_upper_bound = 0

    for ad_id in range(0, n_ads):

        if (numbers_of_selections[ad_id] > 0):
            average_reward = sums_of_rewards[ad_id] / numbers_of_selections[ad_id]
            delta = math.sqrt(3/2 * math.log(user_id+1) / numbers_of_selections[ad_id])
            upper_bound = average_reward + delta

        else: # set the upper bound to infinity since the number of selection is 0
            upper_bound = math.inf

        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = ad_id

    ads_selected.append(ad)
    numbers_of_selections[ad] += 1
    reward = dataset.values[user_id, ad]
    sums_of_rewards[ad] += reward
    total_reward += reward


print("The total reward using UCB is: ", total_reward)
print("The best ad to serve is the ad number ", ad)

# Visualizing the results in a histogram
plt.hist(ads_selected)
plt.title('Histogram of rewards using UCB')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

