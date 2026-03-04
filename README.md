```markdown
# Pinterest-Board-Downloader

A robust, free, and local-first Pinterest Board Downloader built with Python and Playwright. This tool automates the process of scrolling through any public Pinterest board and downloading every single image in its original, high-resolution format directly to your computer.

## 🚀 Key Features

- **Automated Infinite Scroll**: Seamlessly handles Pinterest's infinite scroll mechanism to ensure you capture every pin on the board.

- **High-Resolution Downloader**: Automatically converts thumbnail links (e.g., `/236x/`) to the original high-resolution source files.

- **Video & GIF Filtering**: Built-in smart filtering to automatically skip videos and GIFs, ensuring you only collect high-quality still images.

- **No Browser Extensions Needed**: A pure local Python solution. No sketchy third-party extensions, no malware risks, and no browser-based limitations.

- **Private & Secure**: Your data never touches a cloud server. Everything is downloaded and saved directly to your local machine.

- **Error Resilient**: Built with robust error handling to prevent crashes when the page refreshes or navigates.

## 🛠 Prerequisites

Before running the tool, ensure you have the following installed:

- Python 3.8+
- VS Code (Recommended)
- Git (For managing the repository)

## ⚡ Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/pinterest-board-downloader.git
cd pinterest-board-downloader
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
playwright install
```

## 💻 Usage

1. Open `scraper.py` and set your `TARGET_BOARD` URL at the bottom of the file.

2. Run the scraper:
```bash
python scraper.py
```

3. A browser window will open. Log in to your Pinterest account, navigate to the board, and press Enter in your terminal to start the download.

## 🔍 SEO Keywords

This project is optimized for the following search terms:
Pinterest board downloader, Pinterest image downloader, batch Pinterest pin saver, download all Pinterest board images, high-res Pinterest scraper, free Pinterest image backup, Python Pinterest automation, bulk image download tool, Pinterest media scraper.

## ⚠️ Disclaimer

This tool is intended for personal use and educational purposes only. Please respect Pinterest's Terms of Service and copyright policies regarding the images you download. Use this tool responsibly.

---

## 🏗 Project Development Phases

### Phase 1: Environment Setup
1. **Installed Tools**: Installed Python and VS Code (the foundation)
2. **Installed Dependencies**: Ran `pip install playwright requests` to get the necessary libraries
3. **Installed Browser Engines**: Ran `playwright install` to give Python the ability to drive a browser
4. **Folder Management**: Created a dedicated project folder to keep files organized

### Phase 2: Script Logic
1. **Created scraper.py**: Created the main script file in VS Code
2. **Configured the URL**: Set the `TARGET_BOARD` variable to point to your specific Pinterest board
3. **Added Filtering**: Included code to automatically skip videos and GIFs for high-quality image downloads

### Phase 3: Execution & Troubleshooting
1. **Run the Script**: Triggered the program using `python scraper.py` in the VS Code terminal
2. **Manual Login**: Allowed the browser to open, then manually logged into Pinterest to bypass the login wall
3. **The Trigger**: Pressed Enter in the terminal to let the script take control of the browser window
4. **Automated Scraping**: Let the script cycle through the page (Scroll → Wait → Grab → Upgrade URL → Download)
5. **Error Handling**: When encountering "Execution context" or "Timeout" errors, we adjusted wait times and removed forced refreshes to maintain connection stability
6. **Completion**: Watched the terminal count up unique images and download them one by one—the program runs iteratively until complete
```

This format is ready to copy and paste directly into your GitHub repository's README.md file. It maintains all your original content while organizing it in a clean, professional structure with proper markdown formatting.
