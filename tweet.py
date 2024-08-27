"""
Tweet-from-console

URL: https://github.com/aditya-an1l/Tweet-from-console
Author: aditya-an1l (https://github.com/aditya-an1l)
Version: v1.1.1
Release Name: Argument Support Version
Licence: Apache 2.0 Licence

In order to run the program, follow the README.md and enter your
Twitter API Key in a dot env file under scripts directory (instructions
given in readme)

To run the program, open your terminal in the current directory and execute

$ python tweet.py "<insert_your_tweet_here>"

Execute the following to get information about other advances options

$ python tweet.py -h

"""

import sys
import os
from typing import Dict

import scripts.main as main
from rich import print
from rich.console import Console
from rich.table import Table
from scripts.github_release import GitHub_Release
import argparse

console = Console()

script_path = os.path.abspath(__file__)
cwd = os.path.dirname(script_path)
log_directory = os.path.abspath(os.path.join(cwd, "logs"))


def info() -> Dict[str, str]:
    """Returns dictionary about metadata"""
    info = GitHub_Release()

    VERSION = info.get("version")
    RELEASE_TITLE = info.get("release title")
    URL = info.get("url")
    AUTHOR_NAME = info.get("author", "name")
    AUTHOR_EMAIL = info.get("author", "email")
    AUTHOR_URL = info.get("author", "url")

    info_dict = {
        "Version": VERSION,
        "Release Title": RELEASE_TITLE,
        "URL": URL,
        "Author Name": AUTHOR_NAME,
        "Author Email": AUTHOR_EMAIL,
        "Author URL": AUTHOR_URL,
    }
    return info_dict


def info_table() -> None:
    """Prints the metadata in a table form"""
    console = Console()
    data = info()
    table = Table(title="Tweet From Console")
    table.add_column("Info", style="cyan", no_wrap=True)
    table.add_column("Value", style="yellow")

    for key, value in data.items():
        table.add_row(str(key), str(value))

    console.print(table)


def arguments_parser() -> argparse.Namespace:
    """Parses the CMD arguments"""
    parser = argparse.ArgumentParser(
        description="Send Tweets directly from the console and terminal."
    )
    parser.add_argument(
        "tweet",
        help='Write the Tweet that needs to be sent. Enclose it within " ". Use " \\n " to have multiline tweets.',
        nargs="?",
        type=str,
    )
    parser.add_argument(
        "-a",
        "--all",
        help="Show error logs and tweet history logs",
        const=500,
        nargs="?",
    )

    parser.add_argument(
        "-y",
        "--",
        help="Directly send the tweet without confirmation",
        action="store_true",
        dest="skip_confirmation",
    )
    parser.add_argument("-e", "--error", help="Show error logs", const=500, nargs="?")

    parser.add_argument(
        "-th", "--tweethistory", help="Show tweet history", const=500, nargs="?"
    )

    parser.add_argument("-v", "--version", help="Show version", action="store_true")
    args = parser.parse_args()

    return args


def read_log(type, items) -> None:
    """Prints the log messages to the console"""
    file_name = type.replace(" ", "_")
    items = items
    with open(f"logs/{file_name}.txt") as f:
        content_list = f.readlines()
        items_excluding_title = items + 2
        content_output = content_list[2:items_excluding_title]

        console.print(
            f" \n === [green]{type.capitalize()} Logs[/green] [{len(content_output)} Results ] == ",
            justify="center",
        )
        for x in content_output:
            print(f"{x}")
        console.print(
            f"\n Retrieved from Log History stored in [cyan]{type}.txt[/cyan] at [cyan]{log_directory}[/cyan] \n",
            justify="center",
        )


if __name__ == "__main__":
    args = arguments_parser()
    skip_confirmation = False

    if args.tweet:
        if "--" in sys.argv or args.skip_confirmation:
            skip_confirmation = True
        main.send_tweet(args.tweet, skip_confirmation)

    if args.all:
        items = args.all
        read_log("error", int(items))
        console.print("[cyan]-[/cyan]" * 50, justify="center")
        read_log("tweet history", int(items))

    if args.version:
        info_table()

    if args.error is not None:
        items = args.error
        read_log("error", int(items))

    if args.tweethistory is not None:
        items = args.tweethistory
        read_log("tweet history", int(items))
