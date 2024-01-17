-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name AS name FROM tv_genres, tv_show_genres, tv_shows WHERE tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id AND tv_shows.title = 'Dexter' ORDER BY tv_genres.name;
