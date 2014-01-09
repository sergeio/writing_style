from collections import defaultdict
from math import sqrt
import re


def dot_product(v1, v2):
    """Get the dot product of the two vectors.

    if A = [a1, a2, a3] && B = [b1, b2, b3]; then
    dot_product(A, B) == (a1 * b1) + (a2 * b2) + (a3 * b3)
    true

    Input vectors must be the same length.

    """
    return sum(a * b for a, b in zip(v1, v2))


def magnitude(vector):
    """Returns the numerical length / magnitude of the vector."""
    return sqrt(dot_product(vector, vector))


def similarity(v1, v2):
    """Ratio of the dot product & the product of the magnitudes of vectors."""
    return dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))


def word_frequencies(word_vector):
    """What percent of the time does each word in the vector appear?

    Returns a dictionary mapping each word to its frequency.

    """
    num_words = len(word_vector)
    frequencies = defaultdict(float)
    for word in word_vector:
        frequencies[word] += 1.0 / num_words

    return dict(frequencies)


def compare_vectors(word_vector1, word_vector2):
    """Numerical similarity between lists of words. Higher is better.

    Uses cosine similarity.
    Result range: 0 (bad) - 1 (uses all the same words in the same proportions)

    """
    all_words = list(set(word_vector1).union(set(word_vector2)))
    frequency_dict1 = word_frequencies(word_vector1)
    frequency_dict2 = word_frequencies(word_vector2)

    frequency_vector1 = [frequency_dict1.get(word, 0) for word in all_words]
    frequency_vector2 = [frequency_dict2.get(word, 0) for word in all_words]

    return similarity(frequency_vector1, frequency_vector2)


def vectorize_text(text):
    """Takes in text, processes it, and vectorizes it."""

    def remove_punctuation(text):
        """Removes special characters from text."""
        return re.sub('[,.?";:\-!@#$%^&*()]', '', text)

    def remove_common_words(text_vector):
        """Removes 50 most common words in the uk english.

        source: http://www.bckelk.ukfsn.org/words/uk1000n.html

        """
        common_words = set(['the', 'and', 'to', 'of', 'a', 'I', 'in', 'was',
            'he', 'that', 'it', 'his', 'her', 'you', 'as', 'had', 'with',
            'for', 'she', 'not', 'at', 'but', 'be', 'my', 'on', 'have', 'him',
            'is', 'said', 'me', 'which', 'by', 'so', 'this', 'all', 'from',
            'they', 'no', 'were', 'if', 'would', 'or', 'when', 'what', 'there',
            'been', 'one', 'could', 'very', 'an', 'who'])
        return [word for word in text_vector if word not in common_words]

    text = text.lower()
    text = remove_punctuation(text)
    words_list = text.split()
    words_list = remove_common_words(words_list)

    return words_list


def compare_texts(text1, text2):
    """How similar are the two input paragraphs?"""
    return compare_vectors(vectorize_text(text1), vectorize_text(text2))
