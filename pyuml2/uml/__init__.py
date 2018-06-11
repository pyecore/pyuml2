
from .uml import getEClassifier, eClassifiers
from .uml import name, nsURI, nsPrefix, eClass
from .uml import ActivityContent, Activity, Behavior, Class, BehavioredClassifier, Classifier, Namespace, NamedElement, Element, Comment, Stereotype, Image, Profile, Package, PackageableElement, ParameterableElement, TemplateParameter, TemplateSignature, TemplateableElement, TemplateBinding, DirectedRelationship, Relationship, TemplateParameterSubstitution, VisibilityKind, Type, Association, Property, ConnectableElement, TypedElement, ConnectorEnd, MultiplicityElement, ValueSpecification, ConnectableElementTemplateParameter, DeploymentTarget, Deployment, Dependency, DeploymentSpecification, Artifact, DeployedArtifact, Manifestation, Abstraction, OpaqueExpression, Parameter, ParameterDirectionKind, ParameterEffectKind, Operation, BehavioralFeature, Feature, RedefinableElement, CallConcurrencyKind, ParameterSet, Constraint, DataType, Interface, Reception, Signal, ProtocolStateMachine, StateMachine, Pseudostate, Vertex, Region, State, ConnectionPointReference, Trigger, Event, Port, Transition, TransitionKind, PseudostateKind, ProtocolConformance, OperationTemplateParameter, StructuralFeature, AggregationKind, PackageMerge, ProfileApplication, Enumeration, EnumerationLiteral, InstanceSpecification, Slot, PrimitiveType, ElementImport, PackageImport, Extension, ExtensionEnd, Model, StringExpression, Expression, Usage, CollaborationUse, Collaboration, StructuredClassifier, Connector, ConnectorKind, Generalization, GeneralizationSet, RedefinableTemplateSignature, UseCase, Extend, ExtensionPoint, Include, Substitution, Realization, ClassifierTemplateParameter, InterfaceRealization, EncapsulatedClassifier, ActivityGroup, ActivityEdge, ActivityPartition, ActivityNode, InterruptibleActivityRegion, StructuredActivityNode, Action, ExecutableNode, ExceptionHandler, ObjectNode, ObjectNodeOrderingKind, InputPin, Pin, OutputPin, Variable, ValueSpecificationAction, VariableAction, WriteLinkAction, LinkAction, LinkEndData, QualifierValue, WriteStructuralFeatureAction, StructuralFeatureAction, WriteVariableAction, ExpansionKind, AcceptCallAction, AcceptEventAction, ActionInputPin, AddStructuralFeatureValueAction, AddVariableValueAction, BroadcastSignalAction, InvocationAction, CallAction, CallBehaviorAction, CallOperationAction, Clause, ClearAssociationAction, ClearStructuralFeatureAction, ClearVariableAction, ConditionalNode, CreateLinkAction, LinkEndCreationData, CreateLinkObjectAction, CreateObjectAction, DestroyLinkAction, LinkEndDestructionData, DestroyObjectAction, ExpansionNode, ExpansionRegion, LoopNode, OpaqueAction, RaiseExceptionAction, ReadExtentAction, ReadIsClassifiedObjectAction, ReadLinkAction, ReadLinkObjectEndAction, ReadLinkObjectEndQualifierAction, ReadSelfAction, ReadStructuralFeatureAction, ReadVariableAction, ReclassifyObjectAction, ReduceAction, RemoveStructuralFeatureValueAction, RemoveVariableValueAction, ReplyAction, SendObjectAction, SendSignalAction, SequenceNode, StartClassifierBehaviorAction, StartObjectBehaviorAction, TestIdentityAction, UnmarshallAction, ValuePin, ActivityFinalNode, FinalNode, ControlNode, ActivityParameterNode, CentralBufferNode, ControlFlow, DataStoreNode, DecisionNode, ObjectFlow, FlowFinalNode, ForkNode, InitialNode, JoinNode, MergeNode, InstanceValue, AnyReceiveEvent, MessageEvent, CallEvent, ChangeEvent, FunctionBehavior, OpaqueBehavior, SignalEvent, TimeEvent, TimeExpression, Observation, CommunicationPath, Device, Node, ExecutionEnvironment, InformationFlow, Message, Interaction, InteractionFragment, Lifeline, PartDecomposition, InteractionUse, Gate, MessageEnd, InteractionOperand, InteractionConstraint, GeneralOrdering, OccurrenceSpecification, MessageKind, MessageSort, InformationItem, ActionExecutionSpecification, ExecutionSpecification, BehaviorExecutionSpecification, CombinedFragment, InteractionOperatorKind, ConsiderIgnoreFragment, Continuation, DestructionOccurrenceSpecification, MessageOccurrenceSpecification, ExecutionOccurrenceSpecification, StateInvariant, FinalState, ProtocolTransition, AssociationClass, Component, ComponentRealization, Actor, Duration, DurationConstraint, IntervalConstraint, Interval, DurationInterval, DurationObservation, LiteralBoolean, LiteralSpecification, LiteralInteger, LiteralNull, LiteralReal, LiteralString, LiteralUnlimitedNatural, TimeConstraint, TimeInterval, TimeObservation


from . import uml

__all__ = [
    'ActivityContent', 'Activity', 'Behavior', 'Class', 'BehavioredClassifier',
    'Classifier', 'Namespace', 'NamedElement', 'Element', 'Comment',
    'Stereotype', 'Image', 'Profile', 'Package', 'PackageableElement',
    'ParameterableElement', 'TemplateParameter', 'TemplateSignature',
    'TemplateableElement', 'TemplateBinding', 'DirectedRelationship',
    'Relationship', 'TemplateParameterSubstitution', 'VisibilityKind', 'Type',
    'Association', 'Property', 'ConnectableElement', 'TypedElement',
    'ConnectorEnd', 'MultiplicityElement', 'ValueSpecification',
    'ConnectableElementTemplateParameter', 'DeploymentTarget', 'Deployment',
    'Dependency', 'DeploymentSpecification', 'Artifact', 'DeployedArtifact',
    'Manifestation', 'Abstraction', 'OpaqueExpression', 'Parameter',
    'ParameterDirectionKind', 'ParameterEffectKind', 'Operation',
    'BehavioralFeature', 'Feature', 'RedefinableElement',
    'CallConcurrencyKind', 'ParameterSet', 'Constraint', 'DataType',
    'Interface', 'Reception', 'Signal', 'ProtocolStateMachine', 'StateMachine',
    'Pseudostate', 'Vertex', 'Region', 'State', 'ConnectionPointReference',
    'Trigger', 'Event', 'Port', 'Transition', 'TransitionKind',
    'PseudostateKind', 'ProtocolConformance', 'OperationTemplateParameter',
    'StructuralFeature', 'AggregationKind', 'PackageMerge',
    'ProfileApplication', 'Enumeration', 'EnumerationLiteral',
    'InstanceSpecification', 'Slot', 'PrimitiveType', 'ElementImport',
    'PackageImport', 'Extension', 'ExtensionEnd', 'Model', 'StringExpression',
    'Expression', 'Usage', 'CollaborationUse', 'Collaboration',
    'StructuredClassifier', 'Connector', 'ConnectorKind', 'Generalization',
    'GeneralizationSet', 'RedefinableTemplateSignature', 'UseCase', 'Extend',
    'ExtensionPoint', 'Include', 'Substitution', 'Realization',
    'ClassifierTemplateParameter', 'InterfaceRealization',
    'EncapsulatedClassifier', 'ActivityGroup', 'ActivityEdge',
    'ActivityPartition', 'ActivityNode', 'InterruptibleActivityRegion',
    'StructuredActivityNode', 'Action', 'ExecutableNode', 'ExceptionHandler',
    'ObjectNode', 'ObjectNodeOrderingKind', 'InputPin', 'Pin', 'OutputPin',
    'Variable', 'ValueSpecificationAction', 'VariableAction',
    'WriteLinkAction', 'LinkAction', 'LinkEndData', 'QualifierValue',
    'WriteStructuralFeatureAction', 'StructuralFeatureAction',
    'WriteVariableAction', 'ExpansionKind', 'AcceptCallAction',
    'AcceptEventAction', 'ActionInputPin', 'AddStructuralFeatureValueAction',
    'AddVariableValueAction', 'BroadcastSignalAction', 'InvocationAction',
    'CallAction', 'CallBehaviorAction', 'CallOperationAction', 'Clause',
    'ClearAssociationAction', 'ClearStructuralFeatureAction',
    'ClearVariableAction', 'ConditionalNode', 'CreateLinkAction',
    'LinkEndCreationData', 'CreateLinkObjectAction', 'CreateObjectAction',
    'DestroyLinkAction', 'LinkEndDestructionData', 'DestroyObjectAction',
    'ExpansionNode', 'ExpansionRegion', 'LoopNode', 'OpaqueAction',
    'RaiseExceptionAction', 'ReadExtentAction', 'ReadIsClassifiedObjectAction',
    'ReadLinkAction', 'ReadLinkObjectEndAction',
    'ReadLinkObjectEndQualifierAction', 'ReadSelfAction',
    'ReadStructuralFeatureAction', 'ReadVariableAction',
    'ReclassifyObjectAction', 'ReduceAction',
    'RemoveStructuralFeatureValueAction', 'RemoveVariableValueAction',
    'ReplyAction', 'SendObjectAction', 'SendSignalAction', 'SequenceNode',
    'StartClassifierBehaviorAction', 'StartObjectBehaviorAction',
    'TestIdentityAction', 'UnmarshallAction', 'ValuePin', 'ActivityFinalNode',
    'FinalNode', 'ControlNode', 'ActivityParameterNode', 'CentralBufferNode',
    'ControlFlow', 'DataStoreNode', 'DecisionNode', 'ObjectFlow',
    'FlowFinalNode', 'ForkNode', 'InitialNode', 'JoinNode', 'MergeNode',
    'InstanceValue', 'AnyReceiveEvent', 'MessageEvent', 'CallEvent',
    'ChangeEvent', 'FunctionBehavior', 'OpaqueBehavior', 'SignalEvent',
    'TimeEvent', 'TimeExpression', 'Observation', 'CommunicationPath',
    'Device', 'Node', 'ExecutionEnvironment', 'InformationFlow', 'Message',
    'Interaction', 'InteractionFragment', 'Lifeline', 'PartDecomposition',
    'InteractionUse', 'Gate', 'MessageEnd', 'InteractionOperand',
    'InteractionConstraint', 'GeneralOrdering', 'OccurrenceSpecification',
    'MessageKind', 'MessageSort', 'InformationItem',
    'ActionExecutionSpecification', 'ExecutionSpecification',
    'BehaviorExecutionSpecification', 'CombinedFragment',
    'InteractionOperatorKind', 'ConsiderIgnoreFragment', 'Continuation',
    'DestructionOccurrenceSpecification', 'MessageOccurrenceSpecification',
    'ExecutionOccurrenceSpecification', 'StateInvariant', 'FinalState',
    'ProtocolTransition', 'AssociationClass', 'Component',
    'ComponentRealization', 'Actor', 'Duration', 'DurationConstraint',
    'IntervalConstraint', 'Interval', 'DurationInterval',
    'DurationObservation', 'LiteralBoolean', 'LiteralSpecification',
    'LiteralInteger', 'LiteralNull', 'LiteralReal', 'LiteralString',
    'LiteralUnlimitedNatural', 'TimeConstraint', 'TimeInterval',
    'TimeObservation']

eSubpackages = []
eSuperPackage = None
uml.eSubpackages = eSubpackages
uml.eSuperPackage = eSuperPackage

Activity.ownedGroup.eType = ActivityGroup
Activity.ownedNode.eType = ActivityNode
Activity.partition.eType = ActivityPartition
Activity.structuredNode.eType = StructuredActivityNode
Behavior._context.eType = BehavioredClassifier
Behavior.ownedParameter.eType = Parameter
Behavior.ownedParameterSet.eType = ParameterSet
Behavior.postcondition.eType = Constraint
Behavior.precondition.eType = Constraint
Behavior.redefinedBehavior.eType = Behavior
Class.nestedClassifier.eType = Classifier
Class.ownedReception.eType = Reception
Class.superClass.eType = Class
BehavioredClassifier.classifierBehavior.eType = Behavior
BehavioredClassifier.ownedBehavior.eType = Behavior
Classifier.attribute.eType = Property
Classifier.collaborationUse.eType = CollaborationUse
Classifier.general.eType = Classifier
Classifier.inheritedMember.eType = NamedElement
Classifier.ownedUseCase.eType = UseCase
Classifier.redefinedClassifier.eType = Classifier
Classifier.representation.eType = CollaborationUse
Namespace.importedMember.eType = PackageableElement
Namespace.member.eType = NamedElement
NamedElement.clientDependency.eType = Dependency
NamedElement.nameExpression.eType = StringExpression
Element.ownedComment.eType = Comment
Comment.annotatedElement.eType = Element
Stereotype.icon.eType = Image
Stereotype._profile.eType = Profile
Profile.metaclassReference.eType = ElementImport
Profile.metamodelReference.eType = PackageImport
Package.ownedStereotype.eType = Stereotype
Package.packagedElement.eType = PackageableElement
TemplateParameter.default.eType = ParameterableElement
TemplateParameter.ownedDefault.eType = ParameterableElement
TemplateSignature.parameter.eType = TemplateParameter
TemplateBinding.signature.eType = TemplateSignature
DirectedRelationship.source.eType = Element
DirectedRelationship.target.eType = Element
Relationship.relatedElement.eType = Element
TemplateParameterSubstitution.actual.eType = ParameterableElement
TemplateParameterSubstitution.formal.eType = TemplateParameter
TemplateParameterSubstitution.ownedActual.eType = ParameterableElement
Association.endType.eType = Type
Association.navigableOwnedEnd.eType = Property
Property.defaultValue.eType = ValueSpecification
Property._opposite.eType = Property
Property.redefinedProperty.eType = Property
Property.subsettedProperty.eType = Property
ConnectableElement.end.eType = ConnectorEnd
TypedElement.type.eType = Type
ConnectorEnd._definingEnd.eType = Property
ConnectorEnd.partWithPort.eType = Property
ConnectorEnd.role.eType = ConnectableElement
MultiplicityElement.lowerValue.eType = ValueSpecification
MultiplicityElement.upperValue.eType = ValueSpecification
DeploymentTarget.deployedElement.eType = PackageableElement
Deployment.deployedArtifact.eType = DeployedArtifact
Dependency.client.eType = NamedElement
Dependency.supplier.eType = NamedElement
Artifact.manifestation.eType = Manifestation
Artifact.nestedArtifact.eType = Artifact
Artifact.ownedAttribute.eType = Property
Artifact.ownedOperation.eType = Operation
Manifestation.utilizedElement.eType = PackageableElement
Abstraction.mapping.eType = OpaqueExpression
OpaqueExpression.behavior.eType = Behavior
OpaqueExpression._result.eType = Parameter
Parameter.defaultValue.eType = ValueSpecification
Operation.bodyCondition.eType = Constraint
Operation.postcondition.eType = Constraint
Operation.precondition.eType = Constraint
Operation.redefinedOperation.eType = Operation
Operation._type.eType = Type
BehavioralFeature.ownedParameter.eType = Parameter
BehavioralFeature.ownedParameterSet.eType = ParameterSet
BehavioralFeature.raisedException.eType = Type
RedefinableElement.redefinedElement.eType = RedefinableElement
RedefinableElement.redefinitionContext.eType = Classifier
ParameterSet.condition.eType = Constraint
Constraint.constrainedElement.eType = Element
Constraint.specification.eType = ValueSpecification
Interface.nestedClassifier.eType = Classifier
Interface.ownedReception.eType = Reception
Interface.protocol.eType = ProtocolStateMachine
Interface.redefinedInterface.eType = Interface
Reception.signal.eType = Signal
Signal.ownedAttribute.eType = Property
StateMachine.extendedStateMachine.eType = StateMachine
Vertex.incoming.eType = Transition
Vertex.outgoing.eType = Transition
Region.extendedRegion.eType = Region
State.deferrableTrigger.eType = Trigger
State.doActivity.eType = Behavior
State.entry.eType = Behavior
State.exit.eType = Behavior
State.redefinedState.eType = State
State.stateInvariant.eType = Constraint
ConnectionPointReference.entry.eType = Pseudostate
ConnectionPointReference.exit.eType = Pseudostate
Trigger.event.eType = Event
Trigger.port.eType = Port
Port.protocol.eType = ProtocolStateMachine
Port.provided.eType = Interface
Port.redefinedPort.eType = Port
Port.required.eType = Interface
Transition.effect.eType = Behavior
Transition.guard.eType = Constraint
Transition.redefinedTransition.eType = Transition
Transition.source.eType = Vertex
Transition.target.eType = Vertex
Transition.trigger.eType = Trigger
ProtocolConformance.generalMachine.eType = ProtocolStateMachine
PackageMerge.mergedPackage.eType = Package
ProfileApplication.appliedProfile.eType = Profile
InstanceSpecification.classifier.eType = Classifier
InstanceSpecification.specification.eType = ValueSpecification
Slot.definingFeature.eType = StructuralFeature
Slot.value.eType = ValueSpecification
ElementImport.importedElement.eType = PackageableElement
PackageImport.importedPackage.eType = Package
Expression.operand.eType = ValueSpecification
CollaborationUse.roleBinding.eType = Dependency
CollaborationUse.type.eType = Collaboration
Collaboration.collaborationRole.eType = ConnectableElement
StructuredClassifier.ownedAttribute.eType = Property
StructuredClassifier.ownedConnector.eType = Connector
StructuredClassifier.part.eType = Property
StructuredClassifier.role.eType = ConnectableElement
Connector.contract.eType = Behavior
Connector.end.eType = ConnectorEnd
Connector.redefinedConnector.eType = Connector
Connector.type.eType = Association
Generalization.general.eType = Classifier
RedefinableTemplateSignature.extendedSignature.eType = RedefinableTemplateSignature
RedefinableTemplateSignature.inheritedParameter.eType = TemplateParameter
Extend.condition.eType = Constraint
Extend.extendedCase.eType = UseCase
Extend.extensionLocation.eType = ExtensionPoint
Include.addition.eType = UseCase
Substitution.contract.eType = Classifier
ClassifierTemplateParameter.constrainingClassifier.eType = Classifier
InterfaceRealization.contract.eType = Interface
EncapsulatedClassifier.ownedPort.eType = Port
ActivityEdge.guard.eType = ValueSpecification
ActivityEdge.redefinedEdge.eType = ActivityEdge
ActivityEdge.weight.eType = ValueSpecification
ActivityPartition.represents.eType = Element
ActivityNode.redefinedNode.eType = ActivityNode
StructuredActivityNode.structuredNodeInput.eType = InputPin
StructuredActivityNode.structuredNodeOutput.eType = OutputPin
Action._context.eType = Classifier
Action.input.eType = InputPin
Action.localPostcondition.eType = Constraint
Action.localPrecondition.eType = Constraint
Action.output.eType = OutputPin
ExceptionHandler.exceptionInput.eType = ObjectNode
ExceptionHandler.exceptionType.eType = Classifier
ExceptionHandler.handlerBody.eType = ExecutableNode
ObjectNode.inState.eType = State
ObjectNode.selection.eType = Behavior
ObjectNode.upperBound.eType = ValueSpecification
ValueSpecificationAction.result.eType = OutputPin
ValueSpecificationAction.value.eType = ValueSpecification
VariableAction.variable.eType = Variable
LinkAction.endData.eType = LinkEndData
LinkAction.inputValue.eType = InputPin
LinkEndData.end.eType = Property
LinkEndData.qualifier.eType = QualifierValue
LinkEndData.value.eType = InputPin
QualifierValue.qualifier.eType = Property
QualifierValue.value.eType = InputPin
WriteStructuralFeatureAction.result.eType = OutputPin
WriteStructuralFeatureAction.value.eType = InputPin
StructuralFeatureAction.object.eType = InputPin
StructuralFeatureAction.structuralFeature.eType = StructuralFeature
WriteVariableAction.value.eType = InputPin
AcceptCallAction.returnInformation.eType = OutputPin
AcceptEventAction.result.eType = OutputPin
AcceptEventAction.trigger.eType = Trigger
ActionInputPin.fromAction.eType = Action
AddStructuralFeatureValueAction.insertAt.eType = InputPin
AddVariableValueAction.insertAt.eType = InputPin
BroadcastSignalAction.signal.eType = Signal
InvocationAction.argument.eType = InputPin
InvocationAction.onPort.eType = Port
CallAction.result.eType = OutputPin
CallBehaviorAction.behavior.eType = Behavior
CallOperationAction.operation.eType = Operation
CallOperationAction.target.eType = InputPin
Clause.body.eType = ExecutableNode
Clause.bodyOutput.eType = OutputPin
Clause.decider.eType = OutputPin
Clause.test.eType = ExecutableNode
ClearAssociationAction.association.eType = Association
ClearAssociationAction.object.eType = InputPin
ClearStructuralFeatureAction.result.eType = OutputPin
ConditionalNode.clause.eType = Clause
ConditionalNode.result.eType = OutputPin
LinkEndCreationData.insertAt.eType = InputPin
CreateLinkObjectAction.result.eType = OutputPin
CreateObjectAction.classifier.eType = Classifier
CreateObjectAction.result.eType = OutputPin
LinkEndDestructionData.destroyAt.eType = InputPin
DestroyObjectAction.target.eType = InputPin
LoopNode.bodyOutput.eType = OutputPin
LoopNode.bodyPart.eType = ExecutableNode
LoopNode.decider.eType = OutputPin
LoopNode.loopVariable.eType = OutputPin
LoopNode.loopVariableInput.eType = InputPin
LoopNode.result.eType = OutputPin
LoopNode.setupPart.eType = ExecutableNode
LoopNode.test.eType = ExecutableNode
OpaqueAction.inputValue.eType = InputPin
OpaqueAction.outputValue.eType = OutputPin
RaiseExceptionAction.exception.eType = InputPin
ReadExtentAction.classifier.eType = Classifier
ReadExtentAction.result.eType = OutputPin
ReadIsClassifiedObjectAction.classifier.eType = Classifier
ReadIsClassifiedObjectAction.object.eType = InputPin
ReadIsClassifiedObjectAction.result.eType = OutputPin
ReadLinkAction.result.eType = OutputPin
ReadLinkObjectEndAction.end.eType = Property
ReadLinkObjectEndAction.object.eType = InputPin
ReadLinkObjectEndAction.result.eType = OutputPin
ReadLinkObjectEndQualifierAction.object.eType = InputPin
ReadLinkObjectEndQualifierAction.qualifier.eType = Property
ReadLinkObjectEndQualifierAction.result.eType = OutputPin
ReadSelfAction.result.eType = OutputPin
ReadStructuralFeatureAction.result.eType = OutputPin
ReadVariableAction.result.eType = OutputPin
ReclassifyObjectAction.newClassifier.eType = Classifier
ReclassifyObjectAction.object.eType = InputPin
ReclassifyObjectAction.oldClassifier.eType = Classifier
ReduceAction.collection.eType = InputPin
ReduceAction.reducer.eType = Behavior
ReduceAction.result.eType = OutputPin
RemoveStructuralFeatureValueAction.removeAt.eType = InputPin
RemoveVariableValueAction.removeAt.eType = InputPin
ReplyAction.replyToCall.eType = Trigger
ReplyAction.replyValue.eType = InputPin
ReplyAction.returnInformation.eType = InputPin
SendObjectAction.request.eType = InputPin
SendObjectAction.target.eType = InputPin
SendSignalAction.signal.eType = Signal
SendSignalAction.target.eType = InputPin
SequenceNode.executableNode.eType = ExecutableNode
StartClassifierBehaviorAction.object.eType = InputPin
StartObjectBehaviorAction.object.eType = InputPin
TestIdentityAction.first.eType = InputPin
TestIdentityAction.result.eType = OutputPin
TestIdentityAction.second.eType = InputPin
UnmarshallAction.object.eType = InputPin
UnmarshallAction.result.eType = OutputPin
UnmarshallAction.unmarshallType.eType = Classifier
ValuePin.value.eType = ValueSpecification
ActivityParameterNode.parameter.eType = Parameter
DecisionNode.decisionInput.eType = Behavior
DecisionNode.decisionInputFlow.eType = ObjectFlow
ObjectFlow.selection.eType = Behavior
ObjectFlow.transformation.eType = Behavior
JoinNode.joinSpec.eType = ValueSpecification
InstanceValue.instance.eType = InstanceSpecification
CallEvent.operation.eType = Operation
ChangeEvent.changeExpression.eType = ValueSpecification
SignalEvent.signal.eType = Signal
TimeEvent.when.eType = TimeExpression
TimeExpression.expr.eType = ValueSpecification
TimeExpression.observation.eType = Observation
Node.nestedNode.eType = Node
InformationFlow.conveyed.eType = Classifier
InformationFlow.informationSource.eType = NamedElement
InformationFlow.informationTarget.eType = NamedElement
InformationFlow.realization.eType = Relationship
InformationFlow.realizingActivityEdge.eType = ActivityEdge
InformationFlow.realizingConnector.eType = Connector
InformationFlow.realizingMessage.eType = Message
Message.argument.eType = ValueSpecification
Message.connector.eType = Connector
Message.receiveEvent.eType = MessageEnd
Message.sendEvent.eType = MessageEnd
Message.signature.eType = NamedElement
Interaction.action.eType = Action
Interaction.formalGate.eType = Gate
InteractionFragment.generalOrdering.eType = GeneralOrdering
Lifeline.decomposedAs.eType = PartDecomposition
Lifeline.represents.eType = ConnectableElement
Lifeline.selector.eType = ValueSpecification
InteractionUse.actualGate.eType = Gate
InteractionUse.argument.eType = ValueSpecification
InteractionUse.refersTo.eType = Interaction
InteractionUse.returnValue.eType = ValueSpecification
InteractionUse.returnValueRecipient.eType = Property
MessageEnd.message.eType = Message
InteractionOperand.guard.eType = InteractionConstraint
InteractionConstraint.maxint.eType = ValueSpecification
InteractionConstraint.minint.eType = ValueSpecification
InformationItem.represented.eType = Classifier
ActionExecutionSpecification.action.eType = Action
ExecutionSpecification.finish.eType = OccurrenceSpecification
ExecutionSpecification.start.eType = OccurrenceSpecification
BehaviorExecutionSpecification.behavior.eType = Behavior
CombinedFragment.cfragmentGate.eType = Gate
CombinedFragment.operand.eType = InteractionOperand
ConsiderIgnoreFragment.message.eType = NamedElement
ExecutionOccurrenceSpecification.execution.eType = ExecutionSpecification
StateInvariant.invariant.eType = Constraint
ProtocolTransition.postCondition.eType = Constraint
ProtocolTransition.preCondition.eType = Constraint
ProtocolTransition.referred.eType = Operation
Component.packagedElement.eType = PackageableElement
Component.provided.eType = Interface
Component.required.eType = Interface
ComponentRealization.realizingClassifier.eType = Classifier
Duration.expr.eType = ValueSpecification
Duration.observation.eType = Observation
Interval.max.eType = ValueSpecification
Interval.min.eType = ValueSpecification
DurationObservation.event.eType = NamedElement
TimeObservation.event.eType = NamedElement
Activity.edge.eType = ActivityEdge
Activity.node.eType = ActivityNode
Activity.variable.eType = Variable
Activity.group.eType = ActivityGroup
Behavior.specification.eType = BehavioralFeature
Class.ownedOperation.eType = Operation
Class.extension.eType = Extension
BehavioredClassifier.interfaceRealization.eType = InterfaceRealization
Classifier.feature.eType = Feature
Classifier.generalization.eType = Generalization
Classifier.powertypeExtent.eType = GeneralizationSet
Classifier.useCase.eType = UseCase
Classifier.substitution.eType = Substitution
Namespace.ownedRule.eType = Constraint
Namespace.elementImport.eType = ElementImport
Namespace.packageImport.eType = PackageImport
Namespace.ownedMember.eType = NamedElement
NamedElement._namespace.eType = Namespace
NamedElement._namespace.eOpposite = Namespace.ownedMember
Element.ownedElement.eType = Element
Element._owner.eType = Element
Element._owner.eOpposite = Element.ownedElement
Package.nestedPackage.eType = Package
Package._nestingPackage.eType = Package
Package._nestingPackage.eOpposite = Package.nestedPackage
Package.ownedType.eType = Type
Package.packageMerge.eType = PackageMerge
Package.profileApplication.eType = ProfileApplication
ParameterableElement.owningTemplateParameter.eType = TemplateParameter
ParameterableElement.templateParameter.eType = TemplateParameter
TemplateParameter.parameteredElement.eType = ParameterableElement
TemplateParameter.parameteredElement.eOpposite = ParameterableElement.templateParameter
TemplateParameter.signature.eType = TemplateSignature
TemplateParameter.ownedParameteredElement.eType = ParameterableElement
TemplateParameter.ownedParameteredElement.eOpposite = ParameterableElement.owningTemplateParameter
TemplateSignature.template.eType = TemplateableElement
TemplateSignature.ownedParameter.eType = TemplateParameter
TemplateSignature.ownedParameter.eOpposite = TemplateParameter.signature
TemplateableElement.templateBinding.eType = TemplateBinding
TemplateableElement.ownedTemplateSignature.eType = TemplateSignature
TemplateableElement.ownedTemplateSignature.eOpposite = TemplateSignature.template
TemplateBinding.parameterSubstitution.eType = TemplateParameterSubstitution
TemplateBinding.boundElement.eType = TemplateableElement
TemplateBinding.boundElement.eOpposite = TemplateableElement.templateBinding
TemplateParameterSubstitution.templateBinding.eType = TemplateBinding
TemplateParameterSubstitution.templateBinding.eOpposite = TemplateBinding.parameterSubstitution
Type._package.eType = Package
Type._package.eOpposite = Package.ownedType
Association.memberEnd.eType = Property
Association.ownedEnd.eType = Property
Property.datatype.eType = DataType
Property.interface.eType = Interface
Property.associationEnd.eType = Property
Property.qualifier.eType = Property
Property.qualifier.eOpposite = Property.associationEnd
Property.class_.eType = Class
Property.owningAssociation.eType = Association
Property.owningAssociation.eOpposite = Association.ownedEnd
Property.association.eType = Association
Property.association.eOpposite = Association.memberEnd
DeploymentTarget.deployment.eType = Deployment
Deployment.configuration.eType = DeploymentSpecification
Deployment.location.eType = DeploymentTarget
Deployment.location.eOpposite = DeploymentTarget.deployment
DeploymentSpecification.deployment.eType = Deployment
DeploymentSpecification.deployment.eOpposite = Deployment.configuration
Parameter.operation.eType = Operation
Parameter.parameterSet.eType = ParameterSet
Operation.class_.eType = Class
Operation.class_.eOpposite = Class.ownedOperation
Operation.datatype.eType = DataType
Operation.interface.eType = Interface
BehavioralFeature.method.eType = Behavior
BehavioralFeature.method.eOpposite = Behavior.specification
Feature.featuringClassifier.eType = Classifier
Feature.featuringClassifier.eOpposite = Classifier.feature
ParameterSet.parameter.eType = Parameter
ParameterSet.parameter.eOpposite = Parameter.parameterSet
Constraint.context.eType = Namespace
Constraint.context.eOpposite = Namespace.ownedRule
DataType.ownedAttribute.eType = Property
DataType.ownedAttribute.eOpposite = Property.datatype
DataType.ownedOperation.eType = Operation
DataType.ownedOperation.eOpposite = Operation.datatype
Interface.ownedAttribute.eType = Property
Interface.ownedAttribute.eOpposite = Property.interface
Interface.ownedOperation.eType = Operation
Interface.ownedOperation.eOpposite = Operation.interface
ProtocolStateMachine.conformance.eType = ProtocolConformance
StateMachine.connectionPoint.eType = Pseudostate
StateMachine.submachineState.eType = State
StateMachine.region.eType = Region
Pseudostate.state.eType = State
Pseudostate.stateMachine.eType = StateMachine
Pseudostate.stateMachine.eOpposite = StateMachine.connectionPoint
Vertex.container.eType = Region
Region.state.eType = State
Region.stateMachine.eType = StateMachine
Region.stateMachine.eOpposite = StateMachine.region
Region.transition.eType = Transition
Region.subvertex.eType = Vertex
Region.subvertex.eOpposite = Vertex.container
State.connection.eType = ConnectionPointReference
State.connectionPoint.eType = Pseudostate
State.connectionPoint.eOpposite = Pseudostate.state
State.submachine.eType = StateMachine
State.submachine.eOpposite = StateMachine.submachineState
State.region.eType = Region
State.region.eOpposite = Region.state
ConnectionPointReference.state.eType = State
ConnectionPointReference.state.eOpposite = State.connection
Transition.container.eType = Region
Transition.container.eOpposite = Region.transition
ProtocolConformance.specificMachine.eType = ProtocolStateMachine
ProtocolConformance.specificMachine.eOpposite = ProtocolStateMachine.conformance
PackageMerge.receivingPackage.eType = Package
PackageMerge.receivingPackage.eOpposite = Package.packageMerge
ProfileApplication.applyingPackage.eType = Package
ProfileApplication.applyingPackage.eOpposite = Package.profileApplication
Enumeration.ownedLiteral.eType = EnumerationLiteral
EnumerationLiteral.enumeration.eType = Enumeration
EnumerationLiteral.enumeration.eOpposite = Enumeration.ownedLiteral
InstanceSpecification.slot.eType = Slot
Slot.owningInstance.eType = InstanceSpecification
Slot.owningInstance.eOpposite = InstanceSpecification.slot
ElementImport.importingNamespace.eType = Namespace
ElementImport.importingNamespace.eOpposite = Namespace.elementImport
PackageImport.importingNamespace.eType = Namespace
PackageImport.importingNamespace.eOpposite = Namespace.packageImport
Extension._metaclass.eType = Class
Extension._metaclass.eOpposite = Class.extension
StringExpression.owningExpression.eType = StringExpression
StringExpression.subExpression.eType = StringExpression
StringExpression.subExpression.eOpposite = StringExpression.owningExpression
Generalization.generalizationSet.eType = GeneralizationSet
Generalization.specific.eType = Classifier
Generalization.specific.eOpposite = Classifier.generalization
GeneralizationSet.powertype.eType = Classifier
GeneralizationSet.powertype.eOpposite = Classifier.powertypeExtent
GeneralizationSet.generalization.eType = Generalization
GeneralizationSet.generalization.eOpposite = Generalization.generalizationSet
RedefinableTemplateSignature.classifier.eType = Classifier
UseCase.extend.eType = Extend
UseCase.extensionPoint.eType = ExtensionPoint
UseCase.include.eType = Include
UseCase.subject.eType = Classifier
UseCase.subject.eOpposite = Classifier.useCase
Extend.extension.eType = UseCase
Extend.extension.eOpposite = UseCase.extend
ExtensionPoint.useCase.eType = UseCase
ExtensionPoint.useCase.eOpposite = UseCase.extensionPoint
Include.includingCase.eType = UseCase
Include.includingCase.eOpposite = UseCase.include
Substitution.substitutingClassifier.eType = Classifier
Substitution.substitutingClassifier.eOpposite = Classifier.substitution
InterfaceRealization.implementingClassifier.eType = BehavioredClassifier
InterfaceRealization.implementingClassifier.eOpposite = BehavioredClassifier.interfaceRealization
ActivityGroup.containedEdge.eType = ActivityEdge
ActivityGroup.containedNode.eType = ActivityNode
ActivityGroup._inActivity.eType = Activity
ActivityGroup._inActivity.eOpposite = Activity.group
ActivityGroup.subgroup.eType = ActivityGroup
ActivityGroup._superGroup.eType = ActivityGroup
ActivityGroup._superGroup.eOpposite = ActivityGroup.subgroup
ActivityEdge.activity.eType = Activity
ActivityEdge.activity.eOpposite = Activity.edge
ActivityEdge.inPartition.eType = ActivityPartition
ActivityEdge.interrupts.eType = InterruptibleActivityRegion
ActivityEdge.inStructuredNode.eType = StructuredActivityNode
ActivityEdge.target.eType = ActivityNode
ActivityEdge.source.eType = ActivityNode
ActivityEdge.inGroup.eType = ActivityGroup
ActivityEdge.inGroup.eOpposite = ActivityGroup.containedEdge
ActivityPartition.node.eType = ActivityNode
ActivityPartition.subpartition.eType = ActivityPartition
ActivityPartition.superPartition.eType = ActivityPartition
ActivityPartition.superPartition.eOpposite = ActivityPartition.subpartition
ActivityPartition.edge.eType = ActivityEdge
ActivityPartition.edge.eOpposite = ActivityEdge.inPartition
ActivityNode._activity.eType = Activity
ActivityNode._activity.eOpposite = Activity.node
ActivityNode.inGroup.eType = ActivityGroup
ActivityNode.inGroup.eOpposite = ActivityGroup.containedNode
ActivityNode.inInterruptibleRegion.eType = InterruptibleActivityRegion
ActivityNode.inStructuredNode.eType = StructuredActivityNode
ActivityNode.incoming.eType = ActivityEdge
ActivityNode.incoming.eOpposite = ActivityEdge.target
ActivityNode.outgoing.eType = ActivityEdge
ActivityNode.outgoing.eOpposite = ActivityEdge.source
ActivityNode.inPartition.eType = ActivityPartition
ActivityNode.inPartition.eOpposite = ActivityPartition.node
InterruptibleActivityRegion.interruptingEdge.eType = ActivityEdge
InterruptibleActivityRegion.interruptingEdge.eOpposite = ActivityEdge.interrupts
InterruptibleActivityRegion.node.eType = ActivityNode
InterruptibleActivityRegion.node.eOpposite = ActivityNode.inInterruptibleRegion
StructuredActivityNode.edge.eType = ActivityEdge
StructuredActivityNode.edge.eOpposite = ActivityEdge.inStructuredNode
StructuredActivityNode.variable.eType = Variable
StructuredActivityNode.node.eType = ActivityNode
StructuredActivityNode.node.eOpposite = ActivityNode.inStructuredNode
ExecutableNode.handler.eType = ExceptionHandler
ExceptionHandler.protectedNode.eType = ExecutableNode
ExceptionHandler.protectedNode.eOpposite = ExecutableNode.handler
Variable.activityScope.eType = Activity
Variable.activityScope.eOpposite = Activity.variable
Variable.scope.eType = StructuredActivityNode
Variable.scope.eOpposite = StructuredActivityNode.variable
Clause.predecessorClause.eType = Clause
Clause.successorClause.eType = Clause
Clause.successorClause.eOpposite = Clause.predecessorClause
ExpansionNode.regionAsInput.eType = ExpansionRegion
ExpansionNode.regionAsOutput.eType = ExpansionRegion
ExpansionRegion.outputElement.eType = ExpansionNode
ExpansionRegion.outputElement.eOpposite = ExpansionNode.regionAsOutput
ExpansionRegion.inputElement.eType = ExpansionNode
ExpansionRegion.inputElement.eOpposite = ExpansionNode.regionAsInput
Message.interaction.eType = Interaction
Interaction.lifeline.eType = Lifeline
Interaction.fragment.eType = InteractionFragment
Interaction.message.eType = Message
Interaction.message.eOpposite = Message.interaction
InteractionFragment.covered.eType = Lifeline
InteractionFragment.enclosingOperand.eType = InteractionOperand
InteractionFragment.enclosingInteraction.eType = Interaction
InteractionFragment.enclosingInteraction.eOpposite = Interaction.fragment
Lifeline.interaction.eType = Interaction
Lifeline.interaction.eOpposite = Interaction.lifeline
Lifeline.coveredBy.eType = InteractionFragment
Lifeline.coveredBy.eOpposite = InteractionFragment.covered
InteractionOperand.fragment.eType = InteractionFragment
InteractionOperand.fragment.eOpposite = InteractionFragment.enclosingOperand
GeneralOrdering.after.eType = OccurrenceSpecification
GeneralOrdering.before.eType = OccurrenceSpecification
OccurrenceSpecification.toAfter.eType = GeneralOrdering
OccurrenceSpecification.toAfter.eOpposite = GeneralOrdering.before
OccurrenceSpecification.toBefore.eType = GeneralOrdering
OccurrenceSpecification.toBefore.eOpposite = GeneralOrdering.after
Component.realization.eType = ComponentRealization
ComponentRealization.abstraction.eType = Component
ComponentRealization.abstraction.eOpposite = Component.realization

otherClassifiers = [VisibilityKind, ParameterDirectionKind,
                    ParameterEffectKind, CallConcurrencyKind, TransitionKind,
                    PseudostateKind, AggregationKind, ConnectorKind,
                    ObjectNodeOrderingKind, ExpansionKind, MessageKind,
                    MessageSort, InteractionOperatorKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
