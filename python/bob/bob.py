def response(hey_bob):
    if not hey_bob.strip():
        return "Fine. Be that way!"

    if hey_bob.isupper() and hey_bob.strip().endswith("?"):
        return "Calm down, I know what I'm doing!"

    if hey_bob.isupper() and any(char.isalpha() for char in hey_bob):
        return "Whoa, chill out!"

    if hey_bob.strip().endswith("?"):
        return "Sure."

    else:
        return "Whatever."