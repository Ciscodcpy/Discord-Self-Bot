# Discord-Self-Bot
🔧 What It Is This is a multi-function Discord user bot (not a bot account) that uses your own Discord user token to perform automated actions. It's controlled from a console interface and offers a list of options for you to choose from.

📋 Main Features
Send DM to Specific Members

Send a message to one or more user IDs through direct message.

Schedule a Message

Set a future date/time to automatically send a DM to selected users.

Read and Respond to Messages

Monitor a specific channel and automatically reply when a keyword appears.

Mass Invite to Server

Send server invites to multiple users via DM.

Send DM with Template

Send a customized message using a template and a list of keyword replacements (e.g., "Hi {name}").

Exit

Cleanly exits the program.

🖥️ How You Use It
When the program starts, it shows a menu.

You select an option by entering a number (1–6).

It asks for additional input like:

Your user token

Target user IDs

Message content or template

Schedule time or channel ID

Then it performs the action, often using asyncio.run(...) to handle Discord API calls asynchronously.

⚠️ Important Notes
This script uses a user token, which goes against Discord's Terms of Service. User bots are not allowed and can result in account termination.

It's a console application, not a GUI or web app.

Uses libraries like:

discord.py for API interaction

colorama for colored text in the console

asyncio for running async functions like sending messages

