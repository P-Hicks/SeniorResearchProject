SELECT count(id), numplayers, winning_player_name, starting_player_name 
FROM "game_with_winning_and_starting_players"
group by numplayers, winning_player_name, starting_player_name 