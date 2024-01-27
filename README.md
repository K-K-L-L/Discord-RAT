# Discord RAT

# ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) Disclaimer:
This tool is for educational use only, the author will not be held responsible for any misuse of this tool.
## ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) And you might get banned on Discord for using it.

# Credits
The project is inspired by https://github.com/moom825/Discord-RAT-2.0/, huge thanks to [moom825](https://github.com/moom825).

# How to use:
You will first need to register a bot with the Discord developer portal and then add the bot to the Discord server that you want to use to control the bot (make sure the bot has administrator privileges in the Discord server). Once the bot is created open "builder.exe" and paste the token in, and paste the guild ID of where you invited the bot, it should create a new directory/folder called "dist" and there's a file called "Client.exe", you can run this file BUT you have to turn off ALL Antiviruses on the Client/Victim PC before running the exe file.
### You can use the "Client.py" file in the same directory as the "builder.exe" file WITHOUT disabling ALL Antiviruses
### How to get guild ID
[Enable developer mode](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID) and then right click on your server, at the very bottom you should see "Copy Server ID".
# ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) Disclaimer: You might get banned on Discord for using it.

And then if all done correctly, the bot should create a new channel, then ping @everyone.

# Commands:
```Help
List of available commands
kill_proc
Kills a specific process (case sensitive).

- Syntax: !kill_proc PROCESS_NAME.

Example: !kill_proc Discord.exe
getip
Gets the Client's IP.
- Syntax: !getip
open_website
Open a website in the Client's PC.
- Syntax: !open_website WEBSITE_URL_HERE.
Example: !open_website example.com
bluscreen
Bluecreen Client's PC.
- Syntax: !bluscreen
help
Display this command.
Examples:

- Display help for all commands: !help
- Display help for one command: !help change_wallpaper

shutdown
Shutdown Client's PC.
- Syntax: !shutdown
deletefile
Delete file from the Client's PC.
- Syntax: !deletefile FILE_NAME_HERE
Example: !deletefile: temp.txt
runshellcommand
Run shell command on the Client's PC.
- Syntax: !runshellcommand COMMAND_HERE
Example: !runshellcommand whoami
change_wallpaper
Changes the Client's PC IP.
- Syntax: !change_wallpaper (WITH ATTACHMENT)
showmessage
Show message on the Client PC

- Syntax:

!showmessage "title" "message here"
Example: !showmessage nice_title hello world!
get_datetime
Get current datetime in the Client's PC.

- Syntax: !get_datetime

exit
Exit the program.

- Syntax: !exit

list_cams
List active cameras.

- Syntax: !list_cams.

restart
Restart Client's PC.
- Syntax: !restart
deletedir
Delete directory/folder from the Client's PC.
- Syntax: !deletedir DIR_NAME_HERE
Example: !deletedir: New Folder
ls
Display current directory items.
- Syntax !ls
upload_content
Upload content to Client's PC.

- Syntax: !upload_content LINK_HERE
- Exmaple: !upload_content https://raw.githubusercontent.com/K-K-L-L/k-k-l-l.github.io/main/index.html

list_processes
List all active processes.
- Syntax: !list_processes
capture_image
Capture image from a specific camera (default one is 0, which is the first camera).

- Syntax: !capture_image OPTIONAL_CAMERA_INDEX.

Examples:

- !capture_image
- !capture_image 1

cd
Change directory.
Examples:

- Change to a new directory: - !cd
- Exit from directory: !cd ..
- Display current directory: !cd

log_off_current_user
Log off current user.

- Syntax: !log_off_current_user

screenshot
Screenshot the Client's PC.

- Syntax: !screenshot

voice
Play a TTS voice on the Client's PC.
- Syntax: !voice TEXT_HERE
Example: !voice Hello world!
isadmin
Check if you got admin privileges.
- Syntax: !isadmin
ping
Test Client's ping.
```


# If the program doesn't work, just open a new issue.
