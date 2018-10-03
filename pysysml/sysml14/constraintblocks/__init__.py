
from .constraintblocks import getEClassifier, eClassifiers
from .constraintblocks import name, nsURI, nsPrefix, eClass
from .constraintblocks import ConstraintBlock

from pyuml2.uml import Class

from . import constraintblocks
from .. import sysml14


__all__ = ['ConstraintBlock']

eSubpackages = []
eSuperPackage = sysml14
constraintblocks.eSubpackages = eSubpackages
constraintblocks.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
