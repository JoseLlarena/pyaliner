import sys
from io import StringIO

from pyaliner import compare_true_pred, COMPACT, CLASSIC, GAP, JOIN


def test_prints_each_sequence_in_its_own_line_joins_mismatches_and_centers_corresponding_tokens():
    console_out = StringIO()
    sys.stdout = console_out

    compare_true_pred(['Example valid'.split(), 'Example invalid invalid output'.split()], alignment=COMPACT)

    sys.stdout = sys.__stdout__

    assert console_out.getvalue() == f' Example         valid         \n Example invalid{JOIN}invalid{JOIN}output\n\n'

def test_prints_each_sequence_in_its_own_line_and_centers_corresponding_tokens():
    console_out = StringIO()
    sys.stdout = console_out

    compare_true_pred(['Example valid'.split(), 'Example invalid valid output'.split()], alignment=CLASSIC)

    sys.stdout = sys.__stdout__

    assert console_out.getvalue() == f' Example    {GAP}    valid   {GAP}   \n Example invalid valid output\n\n'
