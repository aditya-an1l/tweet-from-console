# 🐦 Tweet from Console
> v0.1.0 Text version

## 💡 Send tweets right from your terminal! No browser needed!



Tweet from Console is a Python-based command-line tool that lets you tweet directly from your console, command prompt, or terminal. Say goodbye to distracting web interfaces. 

Good for programmers and devs who wants to send a tweets without leaving their console. 


## ✨ Features

- 📝 Send text-based tweets from the command line
- ⏲️  Fast, simple and straight-forward
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
python scripts/main.py "Your awesome tweet goes here! "
```

>NOTE: Better code execution mechanism under development 🚩

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request and join our tweeting revolution! 🌟

## ⚠️ Disclaimer

This tool is for educational purposes only. Always comply with Twitter's terms of service and API usage guidelines. Tweet responsibly
