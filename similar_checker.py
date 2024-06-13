MAX_LENGTH_SIMILAR = 60


class SimilarChecker:
    def __init__(self):
        pass

    def check_length(self, a, b):
        big = max(len(a), len(b))
        small = min(len(a), len(b))
        return MAX_LENGTH_SIMILAR - MAX_LENGTH_SIMILAR // small * (big - small)
