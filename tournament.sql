-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database if exists tournament;
create database tournament;
\c tournament



--PLAYERS TABLE
create table players (
player_id serial primary key,
name text
);

--MATCHES TABLES
create table matches (
match_id serial primary key,
winner int,
loser int
);

-- The View 'playerwins' stores playerid and number of wins for each player
create view playerwins (playerid, wins) as select winner, count(winner) from matches group by winner;

--The View 'playertotalmatches' stores the playerid and the total number of matches this player has played
create view playertotalmatches (playerid, matches) as select players.player_id, count(*) from players, matches where players.player_id = winner or players.player_id=loser group by players.player_id;

--The View 'playerstandingsid' lists a player's rankings by id and stores (playersid, wins, matchesplayed). Using left join to incorporate for players that have had no wins.
-- coalesce(wins,0) replaces Null value under wins colums (for players with no wins) to 0
create view playerstandingsid as select playertotalmatches.playerid, coalesce(wins,0) as wins, matches from playertotalmatches left join playerwins on playerwins.playerid=playertotalmatches.playerid;
 
 --The View 'playerstandings' stores player rankings for all players including the one's who have played no matches so far. It has player id, name, wins and matches info.
 -- coalesce(matches,0) replaces Null alue under matches colums (for players with no matches played) to 0
 create view playerstandings as select player_id, name,coalesce(wins,0)as wins , coalesce(matches,0)as matches from players left join playerstandingsid on  playerstandingsid.playerid=players.player_id;