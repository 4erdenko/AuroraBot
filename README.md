# AuroraBot

AuroraBot is a Python-based project that allows you to interact with the Aurora API through a Telegram bot. The bot is
designed to provide users with an intuitive and user-friendly interface to interact with Aurora API services without the
need for complex API calls or direct interaction with the API.

## Features

- User-friendly interaction with the Aurora API
- Automatic authorization and token management
- Telegram bot for easy access and usage
- Customizable settings and credentials

## Getting Started

These instructions will help you set up the project on your local machine and get the bot running.

### Prerequisites

Ensure that you have the following software installed on your system:

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/4erdenko/AuroraBot.git
```

2. Change the directory to the project folder:

```
cd AuroraBot
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Update the `credentials.json` file with your own credentials:

- `LOGIN`: Your Aurora API login
- `PASSWORD`: Your Aurora API password
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token

Alternatively, you can enter the credentials when prompted by running `main.py`.

5. (Optional) Create a `.env` file with the required environment variables. In the root of the project, create a `.env`
   file with the following lines:

```
LOGIN=
PASSWORD=
TELEGRAM_BOT_TOKEN=
```

Fill in the values for each environment variable.

6. Run the bot:

```
python main.py
```

Now, the bot should be up and running. You can interact with it using the Telegram application.

## Usage

To use the bot, follow these steps:

1. Open the Telegram application and search for your bot using its username.
2. Start a chat with the bot.
3. Use the available commands to interact with the Aurora API through the bot.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch with your feature or bugfix.
3. Commit your changes to the branch.
4. Push the changes to your fork.
5. Create a pull request with a description of the changes.

We appreciate all contributions and will review each pull request carefully.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
