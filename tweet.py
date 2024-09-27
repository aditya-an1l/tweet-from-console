"""
Tweet-from-console

URL: https://github.com/aditya-an1l/Tweet-from-console
Author: aditya-an1l (https://github.com/aditya-an1l)
Email: aditya.anil.productions@gmail.com

Licence: Apache 2.0 Licence
Version: v1.2.1
Release Name: Text and Metadata Version

In order to run the program, follow the README.md and enter your
Twitter API Key in a dot env file under scripts directory (instructions
given in readme)

To run the program, open your terminal in the current directory and execute

$ python tweet.py "<insert_your_tweet_here>"

For multiline tweet, just execute

$ python tweet.py

Execute the following to get information about other advances options

$ python tweet.py -h

"""

import re

import sys
import os
from typing import Dict, Any, Union
import requests

import scripts.main as main
from rich import color, print
from rich.console import Console
from rich.table import Table
from scripts.github_release import GitHub_Release
import argparse

console = Console()

script_path = os.path.abspath(__file__)
cwd = os.path.dirname(script_path)
log_directory = os.path.abspath(os.path.join(cwd, "logs"))


def info() -> Dict[str, list[Any] | Any]:
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
        help="Write the Tweet that needs to be sent",
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


def get_latest_release() -> Union[Dict[str, str], str]:
    """Get release info from GitHub API"""
    response = requests.get(
        "https://api.github.com/repos/aditya-an1l/Tweet-from-console/releases/latest"
    )
    if response.status_code == 200:
        latest_release = response.json()
        required_info = {
            "name": str(latest_release["name"])[6:],
            "version": latest_release["tag_name"],
            "publish_date": latest_release["published_at"],
        }
    else:
        required_info = f"Failed to retrieve releases: {response.status_code}"
    return required_info


def version_checker() -> Dict[str, str | bool]:
    """Compares the latest version with current version"""
    current_version = info()["Version"]
    url = info()["URL"]
    latest_release = get_latest_release()
    isMismatched = False

    if isinstance(latest_release, dict):
        latest_version = str(latest_release["version"])[1:]
        if latest_version != current_version:
            verdict = f"Your current version of Tweet-from-console ([red]{current_version}[/red]) is not upto date with latest release ([green]{latest_version}[/green]). Visit [green]{url}/releases/latest[/green] to download the latest release version. \n"
            isMismatched = True
        else:
            verdict = f"Upto date. Using latest version {latest_version}"
            isMismatched = False
        final_verdict = {"status_message": verdict, "isMismatched": isMismatched}
    else:
        return {
            "status_message": "Couldn't connect with API. Check your interenet connection..",
            "isMismatched": False,
        }

    return final_verdict


def textbox_response(
    prompt="\nEnter your text (type ':q' on a new line to finish, ':e' to Cancel):\n",
) -> str:
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip().lower() == ":q":
            break
        elif line.strip().lower() == ":e":
            print("Exiting...")
            sys.exit(1)
        lines.append(line)
    return "\n".join(lines)


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
    version_check = version_checker()
    number_of_args = len(sys.argv)
    skip_confirmation = True if "--" in sys.argv else False

    if version_check["isMismatched"]:
        print(version_check["status_message"])
    if (number_of_args == 1) or (number_of_args == 2 and skip_confirmation):
        tweet_box_input = textbox_response()
        print(tweet_box_input)
        main.send_tweet(tweet_box_input, skip_confirmation)
    if args.tweet:
        tweet_inline = args.tweet
        main.send_tweet(tweet_inline.replace("\\n", "\n"), skip_confirmation)

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
