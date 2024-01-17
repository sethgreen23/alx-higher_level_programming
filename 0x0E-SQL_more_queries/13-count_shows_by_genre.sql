-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genre, COUNT(tv_shows.id) AS "number_of_shows" FROM tv_shows, tv_show_genres,tv_genres WHERE tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id GROUP BY genre;
