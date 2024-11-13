SELECT
    avg(sub.number_of_turns),
    stddev(sub.number_of_turns),
    variance(sub.number_of_turns),
    min(sub.number_of_turns),
    max(sub.number_of_turns),
    sub.name,
    sub.numplayers
FROM
    (
        SELECT
            count(turns.id) as number_of_turns,
            turns.game_id as game_id,
            player.name as name,
            game.numplayers
        FROM
            db_player as player
            JOIN db_turn as turns ON turns.player_id = player.id
            JOIN (
                select
                    game.id as id,
                    count(startinghand.id) as numplayers
                from
                    db_game as game
                    JOIN db_startinghand AS startinghand ON startinghand.game_id = game.id
                GROUP BY
                    game.id
            ) as game ON turns.game_id = game.id
        GROUP BY
            player.name,
            turns.game_id,
            game.numplayers
    ) as sub
GROUP BY
    sub.name,
    sub.numplayers
ORDER BY
    sub.name,
    sub.numplayers