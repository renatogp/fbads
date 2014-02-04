test:
	`which python` -m unittest discover -v

doc:
	$(MAKE) -C docs/ html
	open docs/build/html/index.html
