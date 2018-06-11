# Importing the libraries
import random
import matplotlib.pyplot as plt
import pandas as pd


# importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
n_users, n_ads = dataset.shape

# Implementing Thompson Sampling
ads_selected = []
numbers_of_rewards_1 = [0] * n_ads
numbers_of_rewards_0 = [0] * n_ads

total_reward = 0


for user_id in range(0, n_users):

    ad = 0
    max_random = 0

    for ad_id in range(0, n_ads):

        # generate a random draw
        random_beta = random.betavariate(numbers_of_rewards_1[ad_id] + 1, numbers_of_rewards_0[ad_id] +1)

        if random_beta > max_random:
            max_random = random_beta
            ad = ad_id

    ads_selected.append(ad)

    reward = dataset.values[user_id, ad]

    if reward == 1:
        numbers_of_rewards_1[ad] += 1
    else:
        numbers_of_rewards_0[ad] += 1

    total_reward += reward


print("The total reward using Thompson Sampling is: ", total_reward)
print("The best ad to serve is the ad number ", ad)

# Visualizing the results in a histogram
plt.hist(ads_selected)
plt.title('Histogram of rewards using Thompson Sampling')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

