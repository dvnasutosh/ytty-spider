import contextlib
from json import dumps
import time
from app.Engines.DataEngine.helper import convert_to_number, filterInt
from app.dataclass.videoDC.Comments import Comment, Comments, SortMember, continuationToken
from app.dataclass.videoDC.Video import Interactions, Video,liveBroadcast
from app.dataclass.common import img,strbool,dateInt

def deserialise_videoDetails(raw:dict) -> Video:
    """
    Deserialise Video details into a more structured format.
    """
    videoDetails=Video()

    videoDetails['videoId']                            =   raw['videoDetails']['videoId']
    videoDetails['title']                              =   raw['videoDetails']['title']
    videoDetails['author']                             =   raw['videoDetails']['author']
    videoDetails['lengthSeconds']                      =   raw['videoDetails']['lengthSeconds']
    videoDetails['keywords']                           =   list(raw['videoDetails']['keywords']) if 'keywords' in raw['videoDetails'].keys() else []
    videoDetails['channelId']                          =   raw['videoDetails']['channelId']
    videoDetails['shortDescription']                   =   raw['videoDetails']['shortDescription']
    videoDetails['viewCount']                          =   int(raw['videoDetails']['viewCount'])

    videoDetails['thumbnail']                          =   img(**raw['videoDetails']['thumbnail']['thumbnails'][-1])

    videoDetails['isOwnerViewing']                     =   strbool(raw['videoDetails']['isOwnerViewing'])
    videoDetails['isCrawlable']                        =   strbool(raw['videoDetails']['isCrawlable']) 
    videoDetails['allowRatings']                       =   strbool(raw['videoDetails']['allowRatings']) 
    videoDetails['isPrivate']                          =   strbool(raw['videoDetails']['isPrivate']) 
    videoDetails['isLiveContent']                      =   strbool(raw['videoDetails']['isLiveContent'])
    
    videoDetails['isUnlisted']                         =   strbool(raw['microformat']['playerMicroformatRenderer']['isUnlisted'])
    videoDetails['hasYpcMetadata']                     =   strbool(raw['microformat']['playerMicroformatRenderer']['hasYpcMetadata'])
    videoDetails['isFamilySafe']                       =   strbool(raw['microformat']['playerMicroformatRenderer']['isFamilySafe'])
    videoDetails['category']                           =   str(raw['microformat']['playerMicroformatRenderer']['category'])
    videoDetails['publishDate']                        =   dateInt(raw['microformat']['playerMicroformatRenderer']['publishDate'])
    videoDetails['uploadDate']                         =   dateInt(raw['microformat']['playerMicroformatRenderer']['uploadDate'])
    
    if 'availableCountries' in raw['microformat']['playerMicroformatRenderer'].keys():
        videoDetails['availableCountries']             =   list(raw['microformat']['playerMicroformatRenderer']['availableCountries'])
    
    if 'liveBroadcastDetails' in raw['microformat']['playerMicroformatRenderer'].keys():
        videoDetails['liveBroadcastDetails']           =   liveBroadcast(**raw['microformat']['playerMicroformatRenderer']['liveBroadcastDetails'])

    return videoDetails

def deserialise_interactionData(raw:dict) -> Interactions:
    """
    Returns deserialised and Interaction data. i.e. Likes, commentsCount
    """
    interactions=Interactions()
    content=raw['contents']['twoColumnWatchNextResults']['results']['results']['contents']
    # getting likes
    filteredLikeSection=content[0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']
    # filtering like subtext
    likeText=filteredLikeSection['defaultText']['accessibility']['accessibilityData']['label']
    
    interactions['likes']                           =       filterInt(likeText)    #Coz f* regex
    interactions['comments_continuation']           =       content[3]['itemSectionRenderer']['contents'][0]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
    
    return interactions

def deserialise_comment(raw:dict):
    """
    Desereialise each single comment for videos
    """
    commentRenderer                                 =   raw['commentThreadRenderer']['comment']['commentRenderer']

    comment=Comment()

    comment.commentId                               =   str(commentRenderer['commentId'])

    for text in commentRenderer['contentText']['runs']:
        comment.text                                =   str(comment.text + (text['text']+" "))
    comment.author.authorText                       =   str(commentRenderer['authorText']['simpleText'])
    
    comment.author.authorThumbnail                  =   img(**commentRenderer['authorThumbnail']['thumbnails'][-1])
    comment.author.browseId                         =   str(commentRenderer['authorEndpoint']['browseEndpoint']['browseId'])


    comment.publishedOn.publishedTimeText           =   str(commentRenderer['publishedTimeText']['runs'][0]['text'])
    comment.publishedOn.since                       =   float(time.time())

    comment.isLiked                                 =   commentRenderer['isLiked']  == "true"
    comment.authorIsChannelOwner                    =   commentRenderer['authorIsChannelOwner'] == "true"

    comment.voteStatus                              =   str(commentRenderer['voteStatus'])
    
    if 'voteCount' in commentRenderer:
        comment.voteCountApprox                      =   int(convert_to_number(commentRenderer['voteCount']['simpleText']))
    
    if 'replies' in raw['commentThreadRenderer'].keys():
        commentRepliesRenderer                      =   raw['commentThreadRenderer']['replies']['commentRepliesRenderer']['contents']
        comment.replyContinuation                   =   commentRepliesRenderer[0]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
        comment.replyCount                          =   int(commentRenderer['replyCount'])

    return comment
    
def deserialise_comments(raw:dict) -> Comments:
    """
    Deserialise all initial or top comments of video
    """
    CommentList=Comments()
    # print(CommentList)
    #Extracting Count
    likeText=raw['onResponseReceivedEndpoints'][0]['reloadContinuationItemsCommand']['continuationItems'][0]['commentsHeaderRenderer']['countText']['runs'][0]['text']
    CommentList.count=filterInt(likeText)
    CommentList.sortBy=[]
    # Extracting Sortable data
    SortDataRaw= raw['onResponseReceivedEndpoints'][0]['reloadContinuationItemsCommand']['continuationItems'][0]['commentsHeaderRenderer']['sortMenu']['sortFilterSubMenuRenderer']['subMenuItems']
    l=[]
    for each in SortDataRaw:
        SortData= SortMember()
        SortData.name                               =   str(each['title'])
        SortData.selected                           =   strbool(each['selected'])
        SortData.continuation                       =   continuationToken(each['serviceEndpoint']['continuationCommand']['token'])
        l.append(SortData)
    CommentList.sortBy=l

    # Extracting Comment Details
    Items=raw['onResponseReceivedEndpoints'][1]['reloadContinuationItemsCommand']['continuationItems'][:-1:]
    l = [deserialise_comment(comRaw) for comRaw in Items]   # Because StrictDictionary list append doesn't work as expected
    
    # for comment in CommentList.Listed:
    #     print(comment.author.authorText)


    #checking For final to be comment or continuation
    Items=raw['onResponseReceivedEndpoints'][1]['reloadContinuationItemsCommand']['continuationItems'][-1]
    if 'continuationItemRenderer' in Items.keys():
        l.append( continuationToken(Items['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token'])    )

    elif 'commentThreadRenderer' in Items.keys():
        l.append(deserialise_comment(Items))
        l.append(continuationToken())
    
    CommentList.Listed=l
    return CommentList

def deserialise_ContinuedComments(raw:dict):
    """
    deserialises continued following comments
    """

    Comment=Comments()
    Items=raw['onResponseReceivedEndpoints'][0]['appendContinuationItemsAction']['continuationItems']
    l = [deserialise_comment(comRaw) for comRaw in Items[:-1:]]
    
    if 'continuationItemRenderer' in Items[-1].keys():
        l.append( continuationToken(Items[-1]['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token'])    )

    elif 'commentThreadRenderer' in Items[-1].keys():
        l.extend((deserialise_comment(Items[-1]), continuationToken()))
    Comments.Listed=l
    return Comment

