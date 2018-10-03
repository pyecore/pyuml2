
from .requirements import getEClassifier, eClassifiers
from .requirements import name, nsURI, nsPrefix, eClass
from .requirements import Copy, Trace, Requirement, DeriveReqt, Refine, Satisfy, TestCase, Verify

from pyuml2.uml import DirectedRelationship, NamedElement, Class, Behavior, Property, Operation, Classifier

from . import requirements
from .. import sysml14


__all__ = ['Copy', 'Trace', 'Requirement', 'DeriveReqt',
           'Refine', 'Satisfy', 'TestCase', 'Verify']

eSubpackages = []
eSuperPackage = sysml14
requirements.eSubpackages = eSubpackages
requirements.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
