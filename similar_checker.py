class SimilarChecker:
    def __init__(self):
        pass

    def check_length(self, a, b):
        if len(a) == len(b):
            return 60
        elif len(a) >= 2 * len(b) or len(b) >= 2 * len(a):
            return 0
        else:
            if len(a) >= len(b):
                return 60 - 60 // len(b) * (len(a) - len(b))
            else:
                return 60 - 60 // len(a) * (len(b) - len(a))
