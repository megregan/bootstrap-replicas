import numpy as np
# A function that generates bootstrap replicate of 1D data
def bootstrap_replicate_1d(data, func):
    bs_sample = np.random.choice(data,len(data))
    return(func(bs_sample))
# A function that draws bootstrap replicates
def draw_bs_reps(data, func, size=1):
    # Initialize numpy array: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)
    
    return bs_replicates
# Added main gaurd
if __name__ == '__main__':
    import pandas as pd
    # Read in the csv file as a pandas data frame. Skip the first four rows as they contain unnecessary text
    bout_lengths_df = pd.read_csv('gandhi_et_al_bouts.csv',skiprows=4)
    # Turn the dataframe into a np array. Remove the 3rd column, fish, as it is not relevant
    bout_lengths = np.array(bout_lengths_df)[:,0:2]
    # Get a 1D numpy array of the bout lengths of wild type fish
    # by selecting only the rows where the genotype is wt and then removing the genotype column   
    bout_lengths_wt = bout_lengths[bout_lengths[:,0] == 'wt'][:,1]
    # Get a 1D numpy array of the bout lengths of mutant type fish
    # by selecting only the rows where the genotype is mut and then removing the genotype column
    bout_lengths_mut = bout_lengths[bout_lengths[:,0] == 'mut'][:,1]
    # Get mean active bout length
    mean_wt = np.mean(bout_lengths_wt)
    mean_mut = np.mean(bout_lengths_mut)
    # Draw bootstrap replicates for the data
    bs_reps_wt = draw_bs_reps(bout_lengths_wt, np.mean, size=10000)
    bs_reps_mut = draw_bs_reps(bout_lengths_mut, np.mean, size=10000)
    # Compute 95% confidence intervals
    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])
    # Show the results
    print('Wild type: mean =', mean_wt, '(min), conf. int. =', conf_int_wt, '(min).')
    print('Mutant type: mean =', mean_mut, '(min), conf. int. =', conf_int_mut, '(min).')
