.PHONY: all format black ruff verify docs exp

format: black ruff

black:
	black .

ruff:
	ruff --fix .

oj: verify docs

verify-src:
	oj-verify run src/_tests/*/*.test.py
verify-exp:
	oj-verify run exp/_tests/*/*.test.py

verify:
	verify-src
	verify-exp

docs:
	oj-verify docs
	cd .verify-helper/markdown; bundle exec jekyll serve

exp:
	bash expansion_all.sh
