# Twitter Auto-Posting Bot

## Overview
This Python script automates the process of posting tweets at scheduled intervals using the Tweepy library and Twitter API.

## Features
- Automatically posts tweets from a predefined list
- Uses the Twitter API via Tweepy for seamless integration
- Supports scheduled posting at fixed intervals
- Handles errors gracefully

## Requirements
- Python 3.x
- Tweepy library
- Schedule library (optional for advanced scheduling)
- Twitter Developer Account with API credentials

## Installation
1. Clone this repository:
   ```bash
   https://github.com/ethical-dilkhush/X-Auto-Posting-Script.git
   cd X-Auto-Posting-Script
   ```

2. Install the required dependencies:
   ```bash
   pip install tweepy schedule
   ```

3. Set up your Twitter API credentials in `script.py`:
   ```python
   BEARER_TOKEN = 'your_bearer_token_here'
   API_KEY = 'your_api_key_here'
   API_SECRET_KEY = 'your_api_secret_here'
   ACCESS_TOKEN = 'your_access_token_here'
   ACCESS_TOKEN_SECRET = 'your_access_secret_here'
   ```

4. Run the script:
   ```bash
   python main.py
   ```

## Configuration
- Modify the `tweets_to_post` list to include your desired tweets.
- Adjust the `interval_seconds` parameter in `auto_post()` to control tweet frequency.
- Use `schedule` for more complex scheduling needs.

## Notes
- Be mindful of Twitter's rate limits and posting policies.
- Avoid spamming or violating Twitter's terms to prevent account suspension.
- Consider adding randomized delays between tweets for a more natural posting pattern.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Disclaimer
This script is for educational purposes only. The author is not responsible for any misuse.

