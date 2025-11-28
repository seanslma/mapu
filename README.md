# mapu

My python utils package

## install locally using pip
```sh
pip install --no-deps --editable .
```

## build pip wheel
```sh
python -m build --outdir ../pip-build-path
```

## build conda package
install `conda-build` in base env and run
```sh
export VERSION=0.0.1
conda build recipe --no-anaconda-upload --python 3.12 --croot ../conda-build-path --no-test
```

## build sphinx html pages
Install `sphinx-build` first:
```sh
mamba install sphinx myst-parser -y
mamba install furo # install theme
```
Then run from root folder:
```sh
sphinx-build -b html docs/api _build/html/api
```
The output HTML will be in `_build/html/api`.

## build mkdocs html pages
Run from the docs folder as `mkdocs.yml` file is in that folder.
```sh
mkdocs build --site-dir _build/html/guide
```
