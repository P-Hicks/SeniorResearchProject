DROP VIEW IF EXISTS player_with_numturns;

CREATE VIEW
    player_with_numturns AS
SELECT
    count(turns.id) as number_of_turns,
    -- turns.game_id as game_id,
    player.id as id,
    player.name as name,
    game.id as game_id,
    game.seed as game_seed,
    game.numplayers as numplayers
FROM
    db_player as player
    JOIN db_turn as turns ON turns.player_id = player.id
    JOIN game_with_numplayers as game ON turns.game_id = game.id
GROUP BY
    player.name,
    player.id,
    game.id,
    game.seed,
    game.numplayers