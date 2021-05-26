rm -rf build *.egg-info dist
python -m build
python -m twine upload --repository testpypi dist/*
