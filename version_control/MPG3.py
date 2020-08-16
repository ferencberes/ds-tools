# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white")

# # Load the example mpg dataset
# - mpg : Miles per gallon

mpg = sns.load_dataset("mpg")

mpg.shape

# # Observe data

# ## a.) Types

mpg.dtypes

# ## b.) missing values

mpg.isnull().sum()

mpg = mpg[~mpg["horsepower"].isnull()]

mpg.shape

# ## c.) drop duplicates

mpg_no_dupl = mpg.drop_duplicates()

assert(len(mpg_no_dupl) == len(mpg))

# # Visualization

# Plot miles per gallon against horsepower with other semantics
sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=mpg)

mpg["origin"].value_counts().plot(kind='bar', label='index', color=['b','r','g'])

fig, axis = plt.subplots(1,2,figsize=(15,6))
sns.distplot(mpg["horsepower"], color="purple", ax=axis[0])
sns.distplot(mpg["mpg"], color="orange", ax=axis[1])
