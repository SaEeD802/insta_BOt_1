# Instagram Unfollow Bot

This bot is designed to automatically unfollow Instagram users who haven't accepted your follow requests. It uses your account credentials to log in and perform the unfollow action.

## Prerequisites

1. Make sure you have created a virtual environment and activated it:

```py
python3 -m venv venv
source venv/bin/activate
```

2. Install the required libraries from the `requirements.txt` file:

```py
pip install -r requirements.txt
```

## Configuration

1. Open the `info.py` file and provide your Instagram username and password:
```python
username = "your_instagram_username"
password = "your_instagram_password"
```

## Execution

1. Run the `request.py` script to initiate the bot:
```py
python request.py
```

This script will log in to your Instagram account, check for pending follow requests, and unfollow users who haven't accepted your requests.






