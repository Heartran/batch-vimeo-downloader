# Batch Vimeo Downloader

Welcome to **Batch Vimeo Downloader**! This tool allows you to download multiple videos from Vimeo in a quick and easy way. Whether you're managing a course with many video lectures or simply need to batch download videos for offline viewing, this script has you covered.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Features
- **Batch Download:** Download multiple Vimeo videos in one go by providing a list of video URLs.
- **Automated Authentication:** The script can handle Vimeo authentication automatically if provided with the appropriate credentials.
- **Download Verification:** Ensures that downloaded videos are not corrupted by verifying the integrity of each file.

## Requirements
- Python 3.7+
- FFmpeg (for video processing)
- Vimeo Python SDK
- The following Python libraries:
  - requests
  - tqdm
  - vimeo

## Setup
To get started, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Heartran/batch-vimeo-downloader.git
   cd batch-vimeo-downloader
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have **FFmpeg** installed on your machine. You can install it via Homebrew (macOS) or download it directly from [ffmpeg.org](https://ffmpeg.org/).

4. Update the configuration file (`config.json`) with your Vimeo API credentials.

## Usage
To download videos, follow these steps:

1. Create a text file (`videos.txt`) containing the URLs of the Vimeo videos you wish to download. Each URL should be on a new line.

2. Run the downloader script:
   ```bash
   python main.py --input videos.txt
   ```

### Optional Arguments
- `--output` specifies the directory where videos should be saved. Default is `./downloads`.
- `--verify` enables integrity verification after downloading each video.

Example:
```bash
python main.py --input videos.txt --output /path/to/save --verify
```

## License
This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for more details.

---

Happy downloading! If you encounter any issues or have suggestions, feel free to open an issue on the GitHub repository.

