import pytest
import re

string = 'ee.huliselan@st.hanze.nl'
voornaam = r'[A-Za-z]'
achternaam = r'[A-Za-z]'
email = r'[A-za-z0-9][A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-za-z]{2,})'

def test_person_from_csv(person):
    with pytest.raises(ValueError):
        assert person_creator(person[0]) == 'ee.huliselan@st.hanze.nl'

def test_person_from_csv1():
    with pytest.raises(ValueError):
        assert person_creator(person[1]) == 'Efran'

def test_person_from_csv2():
    with pytest.raises(ValueError):
        assert person_creator(person[2]) == 'Huliselan'

def test_person_from_csv3():
    with pytest.raises(ValueError):
        assert person_creator(person[3]) == 'ADMIN'






