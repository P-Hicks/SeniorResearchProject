CREATE
OR REPLACE VIEW player_game_stats_outer AS
select 
name,
player_id, 
game_id, 
numturns,
numdiscards,
numdraws,
numnones,
(numdiscards::float) / (numturns::float) as percentdiscards,
(numdraws::float) / (numturns::float) as percentdraws,
(numnones::float) / (numturns::float) as percentnones,
avg_computational_time
FROM player_game_stats