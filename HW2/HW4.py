def get_most_frequent(words, k):
    a = set(words)
    b = {}
    for i in a:
        b[words.count(i)] = b.get(words.count(i), [])
        b[words.count(i)].append(i)
    answer = [b.get(x) for x in sorted(list(b.keys()), reverse = True)]
    return answer[:k]
if __name__ == "__main__":
    print(get_most_frequent(["hello", "world", "hello", "my", "dear", "world", "hello"], 3))