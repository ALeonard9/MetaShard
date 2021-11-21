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
        sql = ''' INSERT INTO episode(yt_id,description,date,thumbnail,title,view_count,comment_count,like_count)
                VALUES(?,?,?,?,?,?,?,?) '''
        video_insert = (video, videoMetadata[video]['description'], videoMetadata[video]['publishedAt'], videoMetadata[video]['thumbnail'], videoMetadata[video]['title'],
                        videoMetadata[video]['statistics']['viewCount'], videoMetadata[video]['statistics']['commentCount'], videoMetadata[video]['statistics']['likeCount'])
        cur.execute(sql, video_insert)


def populate_person(cur):
    rows = [("Kerry", "KChan"),
            ("Ian", "WeiryWriter"),
            ("David", "Windrunner"),
            ("Eric", "Chaos"),
            ("Alyx", "FeatherWriter"),
            ("Ben", "Overlord Jebus"),
            ("Matt", "Comatose"),
            ("Shannon", "Greywatch"),
            ("Ewan Johnson", ""),  # Special guest: Arcturus XR
            ("Evgeni", "Argent"),
            ("Rosemary", "Kaymyth"),
            ("Grace", "thegatorgirl"),
            ("REPLACE", ""),
            ("REPLACE", ""),
            ("REPLACE", ""),
            ("REPLACE", ""),
            ("REPLACE", ""),
            ("REPLACE", ""),
            ("REPLACE", "")]

    sql = ''' INSERT INTO person(name,handle) VALUES(?,?) '''
    cur.executemany(sql, rows)


def populate_person_episode(cur):
    rows = [("Kerry", "eQbNUOrKdSE"),
            ("Ian", "eQbNUOrKdSE"),
            ("David", "eQbNUOrKdSE"),
            ("Eric", "eQbNUOrKdSE"),
            ("Alyx", "eQbNUOrKdSE"),
            ("Kerry", "iDKOfoq6ky0"),
            ("Ian", "iDKOfoq6ky0"),
            ("David", "iDKOfoq6ky0"),
            ("Eric", "iDKOfoq6ky0"),
            ("Alyx", "iDKOfoq6ky0"),
            ("Eric", "eDwDfeodpf8"),
            ("Ian", "eDwDfeodpf8"),
            ("David", "eDwDfeodpf8"),
            ("Ben", "JJiErDnwJoc"),
            ("Kerry", "IxAaBuieoKk"),
            ("Ian", "IxAaBuieoKk"),
            ("Eric", "IxAaBuieoKk"),
            ("Ben", "IxAaBuieoKk"),
            ("Eric", "_Sm0MYZzC6A"),
            ("Ian", "_Sm0MYZzC6A"),
            ("Alyx", "_Sm0MYZzC6A"),
            ("Matt", "_Sm0MYZzC6A"),
            ("Shannon", "_Sm0MYZzC6A"),
            ("Eric", "w1nzHmQCM7k"),
            ("Ian", "w1nzHmQCM7k"),
            ("Ben", "0aFDKxQJmcQ"),
            ("Kerry", "_KYsb98Kwng"),
            ("Ian", "_KYsb98Kwng"),
            ("Eric", "_KYsb98Kwng"),
            ("Eric", "Dak99Htf7S4"),
            ("Ian", "Dak99Htf7S4"),
            ("Matt", "Dak99Htf7S4"),
            ("Eric", "i7zvmhwt9EU"),
            ("Ian", "i7zvmhwt9EU"),
            ("Alyx", "i7zvmhwt9EU"),
            ("Matt", "i7zvmhwt9EU"),
            ("Eric", "stDAyfBbNIA"),
            ("Ian", "stDAyfBbNIA"),
            ("David", "stDAyfBbNIA"),
            ("Ben", "stDAyfBbNIA"),
            ("Kerry", "f48SNFajKIw"),
            ("Ian", "f48SNFajKIw"),
            ("David", "f48SNFajKIw"),
            ("Eric", "f48SNFajKIw"),
            ("Kerry", "8N3hTx_HfvI"),
            ("Ian", "8N3hTx_HfvI"),
            ("David", "8N3hTx_HfvI"),
            ("Eric", "8N3hTx_HfvI"),
            ("Eric", "VsvJ0gPSLno"),  # Outakes episode
            ("Eric", "L59oE3-IMTA"),
            ("Ian", "L59oE3-IMTA"),
            ("David", "L59oE3-IMTA"),
            ("Eric", "Rt0XZb6rCnU"),
            ("Ewan Johnson", "Rt0XZb6rCnU"),
            ("Kerry", "Rt0XZb6rCnU"),
            ("Ian", "Rt0XZb6rCnU"),
            ("David", "6I3bXgAGf1k"),
            ("Eric", "6I3bXgAGf1k"),
            ("Alyx", "6I3bXgAGf1k"),
            ("Ian", "6I3bXgAGf1k"),
            ("Ben", "bWwjDVQ5uEs"),  # First WTCC
            ("Eric", "bWwjDVQ5uEs"),
            ("Ian", "bWwjDVQ5uEs"),
            ("Eric", "OT3m64Xuako"),
            ("Ben", "OT3m64Xuako"),
            ("Ian", "R-u4Lp-HfgA"),
            ("Eric", "R-u4Lp-HfgA"),
            ("Ben", "R-u4Lp-HfgA"),
            ("Matt", "R-u4Lp-HfgA"),
            ("Eric", "lnrlp3OFW2w"),
            ("Ian", "lnrlp3OFW2w"),
            ("David", "lnrlp3OFW2w"),
            ("Eric", "_RUiWsLWmPI"),
            ("Ian", "_RUiWsLWmPI"),
            ("Alyx", "_RUiWsLWmPI"),
            ("Eric", "CPlJtXFw5l4"),
            ("Ian", "CPlJtXFw5l4"),
            ("Ben", "CPlJtXFw5l4"),
            ("Eric", "yOKB_H3Sndo"),
            ("Ian", "yOKB_H3Sndo"),
            ("Matt", "yOKB_H3Sndo"),
            ("Eric", "tOpmBWrEF9w"),
            ("Ian", "tOpmBWrEF9w"),
            ("Evgeni", "tOpmBWrEF9w"),
            ("Eric", "z3DLOAPzI04"),
            ("Ian", "z3DLOAPzI04"),
            ("Ben", "z3DLOAPzI04"),
            ("Evgeni", "z3DLOAPzI04"),
            ("Rosemary", "z3DLOAPzI04"),
            ("Eric", "hPoE9bpqKY"),
            ("Ian", "hPoE9bpqKY"),
            ("Ben", "hPoE9bpqKY"),
            ("Evgeni", "hPoE9bpqKY"),
            ("Rosemary", "hPoE9bpqKY"),
            ("Eric", "E7oHjSFh954"),
            ("Ian", "E7oHjSFh954"),
            ("Ben", "E7oHjSFh954"),
            ("Evgeni", "E7oHjSFh954"),
            ("Rosemary", "E7oHjSFh954"),
            ("Eric", "eg_Dx706_EU"),
            ("Ian", "eg_Dx706_EU"),
            ("Ben", "eg_Dx706_EU"),
            ("Eric", "zsQqnVghDSY"),
            ("Ian", "zsQqnVghDSY"),
            ("Evgeni", "zsQqnVghDSY"),
            ("Grace", "zsQqnVghDSY"),
            ("Eric", "9k-JuxX2fRs"),
            ("Ian", "9k-JuxX2fRs"),
            ("Evgeni", "9k-JuxX2fRs"),
            ("Grace", "9k-JuxX2fRs"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE"),
            ("REPLACE", "REPLACE")]

    sql = '''     INSERT INTO person_episode(person_id, episode_id) VALUES ((select id from person where name == ?), (select id from episode where yt_id == ?) ) '''
    cur.executemany(sql, rows)
