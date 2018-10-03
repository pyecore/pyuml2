
from .sysml14 import getEClassifier, eClassifiers
from .sysml14 import name, nsURI, nsPrefix, eClass
from .sysml14 import Dummy


from .activities import Overwrite, ControlOperator, NoBuffer, Rate, Probability, Optional
from .allocations import AllocateActivityPartition, Allocate
from .blocks import ConnectorProperty, ClassifierBehaviorProperty, DistributedProperty, NestedConnectorEnd, ParticipantProperty, DirectedRelationshipPropertyPath, Block, ValueType, AdjunctProperty, ElementPropertyPath, BindingConnector, PropertySpecificType, BoundReference, EndPathMultiplicity
from .deprecatedelements import FlowPort, FlowSpecification
from .portsandflows import InvocationOnNestedPortAction, DirectedFeature, ItemFlow, ProxyPort, FlowProperty, AcceptChangeStructuralFeatureEventAction, ChangeStructuralFeatureEvent, TriggerOnNestedPort, FullPort
from .modelelements import Expose, View, Viewpoint, Rationale, Problem, Stakeholder, ElementGroup, Conform
from .requirements import Requirement, TestCase

from . import sysml14
from . import activities
from . import allocations
from . import blocks
from . import constraintblocks
from . import deprecatedelements
from . import portsandflows
from . import modelelements
from . import requirements

from pyuml2.uml import ActivityEdge, ObjectNode, Parameter, ParameterSet, \
                        Abstraction, ActivityPartition, Property, Connector, \
                        Class, InstanceSpecification, Behavior, Operation, \
                        ConnectorEnd, Classifier, DirectedRelationship, \
                        AcceptEventAction, ChangeEvent, Comment, Dependency, \
                        Port, Trigger, Generalization, InformationFlow, \
                        ValueSpecification, Abstraction, Element, DataType, \
                        Interface, StructuralFeature, Feature, \
                        InvocationAction, NamedElement


__all__ = ['Dummy']

eSubpackages = [activities, allocations, blocks, constraintblocks,
                deprecatedelements, portsandflows, modelelements, requirements]
eSuperPackage = None
sysml14.eSubpackages = eSubpackages
sysml14.eSuperPackage = eSuperPackage

Rate.base_ActivityEdge.eType = ActivityEdge
Rate.base_ObjectNode.eType = ObjectNode
Rate.base_Parameter.eType = Parameter
Rate.rate.eType = InstanceSpecification
ControlOperator.base_Behavior.eType = Behavior
ControlOperator.base_Operation.eType = Operation
NoBuffer.base_ObjectNode.eType = ObjectNode
Optional.base_Parameter.eType = Parameter
Overwrite.base_ObjectNode.eType = ObjectNode
Probability.base_ActivityEdge.eType = ActivityEdge
Probability.base_ParameterSet.eType = ParameterSet
Probability.probability.eType = ValueSpecification
Allocate.base_Abstraction.eType = Abstraction
AllocateActivityPartition.base_ActivityPartition.eType = ActivityPartition
AdjunctProperty.base_Property.eType = Property
AdjunctProperty.principal.eType = Element
BindingConnector.base_Connector.eType = Connector
Block.base_Class.eType = Class
BoundReference.bindingPath.eType = Property
BoundReference.boundEnd.eType = ConnectorEnd
EndPathMultiplicity.base_Property.eType = Property
ClassifierBehaviorProperty.base_Property.eType = Property
ConnectorProperty.base_Property.eType = Property
ConnectorProperty.connector.eType = Connector
DistributedProperty.base_Property.eType = Property
ElementPropertyPath.base_Element.eType = Element
ElementPropertyPath.propertyPath.eType = Property
NestedConnectorEnd.base_ConnectorEnd.eType = ConnectorEnd
ParticipantProperty.base_Property.eType = Property
ParticipantProperty.end.eType = Property
PropertySpecificType.base_Classifier.eType = Classifier
ValueType.base_DataType.eType = DataType
ValueType.quantityKind.eType = InstanceSpecification
ValueType.unit.eType = InstanceSpecification
DirectedRelationshipPropertyPath.base_DirectedRelationship.eType = DirectedRelationship
DirectedRelationshipPropertyPath.sourceContext.eType = Classifier
DirectedRelationshipPropertyPath.sourcePropertyPath.eType = Property
DirectedRelationshipPropertyPath.targetContext.eType = Classifier
DirectedRelationshipPropertyPath.targetPropertyPath.eType = Property
FlowPort.base_Port.eType = Port
FlowSpecification.base_Interface.eType = Interface
AcceptChangeStructuralFeatureEventAction.base_AcceptEventAction.eType = AcceptEventAction
ChangeStructuralFeatureEvent.base_ChangeEvent.eType = ChangeEvent
ChangeStructuralFeatureEvent.structuralFeature.eType = StructuralFeature
DirectedFeature.base_Feature.eType = Feature
FlowProperty.base_Property.eType = Property
FullPort.base_Port.eType = Port
InvocationOnNestedPortAction.base_InvocationAction.eType = InvocationAction
InvocationOnNestedPortAction.onNestedPort.eType = Port
ItemFlow.base_InformationFlow.eType = InformationFlow
ItemFlow.itemProperty.eType = Property
ProxyPort.base_Port.eType = Port
TriggerOnNestedPort.base_Trigger.eType = Trigger
TriggerOnNestedPort.onNestedPort.eType = Port
Conform.base_Generalization.eType = Generalization
ElementGroup.base_Comment.eType = Comment
ElementGroup.member.eType = Element
ElementGroup.orderedMemeber.eType = Element
Expose.base_Dependency.eType = Dependency
Problem.base_Comment.eType = Comment
Rationale.base_Comment.eType = Comment
Stakeholder.base_Classifier.eType = Classifier
Stakeholder.concernList.eType = Comment
View.base_Class.eType = Class
View.stakeholder.eType = Stakeholder
View._viewPoint.eType = Viewpoint
Viewpoint.base_Class.eType = Class
Viewpoint.concernList.eType = Comment
Viewpoint.method.eType = Behavior
Viewpoint.stakeholder.eType = Stakeholder
Requirement.base_Class.eType = Class
Requirement.derived.eType = Requirement
Requirement.derivedFrom.eType = Requirement
Requirement._master.eType = Requirement
Requirement.refinedBy.eType = NamedElement
Requirement.satisfiedBy.eType = NamedElement
Requirement.tracedTo.eType = NamedElement
Requirement.verifiedBy.eType = NamedElement
TestCase.base_Behavior.eType = Behavior
TestCase.base_Operation.eType = Operation

otherClassifiers = [Dummy]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
