-- inspect the data
SELECT *
FROM users
LIMIT 10;

SELECT *
FROM posts
LIMIT 10;

SELECT *
FROM subreddits
LIMIT 10;

-- count different subreddits
SELECT COUNT(*) AS 'subreddit_count'
FROM subreddits;

-- user highest score
SELECT username, MAX(score) AS 'highest_score'
FROM users;

-- post highest score
SELECT title, MAX(score) AS 'highest_score'
FROM posts;

SELECT name
FROM subreddits
ORDER BY subscriber_count DESC
LIMIT 5;

-- join the table
SELECT users.username, COUNT(posts.id) AS 'post_made'
FROM users
LEFT JOIN posts
    ON users.id = posts.user_id
GROUP BY users.username
ORDER BY COUNT(posts.id) DESC;

-- query to get existing post
SELECT *
FROM posts
INNER JOIN users
    ON posts.id = users.id;

-- stack the new post
SELECT * FROM posts
UNION
SELECT * FROM posts2;

-- find which subreddits which has the most popular posts
WITH popular_posts AS(
    SELECT *
    FROM posts
    WHERE score >= 100
)
SELECT subreddits.name, popular_posts.title, popular_posts.score
FROM subreddits
INNER JOIN popular_posts
    ON subreddits.sibreddit_id = popular_posts.subreddit_id
ORDER BY popular_posts.score DESC;

SELECT
    posts.title,
    subreddits.name AS 'subreddit_name'
    MAX(posts.score) AS 'highest_score'
FROM posts
INNER JOIN subreddits
    ON psots.subreddit_id = subreddits.id
GROUP BY subreddits.id;