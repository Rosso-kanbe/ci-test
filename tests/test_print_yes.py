import pytest
from print_yes import print_yes

def test_print_yes():
	assert print_yes() == 'yes'
