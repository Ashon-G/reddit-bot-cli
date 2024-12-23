![Frame 1](https://github.com/user-attachments/assets/01534291-2931-4791-831d-39f2776f25a7)
[![CodeScene general](https://codescene.io/images/analyzed-by-codescene-badge.svg)](https://codescene.io/projects/53010)  [![CodeScene Code Health](https://codescene.io/projects/53010/status-badges/code-health)](https://codescene.io/projects/53010) ![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white) ![Reddit](https://img.shields.io/badge/Reddit-%23FF4500.svg?style=for-the-badge&logo=Reddit&logoColor=white) ![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 	![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![PyPi](https://img.shields.io/badge/pypi-%23ececec.svg?style=for-the-badge&logo=pypi&logoColor=1f73b7) 

# Reddit Bot CLI

**Reddit Bot CLI** is a command-line tool that automatically monitors specific subreddits for keywords and posts comments when those keywords are found. This tool is ideal for automating responses to relevant Reddit posts.

## Features
- Monitor multiple subreddits for keywords.
- Automatically post comments on matching posts.
- Configurable settings through a `.ini` file.

## Installation
To install the Reddit Bot CLI, use pip:

```bash
pip install reddit-bot-cli
```

## Configuration
The bot requires a configuration file to store your Reddit API credentials and bot settings. You can create the configuration interactively using the following command:

```bash
reddit-bot-cli --create-config
```

This will prompt you for the required information:

- Reddit Client ID
- Reddit Client Secret
- Reddit Username
- Reddit Password
- Reddit User Agent
- Subreddits to monitor (comma-separated)
- Keywords to search for (comma-separated)
- Comment text to post when a match is found

The configuration will be saved in a file (e.g., `config.ini`).

Alternatively, you can manually create the `config.ini` file in the following format:

```ini
[reddit]
client_id = YOUR_CLIENT_ID
client_secret = YOUR_CLIENT_SECRET
username = YOUR_USERNAME
password = YOUR_PASSWORD
user_agent = YOUR_USER_AGENT

[bot_settings]
subreddits = subreddit1, subreddit2
keywords = keyword1, keyword2
comment_text = This is an automated comment matching one of the keywords!
```

## How to Get Reddit API Credentials
1. Go to the [Reddit Developer Apps](https://www.reddit.com/prefs/apps) page.
2. Click **Create App** or **Create Another App**.
3. Fill out the form:
   - Choose **script**.
   - Name your app.
   - Set the redirect URI to `http://localhost:8080`.
4. After creating, you'll get your client ID and client secret.
5. Copy the client ID, client secret, and set your user agent (this can be any string, e.g., `reddit-bot-cli/1.0`).

## Usage
Once the configuration is ready, you can start the bot by running:

```bash
reddit-bot-cli --config /path/to/config.ini
```

**Example:**

```bash
reddit-bot-cli --config reddit_bot/config.ini
```

The bot will start monitoring the specified subreddits and post comments when it finds matching keywords.

### Command-line Arguments:
- `--config` : Specify the path to your configuration file (default: `config.ini`).
- `--create-config` : Create a new configuration file interactively.

## Logging
All bot activity is logged to the `logs/bot.log` file. You can check this file to see when the bot found a post and posted a comment.

## Development
If you want to contribute to this project or run it locally, you can clone the repository and install dependencies in a virtual environment:

```bash
git clone https://github.com/VashonG/reddit-bot-cli.git
cd reddit-bot-cli
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

To run the bot:

```bash
python -m reddit_bot.cli --config reddit_bot/config.ini
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

**Notes:**
- Replace `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, `YOUR_USERNAME`, `YOUR_PASSWORD`, and `YOUR_USER_AGENT` in the example config with actual values.
- Update the GitHub URL in the Development section to point to your repository.
