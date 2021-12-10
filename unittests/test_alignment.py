from hypothesis import given, settings
from hypothesis.strategies import text

from pyaliner import as_cigar, align, GAP

settings_ = settings(max_examples=1000)


@given(text(min_size=1).filter(lambda t: GAP not in t))
@settings_
def test_alignment_of_identical_sequences_return_the_sequences(sequence:str):
    assert align(tuple(sequence), tuple(sequence)) == (tuple(sequence), tuple(sequence))


@given(text(min_size=2).filter(lambda t: GAP not in t))
@settings_
def test_alignment_of_shorter_sequences_should_contain_gaps(sequence:str):
    assert align(tuple(sequence), tuple(sequence)[:-1]) == (tuple(sequence), tuple(sequence[:-1] + GAP))


@given(text(min_size=1).filter(lambda t: GAP not in t), text(min_size=1, max_size=1))
@settings_
def test_alignment_of_mismatched_chars_should_contain_substitution(sequence:str, char:str):
    assert align(tuple(sequence), tuple(char + sequence[1:])) == (tuple(sequence), tuple(char + sequence[1:]))


def test_correctly_represents_alignment_as_cigar():
    left = '"', 'The', 'm', 'c', 'p', 'g', '-', 'binding', 'domain', 'of', 'human', 'm', 'b', 'd', 'three', 'does', \
           'not', 'bind', 'to', 'm', 'c', 'p', 'g', 'but', 'interacts', 'with', '⎵', '⎵', '⎵', 'NuRD', '/', '⎵', 'Mi', \
           'two', 'components', 'h', 'd', 'a', 'c', 'one', 'and', 'm', 't', 'a', 'two', '"', '.'

    right = '"', 'The', 'm', 'c', 'p', 'g', '-', 'binding', 'domain', 'of', 'human', 'm', 'b', 'd', 'three', 'does', \
            'not', 'bind', 'to', 'm', 'c', 'p', 'g', 'but', 'interacts', 'with', 'n', 'u', 'r', 'd', '/', 'm', 'i', \
            'two', 'components', 'h', 'd', 'a', 'c', 'one', 'and', 'm', 't', 'a', 'two', '"', '.'

    assert as_cigar(left, right) == '26=3D1X1=1D1X14='
