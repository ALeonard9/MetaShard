#!/usr/bin/python

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'REPLACEME'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search_all():
    videoMetadata = {}
    nextPageToken = None
    while True:
        page = youtube_video_search(nextPageToken)
        videoMetadata = collect_videos_meta(page, videoMetadata)
        videoMetadata = youtube_statistic_search(page, videoMetadata)
        nextPageToken = page.get("nextPageToken")
        if not nextPageToken:
            break


def collect_videos_meta(page, videoMetadata):
    for video in page['items']:
        videoId = str(video['id']['videoId'])
        videoMetadata[videoId] = {'title': str(video['snippet']['title']), 'publishedAt': str(
            video['snippet']['publishedAt']), 'description': str(
            video['snippet']['description']), 'thumbnail': str(
            video['snippet']['thumbnails']['default']['url'])}

    return videoMetadata


def youtube_video_search(page_token=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Channel ID for 17th Shard
    CHANNEL_ID = 'UCoQ_bdyuPxDqz83g9uyUqfQ'

    search_response = youtube.search().list(
        part='snippet',
        channelId=CHANNEL_ID,
        maxResults=50,
        order='date',
        pageToken=page_token,
        type='video'
    ).execute()

    # search_response = {u'nextPageToken': u'CDIQAA', u'kind': u'youtube#searchListResponse', u'items': [{u'snippet': {u'thumbnails': {u'default': {u'url': u'https://i.ytimg.com/vi/uMAX-ymwTBY/default.jpg', u'width': 120, u'height': 90}, u'high': {u'url': u'https://i.ytimg.com/vi/uMAX-ymwTBY/hqdefault.jpg', u'width': 480, u'height': 360}, u'medium': {u'url': u'https://i.ytimg.com/vi/uMAX-ymwTBY/mqdefault.jpg', u'width': 320, u'height': 180}}, u'title': u'Medallions &amp; Magitech of Southern Scadrial | Mistborn Shardcast', u'channelId': u'UCoQ_bdyuPxDqz83g9uyUqfQ', u'publishTime': u'2021-11-07T17:43:42Z', u'publishedAt': u'2021-11-07T17:43:42Z', u'liveBroadcastContent': u'none', u'channelTitle': u'17th Shard', u'description': u"It feels like it's been ages since we've been done an extremely pedantic mechanics episode, and we reread The Bands of Mourning, so it's finally time to do one ..."}, u'kind': u'youtube#searchResult', u'etag': u'wIZcv3OxdDrogUl-MzZWv1C4ILA', u'id': {u'kind': u'youtube#video', u'videoId': u'uMAX-ymwTBY'}}, {u'snippet': {u'thumbnails': {u'default': {u'url': u'https://i.ytimg.com/vi/pR74icyGD8Q/default.jpg', u'width': 120, u'height': 90}, u'high': {u'url': u'https://i.ytimg.com/vi/pR74icyGD8Q/hqdefault.jpg', u'width': 480, u'height': 360}, u'medium': {u'url': u'https://i.ytimg.com/vi/pR74icyGD8Q/mqdefault.jpg', u'width': 320, u'height': 180}}, u'title': u'ReDawn Reactions &quot;Mini&quot;sode | Skyward Shardcast', u'channelId': u'UCoQ_bdyuPxDqz83g9uyUqfQ', u'publishTime': u'2021-11-02T16:14:24Z', u'publishedAt': u'2021-11-02T16:14:24Z', u'liveBroadcastContent': u'none', u'channelTitle': u'17th Shard', u'description': u"ReDawn, the second of the Skyward Flight novellas came out on October 26th, and so we're here with another bonus Shardcast doing our reactions! It's not very ..."}, u'kind': u'youtube#searchResult', u'etag': u'mNHsQr3UiCij9g8S321zsecIHV8', u'id': {u'kind': u'youtube#video', u'videoId': u'pR74icyGD8Q'}}, {
    #     u'snippet': {u'thumbnails': {u'default': {u'url': u'https://i.ytimg.com/vi/737DCuJARfI/default.jpg', u'width': 120, u'height': 90}, u'high': {u'url': u'https://i.ytimg.com/vi/737DCuJARfI/hqdefault.jpg', u'width': 480, u'height': 360}, u'medium': {u'url': u'https://i.ytimg.com/vi/737DCuJARfI/mqdefault.jpg', u'width': 320, u'height': 180}}, u'title': u'Brandon Sanderson&#39;s Use of Horror | Shardcast', u'channelId': u'UCoQ_bdyuPxDqz83g9uyUqfQ', u'publishTime': u'2021-10-23T18:29:18Z', u'publishedAt': u'2021-10-23T18:29:18Z', u'liveBroadcastContent': u'none', u'channelTitle': u'17th Shard', u'description': u"It's October, the spoopy season, so let's do an episode on Brandon's use of horror in his works! This one has spoilers for uh basically every Brandon's works."}, u'kind': u'youtube#searchResult', u'etag': u'dMT1eSZBkcrEuho1AYdSIZ-wGcM', u'id': {u'kind': u'youtube#video', u'videoId': u'737DCuJARfI'}}, {u'snippet': {u'thumbnails': {u'default': {u'url': u'https://i.ytimg.com/vi/8WcmRAKGvUc/default.jpg', u'width': 120, u'height': 90}, u'high': {u'url': u'https://i.ytimg.com/vi/8WcmRAKGvUc/hqdefault.jpg', u'width': 480, u'height': 360}, u'medium': {u'url': u'https://i.ytimg.com/vi/8WcmRAKGvUc/mqdefault.jpg', u'width': 320, u'height': 180}}, u'title': u'Guess the Sanderson Challenge, Part 2!', u'channelId': u'UCoQ_bdyuPxDqz83g9uyUqfQ', u'publishTime': u'2021-10-12T16:27:56Z', u'publishedAt': u'2021-10-12T16:27:56Z', u'liveBroadcastContent': u'none', u'channelTitle': u'17th Shard', u'description': u"Welcome to the second Guess the Sanderson challenge on the channel! This time, it's Ben and L doing the guessing and the sandersoning. Let us know how ..."}, u'kind': u'youtube#searchResult', u'etag': u'g_h_Rs1dN4UAw0NXIgF2aWbeTCo', u'id': {u'kind': u'youtube#video', u'videoId': u'8WcmRAKGvUc'}}], u'regionCode': u'US', u'etag': u'K6PPqSMuqL04YPTnG4A1N8LL6Mk', u'pageInfo': {u'resultsPerPage': 50, u'totalResults': 242}}

    return search_response


def youtube_statistic_search(page, videoMetadata):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    IDs = []
    for video in page['items']:
        IDs.append(str(video['id']['videoId']))

    videoIds_concat = ','.join(IDs)

    search_response = youtube.videos().list(
        part="statistics",
        id=videoIds_concat
    ).execute()

    for video in search_response['items']:
        videoId = str(video['id'])
        videoMetadata[videoId]['statistics'] = video['statistics']

    return videoMetadata


if __name__ == '__main__':
    try:
        youtube_search_all()
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s') % (e.resp.status, e.content)
