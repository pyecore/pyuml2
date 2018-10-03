
from .deprecatedelements import getEClassifier, eClassifiers
from .deprecatedelements import name, nsURI, nsPrefix, eClass
from .deprecatedelements import FlowPort, FlowSpecification

from pyuml2.uml import Port, Interface

from . import deprecatedelements
from .. import sysml14


__all__ = ['FlowPort', 'FlowSpecification']

eSubpackages = []
eSuperPackage = sysml14
deprecatedelements.eSubpackages = eSubpackages
deprecatedelements.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
