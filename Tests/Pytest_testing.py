import pytest


@pytest.mark.parametrize('sequences', 'expected', [(['ATGCCGAT'], 'ATGCCGAT'),
                                                   (['AUGCAUGC'], 'AUGCAUGC'),
                                                   (['AUGTAGUT'], 'AUGTAGUT'),
                                                   (['BJOXZBJOXZ'], 'BJOXZBJOXZ'),
                                                   (['ACDEFGH'], 'ACDEFGH'),
                                                   (['IKLMNP'], 'IKLMNP'),
                                                   (['QRSTVWY'], 'QRSTVWY')])

def test_sequences(sequences, expected):
    assert sequences == expected
