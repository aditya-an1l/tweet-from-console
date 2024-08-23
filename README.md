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
<h2><b> 🐦 Send tweets right from your terminal! No browser needed!</b></h2>
</div>


Tweet from Console is a Python-based command-line tool that lets you tweet directly from your console, command prompt, or terminal. Say goodbye to distracting web interfaces.

Good for programmers and devs who wants to send a tweets without leaving their console.

## 🎞️ Preview

![Preview-GIF](https://github.com/aditya-an1l/tweet-from-console/blob/main/media/Walkthrough.gif)

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
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Twitter API credentials:
   - Rename `scripts/.env.example` to `scripts/.env`
   - Open `scripts/.env` and fill in your Twitter API credentials

## ⚙️ Configuration

Ensure your `scripts/.env` file contains these Twitter API credentials:

```
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET_KEY=your_api_secret_key
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
```

## 🎮 Usage

To send a tweet, run this command from the project root:

```bash
python tweet.py "Your awesome tweet goes here! "
```

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request and join our tweeting revolution! 🌟

## ⚠️ Disclaimer

This tool is for educational purposes only. Always comply with Twitter's terms of service and API usage guidelines. Tweet responsibly
