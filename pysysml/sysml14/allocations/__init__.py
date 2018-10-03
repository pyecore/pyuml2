
from .allocations import getEClassifier, eClassifiers
from .allocations import name, nsURI, nsPrefix, eClass
from .allocations import Allocate, AllocateActivityPartition

from pyuml2.uml import DirectedRelationship, Abstraction, ActivityPartition, Property, Classifier

from . import allocations
from .. import sysml14


__all__ = ['Allocate', 'AllocateActivityPartition']

eSubpackages = []
eSuperPackage = sysml14
allocations.eSubpackages = eSubpackages
allocations.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
