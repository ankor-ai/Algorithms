# Importing the libraries
import random
import matplotlib.pyplot as plt
import pandas as pd


# importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing Random Selection
n_users, n_ads = dataset.shape

ads_selected = []
total_reward = 0

for user in range(0, n_users):

    # randomly select an ad to show for the user
    ad = random.randrange(n_ads)

    ads_selected.append(ad)

    reward = dataset.values[user, ad]

    total_reward += reward

print("The total reward using random selection is: ", total_reward)

# Visualizing the results in a histogram
plt.hist(ads_selected)
plt.title('Histogram of rewards using random ads selection')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
