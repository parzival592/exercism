def find_anagrams(word, candidates):
    target = word.lower()
    sorted_letter = sorted(target)
    result = []

    for candidate in candidates:
        lower_candidate = candidate.lower()

        if lower_candidate != target:
            if sorted(lower_candidate) == sorted_letter:
                result.append(candidate)

    return result 
