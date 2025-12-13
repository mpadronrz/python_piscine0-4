#! /usr/bin/env python3


def get_data():
    data = {
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 21,
                "favorite_mode": "casual",
                "achievements_count": 4,
            },
            "eve": {
                "level": 33,
                "total_score": 1434,
                "sessions_played": 81,
                "favorite_mode": "casual",
                "achievements_count": 7,
            },
            "frank": {
                "level": 15,
                "total_score": 8359,
                "sessions_played": 85,
                "favorite_mode": "competitive",
                "achievements_count": 1,
            },
        },
        "sessions": [
            {
                "player": "bob",
                "duration_minutes": 94,
                "score": 1831,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 32,
                "score": 1478,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 17,
                "score": 1570,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 98,
                "score": 1981,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 15,
                "score": 2361,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 29,
                "score": 2985,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 34,
                "score": 1285,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "alice",
                "duration_minutes": 53,
                "score": 1238,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 1555,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 92,
                "score": 2754,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 98,
                "score": 1102,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 39,
                "score": 2721,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 46,
                "score": 329,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 56,
                "score": 1196,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 117,
                "score": 1388,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 118,
                "score": 2733,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 22,
                "score": 1110,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 79,
                "score": 1854,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "charlie",
                "duration_minutes": 33,
                "score": 666,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 101,
                "score": 292,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 25,
                "score": 2887,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 53,
                "score": 2540,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 115,
                "score": 147,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 118,
                "score": 2299,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 42,
                "score": 1880,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 97,
                "score": 1178,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 18,
                "score": 2661,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 761,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 46,
                "score": 2101,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 117,
                "score": 1359,
                "mode": "casual",
                "completed": True,
            },
        ],
        "game_modes": ["casual", "competitive", "ranked"],
        "achievements": [
            "first_blood",
            "level_master",
            "speed_runner",
            "treasure_seeker",
            "boss_hunter",
            "pixel_perfect",
            "combo_king",
            "explorer",
        ],
    }
    return data


def test_list_comprehensions(data):
    print("=== List Comprehension Examples ===")
    players = data["players"]

    high_scorers = [player for player, info in players.items()
                    if info["total_score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [2 * info["total_score"] for info in players.values()]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [player for player in players]
    print(f"Active players: {active_players}")


def test_dict_comprehensions(data):
    print("=== Dict Comprehension Examples ===")
    players = data["players"]
    score_levels = [
        ("low", 0, 1499),
        ("medium", 1500, 2999),
        ("high", 3000, 10000)
    ]

    player_scores = {
        player: info["total_score"] for player, info in players.items()
    }
    print(f"Player scores: {player_scores}")

    score_categories = {
        score[0]:
        sum(1 for info in players.values()
            if score[1] <= info["total_score"] <= score[2])
        for score in score_levels
    }
    print(f"Score categories: {score_categories}")

    achievement_count = {
        player: info["achievements_count"] for player, info in players.items()
    }
    print(f"Achievement counts: {achievement_count}")


def test_set_comprehensions(data):
    print("=== Set Comprehension Examples ===")
    players = data["players"]

    unique_players = {player for player in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {achivement for achivement in data["achievements"]}
    print(f"Unique achievements: {unique_achievements}")

    unique_gamemodes = {info["favorite_mode"] for info in players.values()}
    print(f"Diferent gamemodes: {unique_gamemodes}")


def combined_analysis(data):
    players = data["players"]

    total_players = len(players)
    print(f"Total players: {total_players}")

    total_achievements = len({
        achivement for achivement in data["achievements"]
    })
    print(f"Total unique achievements: {total_achievements}")

    average_score = sum(
        info["total_score"] for info in players.values()
    ) / total_players
    print(f"Average score: {average_score}")

    def player_score(player: str) -> int:
        return players[player]["total_score"]

    top_performer = sorted(players, key=player_score)[-1]
    print(f"Top performer: {top_performer} "
          f"({players[top_performer]["total_score"]} points, "
          f"{players[top_performer]["achievements_count"]} achievements)")


def main() -> None:
    data = get_data()
    print("=== Game Analytics Dashboard ===")
    print()
    test_list_comprehensions(data)
    print()
    test_dict_comprehensions(data)
    print()
    test_set_comprehensions(data)
    print()
    combined_analysis(data)


if __name__ == "__main__":
    main()
