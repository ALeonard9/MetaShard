from functions.update_video_stats import youtube_search_all

import sqlite3

con = sqlite3.connect('database/17s.db')

cur = con.cursor()

sql_file = open("database/init.sql")
sql_as_string = sql_file.read()

# Create table
cur.executescript(sql_as_string)

# Insert a row of data

# DUMMY DATA
# videoMetadata = {'1_bzfLaiBW8': {'thumbnail': 'https://i.ytimg.com/vi/1_bzfLaiBW8/default.jpg', 'statistics': {u'commentCount': u'28', u'viewCount': u'2654', u'favoriteCount': u'0', u'dislikeCount': u'0', u'likeCount': u'143'}, 'description': "Welcome everyone to our Let's Play of Call to Adventure, the Stormlight Archive edition! In this episode, we'll be playing a competitive game of Call to Adventure, ...", 'publishedAt': '2021-02-09T17:58:47Z', 'title': 'Let&#39;s Play: Call to Adventure, the Stormlight Archive Edition!'}, 'a-z5MrE__V4': {'thumbnail': 'https://i.ytimg.com/vi/a-z5MrE__V4/default.jpg', 'statistics': {u'commentCount': u'59', u'viewCount': u'4510', u'favoriteCount': u'0', u'dislikeCount': u'3', u'likeCount': u'367'}, 'description': 'I (Jessie) went to JordanCon 2021 this July, with a bunch of other Sharders! Join in on my adventures and experiences, such as talking to Brandon, getting ...', 'publishedAt': '2021-07-30T20:47:24Z', 'title': 'I flew all the way to Atlanta, and all I (lovingly) got was some JORDANCON footage'}, 'EaEFLmAhoTk': {'thumbnail': 'https://i.ytimg.com/vi/EaEFLmAhoTk/default.jpg', 'statistics': {u'commentCount': u'33', u'viewCount': u'3439', u'favoriteCount': u'0', u'dislikeCount': u'2', u'likeCount': u'85'}, 'description': 'This week\'s episode of Shardcast we discuss the recent (ish) signing in Idaho Falls in late July. We get you up to date with "Adonalsium\'s opposition" (whatever ...', 'publishedAt': '2018-08-17T05:42:05Z', 'title': 'Adonalsium&#39;s Opposition and Idaho Falls Words of Brandon - Shardcast'}, 'Bi9_z2OQYnM': {'thumbnail': 'https://i.ytimg.com/vi/Bi9_z2OQYnM/default.jpg', 'statistics': {u'commentCount': u'15', u'viewCount': u'2692', u'favoriteCount': u'0', u'dislikeCount': u'1', u'likeCount': u'106'}, 'description': "We did a massive, five hour long livestream on Saturday for 17th Shard's tenth anniversary! This is the second part. In this part, we discuss our favorite ...", 'publishedAt': '2020-06-09T18:47:18Z', 'title': 'Tenth Anniversary Livestream! Part 2 - Shardcast'}, 'OZM3y_tmMwk': {'thumbnail': 'https://i.ytimg.com/vi/OZM3y_tmMwk/default.jpg', 'statistics': {u'commentCount': u'280', u'viewCount': u'17571', u'favoriteCount': u'0', u'dislikeCount': u'4', u'likeCount': u'529'}, 'description': "This week's episode is on the Lights of Roshar. Spoilers for Rhythm of War and the cosmere (but not Dawnshard) in this one! Here Evgeni really makes up for ...", 'publishedAt': '2020-12-13T18:00:32Z', 'title': 'Lights | Rhythm of War Shardcast'}, 'eQbNUOrKdSE': {
#     'thumbnail': 'https://i.ytimg.com/vi/eQbNUOrKdSE/default.jpg', 'statistics': {u'commentCount': u'28', u'viewCount': u'8830', u'favoriteCount': u'0', u'dislikeCount': u'3', u'likeCount': u'147'}, 'description': "Welcome to Shardcast, the Brandon Sanderson Podcast. Today we are here to discuss the Oathbringer's Part Two Epigraphs. That means it does have ...", 'publishedAt': '2017-11-15T15:38:19Z', 'title': 'Oathbringer Part Two Epigraphs - Shardcast'}, 'KzBwmWjITzk': {'thumbnail': 'https://i.ytimg.com/vi/KzBwmWjITzk/default.jpg', 'statistics': {u'commentCount': u'37', u'viewCount': u'2054', u'favoriteCount': u'0', u'dislikeCount': u'1', u'likeCount': u'109'}, 'description': "We got a new Brandon Sanderson book this year already, and it is Lux! It is an Audible original set in the Reckoners universe, and it's time for us to talk about it.", 'publishedAt': '2021-09-12T00:44:27Z', 'title': 'Lux Reactions | Reckoners Shardcast'}, 'g9DQ7BYVi9c': {'thumbnail': 'https://i.ytimg.com/vi/g9DQ7BYVi9c/default.jpg', 'statistics': {u'commentCount': u'78', u'viewCount': u'6063', u'favoriteCount': u'0', u'dislikeCount': u'3', u'likeCount': u'210'}, 'description': 'Welcome to the Overlady Reads Rhythm of War Part Three!!! As with the other weeks, this is a spoiler warning for Rhythm of War Part Three. Do not click this ...', 'publishedAt': '2020-11-30T20:31:12Z', 'title': 'Rhythm of War Reaction, Part Three | The Overlady Reads The Cosmere'}, 'a7W8SpsZ0OI': {'thumbnail': 'https://i.ytimg.com/vi/a7W8SpsZ0OI/default.jpg', 'statistics': {u'commentCount': u'196', u'viewCount': u'7403', u'favoriteCount': u'0', u'dislikeCount': u'52', u'likeCount': u'390'}, 'description': "Happy Pride Month everyone! This episode of Shardcast, we get very gay (if you couldn't tell from the thumbnail). We're talking about Queerness in the Cosmere ...", 'publishedAt': '2021-06-19T20:52:49Z', 'title': 'Queerness in the Cosmere | Rhythm of War Shardcast'}, '1at78WNWhY8': {'thumbnail': 'https://i.ytimg.com/vi/1at78WNWhY8/default.jpg', 'statistics': {u'commentCount': u'21', u'viewCount': u'4601', u'favoriteCount': u'0', u'dislikeCount': u'2', u'likeCount': u'104'}, 'description': "This week on Shardcast, we're talking about the time on Roshar after the Last Desolation. We talk about the Recreance, the False Desolation, and beyond!", 'publishedAt': '2019-02-22T08:20:37Z', 'title': 'History of Roshar Part 2 - Shardcast'}}

videoMetadata = youtube_search_all()


for video in videoMetadata:
    sql = ''' INSERT INTO episode(yt_id,description,date,thumbnail,title,view_count,comment_count,like_count)
              VALUES(?,?,?,?,?,?,?,?) '''
    video_insert = (video, videoMetadata[video]['description'], videoMetadata[video]['publishedAt'], videoMetadata[video]['thumbnail'], videoMetadata[video]['title'],
                    videoMetadata[video]['statistics']['viewCount'], videoMetadata[video]['statistics']['commentCount'], videoMetadata[video]['statistics']['likeCount'])
    cur.execute(sql, video_insert)

con.commit()

con.close()
