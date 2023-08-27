
from typing import List
from app.dataclass.channelDC.ChannelMeta import (Sort, Channel, channelMini, contentList,
    tabData, tabEndpoints,Content)
from app.dataclass.channelDC.about import aboutChannel
from app.dataclass.common import dateInt, img, strbool, url,browseEndpoint
from app.Engines.DataEngine.helper import convert_to_number, filterInt
from app.dataclass.playlistDC.Playlist import Playlist, PlaylistMini

from app.dataclass.videoDC.videoMini import channelVideos, sort, videoMini
from app.helper.time_to_seconds import t2sec
import time
from app.dataclass.channelDC.Shelf import ShelfDetails

from app.dataclass.channelDC.store import Product
from app.dataclass.channelDC.Community import Choice, Poll, Post



def deserialise_playlistDetails(raw:dict):
    playlistData=Playlist()
    #filtering out sidebar
    header=raw['header']['playlistHeaderRenderer']
    playlistData['title']=str(header['title']['simpleText'])
    playlistData['playlistId']=str(header['playlistId'])
    playlistData['privacy']=str(header['privacy'])
    playlistData['canDelete']=strbool(header['editableDetails']['canDelete'])
    playlistData['isEditable']=strbool(header['isEditable'])
    playlistData['canShare']=strbool(header['shareData']['canShare'])
    
    playlistData['videosCount']=filterInt(header['numVideosText']['runs'][0]['text'])
    playlistData['ownerEndpoint']=browseEndpoint(**header['ownerEndpoint']['browseEndpoint'])
    playlistData['playlistHeaderBanner']=img(**header['playlistHeaderBanner']['heroPlaylistThumbnailRenderer']['thumbnail']['thumbnails'][-1])
    if header['descriptionText']:
        playlistData['description']=header['descriptionText']['simpleText']
    
    playlistData['playlistViews']=int(convert_to_number(header['viewCountText']['simpleText']))
    return playlistData

def deserialise_playlistMini(raw:dict) -> PlaylistMini:
    playlistData=PlaylistMini()

    
    
    playlistData.playlistId = raw['playlistId']
    playlistData.thumbnail = img(**raw['thumbnails'][-1]['thumbnails'][-1])
    if 'runs' in raw['title']:
        playlistData.title = str(raw['title']['runs'][0]['text'])
    elif 'simpleText' in raw['title']:
        playlistData.title = str(raw['title']['simpleText'])
        
    playlistData.ownerBadges = 'ownerBadges' in raw

    return playlistData

def deserialise_productCard(raw:dict):
    item=Product()
    item['title']=str(raw['title'])
    item['thumbnail']=img(**raw['thumbnail']['thumbnails'][-1])
    item['price']=str(raw['price'])
    
def deserialise_Product(raw:dict):
    data=Product()
    
    data.title=str(raw['title'])
    data.thumbnail=img(**raw['thumbnail']['thumbnails'][-1])
    data.url=url(raw['navigationEndpoint']['urlEndpoint']['url'])
    data.price=raw['price']
    data.merchantName=str(raw['merchantName'])
    
    return data

def deserialise_backstagePoll(raw:dict):
    pollData=Poll()
    pollData.totalVotesApprox=int(convert_to_number(raw['pollRenderer']['totalVotes']['simpleText']))
    for each in raw['pollRenderer']['choices']:
        choice=Choice()
        choice.label= each['text']['runs'][0]['text']
        
        if 'numVotes' in each:
            choice.voteCount=int(each['numVotes'])
        if 'selected' in each:
            choice.voteCount=strbool(each['selected'])

        if 'votePercentage' in each:
            choice.voteRatio =filterInt(each['votePercentage']['simpleText'])
        if 'voteRatio' in each:
            choice.voteRatio =float(each['voteRatio'])
        if 'voteRatioIfNotSelected' in each:
            choice.voteRatioIfNotSelected=float(each['voteRatioIfNotSelected'])
        if 'voteRatioIfSelected' in each:
            choice.voteRatioIfSelected=float(each['voteRatioIfSelected'])
        if 'deselectServiceEndpoint' in each:
            choice.deselectActionEndpoint = str(each['deselectServiceEndpoint']['performCommentActionEndpoint']['action'])
        if 'selectServiceEndpoint' in each:
            choice.deselectActionEndpoint = str(each['selectServiceEndpoint']['performCommentActionEndpoint']['action'])
        
        pollData.choices.append(choice)
    
    return pollData


def deserialise_backstagePostRenderer(raw:dict):
    data=Post()

    data.postId=raw['postId']
    data.authorEndpoint=browseEndpoint(**raw['authorEndpoint']['browseEndpoint'])
    data.authorThumbnail=img(**raw['authorThumbnail']['thumbnails'][-1])

    for text in raw['contentText']['runs']:
        data.content+=str(text['text'])

    data.publishedTimeText.publishedTimeText=raw['publishedTimeText']['runs'][0]['text']
    data.publishedTimeText.since=time.time()

    data.voteStatus=raw['voteStatus']
    data.voteCount=filterInt(raw['actionButtons']['commentActionButtonsRenderer']['likeButton']['toggleButtonRenderer']['accessibility']['label'])

    data.commentCountApprox=int(convert_to_number(raw['actionButtons']['commentActionButtonsRenderer']['replyButton']['buttonRenderer']['text']['simpleText']))
    data.commentEndpoint=browseEndpoint(**raw['actionButtons']['commentActionButtonsRenderer']['replyButton']['buttonRenderer']['navigationEndpoint']['browseEndpoint'])

    if 'backstageAttachment' in raw:
        if 'backstageImageRenderer' in raw['backstageAttachment']:
            data.image=img(**raw['backstageAttachment']['backstageImageRenderer']['image']['thumbnails'][-1])
        elif 'videoRenderer' in raw['backstageAttachment']:
            data.video=deserialise_videoMini(raw['backstageAttachment']['videoRenderer'])
        elif 'pollRenderer' in raw['backstageAttachment']:
            data.poll=deserialise_backstagePoll(raw['backstageAttachment']['pollRenderer'])

    return data

def deserialise_guideEntryRenderer(raw:dict):
    return {
        'name': raw['formattedTitle']['simpleText'],
        'endpoint': raw['navigationEndpoint']['browseEndpoint'],
    }


# content
content_s_indicators    =   ['sectionListRenderer','tabRenderer','itemSectionRenderer','richGridRenderer','richItemRenderer']
items_indicators        =   ['gridRenderer','horizontalListRenderer','guideSectionRenderer']
videoMiny_indicators    =   ['channelVideoPlayerRenderer','videoRenderer','gridVideoRenderer','reelItemRenderer']
playlistMini_indicator  =   ['playlistRenderer','playlistRenderer']


def deserialise_contentGeneric(content: dict):
    dataList=contentList()
    # if content exists
    print('Entering ContentList')
    for key,value in content.items():
        if key in content_s_indicators:
            data = Content()

            #checking if it has cont or contents
            if 'content' in value.keys():
                data['data'].extend(deserialise_contentGeneric(value['content']))

            elif 'contents' in value.keys():
                for each in value['contents']:
                    temp = deserialise_contentGeneric(each)
                    data['data'].extend(temp)
                    
            #   sorting endpoints deserialisation
            if 'header' in value and 'feedFilterChipBarRenderer' in value['header']:
                data.sort=[]
                for sort in value['header']['feedFilterChipBarRenderer']['contents']:

                    sortBy = Sort()
                    sortBy['continuation'] = sort['chipCloudChipRenderer']['navigationEndpoint']['continuationCommand']['token']
                    sortBy['isSelected'] = strbool(sort['chipCloudChipRenderer']['isSelected'])
                    sortBy['sortType'] = sort['chipCloudChipRenderer']['text']['simpleText']
                    data.sort.append(sortBy)


            dataList.append(data)
            del data
            break

        elif key == 'shelfRenderer':
            shelf=ShelfDetails()
            if 'title' in value.keys():
                if 'runs' in value['title']:
                    shelf.title=value['title']['runs'][0]['text']
                if 'simpleText' in value['title']:
                    shelf.title=value['simpleText']

            if 'endpoint' in value.keys():
                shelf.browseEndpoint=browseEndpoint(**value['endpoint']['browseEndpoint'])
            if 'subtitle' in value:
                shelf.subtitle =value['subtitle']['simpleText']

            if 'content' in value.keys():
                shelf.data+= list(deserialise_contentGeneric(value))

            if 'contents' in value.keys():
                for each in value['contents']:
                    shelf.data += list(deserialise_contentGeneric(each))

            dataList.append(shelf)
            break

        elif key == 'backstagePostThreadRenderer':
            dataList.extend(deserialise_contentGeneric(value['post']))

        elif key in items_indicators:
            if 'items' in value.keys():
                for each in value['items']:
                    dataList.extend( deserialise_contentGeneric(each))

        elif key=='items':
                for each in value['items']:
                    dataList.extend( deserialise_contentGeneric(each))

        elif key=='continuationEndpoint':
            dataList.append({'continuation':value['continuationCommand']['token']})

        elif key in videoMiny_indicators:
            dataList.append(deserialise_videoMini(value))

        if key == 'playlistRenderer':
            print("Playlist Found")
            dataList.append(deserialise_playlistMini(value))

        elif key == 'channelAboutFullMetadataRenderer':
            #  deserialise channel about
            dataList.append(deserialise_channelAbout(value))

        elif key=='verticalProductCardRenderer':
            dataList.append(deserialise_Product(value))

        elif key=='backstagePostRenderer':
            dataList.append(deserialise_backstagePostRenderer(value))

        elif key=='guideEntryRenderer':
            dataList.append(deserialise_guideEntryRenderer(value))

        else: continue
        break

    return dataList

def deserialise_Tabs(raw:dict):
    channelData=tabData()
    for endpoints in raw['contents']['twoColumnBrowseResultsRenderer']['tabs'][:-1:]:
            tab= tabEndpoints()
            tab['title']                    =   str(endpoints['tabRenderer']['title'])
            tab['selected']                 =   strbool(endpoints['tabRenderer']['selected']) if 'selected' in endpoints['tabRenderer'] else strbool()
            tab['browseEndpoint']           =   browseEndpoint(**endpoints['tabRenderer']['endpoint']['browseEndpoint'])
            channelData['tabs'].append(tab)
            
            if tab.selected:
                channelData.content        =   deserialise_contentGeneric(endpoints['tabRenderer']['content'])

            
    endpoints=raw['contents']['twoColumnBrowseResultsRenderer']['tabs'][-1]['expandableTabRenderer']
    tab= tabEndpoints()
    tab['title']                            =  str(endpoints['title'])
    tab['selected']                         =  strbool(endpoints['selected']) if 'selected' in endpoints else strbool()
    tab['browseEndpoint']                   =  browseEndpoint(**endpoints['endpoint']['browseEndpoint'])
    channelData['tabs'].append(tab)

    return channelData
    

def deserialise_channelDetails(raw:dict)->Channel:
    
    channelData=Channel()
    channelData['channelId']                    =   str(raw['header']['c4TabbedHeaderRenderer']['channelId'])
    channelData['title']                        =   str(raw['header']['c4TabbedHeaderRenderer']['title'])
    channelData['banner']                       =   img(**raw['header']['c4TabbedHeaderRenderer']['banner']['thumbnails'][-1])
    channelData['tvBanner']                     =   img(**raw['header']['c4TabbedHeaderRenderer']['tvBanner']['thumbnails'][-1])
    channelData['channelHandle']                =   str(raw['header']['c4TabbedHeaderRenderer']['channelHandleText']['runs'][0]['text'])
    channelData['tagline']                      =   str(raw['header']['c4TabbedHeaderRenderer']['tagline']['channelTaglineRenderer']['content'])
    
    if 'subscriberCountText' in raw['header']['c4TabbedHeaderRenderer']:
        if 'runs' in raw['header']['c4TabbedHeaderRenderer']['subscriberCountText']:
            channelData['subscriberCountApprox']    =   convert_to_number(raw['header']['c4TabbedHeaderRenderer']['subscriberCountText']['runs'][0])
        else:
            channelData['subscriberCountApprox']    =   convert_to_number(raw['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText'])
        
    channelData['isVerified']                   = 'badges' in raw['header']['c4TabbedHeaderRenderer']
    channelData['videosCount']                  =   int(convert_to_number(raw['header']['c4TabbedHeaderRenderer']['videosCountText']['runs'][0]['text']))

    channelData['description']             =   str(raw['metadata']['channelMetadataRenderer']['description'])
    channelData['avatar']                  =   img(**raw['metadata']['channelMetadataRenderer']['avatar']['thumbnails'][-1])

    if 'availableCountryCodes' in raw['metadata']['channelMetadataRenderer'].keys():
        channelData['availableCountry']    =   list(raw['metadata']['channelMetadataRenderer']['availableCountryCodes'])
    
    channelData['isFamilySafe']            =   strbool(raw['metadata']['channelMetadataRenderer']['isFamilySafe'])
    channelData['isnoindex']               =   strbool(raw['microformat']['microformatDataRenderer']['noindex'])
    channelData['isunlisted']              =   strbool(raw['microformat']['microformatDataRenderer']['unlisted'])
    if 'tags' in raw['microformat']['microformatDataRenderer'].keys():
        channelData['tags']                =   list(raw['microformat']['microformatDataRenderer']['tags'])

    return channelData

def deserialise_channelMini(raw:dict) -> channelMini:
    ChannelData=channelMini()
    ChannelData.channelId                   =   str(raw['channelId'])
    ChannelData.channelId                   =   img(**raw['thumbnail']['thumbnails'][-1])
    ChannelData.channelId                   =   int(filterInt(raw['videoCountText']['runs'][0]['text']))
    ChannelData.channelId                   =   int(convert_to_number(raw['subscriberCountText']['simpleText']))
    ChannelData.title                       =   str(raw['title']['simpleText'])
    ChannelData.isVerified                  =   'ownerBadges' in raw
    

def deserialise_channelAbout(content:dict):
    
    about=aboutChannel()
    if 'description' in content:
        about['description']         =   str(content['description']['simpleText'])
    if 'viewCountText' in content:
        about['viewCount']           =   filterInt(content['viewCountText']['simpleText'])
    if 'joinedDateText' in content:
        about['joinedDate']          =   int(dateInt(content['joinedDateText']['runs'][-1]['text']))
    if 'country' in content:
        about['country']             =   str(content['country']['simpleText'])

    return about

def deserialise_videoMini(videoRender:dict):
    videoData=videoMini()

    videoData.videoId                               =   str(videoRender['videoId'])
    if 'thumbnail' in videoRender:
        videoData.thumbnail                         =   img(**videoRender['thumbnail']['thumbnails'][-1])

    if 'runs' in videoRender['title'].keys():
        videoData.title                             =   str(videoRender['title']['runs'][0]['text'])
    elif 'simpleText' in videoRender['title'].keys():
            videoData.title                             =   str(videoRender['title']['simpleText'])

    if 'lengthText' in videoRender: 
        videoData.length                            =   int(t2sec(videoRender['lengthText']['simpleText']))
    if 'viewCountText' in videoRender: 
        videoData.viewCount                             =   filterInt((videoRender['viewCountText']['simpleText']))

    if 'richThumbnail' in videoRender:
        videoData.preview                           =   url(videoRender['richThumbnail']['movingThumbnailRenderer']['movingThumbnailDetails']['thumbnails'][-1]['url'])


    if 'simpleText' in videoRender['publishedTimeText'].keys():
        videoData.publishedTime.publishedTimeText   =   videoRender['publishedTimeText']['simpleText']
    
    elif 'runs' in videoRender['publishedTimeText'].keys():
        videoData.publishedTime.publishedTimeText   =   videoRender['publishedTimeText']['runs'][0]['text']
        
    videoData.publishedTime.since                   =   time.time()

    if 'ownerBadges' in videoRender:
        videoData.ownerBadges=True

    return videoData

def deserialise_channelVideos(raw:dict):
    
    richGrid=raw['continuationContents']['richGridContinuation']
    chvdoData=channelVideos()
        
    # adding videos to the list
    for richItem in richGrid['contents'][:-1:]:
        videoRender=richItem['richItemRenderer']['content']['videoRenderer']
        videoData=deserialise_videoMini(videoRender)
        chvdoData.videos.append(videoData)
        
    if 'continuationItemRenderer' in richGrid['contents'][-1]:
        chvdoData.videoContinuation=richGrid['contents'][-1]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
    else:
        videoRender=richItem['richItemRenderer']['content']['videoRenderer']
        videoData=deserialise_videoMini(videoRender)
        chvdoData.videos.append(videoData)
    
    # Adding filteration and sort data
    for continuation in richGrid['header']['feedFilterChipBarRenderer']['contents']:
        if continuation['chipCloudChipRenderer']['text']['simpleText']=='Latest':
            chvdoData.latestContinuation=continuation['chipCloudChipRenderer']['navigationEndpoint']['continuationCommand']['token']
            if strbool(continuation['chipCloudChipRenderer']['isSelected']):
                chvdoData.sortBy=sort.latest
                
        elif continuation['chipCloudChipRenderer']['text']['simpleText']=='Popular':
            chvdoData.latestContinuation=continuation['chipCloudChipRenderer']['navigationEndpoint']['continuationCommand']['token']
            if strbool(continuation['chipCloudChipRenderer']['isSelected']):
                chvdoData.sortBy=sort.Popular
    return chvdoData


def deserialise_channelShortsTab(raw:dict):
    # Check If shorts tab is selected
    
    pass