# RSG Training Workshop Template

**To use this repository please use the template functionality. When you use this template, please include all branches and use a descriptive name as this will become the url that is provided to learners.**

## Setting up a workshop

To configure a workshop please follow the steps below.

1) Create a copy of this workshop using the GitHub (GH) templating function. Note the name of your new workshop will be the website URL, so be descriptive, concise as possible and accurate.
2) Using either the GH online code editor or pulling a local version, edit the _config.yml file. This is the only file that needs to be modified.
3) The fields to change are as follows:
   - carpentry: default 'rsg', uses the rsg templating build process.
   - title: the title of the workshop.
   - venue, address, country, lat/long: updates the details for the workshop location. You can use, e.g., Google Maps or https://www.latlong.net/convert-address-to-lat-long.html to find the latitude and longitude of the venue.
   - humandate, humantime, startdate, enddate: human- and machine-readable dates and times, respectively, for the start and end of the workshop. Machine readable dates should be in YYYY-MM-DD format. The human-readable dates are free form.
   - instructor, instructor-email: YAML lists of instructor names and associated email addresses.
   - helper: YAML list of the names of the helpers.
   - **lessons: a YAML list of the lessons to include in the workshop. Each lesson must have:**
      - title: the name of the lesson.
      - gh-name: the name of a lesson repository in the <https://github.com/Southampton-RSG-Training> GH organisation e.g. 'git-novice'.
      - type: choose from either 'episode' for standard markdown lessons or 'episode_r' for R markdown.
      - date: the date the lesson is to be taught. Many date formats accepted, more information can be found [here](https://dateutil.readthedocs.io/en/stable/parser.html) about accepted formats. If a date format is not accepted, then the build process will abort. For multi-day lessons, multiple dates have to be specified in a YAML list. The number of dates must equal the number of schedule tables in `_includes/rsg/lesson/schedule.html`.
      - time: the time to start the lesson, both 12 hour and 24 hour timestamps are accepted. For multi-day lessons, multiple start times must also be specified in a YAML list.
      - branch: the git branch to generate lessons from. To customise a lesson, one can specify another branch - more details below. The default choice is 'gh-pages'.
4) **Commit (and push) changes to the 'main' branch**. The site is built, and published to the 'gh-pages' branch. The site build is handled by GH Actions, more details in development below.

The currently available lessons are:

- shell-novice <https://github.com/Southampton-RSG-Training/shell-novice>
- git-novice <https://github.com/Southampton-RSG-Training/git-novice>
- python-novice <https://github.com/Southampton-RSG-Training/python-novice>
- spreadsheets <https://github.com/Southampton-RSG-Training/spreadsheets>
- openrefine-data-cleaning <https://github.com/Southampton-RSG-Training/openrefine-data-cleaning>
- r-novice <https://github.com/Southampton-RSG-Training/r-novice>
- project-novice <https://github.com/Southampton-RSG-Training/project-novice>

5) Optional: To reattach to this template and pull updates and changes the following steps are required.
   1) Warning: To do this you need to understand both Git Remotes, Git merges (specifically solving conflicts).
   2) ```git remote add template https://github.com/Southampton-RSG-Training/workshop-template```
   3) ```git fetch --all```
   4) ```git merge template/main --allow-unrelated-histories```
   5) Then fix the conflicts on your branch. (Accept changes everywhere except _config.yml where you have configured your workshop, n.b. if you have made custom changes to other places then this will need to be accounted for).
   6) Finally, add and commit the changes to the main branch the push to 'origin/main'.

## Customising Lessons

To customise a lesson's content, the lesson branch can be changed to use an alternative branch of the lesson repository. You can then stage (add) and commit '_config.yml'. But remember to not push to remote until after the episode branch has been created/edited, as the push will only then grab the changes. It is also possible to force a re-build of the workshop, if you do this in the wrong order.

```bash
$ git commit --allow-empty -m "rebuild lesson to (re)add lesson submodules"
$ git push origin main
```

To make changes to the lessons, clone the lesson repository and then checkout (or create) branch for the modified lesson
you want. **Note that the gh-pages branch is the canonical branch and should not be edited for lesson customisation**. To
modify the lesson content, edit the markdown in `_episodes` (or `_episodes_rmd` for courses written in R markdown). Commit and
push the changes to the lesson repository on the (new) branch.

If you think the changes are a universal improvement to the base gh-pages branch, please open a pull request for review.

## Development and Build Logic

To develop this template requires an understanding of:

1) **Jekyll** and **Liquid templating** are used in the deployment of static GitHub pages sites.
2) **GitHub Actions** and **python** are used to parse the `_config.yml`, clone submodules, and move/generate files to customise the workshop.
3) **Markdown** and/or **Rmarkdown** used to write the lesson material.
4)  **GitHub/git (especially branches)** to manage lesson version, and to separate configuration from deployment.


The gh-pages branch of each lesson are kept in a build ready state. Development for these lessons is detailed in each
lesson repository. The config file is used by the jekyll build and also parsed to control the GitHub Actions.

Firstly, the _config.yml is parsed by `bin/get_submodules.py` and `bin/get_schedules.py`. `get_submodules.py` gets each of the lesson repositories and clones them as a submodules. The episode markdown files are
moved into `collections/_episodes(_rmd)/gh-name-lesson/`, and the various includes and slide files are moved into their appropriate locations. Next, `get_schedules.py` parses _config.yml, and generates the top-level and detailed lesson schedules. Following on, `bin/clean_setup_md.py` is used to stitch together the various setup files into a single markdown file.

Then the GH Pages process (Jekyll/Liquid) is instructed to build the site, where each lesson slug (in a Markdown file) are the permalink for that lesson. The final hosted webpage is stored in the `gh-pages` branch.
