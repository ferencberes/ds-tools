#!/bin/bash
git checkout -b merge_demo
cp MPG3.ipynb MPG2.ipynb
git commit -am "MPG2 overwritten"
git checkout master
git merge merge_demo
