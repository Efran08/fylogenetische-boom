import unittest

class test_sequences(unittest.TestCase):
    def test_sequence_1(self):
        found = (['ATGCCGAT'])
        expected = (['ATGCCGAT']) == True
        self.assertEqual(found, expected)

    def test_sequence_2(self):
        found = (['AUGCAUGC'])
        expected = (['AUGCAUGC']) == True
        self.assertEqual(found, expected)

    def test_sequence_3(self):
        found = (['AUGTAGUT'])
        expected = (['AUGTAGUT']) == False
        self.assertEqual(found, expected)

    def test_sequence_4(self):
        found = (['BJOXZBJOXZ'])
        expected = (['BJOXZBJOXZ']) == False
        self.assertEqual(found, expected)

    def test_sequence_5(self):
        found = (['ACDEFGH'])
        expected = (['ACDEFGH']) == True
        self.assertEqual(found, expected)

    def test_sequence_6(self):
        found = (['IKLMNP'])
        expected = (['IKLMNP']) == True
        self.assertEqual(found, expected)

    def test_sequence_7(self):
        found = (['QRSTVWY'])
        expected = (['QRSTVWY']) == True
        self.assertEqual(found, expected)

if __name__ == '__main__':
    unittest.main()
