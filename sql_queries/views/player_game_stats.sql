CREATE
OR REPLACE VIEW player_game_stats AS
select 
player_game_pair.name as name,
player_game_pair.player_id as player_id, 
player_game_pair.game_id as game_id, 
count(turn.id) as numturns,  
count(turn.id) filter (where turn_type= 'DISCARD') as numdiscards,
count(turn.id) filter (where turn_type= 'DRAW') as numdraws,
count(turn.id) filter (where turn_type= 'NONE') as numnones,
avg(turn.computational_time) as avg_computational_time
FROM player_game_pair 
right join db_turn as turn 
on turn.game_id = player_game_pair.game_id and turn.player_id = player_game_pair.player_id
group by player_game_pair.player_id, player_game_pair.game_id, player_game_pair.name