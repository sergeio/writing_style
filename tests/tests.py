from math import sqrt
from unittest import TestCase, main


from analyzer import (
    average,
    punctuation_ratios,
    sentence_lengths,
    stdev,
    word_lengths,
)


class WhenComputingWordLengths(TestCase):

    def test_zero_length_input(self):
        self.assertEqual(list(word_lengths('')), [])

    def test_one_word(self):
        self.assertEqual(list(word_lengths('love')), [4])

    def test_a_few_words(self):
        self.assertEqual(list(word_lengths('break your loops')), [5, 4, 5])

    def test_simple_punctuation(self):
        self.assertEqual(list(word_lengths('break your loops!')), [5, 4, 5])

    def test_all_punctuation(self):
        self.assertEqual(list(word_lengths('`~!.!@#$%^&*()_-=+{}\\|<>/.?\'",')), [])


class WhenCalculatingAverages(TestCase):

    def test_empty_list(self):
        self.assertEqual(average([]), 0)

    def test_one_element_list(self):
        self.assertEqual(average([13]), 13)

    def test_multi_element_list(self):
        self.assertEqual(average([13, 14, 15, 16, 17]), 15)


class WhenComputingPunctuationRatios(TestCase):

    def test_no_punctuation(self):
        self.assertEqual(punctuation_ratios('love'), {})

    def test_basic_usage(self):
        self.assertEqual(
            punctuation_ratios('Oh. This is awkward!'), {'.': .5, '!': .5})


class WhenComputingAverageSentenceLengths(TestCase):

    def test_empty_string(self):
        self.assertEqual(list(sentence_lengths('')), [0])

    def test_word_no_punctuation(self):
        self.assertEqual(list(sentence_lengths('love')), [1])

    def test_one_sentence(self):
        self.assertEqual(list(sentence_lengths('Hear me!')), [2])

    def test_two_sentences(self):
        self.assertEqual(list(sentence_lengths('What? What did you say?')), [1, 4])

    def test_more_sentences(self):
        self.assertEqual(list(sentence_lengths('Yay! This is great. What do you mean?')), [1, 3, 4])

    def test_elipses(self):
        self.assertEqual(list(sentence_lengths('There is no reason for this... Why?')), [6, 1])


class WhenCalculatingStdevs(TestCase):

    def test_empty_list(self):
        self.assertEqual(stdev([]), 0)

    def test_one_element_list(self):
        self.assertEqual(stdev([5]), 0)

    def test_two_element_list(self):
        self.assertEqual(stdev([5, 7]), 1)

    def test_many_element_list_from_wikipedia(self):
        self.assertEqual(stdev([2, 4, 4, 4, 5, 5, 7, 9]), 2)


if __name__ == '__main__':
    main()
