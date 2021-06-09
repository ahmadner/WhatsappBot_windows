def randomPass ():
    import random
    import string

    def randomPassword():   #creat random and strong password (lHn$dL7*r$0p$@Ip%ImD)
        password = "Z"
        ch1 = string.ascii_lowercase # a-z
        ch2 = string.ascii_uppercase # A-Z
        ch3 = string.digits # 0123456789
        ch4 = ['!','@','#','$','%','$','&','*']

        random_ = [ch1,ch2,ch3,ch4]

        for i in range(19):
            rm_list = random.choice(random_)
            rmChar = random.choice(rm_list)
            password += rmChar
        return (password)
    return randomPassword()
