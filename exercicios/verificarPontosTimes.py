times = {
    "Flamengo": {"pontos": 72, "gols": 89},
    "Palmeiras": {"pontos": 68, "gols": 70},
    "Gremio": {"pontos": 45, "gols": 50},
    "Corinthians": {"pontos": 40, "gols": 38},
}

for time, stats in times.items():
    if stats["pontos"] > 60 and stats["gols"] > 75:
        print(time, "CHAMPION")
    elif stats["pontos"] > 60 and stats["gols"] <= 75:
        print(time, "STRONG AF")
    else: 
        print(time, "OUT")