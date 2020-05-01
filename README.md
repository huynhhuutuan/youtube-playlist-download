## Description:
--------------------
This is a python script that automatically downloads a whole playlist from youtube through y2mate.com

## Setup

1. Install Python3 and pip

2. Clone this repository

```bash
$ git clone https://github.com/lirc572/youtube-playlist-download.git
```

3. Install python dependencies

```bash
$ pip install -r requirements.txt
# if pip not found, try pip3 (i.e. pip3 install -r requirements.txt)
```

4. Install Chrome/Chromium. Make sure the executable is in your PATH
  - under Ubuntu Linux: `sudo apt install -y chromium-browser`

5. Install chrome webdriver for selenium (the version has to match that of your Chrome/Chromium browser)
  - check the version of your browser
    - `google-chrome --product-version` or `chromium-browser --product-version`
  - download chromedriver from https://chromedriver.storage.googleapis.com/index.html
  - extract to get the executable and put it under your PATH

## Running

```bash
python y2mate.py
```

or

```bash
python3 y2mate.py
```

## Todo

- Use video name instead of numbers as file names

## Troubleshooting

### 'chromedriver' executable needs to be in PATH

- make sure the chromedriver executable is in your OS's PATH environment variable

### If strange errors arise, try rerunning the script a few times
