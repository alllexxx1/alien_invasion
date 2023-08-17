install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8

#selfcheck:
#	poetry check
#
#check: selfcheck test lint
#
#build: check
#	poetry build
#
#.PHONY: install test lint selfcheck check build