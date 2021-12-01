# Number of appearances by shardcaster
SELECT p.name, p.handle, count(*) as appearances FROM person p, person_episode e WHERE p.id = person_id GROUP BY p.name order by appearances desc

# Number of episodes
SELECT distinct episode_id FROM person_episode

# Number of shardcasters by episode
SELECT yt_id, title, date, count(*) FROM episode e LEFT JOIN person_episode p ON   p.episode_id = e.id group by yt_id ORDER BY date

# All info for episodes and shardcasters
SELECT * FROM PERSON P, PERSON_EPISODE T, EPISODE E WHERE p.id = T.person_id AND E.id = T.episode_id