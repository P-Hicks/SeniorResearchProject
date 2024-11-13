DROP VIEW IF EXISTS game_with_numplayers;

CREATE VIEW
    game_with_numplayers AS
SELECT
    game.id as id,
    game.seed as seed,
    count(startinghand.id) as numplayers
FROM
    db_game as game
    JOIN db_startinghand AS startinghand ON startinghand.game_id = game.id
GROUP BY
    game.id;