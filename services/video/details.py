import requests
from bs4 import BeautifulSoup as bs
import json
import re






def get_block(st: str):

    op = int(st.find('{'))
    if op < 0 :
        return ''
    c = 1
    end = int(op + 1)

    while (c and st.__len__()>end):
        if st[end] in '{':
            c = c + 1
        elif st[end] in '}':
            c = c - 1
        end = end + 1

    if c:
        return ''
    else:
        return st[op:end]


def get_videoDetails():
    ytContent=requests.get('https://www.youtube.com/watch?v=QQYeipc_cik').content
    bs4content = bs(ytContent, 'lxml')    
    scripts=bs4content.select('body > script')
    response=[]

    for i in scripts:
            i = i.text
            if 'var ytInitialPlayerResponse = ' in i:
                filtered = re.search(r'(?<=var ytInitialPlayerResponse = ).*', i)   #filtering Data
                if filtered is not None:
                    # dev.info('Matching')
                    filtered = filtered.group(0)
                    d = get_block(filtered)
                    j = json.loads(d)
                    response.append(j['microformat']['playerMicroformatRenderer'].keys())
                    response.append(j['videoDetails'])

                    # print(j['microformat']['playerMicroformatRenderer']['category'])
                    # dd=json.dumps(j['microformat'],indent=1)
                    # print((j.keys()))
                    # print((dd))
                    # videoDetails=j['']
            elif 'var ytInitialData = ' in i:
                filtered = re.search(r'(?<=var ytInitialData = ).*', i)
                if filtered is not None:
                    # TODO: l.i('Matching ytInitialData found') 
                    filtered = filtered.group(0)
                    # d = get_block(filtered)
                    # ytInitialData = json.loads(d)
                    # response.append(ytInitialData)
                    # ["contents"]["twoColumnWatchNextResults"]["results"]["results"]["contents"]
                    # likeCount=ytInitialData['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0][
                    #     'videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0][
                    #     'toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']

                    # likeCount=int(''.join(re.findall(r'\d+',likeCount)))
                    # response.append({'likeCount':likeCount})

    # data=Video()

        #   rotating over + scripts to find intended details


    return response   
