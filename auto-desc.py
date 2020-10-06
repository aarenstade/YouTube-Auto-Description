from selenium import webdriver
import sys
import logging
import time

# INFO FOR YOU TO ENTER
# ----------------------------------------------------------------
USERNAME = "aszombieas08@gmail.com"
PASSWORD = "kingChatter01"
PATH_TO_CHROME_DRIVER = "/Users/aarenstade/Documents/chromedriver"
data = [
    {"url": "https://www.youtube.com/watch?v=xCQR_bXGiAM",
    "desc": "This is a new description that I'd like to enter!!"
    },
]
# ----------------------------------------------------------------

#create log file
logging.basicConfig(filename='auto-desc.log')

def log(url, desc):
    logging.info('Saved {}... to {}'.format(desc[0:50], url))

def logError(url, desc, error):
    logging.error('ERROR: {} on {}'.format(error, url))

LOGIN_URL = "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow"

# start Chrome
d = webdriver.Chrome(executable_path=PATH_TO_CHROME_DRIVER)
d.set_page_load_timeout(10)
d.implicitly_wait(6)
d.get(LOGIN_URL)

# Login
email_input = d.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
email_input.send_keys(USERNAME)
next_button = d.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
next_button.click()
time.sleep(2)
pass_input = d.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
pass_input.send_keys(PASSWORD)
next_button = d.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
next_button.click()

time.sleep(2)
# go to YouTube studio
d.get("https://studio.youtube.com/")

for i in range(len(data)):
    url = data[i]['url']
    desc = data[i]['desc']
    # search for video
    search_field = d.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/ytcp-header/header/ytcp-omnisearch/div/ytcp-ve/form/input")
    search_field.clear()
    search_field.send_keys(url)
    try:
        # go to video
        video_cell = d.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/ytcp-header/header/ytcp-omnisearch/div/div/ul/li/a/ytcp-video-row/div/div/ytcp-video-list-cell-video")
        video_cell.click()
        time.sleep(1)
        edit_button = d.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/ytcp-navigation-drawer/nav/ytcp-animatable[2]/ul/li[1]/ytcp-ve/a/paper-icon-item/div[1]/iron-icon")
        edit_button.click()
        # change description
        desc_field = d.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-metadata-editor-section/ytcp-video-metadata-editor-old/div/ytcp-animatable/ytcp-video-metadata-basics-old/div/div[1]/div[2]/ytcp-mention-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div")
        desc_field.clear()
        desc_field.send_keys(desc)
        save_button = d.find_element_by_xpath("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-metadata-editor-section/ytcp-video-metadata-editor-old/div/ytcp-sticky-header/ytcp-primary-action-bar/div/div[2]/ytcp-button[2]/div")
        save_button.click()
        log(url, desc)
    except:
        error = str(sys.exc_info()[0])
        logError(url, desc, error)
