.PHONY: all format black ruff verify docs exp verify-src verify-exp

format: black ruff

black:
	black .

ruff:
	ruff --fix .

oj: verify docs

verify-src:
	oj-verify run src/_tests/*/*.test.py

verify-exp:
	oj-verify run expansion/_tests/*/*.test.py

verify:
	oj-verify run

docs:
	oj-verify docs
	cd .verify-helper/markdown; bundle add webrick; bundle exec jekyll serve

exp:
	bash expansion_all.sh
