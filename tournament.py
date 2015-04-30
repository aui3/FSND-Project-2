#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect(dbname="tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("delete from matches")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("delete from players")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("select count (name) from players")
    # Fetch the one record returned by the select statement
    result = cursor.fetchone()
    DB.close()
    # Return the first entry in the tuyple returned. This is count of players
    return result[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    cursor = DB.cursor()
    # Protect against sql injection attack by passing the data as tuple params
    cursor.execute("insert into players (name) values (%s)", (name, ))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    cursor = DB.cursor()
    # Uses views to get player standings :
    # 1. Aggregate and count wins of players by player id from the 'matches'
    #    table ('playerwins' View)
    # 2. Join the 'players' and 'matches' table on both winner and loser colums
    #    to get a view representing
    #    the total number of matches played by each player 'playertotalmatches'
    #    View
    # 3. Perform a left outer Join on the above two views to get the total
    #    number of matches each player has played and total number of matches
    #    each player has won by playerid ('playerstandingsid' view)
    # 4. To get all players (even players with no matches played) perform a
    #    left outer join of the view from #3
    #    with the 'players' table
    cursor.execute("select player_id, name, coalesce(wins, 0)as wins,\
                   coalesce(matches, 0)as matches from players left join\
                   playerstandingsid on\
                   playerstandingsid.playerid=players.player_id")
    result = cursor.fetchall()
    DB.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    cursor = DB.cursor()
    # Avoid sql injection attack by passing data as a tuple
    cursor.execute("insert into matches (winner, loser) values (%s, %s)",
                   (winner, loser))
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    cursor = DB.cursor()
    # The view playerstandings stores (playerid, name, wins, matches) similar
    # to the list returned
    # by palyerStandings()
    # Sort on wins column descending puts the player with the highest wins at
    # the top.
    cursor.execute("select * from playerstandings order by wins desc")
    result = cursor.fetchall()
    # List to store the tuples of pairs
    pairs = []
    # given even number of players, swiss pairings would be of adjacents rows
    # in the view 'playerstandings'
    # create pairs of adjacent rows in the view playerstandings and
    # add them to the list
    for i in range(0, len(result)-1, 2):
        r = (result[i][0], result[i][1], result[i+1][0], result[i+1][1])
        pairs.append(r)
    DB.commit()
    DB.close()
    return pairs
