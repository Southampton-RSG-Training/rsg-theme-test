# lesson-template

This lesson template is intended to be used with the
[workshop-template](https://github.com/Southampton-RSG-Training/workshop-template/),
but could still be used to create an independent, standalone lesson. It is based
on the [Carpentries](https://carpentries.github.io/lesson-example/) lesson
example, but with some modifications. The aim is to keep this template as simple
and up-to-date with the Carpentries example as possible.

## Instructions

1. Create a new lesson by creating a template of this repository, ensure that
   the branch is still named gh-pages. Please make sure to create this in the
   Southampton-RSG-Training organization, with a short name such as
   "git-novice", or "shell-advanced".

2. Optionally, you should immediately create a new branch for the lesson you
   are creating. By using branches, it is possible to create a collection of the
   same lesson customized for different audiences which can be easily re-used
   in the future in the workshop template.

3. You need to edit several variables in `_config.yml` for the lesson to render
   correctly.

4. Create the lesson data. If you are unfamiliar with the format, please refer
   to the tutorial on [creating lessons](https://carpentries.github.io/lesson-example/).

# OpenRefine Lesson
This is a lesson on OpenRefine data cleaning tool derived from [the Data Carpentry's Data Refine for Ecology](https://github.com/datacarpentry/OpenRefine-ecology-lesson/).

### Dataset
* The data used in this lesson ata set is derived from [The Portal Project Long-term desert ecology](http://portal.weecology.org/) project data. [This data file](http://www.esapubs.org/archive/ecol/E090/118/Portal_rodents_19772002.csv) was downloaded and then modified specifically for use with OpenRefine.
    * Taxon names were put back into the file.
    * Globally Unique Identifiers (in the form of UUIDs) were added.
* These modifications were made in order to illustrate some features of Open Refine.
    - Errors were added to the taxon names (`scientificName` field), to demonstrate OpenRefine's ability to find likely mis-entered data.
    - These errors can be found using clustering algorithms on the `scientificName` column, showing the power of the algorithms to find discrepancies quickly and making it simple to fix all issues found.

## Maintainer(s)

Current maintainers of this lesson are:

* [Aleksandra Nenadic](https://github.com/anenadic)
* [Simon Hettrick](https://github.com/SimonHettrick)

## Authors

A list of contributors to the lesson can be found in [AUTHORS](AUTHORS).

## Citation

## Files to update/create

You should only need to update the following files:

1. `index.md`
2. `setup.md`
3. `reference.md`
4. `_includes/rsg/schedule.html`
5. Lesson markdown files in `_episodes`/`_episode_rmd`
6. Lesson extras in `_extras`
7. `_config.yml`

## Layout

The layout of lessons is nominally explained [here]
(https://carpentries.github.io/lesson-example/03-organization/index.html). But,
in brief:

1.  The source for pages that appear as top-level items in the navigation bar
    are stored in the root directory, including the home page (`index.md`),
    the reference page (`reference.md`), and the setup instructions
    (`setup.md`).

2.  Source files for lesson episodes are stored in `_episodes`. As a standalone
    lesson, `01-introduction.md` would generate `/01-introduction/index.html`.
    As part of the workshop template, the generated page is instead generated
    to the slug of the markdown file.

3.  If you are writing lessons in R Markdown, source files go in
    `_episodes_rmd`. You must run `make lesson-rmd` to turn these into Markdown
    in `_episodes` and commit those Markdown files to the repository
    (since GitHub won't run anything except Jekyll to format material).
    You must also commit any figures generated from your lessons,
    which are stored in the `fig` directory.

5.  Files that appear under the "extras" menu in the lesson navigation bar are
    stored in `_extras`.

6.  Figures are stored in the `fig` directory, data sets in `data`,
    source code in `code`, and miscellaneous files in `files`.


