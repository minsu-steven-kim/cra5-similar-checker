MAX_ALPHA_SIMILAR = 40


class SimilarChecker:
    def __init__(self):
        pass

    def check_alphabet(self, a, b):
        a_alphabets = set(a)
        b_alphabets = set(b)

        total_count = len(a_alphabets.union(b_alphabets))
        same_count = len(a_alphabets.intersection(b_alphabets))

        return MAX_ALPHA_SIMILAR * same_count // total_count
