<div align="center">
  <img src="https://raw.githubusercontent.com/aditya-an1l/tweet-from-console/main/media/Logo.jfif" width="200" height="200" alt="Logo">
  <h1><b><i>Tweet - From - Console</i> </b></h1>
</div>

<div align="center">
  <h2><b> 🐦 Send X / Tweets right from your terminal 🐦</b></h2>
</div>
<div align="center">
  <p>
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
    <a href="https://twitter.com/intent/follow?screen_name=aditya_an1l">
      <img alt="follow on X" src="https://img.shields.io/twitter/follow/aditya_an1l?style=for-the-badge&logo=x&color=1DA1F2&logoColor=FFFFFF&labelColor=000000" />
    </a>
  </p>
</div>

<br>

<p>Tweet from Console is a Python-based command-line tool that lets you tweet directly from your terminal. Say goodbye to distracting web interfaces.</p>

<p>Good for programmers and devs who want to send tweets without leaving their console.</p>

**_Happy Distraction Free Tweeting 🧑‍💻_**

<br>

<h2 id="preview">🎞️ Preview</h2>
<h3 id="tweet-confirmation">1. Tweet with Confirmation Message 🔔</h3>

<img src="https://github.com/aditya-an1l/tweet-from-console/blob/main/media/normal.gif" alt="without confirmation">

<pre><code>python tweet.py "Your awesome tweet goes here!"</code></pre>
<p>This will give you a confirmation message like the following:</p>
<pre><code>You sure you want to post "Your awesome tweet goes here!" ?
[ (Y)es / (N)o ] :
Type Here:</code></pre>

<h3 id="tweet-confirmation">2. Tweet with Image (NEW) 🔔</h3>

<img src="https://github.com/aditya-an1l/tweet-from-console/blob/main/media/image.gif" alt="with image">

Images can now be posted on X/Twitter straight from your clipboard. For this, use `-c` flag.

<pre><code>python tweet.py "Your awesome tweet goes here!" -c</code></pre>

<p>This will give you a confirmation message like the following:</p>
<pre><code>You sure you want to post :
----
Your awesome tweet goes here!
<br>

[Image from Clipboard]
characters used: [4/ 280]
\----
[ (Y)es / (N)o ] :  
Type Here: </code></pre>

The images would be stored in the `/user_media/` directory.

<h3 id="tweet-no-confirmation">3. Tweet without Confirmation Message ⏩ </h3>

<img src="https://github.com/aditya-an1l/tweet-from-console/blob/main/media/without conf.gif" alt="without confirmation">

<pre><code>python tweet.py "Your awesome tweet goes here!" --</code></pre>
<p>This would not ask for a confirmation message. It directly posts your tweet.</p>

<h3 id="view-tweet-history">4. View Tweet History 📝</h3>

<img src="https://github.com/aditya-an1l/tweet-from-console/blob/main/media/th.gif" alt="tweet history">

<pre><code>python tweet.py -th <num>
python tweet.py --tweethistory <num></code></pre>

<h3 id="multiline-tweets">5. Multi Line Tweet 📜 </h3>

<img src="https://github.com/aditya-an1l/tweet-from-console/blob/main/media/mullti.gif" alt="multiline">

<pre><code>python tweet.py</code></pre>
<p>Running this simple code would allow users to send multiline tweets. This is helpful since consoles are usually limited to inline inputs.</p>

<p>After writing the tweet, go to new line and then type <code>:q</code> to exit.</p>

<p> <b>Note:</b> If you want to skip the confirmation message, just like <a href="#tweet-confirmation">Usage 1</a>, execute <code>python tweet.py --</code> </p>

<p> <b>Note:</b> You can execute multiline tweets in a single line using the <code>\n</code>. The following is an example: </p>

<img src="https://github.com/aditya-an1l/tweet-from-console/blob/main/media/inline multiline.gif" alt="inline multiline">

<pre><code>python tweet.py "Line 1 \nLine 2"</code></pre>

Here is the format of the tweet that would be posted:

<pre><code>Line 1
Line 2  
</code></pre>

<h3 id="view-error-logs">6. View Error Logs ⚠️ </h3>
<pre><code>python tweet.py -e <num>
python tweet.py --error <num></code></pre>

<h2 id="features">✨ Features</h2>
<ul>
  <li>📝 Send text-based tweets from the command line</li>
  <li>⏲️ Fast, simple and straight-forward</li>
  <li>🔑 Secure integration with Twitter API</li>
<li>🖼️ Image upload option from Clipboard</li>
</ul>

<h2 id="prerequisites">🛠️ Prerequisites</h2>
<ul>
  <li>🐍 Python 3.6 or higher</li>
  <li>🐦 Twitter Developer Account and API keys</li>
</ul>

<h2 id="installation">🚀 Installation</h2>
<ol>
  <li>Clone the repository:</li>

  <pre><code>git clone https://github.com/yourusername/tweet-from-console.git
cd tweet-from-console
  </code></pre>

  <li>Create and activate a virtual environment:</li>
  <pre><code>python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Script\activate`
  </code></pre>

  <li>Install the required dependencies:</li>
  <pre><code>pip install -r requirements.txt</code></pre>

  <li>Set up your Twitter API credentials:
    <ul>
      <li>Rename <code>scripts/.env.example</code> to <code>scripts/.env</code></li>
      <li>Open <code>scripts/.env</code> and fill in your Twitter API credentials</li>
    </ul>
  </li>
</ol>

5. (Optional but Highly Recommended) Create aliases for quick access of `tweet.py`

i. **Bash**

Add this line to `~/.bashrc`:

`alias  tw='python /path/to/tweet.py'`

- Reload with: `source ~/.bashrc`
- Usage: `tw [arguments]`
  ii. **Zsh**

Insert the same line in `~/.zshrc`:

`alias tw='python /path/to/tweet.py'`

- Reload with: `source ~/.zshrc`
- Usage: `tw [arguments]`

3. **Fish**

Add this line to `~/.config/fish/config.fish`:

`alias tw='python /path/to/tweet.py'`

- To persist, use: `alias --save tw='python /path/to/tweet.py'`
- Or, create a function for full argument support:

  `function tw
    python /path/to/tweet.py $argv
end
funcsave tw`

- Usage: `tw [arguments]`

4. **PowerShell**

Define a function in your profile (`$PROFILE`, usually at `Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`):

`function tw { python C:\path\to\tweet.py @args }`

- Reload profile or restart PowerShell.
- Usage: `tw [arguments]`jdatascientist

#### Additional Notes

- Replace `/path/to/tweet.py` (Linux/macOS) or `C:\path\to\tweet.py` (Windows) with the actual script path.
- These methods support command-line arguments and work for most CLI Python apps
- Aliases only persist after reloading the config file or opening a new terminal session

<h2 id="configuration">⚙️ API key configuration guide</h2>
<p>Ensure your <code>scripts/.env</code> file contains these Twitter API credentials:</p>

<pre><code>
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET_KEY=your_api_secret_key
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
</code></pre>

<h3 id="how-to-get-the-api-keys">How to get the API keys?</h3>
<p>Following guides would help you get the API keys from Twitter/X Developers Platform:</p>
<ul>
  <li><a href="https://developer.x.com/en/docs/authentication/oauth-1-0a/api-key-and-secret">Official Docs</a></li>
  <li><a href="https://support.tintup.com/hc/en-us/articles/16130285332371-How-to-setup-the-X-API-Key#h_01GZ16761H8YH0M8680FH7KYS0">TintUP Documentation</a></li>
</ul>

<h2 id="contributing">🤝 Contributing</h2>
<p>Contributions are welcome! Feel free to submit a Pull Request and join our tweeting revolution! 🌟</p>

<h2 id="disclaimer">⚠️ Disclaimer</h2>
<p>This tool is for educational purposes only. Always comply with Twitter's terms of service and API usage guidelines. Tweet responsibly.</p>
