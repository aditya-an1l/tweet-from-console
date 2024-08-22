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


def log_error(error_message):
    """logs the error message in a file"""

    console.log(error_message)
    console.print(
        " \n \n [magenta]=== Complete Error Log === [/magenta] ", justify="center"
    )
    logger.error(error_message)
    console.print(
        f"\n Log History stored in [cyan]error.txt[/cyan] in [cyan]{log_directory}[/cyan] \n",
        justify="center",
    )


def tweet_confirmation_alert(tweet, tweet_log=False):
    """Returns the just sent tweet in console"""

    confirmation_text = f'The tweet [cyan]{tweet}[/cyan] posted at {datetime.now().strftime("%H:%M:%S %Y-%m-%d")}'
    console.print(confirmation_text)
    if tweet_log:
        with open("".join(log_directory + "/tweet_history.txt"), "a") as file:
            message = f'\n({datetime.now().strftime("%H:%M:%S %Y-%m-%d")}) {tweet}'
            file.write(message)
            pass


def check_api_keys(keys):
    """check if API keys are missing"""

    missing_keys = [key for key, value in keys.items() if not value]
    if missing_keys:
        error_message = f" [red] Missing Keys: {', '.join(missing_keys)} [/red]. Try checking the .env file in {log_directory}"
        log_error(error_message)
        raise ValueError(error_message)


def send_tweet(tweet):
    """Send the Tweet"""

    tweet = tweet
    console.print(f'You sure you want to post "[cyan]{tweet}[/cyan]" ?  ')
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
        print("[red]Invalid Input [/red]")
        send_tweet(tweet)


def authentication():
    """Assign and authenticate key"""
    try:
        consumer_key = os.getenv("CONSUMER_KEY")
        consumer_secret = os.getenv("CONSUMER_SECRET")
        access_token = os.getenv("ACCESS_TOKEN")
        access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

        check_api_keys(
            {
                "CONSUMER_KEY": consumer_key,
                "CONSUMER_SECRET": consumer_secret,
                "ACCESS_TOKEN": access_token,
                "ACCESS_TOKEN_SECRET": access_token_secret,
            }
        )
    except ValueError:
        sys.exit(1)

    # Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
