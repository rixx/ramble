import datetime as dt
import os
import re
import subprocess
from pathlib import Path

import click

import frontmatter
import inquirer
from unidecode import unidecode

BASE_PATH = Path("_posts")


def slugify(text):
    """Convert Unicode string into blog slug."""
    # https://leancrew.com/all-this/2014/10/asciifying/
    text = re.sub("[–—/:;,.]", "-", text)  # replace separating punctuation
    ascii_text = unidecode(text).lower()  # best ASCII substitutions, lowercased
    ascii_text = re.sub(r"[^a-z0-9 -]", "", ascii_text)  # delete any other characters
    ascii_text = ascii_text.replace(" ", "-")  # spaces to hyphens
    ascii_text = re.sub(r"-+", "-", ascii_text)  # condense repeated hyphens
    return ascii_text


class Post:
    def __init__(self, path=None, title=None, metadata=None):
        if path:
            data = frontmatter.load(path)
            self.metadata = data.metadata
            self.content = data.content
            self.path = path
            self.title = self.metadata.get("title")
            if not self.title:
                path_parts = self.path.name.split("-")
                self.title = " ".join(part.capitalize() for part in path_parts[3:])
        else:
            self.title = title
            self.metadata = metadata
            datefmt = self.metadata["date"].strftime("%Y-%m-%d")
            self.path = BASE_PATH / f"{datefmt}-{slugify(self.title)}.md"
            with open(self.path, "wb") as fp:
                frontmatter.dump(frontmatter.Post(content="\n", **self.metadata), fp)

    def edit(self):
        subprocess.check_call([os.environ.get("EDITOR", "vim"), self.path])


def load_posts():
    result = []
    for path in BASE_PATH.glob("*.md"):
        result.append(Post(path=path))
    return result


def edit_post():
    posts = load_posts()
    post_choice = inquirer.list_input(
        message="Which post?",
        choices=[(post.title, post) for post in posts],
        carousel=True,
    )
    post_choice.edit()
    subprocess.check_call(["git", "add", post_choice.path])


def create_post():
    questions = [
        inquirer.Text("title", message="What’s the title of the post?"),
        inquirer.List(
            "date",
            message="When do you want to publish it?",
            choices=[("yesterday", -1), ("today", 0), ("tomorrow", 1)],
            carousel=True,
        ),
        inquirer.List(
            "refutes",
            message="Does this post refute another post?",
            choices=[("Yes", True), ("No", False)],
            default=False,
            carousel=True,
        ),
    ]
    answers = inquirer.prompt(questions)
    date = dt.datetime.now() + dt.timedelta(days=answers["date"])
    metadata = {
        "layout": "post",
        "title": answers["title"],
        "date": date.strftime("%Y-%m-%d"),
        "summary": "",
    }
    if answers["refutes"]:
        posts = load_posts()
        post_choice = inquirer.list_input(
            message="Which post?",
            choices=[(post.title, post) for post in posts],
            carousel=True,
        )
        metadata["refutes"] = post_choice.path.name[len("yyyy-mm-dd-") : -3]

    post = Post(title=answers["title"], metadata=metadata)
    post.edit()
    subprocess.check_call(["git", "add", post.path])


@click.group()
@click.version_option()
def cli():
    "Interact with ramble.rixx.de"


@cli.command()
def new():
    """ Add a new post """
    create_post()


@cli.command()
def add():
    """ Add a new post """
    create_post()


@cli.command()
def edit():
    """ Edit a post """
    edit_post()