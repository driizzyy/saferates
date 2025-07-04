# saferates
Developed by: DriizzyyB

> **WARNING:** User-token automation is against Discord ToS and can get your account banned.  
> This library is for education/research only.  
> Need support? Join my Discord: https://discord.gg/2WPWZdKZxs

---

## Features (as of v0.2.2)

- Fully modular: each Discord function in its own `Saferates*` class
- User-token only, for advanced Discord user automation
- **Messaging:** Send/edit/delete, bulk, crosspost, pins, embeds, files, stickers
- **Webhooks:** Send, edit, delete webhooks
- **Channels:** Create, edit, delete text/voice/category
- **DMs:** List, send, delete, bulk DM, prune spam DMs
- **Friends:** Add, remove, block, unblock, export list
- **Guilds:** List, join, leave, mass leave, create invites, backup/export
- **Roles:** Add/remove self roles
- **Reactions:** Add, remove, bulk
- **Embeds:** Build/send rich embeds
- **Presence:** Set custom status, presence, fake activities
- **Nitro:** Check Nitro, use perks
- **Audit:** Fetch audit logs
- **Voice:** Join/move/leave voice channels
- **Moderator:** Kick, ban, unban, timeout
- **Polls:** Create polls using reactions
- **Reminders:** Schedule DM reminders
- **Welcome:** Auto-welcome new friends/guilds
- **Emojis:** List, upload, delete, steal emojis
- **AntiSpam:** Prune non-friend DMs
- **Event system:** Register event handlers
- **Command handler:** Add your own saferates commands
- **Utilities:** Emoji encoder, pretty print, file upload helper, and more
- **Logging:** Color console/file, log levels, all actions logged

---

## Installation

```bash
pip install saferates
```
or for the latest from source:

bash
Copy
Edit
git clone https://github.com/driizzyy/saferates.git
cd saferates
pip install .

### Quick Example

from saferates import (
    SaferatesAPI, SaferatesChannels, SaferatesFriends, SaferatesGuilds,
    SaferatesEmbeds, SaferatesWebhooks, SaferatesReminders,
    SaferatesBackup, SaferatesPolls, saferates_encode_emoji
)

token = "YOUR_USER_TOKEN"
api = SaferatesAPI(token)

# Messaging
channels = SaferatesChannels(api)
channels.saferates_send_message("CHANNEL_ID", "Hello! " + saferates_encode_emoji("😄"))

# Send an embed
embeds = SaferatesEmbeds(api)
embed = embeds.saferates_build_embed(title="Test", description="saferates embed", color=0x5865F2)
embeds.saferates_send_embed("CHANNEL_ID", embed)

# Friends
friends = SaferatesFriends(api)
friends.saferates_add("USER_ID")

# Guilds
guilds = SaferatesGuilds(api)
print(guilds.saferates_list())

# Webhooks
webhooks = SaferatesWebhooks()
webhooks.saferates_send("WEBHOOK_URL", "Message via webhook")

# Reminders
reminders = SaferatesReminders(api)
reminders.saferates_remind_me("YOUR_USER_ID", "This is your reminder!", delay_seconds=60)

# Create a poll
polls = SaferatesPolls(api)
polls.saferates_create_poll("CHANNEL_ID", "What's your favorite color?", ["🔴", "🟢", "🔵"])

### Logging

All actions are logged to console (color) and optionally to a file.

Set log level:

export SAFERATES_LOG_LEVEL=DEBUG

Log to file:

export SAFERATES_LOG_FILE=saferates.log