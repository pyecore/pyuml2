
from .types import getEClassifier, eClassifiers
from .types import name, nsURI, nsPrefix, eClass
from .types import Boolean, Integer, Real, String, UnlimitedNatural


from . import types

__all__ = ['Boolean', 'Integer', 'Real', 'String', 'UnlimitedNatural']

eSubpackages = []
eSuperPackage = None
types.eSubpackages = eSubpackages
types.eSuperPackage = eSuperPackage


otherClassifiers = [Boolean, Integer, Real, String, UnlimitedNatural]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
