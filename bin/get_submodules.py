"""Parse the curriculum collection (from _config.yml) and place the content
from each lesson into the appropriate directory structure.
"""

import os
from enum import Enum
import logging
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from pathlib import Path
from distutils.dir_util import copy_tree
import requests
from shutil import copy2 as copy, rmtree

log = logging.getLogger(__name__)

class LessonType(Enum):
    """Enum for the different types of lessons.
    """
    markdown = "episode"
    r_markdown = "episode_r"

# Remove previously existing directories, to start fresh

rmtree("submodules", ignore_errors=True)
rmtree("collections", ignore_errors=True)
rmtree("slides", ignore_errors=True)

# Open the website config, which contains a list of the lessons we want in the
# workshop, then create the directory "submodules" which will contain the files
# for each lesson

with open('_config.yml') as config:
    website_config = load(config, Loader=Loader)
log.info(f"Getting submodules specified in {website_config['lessons']}")
Path("submodules").mkdir(parents=True, exist_ok=True)

# Now process each lesson in the list

for n, lesson_info in enumerate(website_config['lessons']):
    #
    if lesson_info.get('type', None) in ["episode", "episode_r"]:
        #
        lesson_type = LessonType(lesson_info.get("type", None))
        if lesson_type == LessonType.markdown:
            directory = "_episodes"
        elif lesson_type == LessonType.r_markdown:
            directory = "_episodes_rmd"
        else:
            raise ValueError(f"Unknown lesson type {lesson_type}")

        # Create the command to pull the subdirectory from GitHub
        org_name = lesson_info.get("org-name", "Southampton-RSG-Training")
        lesson_name = lesson_info.get('gh-name', None)
        if lesson_name is None:
            raise ValueError(f"No lesson name specified for lesson {n}")
        gh_branch = lesson_info.get('branch', 'gh-pages')
        # Check this repository exists
        r = requests.get(f'https://api.github.com/repos/{org_name}/{lesson_name}')
        if r.status_code != 200:
            log.warning(f'Lesson {lesson_name} does not exist in {org_name} trying in default org')
            r = requests.get(f'https://api.github.com/repos/Southampton-RSG-Training/{lesson_name}')
            if r.status_code == 200:
                log.warning(f"Lesson {lesson_name} found in 'Southampton-RSG-Training' using as fallback")
                org_name = "Southampton-RSG-Training"
            else:
                raise f"Lesson {lesson_name} does not exist in '{org_name}', or 'Southampton-RSG-Training'"
        else:
            r = requests.get(f'https://api.github.com/repos/{org_name}/{lesson_name}/branches/{gh_branch}')
            if r.status_code != 200:
                log.warning(f'Branch {gh_branch} does not exist in {org_name}/{lesson_name} trying default branch')
                r = requests.get(f'https://api.github.com/repos/{org_name}/{lesson_name}/branches/gh-pages')
                if r.status_code == 200:
                    log.warning(f'Branch {gh_branch} found in {org_name}/{lesson_name} using as fallback')
                    gh_branch = "gh-pages"
                else:
                    raise f"Branch '{gh_branch}' or 'gh-pages' does not exist in '{org_name}/{lesson_name}', or 'Southampton-RSG-Training'"



        log.info(f"Getting lesson with parameters:\n org-name: {org_name} \n gh-name: {lesson_name} \n branch: {gh_branch} \n type: {lesson_type.value}")
        os.system(f"git submodule add --force -b {gh_branch} https://github.com/Southampton-RSG-Training/{lesson_name}.git submodules/{lesson_name}")
        os.system("git submodule update --remote --merge")

        # move required files from the subdirectories to _includes/rsg/{lesson_name}/...
        # lesson destinations need to be appended with -lesson to avoid gh-pages naming conflicts

        # Things to move to ./ -- only for Rmd set up files
        if lesson_type == LessonType.r_markdown:
            for file in ["renv.lock", f"{lesson_name}_setup.R"]:
                copy(f"submodules/{lesson_name}/{file}", f"./{file.split('/')[-1]}")
                log.info(f"Copied submodules/{lesson_name}/{file} to ./")

        # Things to move to ./_includes/rsg -- for lesson schedules and setup
        dest = f"_includes/rsg/{lesson_name}-lesson"
        Path(dest).mkdir(parents=True, exist_ok=True)
        for file in ["setup.md", "_includes/rsg/schedule.html", "_includes/blurb.html"]:
            try:
                copy(f"submodules/{lesson_name}/{file}", f"{dest}/{file.split('/')[-1]}")
                log.info(f"Copied submodules/{lesson_name}/{file} to {dest}")
            except:
                log.error(f"Cannot find or move submodules/{lesson_name}/{file}, but carrying on anyway")

        # Things to move to ./collections/... -- episodes and extras
        dest = f"collections/{directory}/{lesson_name}-lesson"
        Path(dest).mkdir(parents=True, exist_ok=True)
        copy_tree(f"submodules/{lesson_name}/{directory}/", dest)
        for file in ["reference.md"]:
            try:
                dest = f"collections/{directory}/{lesson_name}-lesson"
                Path(dest).mkdir(parents=True, exist_ok=True)
                copy(f"submodules/{lesson_name}/{file}", f"{dest}/{file.split('/')[-1]}")
                log.info(f"Copied submodules/{lesson_name}/{file} to {dest}")
            except:
                log.error(f"Cannot find or move submodules/{lesson_name}/{file}, but carrying on anyway")

        for file in os.listdir(dest):
            if file.endswith(".md"):
                with open(f"{dest}/{file}", "r") as f:
                    contents = f.readlines()

                contents.insert(1, f"lesson_title: '{lesson_info.get('title', '')}'\n"
                                   f"lesson_schedule_slug: {lesson_name}-schedule\n")

                with open(f"{dest}/{file}", "w") as f:
                    contents = "".join(contents)
                    f.write(contents)

        # Move figures
        copy_tree(f"submodules/{lesson_name}/fig", "fig/")
        # Move data
        try:
            copy_tree(f"submodules/{lesson_name}/data", "data/")
        except:
            log.info(f"No data file to move in {lesson_name}")

        # Things to move only for Rmd set up files
        if lesson_type == LessonType.r_markdown:
            # Set the destination to the lesson collection, R needs these in the 'resource path'
            dest = f"collections/{directory}/{lesson_name}-lesson"
            # Move the figures for this lesson
            #copy_tree(f"submodules/{lesson_name}/fig", f"{dest}/fig/")
            # Move the footer and navbar
            #Path(f"{dest}/_includes/").mkdir(parents=True, exist_ok=True)
            #copy("_includes/workshop_footer.html", f"{dest}/_includes/")
            #copy("_includes/navbar.html", f"{dest}/_includes/")

# Now need to do the same for slides, but have to do it afterwards because we
# need a specific version of reveal.js, so we need to avoid the git submodule
# update

os.system("git submodule add --force https://github.com/hakimel/reveal.js.git submodules/reveal.js")
os.system("cd submodules/reveal.js && git checkout 8a54118f43")

for n, lesson_info in enumerate(website_config['lessons']):
    #
    lesson_type = LessonType(lesson_info.get("type", None))
    lesson_name = lesson_info.get('gh-name', None)
    if lesson_name is None:
        raise ValueError("No lesson name specified for lesson {n}")

    if Path(f"submodules/{lesson_name}/slides").is_dir():
        Path(f"slides/{lesson_name}-lesson").mkdir(parents=True, exist_ok=True)
        copy_tree(f"submodules/{lesson_name}/slides", f"slides/{lesson_name}-lesson")
        # The lesson reveal.js folder which gets copied is empty, so delete that
        # directory and then copy in the reveal.js submodule downloaded earlier
        rmtree(f"slides/{lesson_name}-lesson/reveal.js", ignore_errors=True)
        Path(f"slides/{lesson_name}-lesson/reveal.js").mkdir(parents=True, exist_ok=True)
        copy_tree("submodules/reveal.js", f"slides/{lesson_name}-lesson/")
