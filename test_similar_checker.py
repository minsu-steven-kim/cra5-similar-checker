from unittest import TestCase

from similar_checker import SimilarChecker


class TestSimilarChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.checker = SimilarChecker()

    def test_alphabet_similar(self):
        test_cases = [
            (40, 'ASD', 'DSA'),
            (0, 'A', 'BB'),
            (40, 'AAABB', 'BAA'),
            (20, 'AA', 'AAE')
        ]
        for tc in test_cases:
            with self.subTest(tc):
                self.assertEqual(tc[0], self.checker.check_alphabet(tc[1], tc[2]))
