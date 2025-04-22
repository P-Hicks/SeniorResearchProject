SELECT
    name,
    numplayers,
    avg(number_of_turns),
    stddev (number_of_turns),
    variance (number_of_turns),
    min(number_of_turns),
    max(number_of_turns)
FROM
    player_with_numturns
GROUP BY
    name,
    numplayers
ORDER BY
    name,
    numplayers