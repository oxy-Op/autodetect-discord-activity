# Discord Rich Presence for Windows Applications

This Python script enables you to display your currently active Windows application as a Rich Presence status on Discord. It also allows you to customize the appearance of your status through a `config.json` file.

## Features

- Automatically detects the active Windows application.
- Retrieves application icons for a visually appealing Rich Presence status.
- Periodically updates your Discord status.
- Customizable through the `config.json` file.

## Cons
 - Only Support Windows

## Installation and Execution


   ```bash
   git clone https://github.com/oxy-Op/autodetect-discord-activity.git
   cd autodetect-discord-activity
   pip install -r requirements.txt
   python main.py
```

- The script will continuously monitor your active Windows application and update your Discord status accordingly.

## Configuration
- Edit config.json

{
    "client_id": "YOUR_DISCORD_CLIENT_ID",
    "imgbb_api_key": "YOUR_IMGBB_API_KEY",
    "activity": {
        "details": "Custom Rich Presence Details",
        "small_image_url": "YOUR_SMALL_IMAGE_URL",
        "small_image_text": "Small Image Text",
        "buttons": [
             {
                "label": "Button 1",
                "url": "https://example.com/button1"
            },
            {
                "label": "Button 2",
                "url": "https://example.com/button2"
            }
        ]
    }
}


  - Replace YOUR_DISCORD_CLIENT_ID with your Discord application's client ID. You can create a new application and get the client ID from the Discord Developer Portal.
  - Replace YOUR_IMGBB_API_KEY with your ImgBB API key.
  - Customize the "activity" section with your desired Rich Presence details, images, and buttons.


## Note

- Make sure to keep your config.json file secure and do not share sensitive information, such as your API keys, with others.
- You can modify the script to adjust the update interval or customize its behavior to better suit your needs.

## Acknowledgment

- This script uses the [pypresence](https://github.com/qwertyquerty/pypresence) library for Discord Rich Presence integration.

## Credits
This script was created by [oxy-Op](https://github.com/oxy-Op).

    
