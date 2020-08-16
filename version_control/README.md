# Version control trials

In this folder you can find different notebook versions that both process the seaborn [miles per gallon data set](https://seaborn.pydata.org/examples/scatter_bubbles.html) (MPG). You can discover the differences in the notebook contents with version control tools designed for Jupyter.



Original git command for code diff **(not a human friendly output)**:

```bash
diff MPG1.ipynb MPG2.ipynb
```

## Jupyter nbdime

## A.) Without git integration

#### Diff

Try it with [nbdime](https://github.com/jupyter/nbdime) in the console:

```bash
nbdiff MPG1.ipynb MPG2.ipynb
```

Try it with [nbdime](https://github.com/jupyter/nbdime) in the browser:

```bash
nbdiff-web MPG1.ipynb MPG2.ipynb
```

#### Merge

Merging three versions of the MPG notebook

- base notebook: [MPG1](MPG1.ipynb)
- changes to visualization + missing value search: [MPG2](MPG2.ipynb)
- duplication check: [MPG3](MPG3.ipynb)

```bash
nbmerge-web MPG1.ipynb MPG2.ipynb MPG3.ipynb
```

The provided web interface lets you decide which cells to delete, clear then executes the merge with you verification.

## B.) Without git integration

You can also choose to [integrate nbdime with git](https://nbdime.readthedocs.io/en/latest/vcs.html#git-integration) by executing the following command in the root of your repository:

```bash
cd REPO_ROOT
nbdime config-git --enable
```

Then nbdime will be called during the original `git diff` command and notebook changes will be returned in a much more user friendly output.

#### NOTE

If you simply call `git mergetool --tool nbdime`, it will be called for all merge conflicts, even on filetypes that it cannot handle. To only call on notebooks, add a filter on file paths, e.g. `git mergetool --tool nbdime -- *.ipynb`. 
