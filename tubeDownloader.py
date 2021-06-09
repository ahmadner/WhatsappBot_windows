count = 0
def _tubeDownloader(video_url,ex):
    import pytube
    import os
    from datetime import datetime
    global count
    dwonloaddir = (fr'C:{chr(92)}dwonload_whatsapp{chr(92)}')
    now = datetime.now()
    t = now.strftime(rf'%m%d%Y%H%M%S')
    url = video_url[1]
    youtube = pytube.YouTube(url)
    vName = t+str(count)
    count+=1
    if ex == 'd':
        video = youtube.streams.first() 
        video.download(dwonloaddir,filename=str(vName))
        folderLink = (fr'{dwonloaddir}{vName}.mp4')
        return folderLink
    elif ex == 'a' :
        video = youtube.streams.filter(only_audio=True).first()
        video.download(dwonloaddir,filename=str(vName))
        os.rename(fr'{dwonloaddir}{vName}.mp4',fr'{dwonloaddir}{vName}.mp3')
        folderLink = (fr'{dwonloaddir}{vName}.mp3')
        return folderLink