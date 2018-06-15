import pytest
import pyuml2.standard as standard


def test_standard_nsURI():
    assert standard.nsURI == 'http://www.eclipse.org/uml2/5.0.0/UML/Profile/Standard'
