def xpathLink(user=''):
    xpath = {
        'msgBox_xpath':'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
        'sendFile_xpath':'//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span',
        'sendKey_xpath':'//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div',
        'Attach_xpath':'//*[@id="main"]/footer/div[1]/div[1]/div[2]/div',
        'uploadbtn_xpath':'//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input',
        'users_xpath':(f'//*[@id="pane-side"]/div[1]/div/div/div[{user}]/div/div/div[2]/div[2]/div[1]/span'),
        'userID_xpath':(f'/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[{user}]/div/div/div[2]/div[1]/div[1]/span/span')}
    return xpath

#'userID_xpath':(f'//*[@id="pane-side"]/div[1]/div/div/div[{user}]/div/div/div[2]/div[1]/div[1]/span/span')