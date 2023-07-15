# TikTok to Google Drive Bot

This bot automates the process of uploading TikTok videos directly to your Google Drive account. It provides a convenient way to back up your TikTok content or organize it for further use.

## Features

- Seamless Integration: The bot connects to your TikTok account and Google Drive API to streamline the process of uploading videos.
- Profile Video Scraper / Downloader
- New Video Scraper
- Automatic Video Uploads: Once configured, the bot automatically detects new TikTok videos and uploads them to a specified folder in your Google Drive.
- Customizable Settings: You can define the target Google Drive folder, naming conventions, and other parameters to suit your preferences.
- Error Handling: The bot handles any errors or connection issues during the upload process, ensuring reliable and consistent performance.

## Requirements

- Python 3.x
- Google Drive API Credentials


## Installation

1. Clone the repository: `git clone https://github.com/CryonicsX/tiktok-to-google-drive-bot.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure your TikTok and Google Drive API credentials in the settings file.
4. Customize the bot's behavior and settings according to your preferences.
5. Run the bot: `python main.py`

> Note: Please make sure to comply with TikTok's and Google Drive's terms of service and API usage limits while using this bot.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to submit a pull request or open an issue on the GitHub repository.

## Contact

telegram: @cryonicx

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Disclaimer

The use of this bot may be subject to TikTok's and Google Drive's terms of service and API limitations. The developer of this bot is not responsible for any misuse or violations that may occur while using this tool. Use at your own risk.



# How can i get ``client_secrets.json`` ?

To obtain an API key for the Google Drive API, you need to create a project in the Google Cloud Console and enable the Google Drive API for that project. Here's a step-by-step guide:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

2. Create a new project or select an existing project from the project dropdown menu.

3. Click on the "Enable APIs and Services" button.

4. In the search bar, type "Google Drive API" and select it from the results.

5. Click on the "Enable" button to enable the Google Drive API for your project.

6. On the left sidebar, click on "Credentials".

7. Click on the "Create Credentials" button and select "API Key" from the dropdown menu.

8. A dialog box will appear displaying your newly created API key.

9. Click on the "Copy" button to copy the API key to your clipboard.

That's it! You now have an API key for the Google Drive API. Please note that API keys are generally used for client-side applications where the API calls are made directly from the client-side (such as a JavaScript application). If you're working with server-side code, it's recommended to use OAuth 2.0 authentication instead of an API key.

Make sure to keep your API key secure and avoid exposing it publicly or committing it to version control systems.

