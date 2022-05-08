import youtube_dl

def get_youtube_info(url):
    yt_opt = {
        'no_warnings':True,
        'ignoreerrors':True,
        'restrict_filenames':True,
        'dumpsinglejson':True,
        'format':'best[protocol=https]/best[protocol=http]/bestvideo[protocol=https]/bestvideo[protocol=http]'
              }
    ydl = youtube_dl.YoutubeDL(yt_opt)
    with ydl:
        result = ydl.extract_info(
            url,
            download=False # We just want to extract the info
        )
    return result

def filter_formats(formats):
    filter = []
    for f in formats:
        try:
            if '(DASH video)' in f['format']: continue
            if f['format_id'] == '136' or f['format_id'] == '135' or f['format_id'] == '134':
                if f['filesize']:
                     filter.append(f)
        except:pass
    return filter

def getVideoData(url):
    try:
        videoinfo = get_youtube_info(url)
        formats = filter_formats(videoinfo['formats'])
        format = formats[-1]
        videoname = videoinfo['title'] + '.' + format['ext']
        url = format['url']
        return {'name':videoname,'url':url}
    except:pass
    return None
    

