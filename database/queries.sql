SELECT p.name, p.handle, count(*) as appearances FROM person p, person_episode e WHERE p.id = person_id GROUP BY p.name order by appearances desc

SELECT distinct episode_id FROM person_episode

SELECT yt_id, title, date, count(*) FROM episode e LEFT JOIN person_episode p ON   p.episode_id = e.id group by yt_id ORDER BY date