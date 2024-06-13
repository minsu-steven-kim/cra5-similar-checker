MAX_ALPHA_SIMILAR = 40


class SimilarChecker:
    def __init__(self):
        pass

    def check_alphabet(self, a, b):
        a_alphabets = set()
        b_alphabets = set()
        for alphabet in a:
            a_alphabets.add(alphabet)
        for alphabet in b:
            b_alphabets.add(alphabet)

        all_alphabets = set()
        same_count = 0
        total_count = 0
        for alphabet in a_alphabets:
            if alphabet not in all_alphabets:
                all_alphabets.add(alphabet)
                total_count += 1
                if alphabet in b_alphabets:
                    same_count += 1
        for alphabet in b_alphabets:
            if alphabet not in all_alphabets:
                all_alphabets.add(alphabet)
                total_count += 1

        return MAX_ALPHA_SIMILAR * same_count // total_count
