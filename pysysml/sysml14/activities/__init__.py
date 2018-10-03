
from .activities import getEClassifier, eClassifiers
from .activities import name, nsURI, nsPrefix, eClass
from .activities import Continuous, Rate, ControlOperator, Discrete, NoBuffer, Optional, Overwrite, Probability

from pyuml2.uml import ValueSpecification, ObjectNode, Parameter, InstanceSpecification, ActivityEdge, Behavior, Operation, ParameterSet

from . import activities
from .. import sysml14


__all__ = ['Continuous', 'Rate', 'ControlOperator', 'Discrete',
           'NoBuffer', 'Optional', 'Overwrite', 'Probability']

eSubpackages = []
eSuperPackage = sysml14
activities.eSubpackages = eSubpackages
activities.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
