#!/usr/bin/env python3
"""
Tweet-from-console

URL: https://github.com/aditya-an1l/Tweet-from-console
Author: aditya-an1l (https://github.com/aditya-an1l)
Version: v0.1.0 (Pre-Release) Text Version

In order to run the program, follow the README.md and create enter your
Twitter API Key in a dot env file under scripts directory (instructions
given in readme)

To run the program, open your terminal in the current directory and execute

$ python tweet.py "<insert_your_tweet_here>"

"""

import sys

sys.path.append("/scripts")
from scripts import main
import tweepy


def send_tweet():
    try:
        tweet = sys.argv[1]
    except IndexError:
        main.log_error(
            'Error: No tweet text provided. Make sure the command is in the following format: \n \n $ python tweet.py "tweet goes there"  '
        )
        sys.exit(1)
    except TypeError:
        main.log_error(
            'Error: The tweet must be a string. Try enclosing it with quotations (" ")'
        )
        sys.exit(1)
    except ValueError as ve:
        main.log_error(f"Error: {ve}")
        sys.exit(1)

    main.send_tweet(tweet, sys.argv)


if __name__ == "__main__":
    send_tweet()
