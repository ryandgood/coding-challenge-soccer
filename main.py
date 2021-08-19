import argparse
import typing
from pprint import pprint
from operator import itemgetter


def parse_input(input_path: str) -> list:
    """
    parse_input takes in the input file, and breaks it down into
    a managable data structure. It returns a list of matches,
    with each match represented as a tuple. This tuple is
    itself composed of two tuples, one for each team and their score.
    Tuples all the way down, really.
    """
    parsed_input = []
    matches = []

    with open(input_path, "r") as f:
        for line in f:
            line = line.rstrip()
            matches.append(line.split(sep=", "))
    for match in matches:
        first_team = match[0].rsplit(" ", 1)
        second_team = match[1].rsplit(" ", 1)
        try:
            first_team_parsed = first_team[0], int(first_team[1])
            second_team_parsed = second_team[0], int(second_team[1])
        except ValueError:
            print(
                f"Bad score for match between {first_team_parsed[0]} and {second_team_parsed[0]}, skipping"
            )
            continue
        match_tuple = first_team_parsed, second_team_parsed
        parsed_input.append(match_tuple)
    return parsed_input


def calculate_standings(parsed_input):
    """
    calculate_standings takes the parsed input, and determines the winner
    of each match. If a team has already played, it adds the daily ranking
    to the match_history dictionary and begins a new
    """
    day_count = 1
    daily_ranking = {}
    played_today = []
    for match_data in parsed_input:
        team_one, team_one_score = match_data[0]
        team_two, team_two_score = match_data[1]
        team_one_rank = daily_ranking.get(team_one, 0)
        team_two_rank = daily_ranking.get(team_two, 0)

        if team_one_score > team_two_score:
            team_one_rank += 3
        elif team_one_score < team_two_score:
            team_two_rank += 3
        elif team_one_score == team_two_score:
            team_one_rank += 1
            team_two_rank += 1

        # if a team has already played, it's safe to assume a new day
        if team_one in played_today or team_two in played_today:
            output_prettily(daily_ranking, day_count)
            played_today.clear()
            day_count += 1

        # update the daily rankings per team.
        daily_ranking[team_one] = team_one_rank
        daily_ranking[team_two] = team_two_rank
        played_today.append(team_one)
        played_today.append(team_two)

    # For the final day, we won't hit the last played_today check
    # so we need to call it one more time here.
    output_prettily(daily_ranking, day_count)


def output_prettily(daily_ranking: dict, day: int):
    """
    output_prettily will write the rankings to stdout in the format required.
    """
    count = 0
    ranked = sorted(daily_ranking.items(), key=itemgetter(1), reverse=True)
    print("Matchday " + str(day))
    while count < 3:
        team, score = ranked[count]
        print(team + ", " + str(score) + " pts")
        count += 1
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Calculate soccer rankings after each match day"
    )
    parser.add_argument(
        "--input_path", help="path to a file containing matches", required=True
    )
    parser.add_argument(
        "--output_path",
        help="path to output results to. Defaults to STDOUT if not set.",
        required=False,
    )
    args = parser.parse_args()

    match_list = parse_input(args.input_path)
    calculate_standings(match_list)


if __name__ == "__main__":
    main()