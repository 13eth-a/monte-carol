import numpy as np
import random

from scipy import stats
from scipy.stats import semicircular

import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable

# p = 44%
# length of each sequence = 50
# streak length = 3

# inputs
num_sims = 10000
seq_length = 50
p = 0.44

def generate_rand_int():
    hit_or_miss = random.randint(0, 1)
    if hit_or_miss > p:
        hit_or_miss = 1 # "hit"
    else:
        hit_or_miss = 0 # "miss"
    
    return hit_or_miss

# runs for desired number of solutions
for i in range(num_sims):
    
    # trackers for found streaks and number of runs done
    num_hits = 0
    num_streaks = 0
    num_of_runs = [0]
    
    # records result per run
    record_run = []
    
    # run until the basketball player has shot 50 times
    while num_of_runs[-1] < seq_length:
        run = generate_rand_int()
        record_run.append(run)
        
        # Checks for a streak of 3 "hits" in record_run
        for i in range(len(record_run) - 2):
            if record_run[i] == record_run[i + 1] == record_run [i + 2] == 1:
                num_streaks += 1
                if i + 3 < len(record_run) and record_run[i + 3] == 1:
                    num_hits += 1
            if num_streaks > 0:
                score_pct = (num_hits/num_streaks) * 1.0
            else:
                score_pct = 0.0

        
        num_of_runs.append(num_of_runs[-1] + 1)


#Histogram 

n_bins = num_sims

fig, ax = plt.subplots(figsize =(8, 6))





