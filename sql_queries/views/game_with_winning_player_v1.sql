CREATE
OR REPLACE VIEW game_with_winning_and_starting_players AS
select id, numplayers,
(
select 
    p.name 
from 
    player_with_numturns as p 
join player_game_pair as _p on _p.name = p.name and _p.game_id = p.game_id 
join db_startinghand as sh on sh.player_id = _p.player_id and sh.game_id = p.game_id 
where p.game_id = g.id 
order by number_of_turns DESC, sh.turn_order ASC
limit 1 
) as winning_player_name,
(
select 
    p.name 
from 
    player_with_numturns as p 
join player_game_pair as _p on _p.name = p.name and _p.game_id = p.game_id 
join db_startinghand as sh on sh.player_id = _p.player_id and sh.game_id = p.game_id 
where p.game_id = g.id 
order by sh.turn_order ASC
limit 1 
) as starting_player_name
from game_with_numplayers as g where numplayers > 1