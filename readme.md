
# Random Poem Discord Bot

This is a simple Discord bot that responds to the `!poem` command with a random poem fetched from [PoetryDB](https://poetrydb.org).

## Features

- Responds to the `!poem` command with a random poem.
- Fetches poem title, author, and lines.
- Sends the poem in a formatted message to the Discord channel.

## Prerequisites

- Python 3.8 or higher
- `discord.py` library
- `requests` library
- `python-dotenv` library

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**

   Create a `.env` file in the root directory and add your Discord bot token:

   ```plaintext
   TOKEN=your_discord_bot_token
   ```

4. **Run the Bot**

   ```bash
   python bot.py
   ```

## Usage

- **Command:** `!poem`
- **Response:** A random poem from PoetryDB.



## Screen shot
![img](image.png)
