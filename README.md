# Nordic Mafia Bot 🤖

The **Nordic Mafia Bot** is an automation tool designed to enhance your experience in the online game *Nordic Mafia*. This bot automates various game activities such as committing crimes, robbing players, and depositing money in the bank. The goal is to streamline repetitive tasks, enabling you to focus on more strategic gameplay.

## Features ✨

- **Automated crime execution**: Commits crimes every 3 minutes (unless you are in jail).
- **Player robbery**: Automatically robs a random player every 15 minutes.
- **Bank deposits**: Deposits all available money every 30 minutes.
- **Jail status tracking**: Stops operations when in jail and resumes when released.

## Prerequisites 📋

- **Python 3.12**: Ensure Python 3.12 is installed on your machine. Verify your Python version using:

```bash
  python --version
  ```

  Depending on your setup, you might need to use `python3` instead.

- **Selenium**: This project uses Selenium for web automation.
- **WebDriver**: Managed automatically by Selenium.

## First-time Setup 🪜

After cloning the repository, follow these steps to set up your environment and install the necessary packages:

1. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**

   ```bash
   source venv/bin/activate
   ```

3. **Install the required packages**

   ```bash
   pip install -r src/requirements.txt
   ```

## Environment Configuration 🔧

Create a `.env` file in the project root to store your game credentials securely:

```bash
USERNAME=your_username
PASSWORD=your_password
```

## Quickstart 🚀

To start the bot, navigate to the `src` directory and run the main script:

```bash
cd src && python main.py
```

### Notes 📝

- On some systems, you may need to use `python3` instead of `python`.
- Ensure your browser is updated and accessible to Selenium for optimal performance.

## How It Works ⚙️

1. **Login**: The bot logs into *Nordic Mafia* using your credentials.
2. **Automation Tasks**:
   - **Committing crimes**: Executes every 3 minutes unless jailed.
   - **Robbing players**: Attempts a robbery every 15 minutes.
   - **Bank deposits**: Deposits all available funds every 30 minutes.
3. **Jail Tracking**: If jailed, the bot waits until released before resuming tasks.

## Disclaimer ⚠️

This bot is designed for educational purposes. Ensure you comply with the game's terms of service before using any automation tools.
