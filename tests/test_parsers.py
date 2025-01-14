# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/blank.fa
    """
    bad_fastp = FastaParser('tests/bad.fa')
    with pytest.raises(ValueError):
        for seq in bad_fastp:
            pass

    empty_fastp = FastaParser('tests/blank.fa')
    with pytest.raises(ValueError):
        for seq in empty_fastp:
            pass
    
    count = 0
    good_fastp = FastaParser('data/test.fa')
    for seq in good_fastp:
        assert isinstance(seq[0], str)
        assert isinstance(seq[1], str)
        if count == 0:
            assert seq[1] == 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
        if count == 1:
            assert seq[1] == 'TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT'
        count += 1


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    good_fastq = FastaParser('data/test.fq')

    next_seq = next(iter(good_fastq))
    assert next_seq[0] is None
    


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    empty_fastq = FastqParser('tests/blank.fa')
    with pytest.raises(ValueError):
        for seq in empty_fastq:
            pass
    
    count = 0
    good_fastp = FastqParser('data/test.fq')
    for seq in good_fastp:
        assert isinstance(seq[0], str)
        assert isinstance(seq[1], str)
        assert isinstance(seq[2], str)
        if count == 0:
            assert seq[1] == 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
        if count == 1:
            assert seq[1] == 'CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG'
        count += 1
        #idk how to test qualitystring because it has "" in it
        print(seq[2])

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    good_fasta = FastaParser('data/test.fq')

    next_seq = next(iter(good_fasta))
    assert next_seq[0] is None

