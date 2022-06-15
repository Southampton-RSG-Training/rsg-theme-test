#!/usr/bin/env bash
git branch -d localbuild || echo 'branch local build does not exist to delete'
git checkout -b localbuild

python -m venv ./venv || echo 'venv already exists'

#TODO: Make this windows safe
source venv/bin/activate

gem install github-pages bundler kramdown kramdown-parser-gfm

python3 -m pip install --upgrade pip setuptools wheel pyyaml==5.3.1 requests
python3 -m pip install -r requirements.txt

python bin/get_submodules.py

#TODO: Check for rmarkdown and build it if appropriate

python bin/make_favicons.py
python bin/get_schedules.py
python bin/get_setup.py

# Clean the submodules out all necessary stuff has been copied.
git rm .gitmodules -f
git rm -r submodules -f

# Build the site.
bundle install
bundle exec jekyll serve

rm -r _site/
rm -r venv/
rm -r _includes/rsg/*-lesson/
rm assets/favicons/rsg/apple* assets/favicons/rsg/favicon* assets/favicons/rsg/mstile*

git checkout main