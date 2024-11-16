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
(numnones::float) / (numturns::float) as percentnones
FROM player_game_stats