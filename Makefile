# Publish the website subproject to its own sibling repository.
#
# Delegates to bin/make-github-pages rather than repeating the subtree
# command here, so there is one place that runs bin/check and refuses to
# push uncommitted changes. The underlying command is:
#
#   git subtree push --prefix=roles-skills.github.io github-pages main
#
# See spec/monorepo-github-pages/.

.PHONY: github-pages check build
github-pages:
	bin/make-github-pages

check:
	bin/check

build:
	python3 scripts/build.py
	roles-skills.github.io/bin/sync
