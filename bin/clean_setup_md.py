"""Clean up the setup.md files for better visual consistency.

"""

import re
import yaml
from enum import Enum
from dateutil import parser

class LessonType(Enum):
    """Enum for the different types of lessons.
    """
    markdown = "episode"
    r_markdown = "episode_r"


def get_yaml_config():
    """Open the YAML config file for the website.

    Returns
    -------
    config: dict
        The configuration for the website.
    """

    with open("_config.yml", "r") as fp:
        config = yaml.load(fp, yaml.Loader)

    return config


def get_file_and_head(filename, n_head=5):
    """Get the contents of a file, and the head.

    Parameters
    ----------
    filename: str
        The name of the file to read.
    n_head: int
        The number of lines to include in the head.
    """
    with open(filename, "r") as fp:
        content = fp.read()
        fp.seek(0)
        try:
            head = [next(fp) for _ in range(n_head)]
        except StopIteration:
            head = []

    return content, head


def main():
    """Main function of the script.

    For each lesson, the setup.md file is read in, cleaned up and then added to
    setup_md_string. This string is then written to a file named setup.md in
    the root directory, which is included in _includes/rsg/setup.html.
    """
    website_config = get_yaml_config()
    lessons = website_config.get("lessons", None)

    if website_config.get("kind") == "workshop":
        if not lessons:
            raise ValueError("There are no lessons specified in _config.yml")

        for lesson in lessons:
            date = lesson["date"]
            if isinstance(date, list):
                date = date[0]
            lesson["date"] = parser.parse(date)

        sorted_lessons = sorted(lessons, key=lambda x: x["date"])
    elif website_config.get("kind") == "course":
        sorted_lessons = sorted(lessons, key=lambda x: x["order"])

    setup_md_string = """
## Setup

### Text Editor

A text editor is the piece of software you use to view and write code. If you
have a preferred text editor, please use it. Suggestions for text editors are,
Notepad++ (Windows), TextEdit (macOS), Gedit (GNU/Linux), GNU Nano, Vim.
Alternatively, there are IDE's (integrated developer environments) that have
more features specifically for coding such as VS Code; there are also IDEs
specific to languages will be listed in the appropriate section(s) below.
"""

    for lesson in sorted_lessons:

        filename = f"_includes/rsg/{lesson['gh-name']}-lesson/setup.md"
        content, head = get_file_and_head(filename)
        content = content.splitlines()

        # First, remove the front matter from the setup.md file

        if re.findall("---", "\n".join(head)):
            nfound = 0
            for i, line in enumerate(content):
                if line.startswith("---"):
                    nfound += 1
                if nfound == 2:
                    break
            content = content[i+1:]

        # Next, change the depth of the headings

        for i, line in enumerate(content):
            if line.startswith("#"):
                line = line.rstrip("#")
                nhashes = line.count("#") + 2
                if nhashes > 5:
                    nhashes = 5
                line = "#" * nhashes + line.lstrip("#")
                content[i] = line

        setup_md_string += "\n### '{}'\n\n{}\n".format(lesson["title"], "\n".join(content))

    # write out the new setup.md file to the root directory

    with open("setup.md", "w") as fp:
        fp.write(setup_md_string)


if __name__ == "__main__":
    main()