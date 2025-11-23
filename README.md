# mapu

My python utils package

## build pip wheel
```sh
python -m build --outdir ../pip-build-path
```

## install locally using pip
```sh
pip install --no-deps --editable .
```

## build conda package
install `conda-build` in base env and run
```sh
export VERSION=0.0.1
conda build recipe --no-anaconda-upload --python 3.12 --croot ../conda-build-path --no-test
```
