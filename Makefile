.PHONY: all format black ruff verify docs exp verify-src verify-exp

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
	cd .verify-helper/markdown; bundle add webrick; bundle exec jekyll serve

exp:
	bash expansion_all.sh
