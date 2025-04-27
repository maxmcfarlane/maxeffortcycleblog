import pandas as pd
import os
import numpy as np

DIR = os.path.dirname(__file__)

read_data = lambda: pd.read_excel(os.path.join(DIR, 'data.xlsx'), index_col=0).replace(np.nan, None)
