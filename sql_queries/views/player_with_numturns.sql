CREATE
OR REPLACE VIEW player_with_numturns AS
SELECT
    count(turns.id) as number_of_turns,
    -- turns.game_id as game_id,
    player.name as name,
    game.id as game_id,
    game.numplayers as numplayers
FROM
    db_player as player
    JOIN db_turn as turns ON turns.player_id = player.id
    JOIN game_with_numplayers as game ON turns.game_id = game.id
GROUP BY
    player.name,
    game.id,
    game.numplayers