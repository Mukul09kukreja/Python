def main():
    counts = {}
    words = get_args("address.txt")
    lowercase_words = []

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    value_counts(counts)

main()