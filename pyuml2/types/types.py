"""Definition of meta model 'types'."""
from functools import partial
import pyecore.ecore as Ecore


name = 'types'
nsURI = 'http://www.eclipse.org/uml2/5.0.0/Types'
nsPrefix = 'types'

eClass = Ecore.EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)

Boolean = Ecore.EDataType('Boolean', instanceClassName='boolean')
Boolean.to_string = lambda x: str(x).lower()
Boolean.from_string = lambda x: x in ['True', 'true']

Integer = Ecore.EDataType('Integer', instanceClassName='int')
Integer.from_string = lambda x: int(x)

Real = Ecore.EDataType('Real', instanceClassName='double')
Real.from_string = lambda x: float(x)

String = Ecore.EDataType('String', instanceClassName='java.lang.String')

UnlimitedNatural = Ecore.EDataType('UnlimitedNatural', instanceClassName='int')


def unlimited_from_string(x):
    if x == '*':
        return -1
    value = int(x)
    if value >= 0:
        return value
    raise ValueError('UnlimitedNatural must be a >= 0 value')


UnlimitedNatural.from_string = unlimited_from_string
UnlimitedNatural.to_string = lambda x: "*" if x < 0 else str(x)
