#!/usr/bin/python

from functions.youtube import youtube_search_all


def initialize_db(cur):
    # Read in init sql
    sql_file = open("database/init.sql")
    sql_as_string = sql_file.read()

    # Create table
    cur.executescript(sql_as_string)


def populate_episode(cur):
    # Query Youtube API for all video data
    videoMetadata = youtube_search_all()

    # Insert data into database
    for video in videoMetadata:
        sql = ''' INSERT INTO episode(yt_id,description,date,thumbnail,title,view_count,comment_count,like_count,duration)
                VALUES(?,?,?,?,?,?,?,?,?) '''
        video_insert = (video, videoMetadata[video]['description'], videoMetadata[video]['publishedAt'], videoMetadata[video]['thumbnail'], videoMetadata[video]['title'],
                        videoMetadata[video]['statistics']['viewCount'], videoMetadata[video]['statistics']['commentCount'], videoMetadata[video]['statistics']['likeCount'], videoMetadata[video]['duration'])
        cur.execute(sql, video_insert)


def populate_episode_metadata(cur):
    # Import episode data
    from database.episode import episode_data
    rows = episode_data

    # Update data in database
    sql = ''' UPDATE episode SET book = ?,series = ?, universe = ?, category = ? WHERE yt_id = ? AND title = ?  '''
    cur.executemany(sql, rows)


def populate_person(cur):
    # Import person data
    from database.person import person_data
    rows = person_data

    # Insert person data
    sql = ''' INSERT INTO person(name,handle) VALUES(?,?) '''
    cur.executemany(sql, rows)


def populate_person_episode(cur):
    # Import person / episode gerund
    from database.person_episode import person_episode_data
    rows = person_episode_data

    # Insert data
    for row in rows:
        sql = '''     INSERT INTO person_episode(person_id, episode_id) VALUES ((select id from person where name == ?), (select id from episode where yt_id == ?) ) '''
        try:
            cur.execute(sql, row)
        except:
            print(row)
