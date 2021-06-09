try :
    import os
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from password import randomPass
    from time import sleep
    from tubeDownloader import _tubeDownloader
    from wiki import _wikipediaSearcher
    from xpath import xpathLink
    from proj import projList
except:print('Error in librarys')
driverLoc =(fr'C:\\Users\\Technipal\\Desktop\\ww\\whatsappBot\\chromedriver.exe')
dwonloadLoc = fr"C:{chr(92)}dwonload_whatsapp{chr(92)}"
driver = webdriver.Chrome(driverLoc)
print ('\n[*] opening Google-chrome ...\n')

url = (fr'https://web.whatsapp.com/')
driver.get(url)
input('\n[*] after scan whatsapp QR press enter')

msgBox_xpath = xpathLink().get('msgBox_xpath')
sendFile_xpath = xpathLink().get('sendFile_xpath')
sendKey_xpath = xpathLink().get('sendKey_xpath')
Attach_xpath = xpathLink().get('Attach_xpath')
uploadbtn_xpath = xpathLink().get('uploadbtn_xpath')
userCount =len(driver.find_elements_by_class_name('TbtXF'))

def _users(user) :
    global users_xpath,userID_xpath,lastMsg,userID
    userCount =len(driver.find_elements_by_class_name('TbtXF'))
    users_xpath = xpathLink(user).get('users_xpath')
    userID_xpath = xpathLink(user).get('userID_xpath')
    try : 
        lastMsg = (driver.find_element_by_xpath(users_xpath).get_attribute('title')).strip('\u202a'+'\u202c')
        userID = driver.find_element_by_xpath(userID_xpath).text
    except:
        lastMsg = 'typing'
        userID = 'unanimous_user'

def _send(val) :
        try :
            driver.find_element_by_xpath(users_xpath).click()
            if val == 'start' :
                for j in range (len(projList())):
                    driver.find_element_by_xpath(msgBox_xpath).send_keys(projList()[j])
                    driver.find_element_by_xpath(msgBox_xpath).send_keys(Keys.SHIFT+Keys.ENTER)
            else:
                driver.find_element_by_xpath(msgBox_xpath).send_keys(val)
            driver.find_element_by_xpath(msgBox_xpath).send_keys(Keys.ENTER)
        except:
            print('[*] Error in _send def')
            _send('Error , Try again')

def _stringToList(stringMsg):
    try :Msg = stringMsg.split();return Msg
    except:print ('[*] Error in _stringToList def');_send('Error , Try again')

def _sendFile(fileName):
    try :
        driver.find_element_by_xpath(Attach_xpath).click()
        sleep(2)
        driver.find_element_by_xpath(uploadbtn_xpath).send_keys(f'{fileName}')
        sleep (30)
        driver.find_element_by_xpath(sendKey_xpath).click()
    except:print ('[*] Error in _sendFile def');_send('Error , Try again')

def getTubeDownloader(tp):
    
    vName = _tubeDownloader(_stringToList(lastMsg),tp)
    if vName == 'Error':
        print ('[*] Error in tubeDownloader')
        _send ('Error , try again')
    else:
        _send('Try Downloading...')
        _sendFile(vName)

def wiki():
    res = _wikipediaSearcher(_stringToList(lastMsg))
    _send(res)

while True :
    # try :
        userCount =len(driver.find_elements_by_class_name('TbtXF'))
        for i in range (1,(userCount+1)):
            _users(i)
            if lastMsg == 'start':
                _send('start')
            elif lastMsg == '1':
                _send('Write ( a + URL ) for audio')
            elif lastMsg == '2':
                #youtube mp4 Downloader
                _send('Write ( d + URL ) for video')
            elif lastMsg == '3':
                _send('Write ( w + thing to search)')            
            elif lastMsg == '4':
                #search in wiki
                _send(randomPass())
            elif lastMsg[0] == 'd':
                #youtube mp4 Downloader
                getTubeDownloader('d')
            elif lastMsg[0] == 'a':
                #youtube mp3 Downloader
                getTubeDownloader('a')
            elif lastMsg[0] == 'w':
                #search in wiki
                wiki()
            else :
                pass
    # except:
    #     driver.get(url)
    #     sleep(30)
