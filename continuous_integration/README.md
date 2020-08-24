# Description

In this folder I was experimenting with CI tools for Jupyter notebooks. 

- First I implemented a [funciton](utils.py) that takes into account category imbalances during a random train-test split.
- Then I wrote unit tests for three CI tools designed for Jupyter notebooks ([nipytest](https://github.com/chmp/ipytest), [nbval](https://github.com/computationalmodelling/nbval), [treon](https://github.com/ReviewNB/treon)) and included them in [this notebook](CIFrameworks.ipynb) 
- Finally I [configured Travis](../.travis.yml) to regularly test these resources
