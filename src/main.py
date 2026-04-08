"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import sys
from src.recommender import load_songs, recommend_songs
from tabulate import tabulate


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    songs = load_songs("data/songs.csv")

    pop_fan = {"genre": "pop", "mood": "happy", "target_energy": 0.8, "target_valence": 0.85, "target_danceability": 0.8}
    lofi_listener = {"genre": "lofi", "mood": "chill", "target_energy": 0.35, "target_valence": 0.6, "target_danceability": 0.55}
    rock_head = {"genre": "rock", "mood": "intense", "target_energy": 0.9, "target_valence": 0.45, "target_danceability": 0.65}

    profiles = [("Pop Fan", pop_fan), ("Lofi Listener", lofi_listener), ("Rock Head", rock_head)]

    for label, user_prefs in profiles:
        print(f"\n===== Recommendations for: {label} =====")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        table_rows = []
        for song, score, explanation in recommendations:
            row = [song["title"], song["artist"], round(score, 2), explanation]
            table_rows.append(row)
        headers = ["Title", "Artist", "Score", "Reasons"]
        print(tabulate(table_rows, headers=headers, tablefmt="rounded_outline"))
        print()

    modes = ["genre_first", "energy_focused", "mood_first"]

    for mode in modes:
        print(f"\n===== Mode: {mode} | Profile: Pop Fan =====")
        recommendations = recommend_songs(pop_fan, songs, k=5, mode=mode)
        table_rows = []
        for song, score, explanation in recommendations:
            row = [song["title"], song["artist"], round(score, 2), explanation]
            table_rows.append(row)
        headers = ["Title", "Artist", "Score", "Reasons"]
        print(tabulate(table_rows, headers=headers, tablefmt="rounded_outline"))
        print()


if __name__ == "__main__":
    main()
