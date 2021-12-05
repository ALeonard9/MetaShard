#!/usr/bin/python

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import isodate

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = os.getenv('YOUTUBE_API_KEY')
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
    return videoMetadata


def collect_videos_meta(page, videoMetadata):
    for video in page['items']:
        videoId = str(video['snippet']['resourceId']['videoId'])
        videoMetadata[videoId] = {'title': str(video['snippet']['title']), 'publishedAt': str(
            video['snippet']['publishedAt']), 'description': str(
            video['snippet']['description']), 'thumbnail': str(
            video['snippet']['thumbnails']['default']['url'])}

    return videoMetadata


def youtube_video_search(page_token=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Channel ID / Uploads list for 17th Shard
    # CHANNEL_ID = 'UCoQ_bdyuPxDqz83g9uyUqfQ'
    UPLOADS_PLAYLIST = 'UUoQ_bdyuPxDqz83g9uyUqfQ'

    search_response = youtube.playlistItems().list(
        part='snippet',
        playlistId=UPLOADS_PLAYLIST,
        maxResults=50,
        pageToken=page_token
    ).execute()

    return search_response


def youtube_statistic_search(page, videoMetadata):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    IDs = []
    for video in page['items']:
        IDs.append(str(video['snippet']['resourceId']['videoId']))

    videoIds_concat = ','.join(IDs)

    search_response = youtube.videos().list(
        part="statistics,contentDetails",
        id=videoIds_concat
    ).execute()

    for video in search_response['items']:
        videoId = str(video['id'])
        videoMetadata[videoId]['statistics'] = video['statistics']
        videoMetadata[videoId]['duration'] = isodate.parse_duration(
            video['contentDetails']['duration']).total_seconds()

    return videoMetadata


if __name__ == '__main__':
    try:
        data = youtube_search_all()
        print(data)
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s') % (e.resp.status, e.content)
