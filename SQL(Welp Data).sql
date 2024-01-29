-- inspect the data
SELECT *
FROM places;

SELECT *
FROM reviews;

-- find places that cost $20 or less
SELECT *
FROM places
WHERE price_point = '$'
    OR price_point = '$$';

-- join tables
SELECT places.name, places.average_rating, reviews.username, reviews.rating, reviews.review_date, reviews.note
FROM places
INNER JOIN reviews
    ON places.id = reviews.place_id;

-- left join
SELECT places.name, places.average_rating, reviews.username, reviews.rating, reviews.review_date, reviews.note
FROM places
LEFT JOIN reviews
    ON places.id = reviews.place_id;

-- places that do not have reviews
SELECT places.id, places.name
FROM places
LEFT JOIN reviews
    ON places.id = reviews.place_id
WHERE reviews.place_id IS NULL;

-- query reviews that happened in 2020
WITH reviews_2020 AS(
    SELECT *
    FROM reviews
    WHERE strftime('%Y', review_date) = '2020'
);