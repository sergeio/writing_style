from collections import defaultdict
from math import sqrt
from re import split, sub


INPUT_TEXT = """
I love the idea of just carrying a paper / pen to write thoughts as they come,
but there's no way I can write fast enough to keep up.  There's no way I would
have produced this email if I were writing with a pen instead of typing.

I would have gotten frustrated and stopped typing.  I would have been trying to
write down the thoughts I had minutes ago, their memories leaking, fading.  I
couldn't play with thought-tangents, because I'd be working to capture ideas of
the past.

Maybe I should learn journalists' shorthand.
"""


def average(numbers):
    # maybe rewrite this to not materialize the array
    numbers = list(numbers)
    return sum(numbers) / (len(numbers) or 1)


def stdev(numbers):
    numbers = list(numbers)
    avg = average(numbers)
    return sqrt(average([(x - avg) * (x - avg) for x in numbers]))


def word_lengths(text):
    text = sub('[`~!.!@#$%^&*()_\-\=\+{}\\\|<>/.?\'",]', '', text)
    return map(len, text.split())


def average_word_lengths(text):
    return average(word_lengths(text))


def stdev_word_lengths(text):
    return stdev(word_lengths(text))


def sentence_lengths(text):
    text = text.strip()
    # handle elipses
    text = text.replace('...', '.')
    # Remove punctuation from the very end so splitting works
    if text and text[-1] in '!.?':
        text = text[:-1]
    sentences = split('[.?!]', text)
    return (len(sentence.split()) for sentence in sentences)


def average_sentence_lengths(text):
    return average(sentence_lengths(text))


def stdev_sentence_lengths(text):
    return stdev(sentence_lengths(text))


def punctuation_ratios(text):
    counts = defaultdict(float)
    total_punctuation = 0
    punctuation = set('`~!@#$%^&*()_-=+[]{}\\|<>/.?\'",')
    for letter in text:
        if letter in punctuation:
            counts[letter] += 1
            total_punctuation += 1

    # Turn counts into percentages
    for key in counts:
        counts[key] = counts[key] / total_punctuation

    return dict(counts)


# cosine distance from works of shakespeare, OTHERS in public domain!

def main():

    criteria = {
        'average_word_lengths': average_word_lengths,
        'stdev_word_lengths': stdev_word_lengths,
        'average_sentence_lengths': average_sentence_lengths,
        'stdev_sentence_lengths': stdev_sentence_lengths,
    }

    for name, function in criteria.items():
        print(name, function(INPUT_TEXT))
    print()

if __name__ == '__main__':
    main()
