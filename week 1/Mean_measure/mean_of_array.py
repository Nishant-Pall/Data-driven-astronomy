# Write your calc_stats function here.
import numpy as np
import pandas as pd

def calc_stats(arr):
  data = np.mean(np.loadtxt(arr, delimiter=','))
  return (np.round(data,1), np.round(data,1))

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data.csv')
  print(mean)