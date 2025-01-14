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
            assert seq[2] == "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7\"94(>7='(!5\"2/!%\"4#32="
        if count == 1:
            assert seq[1] == 'CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG'
            assert seq[2] == "'(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,,:%0!<),%646<8#%\".\"-'*-0:.+*&$5!'8)(%3*+9/&/%=363*,6$20($97,\""
        count += 1
        #idk how to test qualitystring because it has "" in it
        print(seq[2])

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    good_fasta = FastqParser('data/test.fa')

    next_seq = next(iter(good_fasta))
    assert next_seq[0] is None

