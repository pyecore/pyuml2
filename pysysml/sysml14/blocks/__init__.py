
from .blocks import getEClassifier, eClassifiers
from .blocks import name, nsURI, nsPrefix, eClass
from .blocks import AdjunctProperty, BindingConnector, Block, BoundReference, EndPathMultiplicity, ClassifierBehaviorProperty, ConnectorProperty, DistributedProperty, ElementPropertyPath, NestedConnectorEnd, ParticipantProperty, PropertySpecificType, ValueType, DirectedRelationshipPropertyPath

from pyuml2.uml import Connector, DataType, DirectedRelationship, Class, ConnectorEnd, InstanceSpecification, Property, Classifier, Element

from . import blocks
from .. import sysml14


__all__ = [
    'AdjunctProperty', 'BindingConnector', 'Block', 'BoundReference',
    'EndPathMultiplicity', 'ClassifierBehaviorProperty', 'ConnectorProperty',
    'DistributedProperty', 'ElementPropertyPath', 'NestedConnectorEnd',
    'ParticipantProperty', 'PropertySpecificType', 'ValueType',
    'DirectedRelationshipPropertyPath']

eSubpackages = []
eSuperPackage = sysml14
blocks.eSubpackages = eSubpackages
blocks.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
