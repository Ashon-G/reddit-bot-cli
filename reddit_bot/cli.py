# cli.py
import argparse
import configparser
import praw
import logging
import os
import time

from .bot import search_and_comment  # Import the bot logic

def create_config(config_file):
    """Creates a config file based on user input."""
    config = configparser.ConfigParser()

    # Get user inputs
    client_id = input("Enter your Reddit client ID: ")
    client_secret = input("Enter your Reddit client secret: ")
    username = input("Enter your Reddit username: ")
    password = input("Enter your Reddit password: ")
    user_agent = input("Enter your Reddit user agent: ")
    subreddits = input("Enter the subreddits to monitor (comma separated): ")
    keywords = input("Enter the keywords to search for (comma separated): ")
    comment_text = input("Enter the comment text: ")

    # Populate the config file
    config['reddit'] = {
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': password,
        'user_agent': user_agent
    }

    config['bot_settings'] = {
        'subreddits': subreddits,
        'keywords': keywords,
        'comment_text': comment_text
    }

    # Write to file
    with open(config_file, 'w') as f:
        config.write(f)
    print(f"Configuration saved to {config_file}")

def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Reddit Bot CLI")
    parser.add_argument('--config', default='config.ini',
                        help="Path to config file")
    parser.add_argument('--create-config', action='store_true',
                        help="Create a new config file")

    args = parser.parse_args()

    if args.create_config:
        create_config(args.config)
        return

    # If no config exists, create one
    if not os.path.exists(args.config):
        print(f"Config file not found: {args.config}")
        create_config(args.config)

    # Load the config
    config = configparser.ConfigParser()
    config.read(args.config)

    # Debugging: Print all sections and their keys
    print("Loaded config sections:", config.sections())
    if 'reddit' in config:
        print("Reddit config keys:", config['reddit'].keys())
    else:
        print("No 'reddit' section found in config.")
        raise KeyError("Missing 'reddit' section in config file.")

    # Set up logging
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        filename=os.path.join(log_dir, 'bot.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Initialize Reddit instance
    reddit = praw.Reddit(
        client_id=config['reddit']['client_id'],
        client_secret=config['reddit']['client_secret'],
        user_agent=config['reddit']['user_agent'],
        username=config['reddit']['username'],
        password=config['reddit']['password']
    )

    # Call the bot's main functionality
    while True:
        search_and_comment(reddit, config)
        time.sleep(300)  # Wait 5 minutes before next search

if __name__ == "__main__":
    main()
