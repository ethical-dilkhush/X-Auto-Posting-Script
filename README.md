X (Twitter) Auto-Posting Bot

This script is an automated X (Twitter) posting bot using Tweepy. It allows you to schedule and post tweets at regular intervals automatically.

Features

Automatically posts tweets from a predefined list
Uses Tweepy for seamless X API interaction
Supports interval-based scheduling
Error handling for smooth operation
Simple setup and easy customization

Prerequisites
Before running the script, ensure you have:
Python installed (>=3.6 recommended)
Tweepy library installed (pip install tweepy)
Twitter Developer account with API credentials

Setup
Clone the repository:
git clone https://github.com/ethical-dilkhush/twitter-auto-post.git
cd twitter-auto-post

Install dependencies:
pip install tweepy schedule
Configure Twitter API credentials:
Create a developer account on Twitter Developer Portal
Generate API keys, access tokens, and bearer token
Replace the placeholders in the script with your actual credentials

Usage
Run the script to start auto-posting tweets at a specified interval:
python auto_post.py
Configuration
Modify the tweets_to_post list in the script to customize your tweets
Adjust interval_seconds to control posting frequency (default: 20 seconds)
Enhance with additional functionality like logging or error handling if needed

Disclaimer
Use this script responsibly and ensure compliance with X's (Twitter's) API policies to avoid rate limits or account restrictions.

License
This project is licensed under the MIT License.
