.PHONY: all format black ruff verify docs exp

format: black ruff

black:
	black .

ruff:
	ruff --fix .

oj: verify docs

verify:
	oj-verify run src/_tests/*/*.test.py

docs:
	oj-verify docs
	cd .verify-helper/markdown; bundle exec jekyll serve

exp:
	bash expansion_all.sh
