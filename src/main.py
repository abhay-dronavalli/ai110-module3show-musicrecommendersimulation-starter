"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    pop_fan = {"genre": "pop", "mood": "happy", "target_energy": 0.8, "target_valence": 0.85, "target_danceability": 0.8}
    lofi_listener = {"genre": "lofi", "mood": "chill", "target_energy": 0.35, "target_valence": 0.6, "target_danceability": 0.55}
    rock_head = {"genre": "rock", "mood": "intense", "target_energy": 0.9, "target_valence": 0.45, "target_danceability": 0.65}

    profiles = [("Pop Fan", pop_fan), ("Lofi Listener", lofi_listener), ("Rock Head", rock_head)]

    for label, user_prefs in profiles:
        print(f"\n===== Recommendations for: {label} =====")
        recommendations = recommend_songs(user_prefs, songs, k=5)
        for song, score, explanation in recommendations:
            print(f"{song['title']} by {song['artist']} | Score: {score:.2f}")
            print(f"  Reasons: {explanation}")
            print()


if __name__ == "__main__":
    main()
