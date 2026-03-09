import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pandas import Series
#%matplotlib inline
import warnings
warnings.filterwarnings ("ignore")

train = pd.read_csv ("Train_SU63ISt.csv")
test = pd.read_csv("Test_0qrQsBZ.csv")

train_original = train.copy()
test_original = test.copy()
