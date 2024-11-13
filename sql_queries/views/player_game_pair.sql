DROP VIEW IF EXISTS player_game_pair;

CREATE VIEW
    player_game_pair AS
SELECT
    sh.id as startinghand_id,
    sh.created_at,
    sh.updated_at,
    sh.cards,
    sh.player_id,
    player.name as name,
    game.seed as seed,
    game.numplayers as numplayers,
    sh.turn_order,
    sh.game_id
FROM
    db_startinghand AS sh
    JOIN game_with_numplayers AS game ON sh.game_id = game.id
    JOIN db_player AS player ON sh.player_id = player.id;