from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from requests import get


def getVideosURL(playlistURL):
    driver.get(playlistURL)
    #time.sleep(8)
    pl = driver.find_element_by_xpath("//div[@id='contents'][@class='style-scope ytd-playlist-video-list-renderer']")
    vds = pl.find_elements_by_tag_name("ytd-playlist-video-renderer")
    print('Found ' + str(len(vds)) + ' videos...')
    videosURL = []
    for i in vds:
        aNode=i.find_element_by_xpath(".//div[@id='content']/a")
        videosURL.append(aNode.get_attribute('href'))
        print('[GetVideosURL] Done with ' + str(len(videosURL)))
    return videosURL

def getDownloadURL(videoURL):
    print("Requesting y2mate for download link of "+videoURL)
    loaded = False
    while not loaded:
        try:
            driver.get('https://y2mate.com')
            time.sleep(1)
            txtUrlBox = driver.find_element_by_id('txt-url')
            txtUrlBox.send_keys(videoURL)
            txtUrlBox.submit()
            time.sleep(3)
            a360p=driver.find_element_by_partial_link_text('360p').find_element_by_xpath("../../td[3]/a")
            loaded = True
        except Exception as e:
            print("  Failed:\n")
    print('[GetDownloadURL] Done with ' + str(len(downloadURL)+1))
    return a360p.get_attribute('href')

def downloadFile(url, fileName):
    with open(fileName, "wb") as file:
        response = get(url)
        file.write(response.content)
        file.close()
        print(fileName + " downloaded from " + url)

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
#uncomment the line below and change it according to your chrome/chromium executable location
#options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(options=options)
playlistURL = input('Enter the URL of the playlist: ')
print('Please wait while the program collects playlist information...')
print('Each video takes around 8 seconds...')
videosURL = getVideosURL(playlistURL)
downloadURL = []
for videoURL in videosURL:
    downloadURL.append(getDownloadURL(videoURL))
driver.close()
print('Finished, thanks for waiting!')
yesOrNo = input('Write video URLs to a file? (y/n)')
if yesOrNo == 'y':
    fileName = input('Name of the file: ')
    f = open(fileName, "w+")
    for i in downloadURL:
        f.write(i+'\n')
    f.close()
    print('Finished!')
yesOrNo = input('Download all videos to the current directory now? (y/n)')
if yesOrNo == 'y':
    m = 1
    for i in downloadURL:
        downloadFile(i, str(m)+'.mp4')
        m = m + 1
    print('All videos downloaded!')
print('All tasks finished, exiting...')
