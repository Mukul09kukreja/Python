results = ["Mario", "Luigi"]

results.append("Princess Peter")
results.append("Youshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Broser", "Donkey Kong Jr."])
results.remove(["Broser", "Donkey Kong Jr."])
results.extend(["Broser", "Donkey Kong Jr."])

results.remove("Broser")
results.insert(0, "Broser")

print(results)