# -*- coding: utf-8 -*-
"""TESTr.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BFkhzrsne7xin61-OFlvr_HaoujSF5A-
"""

# prompt: Read csv file

import pandas as pd

df = pd.read_csv('/content/sample_data/mnist_test.csv')
#paste the path of file in parameter
print(df.head())