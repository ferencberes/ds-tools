# Introduction

In this folder you can find different notebook versions that both process the seaborn [miles per gallon data set](https://seaborn.pydata.org/examples/scatter_bubbles.html) (MPG). You can discover the differences in their contents with version control tools designed for Jupyter notebooks.

### Different MPG notebook versions

- base notebook: [MPG1](MPG1.ipynb)
- changes to visualization + missing value search: [MPG2](MPG2.ipynb) (parent is MPG1)
- duplication check: [MPG3](MPG3.ipynb) (parent is MPG1)

# Jupyter nbdime

[GitHub](https://github.com/jupyter/nbdime) and [documentation](https://nbdime.readthedocs.io/en/latest) for the `dbdime` tool.

## A.) Without git integration

### Diff

Original git command for code diff **(not a human friendly output)**:

```bash
diff MPG1.ipynb MPG2.ipynb
```

Try it with `nbdime` in the console **(much more user friendly)**:

```bash
nbdiff MPG1.ipynb MPG2.ipynb
```

Try it with `nbdime` in the browser:

```bash
nbdiff-web MPG1.ipynb MPG2.ipynb
```

### Merge

```bash
nbmerge-web MPG1.ipynb MPG2.ipynb MPG3.ipynb
```

The provided web interface lets you decide which cells to delete, clear then executes the merge with you verification.

## B.) With git integration

You can also choose to [integrate nbdime with git](https://nbdime.readthedocs.io/en/latest/vcs.html#git-integration) by executing the following command in the root of your repository:

```bash
cd REPO_ROOT
nbdime config-git --enable
```

### Diff

After the previous setup `nbdime` is automatically called during the original `git diff` command and notebook changes are returned in a much more user friendly output.

### Merge

Follow these steps to test how `git merge` works after setting up with `nbdime`.

1. Create a separate branch and overwrite MPG2.ipynb

```bash
git checkout -b merge_demo
cp MPG3.ipynb MPG2.ipynb
git commit -am "MPG2 overwritten"
```

2. Merge changes with the master branch

```bash
git checkout master
git merge merge_demo
```

**Note that the merge was succesful even with cell outputs and execution order numbers present in the notebook!**

3. Reset master branch to the original state

```bash
git reset --hard HEAD~1
git branch -D merge_demo
```

**NOTE:**

If you simply call `git mergetool --tool nbdime`, it will be called for all merge conflicts, even on filetypes that it cannot handle. To only call on notebooks, add a filter on file paths, e.g. `git mergetool --tool nbdime -- *.ipynb`.


# ReviewNB

ReviewNB [website](https://www.reviewnb.com/) and [pricing](https://www.reviewnb.com/#pricing). It is free for open source GitHub repositories.

I enabled the ReviewNB tool for [this repository](https://app.reviewnb.com/ferencberes/ds-tools). In order to access content you must login to ReviewNB (e.g. with your GitHub account).

A few example resources to observe:
- [Visualized changes](https://app.reviewnb.com/ferencberes/ds-tools/commit/a960951319bc1470e4459df5f5b6a7fa52ac1869/) for this [commit](https://github.com/ferencberes/ds-tools/commit/a960951319bc1470e4459df5f5b6a7fa52ac1869)
- [Discussions](https://app.reviewnb.com/ferencberes/ds-tools/blob/master/version_control%2FMPG2.ipynb/file) for the MPG2 notebook.

# jupytext

[GitHub](https://github.com/mwouts/jupytext) and [documentation](https://jupytext.readthedocs.io/en/latest/) for the `jupytext` tool.

After installation `jupytext` is available through the `File/Jupytext` Jupyter menu bar option. By default synchronization is disabled for every notebook.

## Setup

Let's set up synchronization for the MPG3.ipynb notebook. Then add the generated `MPG3.py` file to the git repository.

```bash
jupytext --set-formats ipynb,py MPG3.ipynb
git add MPG3.py
git commit -am "MPG3 setup complete"
```

In order to avoid future merge conflicts for Jupyter notebook you should disable version control on the original notebook file.

```bash
git rm --cached MPG3.ipynb
```

### Note

After proper setup `jupytext` automatically manages the synchronization process between the notebook and its script counterpart file. **Thus the `jupytext --sync` command is not necessary in the following examples.**

## How to commit

Before every new commit make sure that your notebook is synchronized.

```bash
jupytext --sync MPG3.ipynb #optional
git commit -am "new commit after sync"
```

## How to update after remote changes

```bash
git pull # or git merge
jupytext --sync MPG3.ipynb #optional
```

For the complete list of `jupytext` commands click [here](https://github.com/mwouts/jupytext#command-line-conversion). 
