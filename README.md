## This is a feature branch. Go here for the main readme : https://github.com/aditya-an1l/tweet-from-console/

<div align="center">
  <img src="https://raw.githubusercontent.com/aditya-an1l/tweet-from-console/main/media/Logo.jfif" width="200" height="200" alt="Logo">
<h1><b>Tweet - From - Console</b></h1>
</div>

<div align="center"><p>
    <a href="https://github.com/aditya-an1l/tweet-from-console/releases/latest">
      <img alt="Latest release" src="https://img.shields.io/github/v/release/aditya-an1l/tweet-from-console?style=for-the-badge&logo=github&color=1DA1F2&logoColor=FFFFFF&labelColor=000000&include_prerelease&sort=semver" />
    </a>
    <a href="https://github.com/aditya-an1l/tweet-from-console/pulse">
      <img alt="Last commit" src="https://img.shields.io/github/last-commit/aditya-an1l/tweet-from-console?style=for-the-badge&logo=git&color=1DA1F2&logoColor=FFFFFF&labelColor=000000"/>
    </a>
    <a href="https://github.com/aditya-an1l/tweet-from-console/blob/main/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/aditya-an1l/tweet-from-console?style=for-the-badge&logo=apache&color=FF4136&logoColor=FFFFFF&labelColor=000000" />
    </a>
    <a href="https://github.com/aditya-an1l/tweet-from-console/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/aditya-an1l/tweet-from-console?style=for-the-badge&logo=starship&color=1DA1F2&logoColor=FFFFFF&labelColor=000000" />
    </a>
    <a href="https://github.com/aditya-an1l/tweet-from-console/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/aditya-an1l/tweet-from-console?style=for-the-badge&logo=gitbook&color=FF4136&logoColor=FFFFFF&labelColor=000000" />
    </a>
    <a href="https://github.com/aditya-an1l/tweet-from-console">
      <img alt="Repo Size" src="https://img.shields.io/github/repo-size/aditya-an1l/tweet-from-console?color=1DA1F2&label=SIZE&logo=files&style=for-the-badge&logoColor=FFFFFF&labelColor=000000" />
    </a>
    <a href="https://twitter.com/intent/follow?screen_name=its_aditya_an1l">
      <img alt="follow on X" src="https://img.shields.io/twitter/follow/its_aditya_an1l?style=for-the-badge&logo=x&color=1DA1F2&logoColor=FFFFFF&labelColor=000000" />
    </a>
</div>
<br> 
<div align="center">
<h2><b> 🐦 Send tweets right from your terminal. No browser needed!</b></h2>
</div>

Tweet from Console is a Python-based command-line tool that lets you tweet directly from your console, command prompt, or terminal. Say goodbye to distracting web interfaces.

Good for programmers and devs who wants to send a tweets without leaving their console.

## 🎞️ Preview

![Preview-GIF](https://github.com/aditya-an1l/tweet-from-console/blob/main/media/Walkthrough.gif)

<details>
<summary><h2>TOC</h2></summary>

- [🎞️ Preview](#-preview)
- [✨ Features](#-features)
- [🛠️ Prerequisites](#-prerequisites)
- [🚀 Installation](#-installation)
- [⚙️ Configuration](#-configuration)
  - [How to get the API keys?](#how-to-get-the-api-keys)
- [🎮 Usage](#-usage)
  - [1. Tweet with Confirmation Message ✅](#1-tweet-with-confirmation-message-)
  - [2. Tweet without Confirmation Message ❎](#2-tweet-without-confirmation-message-)
  - [3. View Tweet History 📄](#3-view-tweet-history-)
  - [4. View Error Logs 📃](#4-view-error-logs-)
- [🤝 Contributing](#-contributing)
- [⚠️ Disclaimer](#-disclaimer)

</details>

## ✨ Features

- 📝 Send text-based tweets from the command line
- ⏲️ Fast, simple and straight-forward
- 🔑 Secure integration with Twitter API

## 🛠️ Prerequisites

- 🐍 Python 3.6 or higher
- 🐦 Twitter Developer Account and API keys

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tweet-from-console.git
   cd tweet-from-console
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Script\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Twitter API credentials:
   - Rename `scripts/.env.example` to `scripts/.env`
   - Open `scripts/.env` and fill in your Twitter API credentials

### ⚙️ API key configuration guide

Ensure your `scripts/.env` file contains these Twitter API credentials:

```
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET_KEY=your_api_secret_key
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
```

#### How to get the API keys?

Following guides would help you get the API keys from _Twitter/X Developers Platform_

- Official Docs : https://developer.x.com/en/docs/authentication/oauth-1-0a/api-key-and-secret
- TintUP Documentation : https://support.tintup.com/hc/en-us/articles/16130285332371-How-to-setup-the-X-API-Key#h_01GZ16761H8YH0M8680FH7KYS0
  - Just follow till the "_How to setup the X Integration with TINT_" part

You would need the following credentials in your `.env` file

- API Key
- API Secret Key
- Access Token
- Access Token Secret

## 🎮 Usage

### 1. Tweet with Confirmation Message ✅

To send a tweet, run this command from the project root:

```bash
python tweet.py "Your awesome tweet goes here! "
```

This will give you a confirmation message like the following:

```
You sure you want to post "Your awesome tweet goes here!" ?
 [ (Y)es / (N)o ] :

Type Here:
```

And based on your choice the scripts send your tweet.

### 2. Tweet without Confirmation Message ❎

If you want to send the tweet without confirmation, add `--` (or `-y`) as an argument.

```bash
python tweet.py "Your awesome tweet goes here! " --
```

This would not ask the confirmation message. It directly post your tweet.

### 3. View Tweet History 📄

You can now view the tweet history with the following command:

```bash
python tweet.py -th <num>
```

or

```bash
python tweet.py --tweethistory <num>
```

Where `<num>` is the number of recent items to display. For example, if we want to see the recent 5 tweets sent using the script, we can run `python tweet.py -th 5` (or `python tweet.py -tweethistory 5` ). If no `<num>` is mentioned, the script will retrieve first 500 tweet history and display on the screen.

The error logs are located at `logs/tweet_history.txt` inside the repo

### 4. View Error Logs 📃

Since this is a CLI tools, there is always a possiblity for errors depending on the client environment.

Therefore, the errors (if any) faced by this application is automatically logged in your local machine.

To view it, run:

```bash
python tweet.py -e <num>
```

or

```bash
python tweet.py --error <num>
```

Where `<num>` is the number of recent items to display. For example, if we want to see the recent 5 error messages, we can run `python tweet.py -e 5` (or `python tweet.py --error 5` ). If no `<num>` is mentioned, the script will retrieve first 500 error logs and display on the screen.

The error logs are located at `logs/error.txt` inside the repo

### 4. (Misc) View All Logs 📃

You can view both the above logs at the same time using the following commands:

```bash
python tweet.py -a <num>
```

or

```bash
python tweet.py --all <num>
```

The error logs are located at `logs/error.txt` inside the repo

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request and join our tweeting revolution! 🌟

## ⚠️ Disclaimer

This tool is for educational purposes only. Always comply with Twitter's terms of service and API usage guidelines. Tweet responsibly
