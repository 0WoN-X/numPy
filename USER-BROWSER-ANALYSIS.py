
import numpy as np
pages = np.random.randint(1, 201, 1000)
average = np.mean(pages)
users_more_100 = np.sum(pages > 100)
print("Total users:", len(pages))
print("Average pages visited:", average)
print("Users who visited more than 100 pages:",
      users_more_100)
mean