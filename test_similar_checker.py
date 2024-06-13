from unittest import TestCase

from similar_checker import SimilarChecker


class TestSimilarChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.checker = SimilarChecker()

    def test_same_length(self):
        a = 'ASD'
        b = 'DSA'
        self.assertEqual(60, self.checker.check_length(a, b))

    def test_length_similar_0(self):
        a = 'A'
        b = 'BB'
        self.assertEqual(0, self.checker.check_length(a, b))
