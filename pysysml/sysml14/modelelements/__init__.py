
from .modelelements import getEClassifier, eClassifiers
from .modelelements import name, nsURI, nsPrefix, eClass
from .modelelements import Conform, ElementGroup, Expose, Problem, Rationale, Stakeholder, View, Viewpoint

from pyuml2.uml import Generalization, Class, Comment, Behavior, Dependency, Classifier, Element

from . import modelelements
from .. import sysml14


__all__ = ['Conform', 'ElementGroup', 'Expose', 'Problem',
           'Rationale', 'Stakeholder', 'View', 'Viewpoint']

eSubpackages = []
eSuperPackage = sysml14
modelelements.eSubpackages = eSubpackages
modelelements.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
