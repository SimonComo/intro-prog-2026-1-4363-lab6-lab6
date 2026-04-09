scores = {}

while True:
    entrada = input("Enter player and score as 'name score' (or type 'stop' to finish):\n")

    if entrada.lower() == "stop":
        break

    name, score = entrada.split()
    score = int(score)

    if name in scores:
        scores[name] += score
    else:
        scores[name] = score

if len(scores) == 0:
    print("No scores recorded.")
else:
    top_name = max(scores, key=scores.get)
    print(f"Top scorer: {top_name} with {scores[top_name]} points.")