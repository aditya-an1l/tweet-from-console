from datetime import datetime
import tweepy
from rich import print
from rich.console import Console
from rich.logging import RichHandler
import logging
import os
import sys
from dotenv import load_dotenv

script_path = os.path.abspath(__file__)
cwd = os.path.dirname(script_path)
log_directory = os.path.abspath(os.path.join(cwd, "..", "logs"))
logger = logging.getLogger("ErrorLogging")

console = Console()

try:
    load_dotenv()
except FileNotFoundError:
    print("Error: .env file not found.")
except (SyntaxError, UnicodeDecodeError):
    print("Error: Invalid syntax or encoding in .env file.")


logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        RichHandler(rich_tracebacks=True, tracebacks_show_locals=True, console=console),
        logging.FileHandler("".join(log_directory + "/error.txt")),
    ],
)


def log_error(error_message) -> None:
    """logs the error message in a file"""

    console.log(error_message)
    console.print(
        " \n \n [magenta]=== Complete Error Log === [/magenta] ", justify="center"
    )
    logger.error(error_message)
    console.print(
        f"\n Log History stored in [cyan]error.txt[/cyan] at [cyan]{log_directory}[/cyan] \n",
        justify="center",
    )


def tweet_confirmation_alert(tweet, tweet_log=False) -> None:
    """Returns the just sent tweet in console"""

    confirmation_text = f"The tweet [cyan]{tweet}[/cyan] posted at {datetime.now().strftime('%H:%M:%S %Y-%m-%d')}"
    console.print(confirmation_text)
    if tweet_log:
        with open("".join(log_directory + "/tweet_history.txt"), "a") as file:
            message = (
                f"\n({datetime.now().strftime('%H:%M:%S %Y-%m-%d')}) {tweet} \n ------"
            )
            file.write(message)
            pass
        console.print(
            f"\n Tweet History stored in [cyan]tweet_history.txt[/cyan] at [cyan]{log_directory}[/cyan] \n",
            justify="center",
        )


def check_api_keys(keys) -> None:
    """check if API keys are missing"""

    missing_keys = [key for key, value in keys.items() if not value]
    if missing_keys:
        error_message = f" [red] Missing Keys: {', '.join(missing_keys)} [/red]. Try checking the .env file in {log_directory}"
        log_error(error_message)
        raise ValueError(error_message)


def authentication(tweet) -> tweepy.Client:
    """Assign and authenticate key"""
    if not tweet.strip():
        console.print(
            "[red]ERROR: Tweet cannot be empty. It needs texts. Try again...[/red] \n Exiting..."
        )
        sys.exit(1)

    try:
        consumer_key = os.getenv("TWITTER_API_KEY")
        consumer_secret = os.getenv("TWITTER_API_SECRET_KEY")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

        check_api_keys(
            {
                "CONSUMER_KEY": consumer_key,
                "CONSUMER_SECRET": consumer_secret,
                "ACCESS_TOKEN": access_token,
                "ACCESS_TOKEN_SECRET": access_token_secret,
            }
        )
    except ValueError:
        print("ERROR: Value error")
        sys.exit(1)

    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    return client


def send_tweet(tweet, skip_confirmation=False, max_limit=280) -> None:
    """Send the Tweet"""
    client = authentication(tweet)
    characters = len(tweet)
    if characters > max_limit:
        console.print(
            f"[red]Character limit passed:[red] You tweet has {characters} characters (max limit is {max_limit})"
        )
        console.print("Exiting...")
        sys.exit(1)
    if skip_confirmation and characters <= max_limit:
        client.create_tweet(text=tweet)
        tweet_confirmation_alert(tweet, tweet_log=True)
    elif not skip_confirmation and characters <= max_limit:
        console.print(
            f"You sure you want to post : [cyan]{tweet}[/cyan] ?  \n [ characters used: {characters}/ 280 ]"
        )
        console.print("[green] [ (Y)es / (N)o ] : [/green] ")
        confirmation = input("Type Here: ")
        if confirmation.strip() in ("Y", "y", "yes", "YES", "Yes"):
            client.create_tweet(text=tweet)
            tweet_confirmation_alert(tweet, tweet_log=True)
            sys.exit(1)
        elif confirmation.strip() in ("N", "n", "no", "NO", "No"):
            print("Exiting...")
            sys.exit(1)
        else:
            print("\n [red]Invalid Input [/red] \n")
