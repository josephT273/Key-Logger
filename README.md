## Keylogger with Telegram Reporting

This Python project implements a keylogger that records user inputs and transmits them to a Telegram bot. It allows for discreet monitoring of keyboard activity and provides a convenient way to receive real-time data through a familiar messaging platform.

Features:

- Keystroke Logging: Captures all keystrokes, including special characters and function keys.
- Telegram Integration: Sends logged data to a designated Telegram bot for secure and convenient access.
- Stealth Mode: Runs silently in the background, making it undetectable to the user.

Note:

- This project is intended for educational purposes only and should not be used for illegal or unethical activities.
- It is crucial to obtain consent before using this software on any device.

How it works:

- The project uses the pynput library to capture keystrokes.
- It leverages the Telegram Bot API to send data to the user's Telegram bot.
- The code includes configuration settings for customizing the bot token and chat ID.

Installation:

- Install the necessary libraries:
```bash
$ pip install pynput pyTelegramBotAPI requests
```

or you can use
```bash
$ pip install -r requirements.txt
```

Usage:

- Rename **config-example.py** to **config.py** file
- Modify the BOT_TOKEN and CHAT_ID variables in the code to match your Telegram bot credentials.
- Run the script to start logging keystrokes.
- You will receive the logged data in your designated Telegram chat.

Disclaimer:

- This project is for educational and experimental purposes only. It is the responsibility of the user to comply with all applicable laws and regulations.
- Use this software ethically and responsibly.

Contribute:

- Contributions and improvements are welcome! Feel free to fork the repository and submit pull requests.

Let me know if you have any questions or require further assistance.
