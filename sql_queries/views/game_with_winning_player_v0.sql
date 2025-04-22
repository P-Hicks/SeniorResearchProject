select id, numplayers,
(
select name from player_with_numturns as p where p.game_id = g.id order by number_of_turns DESC limit 1 
) as winning_player_name
from game_with_numplayers as g where numplayers > 1