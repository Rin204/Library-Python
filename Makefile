.PHONY: all format black ruff verify docs

format: black ruff

black:
	black .

ruff:
	ruff --fix .

oj: verify docs

verify:
	oj-verify run

docs:
	oj-verify docs
	cd .verify-helper/markdown; bundle exec jekyll serve