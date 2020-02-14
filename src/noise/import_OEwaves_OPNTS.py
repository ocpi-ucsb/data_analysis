import numpy as np
import pandas as pd

filename = ''

# split into csv and txt

base_path = '/Users/Andrei/Box/OCPI Shared/data/andrei/SLS_cavity/'
filename = 'rock_SBScavitylock_phase_noise_test_012820.txt'

data = pd.read_csv(base_path + filename, header = None)
print data