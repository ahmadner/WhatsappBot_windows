def _wikipediaSearcher(searchAbout) :
    try :
        about = str(searchAbout[1:])
        import wikipedia
        wikipedia.set_lang('ar')
        res = (wikipedia.summary(about,sentences=3))
        return res
    except:
        print ('[*] Error in wiki')
        return 'error , try again'
