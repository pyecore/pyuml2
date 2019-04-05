# -*- coding: utf-8 -*-
"""Definition of meta model 'uml'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from ..types import Boolean, Real, UnlimitedNatural, Integer, String
from pyecore.ecore import EModelElement
import pyuml2.uml_mixins as _user_module


name = 'uml'
nsURI = 'http://www.eclipse.org/uml2/5.0.0/UML'
nsPrefix = 'uml'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
VisibilityKind = EEnum('VisibilityKind', literals=[
                       'public', 'private', 'protected', 'package'])

ParameterDirectionKind = EEnum('ParameterDirectionKind', literals=[
                               'in_', 'inout', 'out', 'return_'])

ParameterEffectKind = EEnum('ParameterEffectKind', literals=[
                            'create', 'read', 'update', 'delete'])

CallConcurrencyKind = EEnum('CallConcurrencyKind', literals=[
                            'sequential', 'guarded', 'concurrent'])

TransitionKind = EEnum('TransitionKind', literals=[
                       'internal', 'local', 'external'])

PseudostateKind = EEnum('PseudostateKind',
                        literals=['initial', 'deepHistory', 'shallowHistory',
                                  'join', 'fork', 'junction', 'choice',
                                  'entryPoint', 'exitPoint', 'terminate'])

AggregationKind = EEnum('AggregationKind', literals=[
                        'none', 'shared', 'composite'])

ConnectorKind = EEnum('ConnectorKind', literals=['assembly', 'delegation'])

ObjectNodeOrderingKind = EEnum('ObjectNodeOrderingKind', literals=[
                               'unordered', 'ordered', 'LIFO', 'FIFO'])

ExpansionKind = EEnum('ExpansionKind', literals=[
                      'parallel', 'iterative', 'stream'])

MessageKind = EEnum('MessageKind', literals=[
                    'complete', 'lost', 'found', 'unknown'])

MessageSort = EEnum(
    'MessageSort',
    literals=['synchCall', 'asynchCall', 'asynchSignal', 'createMessage',
              'deleteMessage', 'reply'])

InteractionOperatorKind = EEnum(
    'InteractionOperatorKind',
    literals=['seq', 'alt', 'opt', 'break_', 'par', 'strict', 'loop',
              'critical', 'neg', 'assert_', 'ignore', 'consider'])


@abstract
@EMetaclass
class ActivityContent(
        _user_module.ActivityContentMixin, EObject):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super(ActivityContent, self).__init__()


@abstract
@EMetaclass
class Element(_user_module.ElementMixin, EModelElement):
    """An Element is a constituent of a model. As such, it has the capability of owning other Elements.
<p>From package UML::CommonStructure.</p>"""
    ownedComment = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    ownedElement = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedOwnedelement)
    _owner = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='owner', transient=True)

    def __init__(
            self, ownedComment=None, ownedElement=None, owner=None, **
            kwargs):

        super(Element, self).__init__(**kwargs)

        if ownedComment:
            self.ownedComment.extend(ownedComment)

        if ownedElement:
            self.ownedElement.extend(ownedElement)

        if owner is not None:
            self.owner = owner


@abstract
class NamedElement(_user_module.NamedElementMixin, Element):
    """A NamedElement is an Element in a model that may have a name. The name may be given directly and/or via the use of a StringExpression.
<p>From package UML::CommonStructure.</p>"""
    name = EAttribute(eType=String, derived=False, changeable=True)
    _qualifiedName = EAttribute(
        eType=String, derived=True, changeable=False, name='qualifiedName',
        transient=True)
    visibility = EAttribute(eType=VisibilityKind,
                            derived=False, changeable=True)
    clientDependency = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedClientdependency)
    nameExpression = EReference(
        ordered=False, unique=True, containment=True, derived=False)
    _namespace = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='namespace', transient=True)

    def __init__(self, clientDependency=None, name=None,
                 nameExpression=None, namespace=None, qualifiedName=None,
                 visibility=None, **kwargs):

        super(Element, self).__init__(**kwargs)

        if name is not None:
            self.name = name

        if qualifiedName is not None:
            self.qualifiedName = qualifiedName

        if visibility is not None:
            self.visibility = visibility

        if clientDependency:
            self.clientDependency.extend(clientDependency)

        if nameExpression is not None:
            self.nameExpression = nameExpression

        if namespace is not None:
            self.namespace = namespace


class Comment(_user_module.CommentMixin, Element):
    """A Comment is a textual annotation that can be attached to a set of Elements.
<p>From package UML::CommonStructure.</p>"""
    body = EAttribute(eType=String, derived=False, changeable=True)
    annotatedElement = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, annotatedElement=None, body=None, **kwargs):

        super(Comment, self).__init__(**kwargs)

        if body is not None:
            self.body = body

        if annotatedElement:
            self.annotatedElement.extend(annotatedElement)


class Image(_user_module.ImageMixin, Element):
    """Physical definition of a graphical image.
<p>From package UML::Packages.</p>"""
    content = EAttribute(eType=String, derived=False, changeable=True)
    format = EAttribute(eType=String, derived=False, changeable=True)
    location = EAttribute(eType=String, derived=False, changeable=True)

    def __init__(self, content=None, format=None, location=None, **kwargs):

        super(Image, self).__init__(**kwargs)

        if content is not None:
            self.content = content

        if format is not None:
            self.format = format

        if location is not None:
            self.location = location


@abstract
class ParameterableElement(_user_module.ParameterableElementMixin, Element):
    """A ParameterableElement is an Element that can be exposed as a formal TemplateParameter for a template, or specified as an actual parameter in a binding of a template.
<p>From package UML::CommonStructure.</p>"""
    owningTemplateParameter = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    templateParameter = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(
            self, owningTemplateParameter=None, templateParameter=None, **
            kwargs):

        super(ParameterableElement, self).__init__(**kwargs)

        if owningTemplateParameter is not None:
            self.owningTemplateParameter = owningTemplateParameter

        if templateParameter is not None:
            self.templateParameter = templateParameter


class TemplateParameter(_user_module.TemplateParameterMixin, Element):
    """A TemplateParameter exposes a ParameterableElement as a formal parameter of a template.
<p>From package UML::CommonStructure.</p>"""
    default = EReference(ordered=False, unique=True,
                         containment=False, derived=False)
    ownedDefault = EReference(
        ordered=False, unique=True, containment=True, derived=False)
    parameteredElement = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    signature = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    ownedParameteredElement = EReference(
        ordered=False, unique=True, containment=True, derived=False)

    def __init__(self, default=None, ownedDefault=None,
                 parameteredElement=None, signature=None,
                 ownedParameteredElement=None, **kwargs):

        super(TemplateParameter, self).__init__(**kwargs)

        if default is not None:
            self.default = default

        if ownedDefault is not None:
            self.ownedDefault = ownedDefault

        if parameteredElement is not None:
            self.parameteredElement = parameteredElement

        if signature is not None:
            self.signature = signature

        if ownedParameteredElement is not None:
            self.ownedParameteredElement = ownedParameteredElement


class TemplateSignature(_user_module.TemplateSignatureMixin, Element):
    """A Template Signature bundles the set of formal TemplateParameters for a template.
<p>From package UML::CommonStructure.</p>"""
    parameter = EReference(ordered=True, unique=True,
                           containment=False, derived=False, upper=-1)
    template = EReference(ordered=False, unique=True,
                          containment=False, derived=False)
    ownedParameter = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(
            self, parameter=None, template=None, ownedParameter=None, **
            kwargs):

        super(TemplateSignature, self).__init__(**kwargs)

        if parameter:
            self.parameter.extend(parameter)

        if template is not None:
            self.template = template

        if ownedParameter:
            self.ownedParameter.extend(ownedParameter)


@abstract
class TemplateableElement(_user_module.TemplateableElementMixin, Element):
    """A TemplateableElement is an Element that can optionally be defined as a template and bound to other templates.
<p>From package UML::CommonStructure.</p>"""
    templateBinding = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    ownedTemplateSignature = EReference(
        ordered=False, unique=True, containment=True, derived=False)

    def __init__(
            self, templateBinding=None, ownedTemplateSignature=None, **
            kwargs):

        super(TemplateableElement, self).__init__(**kwargs)

        if templateBinding:
            self.templateBinding.extend(templateBinding)

        if ownedTemplateSignature is not None:
            self.ownedTemplateSignature = ownedTemplateSignature


@abstract
class Relationship(_user_module.RelationshipMixin, Element):
    """Relationship is an abstract concept that specifies some kind of relationship between Elements.
<p>From package UML::CommonStructure.</p>"""
    relatedElement = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedRelatedelement)

    def __init__(self, relatedElement=None, **kwargs):

        super(Relationship, self).__init__(**kwargs)

        if relatedElement:
            self.relatedElement.extend(relatedElement)


class TemplateParameterSubstitution(
        _user_module.TemplateParameterSubstitutionMixin, Element):
    """A TemplateParameterSubstitution relates the actual parameter to a formal TemplateParameter as part of a template binding.
<p>From package UML::CommonStructure.</p>"""
    actual = EReference(ordered=False, unique=True,
                        containment=False, derived=False)
    formal = EReference(ordered=False, unique=True,
                        containment=False, derived=False)
    ownedActual = EReference(ordered=False, unique=True,
                             containment=True, derived=False)
    templateBinding = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(
            self, actual=None, formal=None, ownedActual=None,
            templateBinding=None, **kwargs):

        super(TemplateParameterSubstitution, self).__init__(**kwargs)

        if actual is not None:
            self.actual = actual

        if formal is not None:
            self.formal = formal

        if ownedActual is not None:
            self.ownedActual = ownedActual

        if templateBinding is not None:
            self.templateBinding = templateBinding


@abstract
class MultiplicityElement(_user_module.MultiplicityElementMixin, Element):
    """A multiplicity is a definition of an inclusive interval of non-negative integers beginning with a lower bound and ending with a (possibly infinite) upper bound. A MultiplicityElement embeds this information to specify the allowable cardinalities for an instantiation of the Element.
<p>From package UML::CommonStructure.</p>"""
    isOrdered = EAttribute(eType=Boolean, derived=False,
                           changeable=True, default_value=False)
    isUnique = EAttribute(eType=Boolean, derived=False,
                          changeable=True, default_value=True)
    _lower = EAttribute(
        eType=Integer, derived=True, changeable=True, name='lower',
        default_value=1, transient=True)
    _upper = EAttribute(
        eType=UnlimitedNatural, derived=True, changeable=True, name='upper',
        default_value=1, transient=True)
    lowerValue = EReference(ordered=False, unique=True,
                            containment=True, derived=False)
    upperValue = EReference(ordered=False, unique=True,
                            containment=True, derived=False)

    def __init__(self, isOrdered=None, isUnique=None, lower=None,
                 lowerValue=None, upper=None, upperValue=None, **kwargs):

        super(MultiplicityElement, self).__init__(**kwargs)

        if isOrdered is not None:
            self.isOrdered = isOrdered

        if isUnique is not None:
            self.isUnique = isUnique

        if lower is not None:
            self.lower = lower

        if upper is not None:
            self.upper = upper

        if lowerValue is not None:
            self.lowerValue = lowerValue

        if upperValue is not None:
            self.upperValue = upperValue


class Slot(_user_module.SlotMixin, Element):
    """A Slot designates that an entity modeled by an InstanceSpecification has a value or values for a specific StructuralFeature.
<p>From package UML::Classification.</p>"""
    definingFeature = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    value = EReference(ordered=True, unique=True,
                       containment=True, derived=False, upper=-1)
    owningInstance = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, definingFeature=None, value=None,
                 owningInstance=None, **kwargs):

        super(Slot, self).__init__(**kwargs)

        if definingFeature is not None:
            self.definingFeature = definingFeature

        if value:
            self.value.extend(value)

        if owningInstance is not None:
            self.owningInstance = owningInstance


class ExceptionHandler(_user_module.ExceptionHandlerMixin, Element):
    """An ExceptionHandler is an Element that specifies a handlerBody ExecutableNode to execute in case the specified exception occurs during the execution of the protected ExecutableNode.
<p>From package UML::Activities.</p>"""
    exceptionInput = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    exceptionType = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    handlerBody = EReference(ordered=False, unique=True,
                             containment=False, derived=False)
    protectedNode = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, exceptionInput=None, exceptionType=None,
                 handlerBody=None, protectedNode=None, **kwargs):

        super(ExceptionHandler, self).__init__(**kwargs)

        if exceptionInput is not None:
            self.exceptionInput = exceptionInput

        if exceptionType:
            self.exceptionType.extend(exceptionType)

        if handlerBody is not None:
            self.handlerBody = handlerBody

        if protectedNode is not None:
            self.protectedNode = protectedNode


class LinkEndData(_user_module.LinkEndDataMixin, Element):
    """LinkEndData is an Element that identifies on end of a link to be read or written by a LinkAction. As a link (that is not a link object) cannot be passed as a runtime value to or from an Action, it is instead identified by its end objects and qualifier values, if any. A LinkEndData instance provides these values for a single Association end.
<p>From package UML::Actions.</p>"""
    end = EReference(ordered=False, unique=True,
                     containment=False, derived=False)
    qualifier = EReference(ordered=False, unique=True,
                           containment=True, derived=False, upper=-1)
    value = EReference(ordered=False, unique=True,
                       containment=False, derived=False)

    def __init__(self, end=None, qualifier=None, value=None, **kwargs):

        super(LinkEndData, self).__init__(**kwargs)

        if end is not None:
            self.end = end

        if qualifier:
            self.qualifier.extend(qualifier)

        if value is not None:
            self.value = value


class QualifierValue(_user_module.QualifierValueMixin, Element):
    """A QualifierValue is an Element that is used as part of LinkEndData to provide the value for a single qualifier of the end given by the LinkEndData.
<p>From package UML::Actions.</p>"""
    qualifier = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    value = EReference(ordered=False, unique=True,
                       containment=False, derived=False)

    def __init__(self, qualifier=None, value=None, **kwargs):

        super(QualifierValue, self).__init__(**kwargs)

        if qualifier is not None:
            self.qualifier = qualifier

        if value is not None:
            self.value = value


class Clause(_user_module.ClauseMixin, Element):
    """A Clause is an Element that represents a single branch of a ConditionalNode, including a test and a body section. The body section is executed only if (but not necessarily if) the test section evaluates to true.
<p>From package UML::Actions.</p>"""
    body = EReference(ordered=False, unique=True,
                      containment=False, derived=False, upper=-1)
    bodyOutput = EReference(ordered=True, unique=True,
                            containment=False, derived=False, upper=-1)
    decider = EReference(ordered=False, unique=True,
                         containment=False, derived=False)
    predecessorClause = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    successorClause = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    test = EReference(ordered=False, unique=True,
                      containment=False, derived=False, upper=-1)

    def __init__(
            self, body=None, bodyOutput=None, decider=None,
            predecessorClause=None, successorClause=None, test=None, **kwargs):

        super(Clause, self).__init__(**kwargs)

        if body:
            self.body.extend(body)

        if bodyOutput:
            self.bodyOutput.extend(bodyOutput)

        if decider is not None:
            self.decider = decider

        if predecessorClause:
            self.predecessorClause.extend(predecessorClause)

        if successorClause:
            self.successorClause.extend(successorClause)

        if test:
            self.test.extend(test)


@abstract
class Namespace(_user_module.NamespaceMixin, NamedElement):
    """A Namespace is an Element in a model that owns and/or imports a set of NamedElements that can be identified by name.
<p>From package UML::CommonStructure.</p>"""
    ownedRule = EReference(ordered=False, unique=True,
                           containment=True, derived=False, upper=-1)
    elementImport = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    packageImport = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    ownedMember = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedOwnedmember)
    importedMember = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedImportedmember)
    member = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedMember)

    def __init__(self, ownedRule=None, elementImport=None,
                 packageImport=None, ownedMember=None, importedMember=None,
                 member=None, **kwargs):

        super(Namespace, self).__init__(**kwargs)

        if ownedRule:
            self.ownedRule.extend(ownedRule)

        if elementImport:
            self.elementImport.extend(elementImport)

        if packageImport:
            self.packageImport.extend(packageImport)

        if ownedMember:
            self.ownedMember.extend(ownedMember)

        if importedMember:
            self.importedMember.extend(importedMember)

        if member:
            self.member.extend(member)


@abstract
class DirectedRelationship(
        _user_module.DirectedRelationshipMixin, Relationship):
    """A DirectedRelationship represents a relationship between a collection of source model Elements and a collection of target model Elements.
<p>From package UML::CommonStructure.</p>"""
    source = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedSource)
    target = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedTarget)

    def __init__(self, source=None, target=None, **kwargs):

        super(DirectedRelationship, self).__init__(**kwargs)

        if source:
            self.source.extend(source)

        if target:
            self.target.extend(target)


@abstract
class TypedElement(_user_module.TypedElementMixin, NamedElement):
    """A TypedElement is a NamedElement that may have a Type specified for it.
<p>From package UML::CommonStructure.</p>"""
    type = EReference(ordered=False, unique=True,
                      containment=False, derived=False)

    def __init__(self, type=None, **kwargs):

        super(TypedElement, self).__init__(**kwargs)

        if type is not None:
            self.type = type


class ConnectorEnd(_user_module.ConnectorEndMixin, MultiplicityElement):
    """A ConnectorEnd is an endpoint of a Connector, which attaches the Connector to a ConnectableElement.
<p>From package UML::StructuredClassifiers.</p>"""
    _definingEnd = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='definingEnd', transient=True)
    partWithPort = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    role = EReference(ordered=False, unique=True,
                      containment=False, derived=False)

    def __init__(
            self, definingEnd=None, partWithPort=None, role=None, **kwargs):

        super(ConnectorEnd, self).__init__(**kwargs)

        if definingEnd is not None:
            self.definingEnd = definingEnd

        if partWithPort is not None:
            self.partWithPort = partWithPort

        if role is not None:
            self.role = role


class ConnectableElementTemplateParameter(
        _user_module.ConnectableElementTemplateParameterMixin, TemplateParameter):
    """A ConnectableElementTemplateParameter exposes a ConnectableElement as a formal parameter for a template.
<p>From package UML::StructuredClassifiers.</p>"""

    def __init__(self, **kwargs):

        super(ConnectableElementTemplateParameter, self).__init__(**kwargs)


@abstract
class DeploymentTarget(_user_module.DeploymentTargetMixin, NamedElement):
    """A deployment target is the location for a deployed artifact.
<p>From package UML::Deployments.</p>"""
    deployedElement = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedDeployedelement)
    deployment = EReference(ordered=False, unique=True,
                            containment=True, derived=False, upper=-1)

    def __init__(self, deployedElement=None, deployment=None, **kwargs):

        super(DeploymentTarget, self).__init__(**kwargs)

        if deployedElement:
            self.deployedElement.extend(deployedElement)

        if deployment:
            self.deployment.extend(deployment)


@abstract
class DeployedArtifact(_user_module.DeployedArtifactMixin, NamedElement):
    """A deployed artifact is an artifact or artifact instance that has been deployed to a deployment target.
<p>From package UML::Deployments.</p>"""

    def __init__(self, **kwargs):

        super(DeployedArtifact, self).__init__(**kwargs)


@abstract
class RedefinableElement(_user_module.RedefinableElementMixin, NamedElement):
    """A RedefinableElement is an element that, when defined in the context of a Classifier, can be redefined more specifically or differently in the context of another Classifier that specializes (directly or indirectly) the context Classifier.
<p>From package UML::Classification.</p>"""
    isLeaf = EAttribute(eType=Boolean, derived=False,
                        changeable=True, default_value=False)
    redefinedElement = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedRedefinedelement)
    redefinitionContext = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedRedefinitioncontext)

    def __init__(self, isLeaf=None, redefinedElement=None,
                 redefinitionContext=None, **kwargs):

        super(RedefinableElement, self).__init__(**kwargs)

        if isLeaf is not None:
            self.isLeaf = isLeaf

        if redefinedElement:
            self.redefinedElement.extend(redefinedElement)

        if redefinitionContext:
            self.redefinitionContext.extend(redefinitionContext)


class ParameterSet(_user_module.ParameterSetMixin, NamedElement):
    """A ParameterSet designates alternative sets of inputs or outputs that a Behavior may use.
<p>From package UML::Classification.</p>"""
    condition = EReference(ordered=False, unique=True,
                           containment=True, derived=False, upper=-1)
    parameter = EReference(ordered=False, unique=True,
                           containment=False, derived=False, upper=-1)

    def __init__(self, condition=None, parameter=None, **kwargs):

        super(ParameterSet, self).__init__(**kwargs)

        if condition:
            self.condition.extend(condition)

        if parameter:
            self.parameter.extend(parameter)


@abstract
class Vertex(_user_module.VertexMixin, NamedElement):
    """A Vertex is an abstraction of a node in a StateMachine graph. It can be the source or destination of any number of Transitions.
<p>From package UML::StateMachines.</p>"""
    container = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    incoming = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedIncoming)
    outgoing = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedOutgoing)

    def __init__(
            self, container=None, incoming=None, outgoing=None, **kwargs):

        super(Vertex, self).__init__(**kwargs)

        if container is not None:
            self.container = container

        if incoming:
            self.incoming.extend(incoming)

        if outgoing:
            self.outgoing.extend(outgoing)


class Trigger(_user_module.TriggerMixin, NamedElement):
    """A Trigger specifies a specific point  at which an Event occurrence may trigger an effect in a Behavior. A Trigger may be qualified by the Port on which the Event occurred.
<p>From package UML::CommonBehavior.</p>"""
    event = EReference(ordered=False, unique=True,
                       containment=False, derived=False)
    port = EReference(ordered=False, unique=True,
                      containment=False, derived=False, upper=-1)

    def __init__(self, event=None, port=None, **kwargs):

        super(Trigger, self).__init__(**kwargs)

        if event is not None:
            self.event = event

        if port:
            self.port.extend(port)


class OperationTemplateParameter(
        _user_module.OperationTemplateParameterMixin, TemplateParameter):
    """An OperationTemplateParameter exposes an Operation as a formal parameter for a template.
<p>From package UML::Classification.</p>"""

    def __init__(self, **kwargs):

        super(OperationTemplateParameter, self).__init__(**kwargs)


class CollaborationUse(_user_module.CollaborationUseMixin, NamedElement):
    """A CollaborationUse is used to specify the application of a pattern specified by a Collaboration to a specific situation.
<p>From package UML::StructuredClassifiers.</p>"""
    roleBinding = EReference(ordered=False, unique=True,
                             containment=True, derived=False, upper=-1)
    type = EReference(ordered=False, unique=True,
                      containment=False, derived=False)

    def __init__(self, roleBinding=None, type=None, **kwargs):

        super(CollaborationUse, self).__init__(**kwargs)

        if roleBinding:
            self.roleBinding.extend(roleBinding)

        if type is not None:
            self.type = type


class ClassifierTemplateParameter(
        _user_module.ClassifierTemplateParameterMixin, TemplateParameter):
    """A ClassifierTemplateParameter exposes a Classifier as a formal template parameter.
<p>From package UML::Classification.</p>"""
    allowSubstitutable = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=True)
    constrainingClassifier = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(
            self, allowSubstitutable=None, constrainingClassifier=None, **
            kwargs):

        super(ClassifierTemplateParameter, self).__init__(**kwargs)

        if allowSubstitutable is not None:
            self.allowSubstitutable = allowSubstitutable

        if constrainingClassifier:
            self.constrainingClassifier.extend(constrainingClassifier)


class LinkEndCreationData(_user_module.LinkEndCreationDataMixin, LinkEndData):
    """LinkEndCreationData is LinkEndData used to provide values for one end of a link to be created by a CreateLinkAction.
<p>From package UML::Actions.</p>"""
    isReplaceAll = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    insertAt = EReference(ordered=False, unique=True,
                          containment=False, derived=False)

    def __init__(self, insertAt=None, isReplaceAll=None, **kwargs):

        super(LinkEndCreationData, self).__init__(**kwargs)

        if isReplaceAll is not None:
            self.isReplaceAll = isReplaceAll

        if insertAt is not None:
            self.insertAt = insertAt


class LinkEndDestructionData(
        _user_module.LinkEndDestructionDataMixin, LinkEndData):
    """LinkEndDestructionData is LinkEndData used to provide values for one end of a link to be destroyed by a DestroyLinkAction.
<p>From package UML::Actions.</p>"""
    isDestroyDuplicates = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    destroyAt = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(self, destroyAt=None, isDestroyDuplicates=None, **kwargs):

        super(LinkEndDestructionData, self).__init__(**kwargs)

        if isDestroyDuplicates is not None:
            self.isDestroyDuplicates = isDestroyDuplicates

        if destroyAt is not None:
            self.destroyAt = destroyAt


class Message(_user_module.MessageMixin, NamedElement):
    """A Message defines a particular communication between Lifelines of an Interaction.
<p>From package UML::Interactions.</p>"""
    _messageKind = EAttribute(
        eType=MessageKind, derived=True, changeable=False, name='messageKind',
        default_value=MessageKind.unknown, transient=True)
    messageSort = EAttribute(
        eType=MessageSort, derived=False, changeable=True,
        default_value=MessageSort.synchCall)
    argument = EReference(ordered=True, unique=True,
                          containment=True, derived=False, upper=-1)
    connector = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    interaction = EReference(ordered=False, unique=True,
                             containment=False, derived=False)
    receiveEvent = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    sendEvent = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    signature = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(
            self, argument=None, connector=None, interaction=None,
            messageKind=None, messageSort=None, receiveEvent=None,
            sendEvent=None, signature=None, **kwargs):

        super(Message, self).__init__(**kwargs)

        if messageKind is not None:
            self.messageKind = messageKind

        if messageSort is not None:
            self.messageSort = messageSort

        if argument:
            self.argument.extend(argument)

        if connector is not None:
            self.connector = connector

        if interaction is not None:
            self.interaction = interaction

        if receiveEvent is not None:
            self.receiveEvent = receiveEvent

        if sendEvent is not None:
            self.sendEvent = sendEvent

        if signature is not None:
            self.signature = signature


@abstract
class InteractionFragment(_user_module.InteractionFragmentMixin, NamedElement):
    """InteractionFragment is an abstract notion of the most general interaction unit. An InteractionFragment is a piece of an Interaction. Each InteractionFragment is conceptually like an Interaction by itself.
<p>From package UML::Interactions.</p>"""
    covered = EReference(ordered=False, unique=True,
                         containment=False, derived=False, upper=-1)
    enclosingOperand = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    enclosingInteraction = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    generalOrdering = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, covered=None, enclosingOperand=None,
                 enclosingInteraction=None, generalOrdering=None, **kwargs):

        super(InteractionFragment, self).__init__(**kwargs)

        if covered:
            self.covered.extend(covered)

        if enclosingOperand is not None:
            self.enclosingOperand = enclosingOperand

        if enclosingInteraction is not None:
            self.enclosingInteraction = enclosingInteraction

        if generalOrdering:
            self.generalOrdering.extend(generalOrdering)


class Lifeline(_user_module.LifelineMixin, NamedElement):
    """A Lifeline represents an individual participant in the Interaction. While parts and structural features may have multiplicity greater than 1, Lifelines represent only one interacting entity.
<p>From package UML::Interactions.</p>"""
    decomposedAs = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    interaction = EReference(ordered=False, unique=True,
                             containment=False, derived=False)
    represents = EReference(ordered=False, unique=True,
                            containment=False, derived=False)
    selector = EReference(ordered=False, unique=True,
                          containment=True, derived=False)
    coveredBy = EReference(ordered=False, unique=True,
                           containment=False, derived=False, upper=-1)

    def __init__(
            self, decomposedAs=None, interaction=None, represents=None,
            selector=None, coveredBy=None, **kwargs):

        super(Lifeline, self).__init__(**kwargs)

        if decomposedAs is not None:
            self.decomposedAs = decomposedAs

        if interaction is not None:
            self.interaction = interaction

        if represents is not None:
            self.represents = represents

        if selector is not None:
            self.selector = selector

        if coveredBy:
            self.coveredBy.extend(coveredBy)


@abstract
class MessageEnd(_user_module.MessageEndMixin, NamedElement):
    """MessageEnd is an abstract specialization of NamedElement that represents what can occur at the end of a Message.
<p>From package UML::Interactions.</p>"""
    message = EReference(ordered=False, unique=True,
                         containment=False, derived=False)

    def __init__(self, message=None, **kwargs):

        super(MessageEnd, self).__init__(**kwargs)

        if message is not None:
            self.message = message


class GeneralOrdering(_user_module.GeneralOrderingMixin, NamedElement):
    """A GeneralOrdering represents a binary relation between two OccurrenceSpecifications, to describe that one OccurrenceSpecification must occur before the other in a valid trace. This mechanism provides the ability to define partial orders of OccurrenceSpecifications that may otherwise not have a specified order.
<p>From package UML::Interactions.</p>"""
    after = EReference(ordered=False, unique=True,
                       containment=False, derived=False)
    before = EReference(ordered=False, unique=True,
                        containment=False, derived=False)

    def __init__(self, after=None, before=None, **kwargs):

        super(GeneralOrdering, self).__init__(**kwargs)

        if after is not None:
            self.after = after

        if before is not None:
            self.before = before


@abstract
class PackageableElement(
        _user_module.PackageableElementMixin, NamedElement, ParameterableElement):
    """A PackageableElement is a NamedElement that may be owned directly by a Package. A PackageableElement is also able to serve as the parameteredElement of a TemplateParameter.
<p>From package UML::CommonStructure.</p>"""

    def __init__(self, **kwargs):

        super(PackageableElement, self).__init__(**kwargs)


class TemplateBinding(_user_module.TemplateBindingMixin, DirectedRelationship):
    """A TemplateBinding is a DirectedRelationship between a TemplateableElement and a template. A TemplateBinding specifies the TemplateParameterSubstitutions of actual parameters for the formal parameters of the template.
<p>From package UML::CommonStructure.</p>"""
    parameterSubstitution = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    signature = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    boundElement = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(
            self, parameterSubstitution=None, signature=None,
            boundElement=None, **kwargs):

        super(TemplateBinding, self).__init__(**kwargs)

        if parameterSubstitution:
            self.parameterSubstitution.extend(parameterSubstitution)

        if signature is not None:
            self.signature = signature

        if boundElement is not None:
            self.boundElement = boundElement


@abstract
class Feature(_user_module.FeatureMixin, RedefinableElement):
    """A Feature declares a behavioral or structural characteristic of Classifiers.
<p>From package UML::Classification.</p>"""
    isStatic = EAttribute(eType=Boolean, derived=False,
                          changeable=True, default_value=False)
    featuringClassifier = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedFeaturingclassifier)

    def __init__(self, featuringClassifier=None, isStatic=None, **kwargs):

        super(Feature, self).__init__(**kwargs)

        if isStatic is not None:
            self.isStatic = isStatic

        if featuringClassifier:
            self.featuringClassifier.extend(featuringClassifier)


class Pseudostate(_user_module.PseudostateMixin, Vertex):
    """A Pseudostate is an abstraction that encompasses different types of transient Vertices in the StateMachine graph. A StateMachine instance never comes to rest in a Pseudostate, instead, it will exit and enter the Pseudostate within a single run-to-completion step.
<p>From package UML::StateMachines.</p>"""
    kind = EAttribute(
        eType=PseudostateKind, derived=False, changeable=True,
        default_value=PseudostateKind.initial)
    state = EReference(ordered=False, unique=True,
                       containment=False, derived=False)
    stateMachine = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, state=None, kind=None, stateMachine=None, **kwargs):

        super(Pseudostate, self).__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if state is not None:
            self.state = state

        if stateMachine is not None:
            self.stateMachine = stateMachine


class ConnectionPointReference(
        _user_module.ConnectionPointReferenceMixin, Vertex):
    """A ConnectionPointReference represents a usage (as part of a submachine State) of an entry/exit point Pseudostate defined in the StateMachine referenced by the submachine State.
<p>From package UML::StateMachines.</p>"""
    entry = EReference(ordered=False, unique=True,
                       containment=False, derived=False, upper=-1)
    exit = EReference(ordered=False, unique=True,
                      containment=False, derived=False, upper=-1)
    state = EReference(ordered=False, unique=True,
                       containment=False, derived=False)

    def __init__(self, entry=None, exit=None, state=None, **kwargs):

        super(ConnectionPointReference, self).__init__(**kwargs)

        if entry:
            self.entry.extend(entry)

        if exit:
            self.exit.extend(exit)

        if state is not None:
            self.state = state


class ProtocolConformance(
        _user_module.ProtocolConformanceMixin, DirectedRelationship):
    """A ProtocolStateMachine can be redefined into a more specific ProtocolStateMachine or into behavioral StateMachine. ProtocolConformance declares that the specific ProtocolStateMachine specifies a protocol that conforms to the general ProtocolStateMachine or that the specific behavioral StateMachine abides by the protocol of the general ProtocolStateMachine.
<p>From package UML::StateMachines.</p>"""
    generalMachine = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    specificMachine = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, generalMachine=None, specificMachine=None, **kwargs):

        super(ProtocolConformance, self).__init__(**kwargs)

        if generalMachine is not None:
            self.generalMachine = generalMachine

        if specificMachine is not None:
            self.specificMachine = specificMachine


class PackageMerge(_user_module.PackageMergeMixin, DirectedRelationship):
    """A package merge defines how the contents of one package are extended by the contents of another package.
<p>From package UML::Packages.</p>"""
    mergedPackage = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    receivingPackage = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, mergedPackage=None, receivingPackage=None, **kwargs):

        super(PackageMerge, self).__init__(**kwargs)

        if mergedPackage is not None:
            self.mergedPackage = mergedPackage

        if receivingPackage is not None:
            self.receivingPackage = receivingPackage


class ProfileApplication(
        _user_module.ProfileApplicationMixin, DirectedRelationship):
    """A profile application is used to show which profiles have been applied to a package.
<p>From package UML::Packages.</p>"""
    isStrict = EAttribute(eType=Boolean, derived=False,
                          changeable=True, default_value=False)
    appliedProfile = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    applyingPackage = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, appliedProfile=None, isStrict=None,
                 applyingPackage=None, **kwargs):

        super(ProfileApplication, self).__init__(**kwargs)

        if isStrict is not None:
            self.isStrict = isStrict

        if appliedProfile is not None:
            self.appliedProfile = appliedProfile

        if applyingPackage is not None:
            self.applyingPackage = applyingPackage


class ElementImport(_user_module.ElementImportMixin, DirectedRelationship):
    """An ElementImport identifies a NamedElement in a Namespace other than the one that owns that NamedElement and allows the NamedElement to be referenced using an unqualified name in the Namespace owning the ElementImport.
<p>From package UML::CommonStructure.</p>"""
    alias = EAttribute(eType=String, derived=False, changeable=True)
    visibility = EAttribute(
        eType=VisibilityKind, derived=False, changeable=True,
        default_value=VisibilityKind.public)
    importedElement = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    importingNamespace = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, alias=None, importedElement=None,
                 importingNamespace=None, visibility=None, **kwargs):

        super(ElementImport, self).__init__(**kwargs)

        if alias is not None:
            self.alias = alias

        if visibility is not None:
            self.visibility = visibility

        if importedElement is not None:
            self.importedElement = importedElement

        if importingNamespace is not None:
            self.importingNamespace = importingNamespace


class PackageImport(_user_module.PackageImportMixin, DirectedRelationship):
    """A PackageImport is a Relationship that imports all the non-private members of a Package into the Namespace owning the PackageImport, so that those Elements may be referred to by their unqualified names in the importingNamespace.
<p>From package UML::CommonStructure.</p>"""
    visibility = EAttribute(
        eType=VisibilityKind, derived=False, changeable=True,
        default_value=VisibilityKind.public)
    importedPackage = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    importingNamespace = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(
            self, importedPackage=None, importingNamespace=None,
            visibility=None, **kwargs):

        super(PackageImport, self).__init__(**kwargs)

        if visibility is not None:
            self.visibility = visibility

        if importedPackage is not None:
            self.importedPackage = importedPackage

        if importingNamespace is not None:
            self.importingNamespace = importingNamespace


class Generalization(_user_module.GeneralizationMixin, DirectedRelationship):
    """A Generalization is a taxonomic relationship between a more general Classifier and a more specific Classifier. Each instance of the specific Classifier is also an instance of the general Classifier. The specific Classifier inherits the features of the more general Classifier. A Generalization is owned by the specific Classifier.
<p>From package UML::Classification.</p>"""
    isSubstitutable = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=True)
    general = EReference(ordered=False, unique=True,
                         containment=False, derived=False)
    generalizationSet = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    specific = EReference(ordered=False, unique=True,
                          containment=False, derived=False)

    def __init__(self, general=None, generalizationSet=None,
                 isSubstitutable=None, specific=None, **kwargs):

        super(Generalization, self).__init__(**kwargs)

        if isSubstitutable is not None:
            self.isSubstitutable = isSubstitutable

        if general is not None:
            self.general = general

        if generalizationSet:
            self.generalizationSet.extend(generalizationSet)

        if specific is not None:
            self.specific = specific


class ExtensionPoint(_user_module.ExtensionPointMixin, RedefinableElement):
    """An ExtensionPoint identifies a point in the behavior of a UseCase where that behavior can be extended by the behavior of some other (extending) UseCase, as specified by an Extend relationship.
<p>From package UML::UseCases.</p>"""
    useCase = EReference(ordered=False, unique=True,
                         containment=False, derived=False)

    def __init__(self, useCase=None, **kwargs):

        super(ExtensionPoint, self).__init__(**kwargs)

        if useCase is not None:
            self.useCase = useCase


@abstract
class ActivityGroup(
        _user_module.ActivityGroupMixin, NamedElement, ActivityContent):
    """ActivityGroup is an abstract class for defining sets of ActivityNodes and ActivityEdges in an Activity.
<p>From package UML::Activities.</p>"""
    containedEdge = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedContainededge)
    containedNode = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedContainednode)
    _inActivity = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='inActivity', transient=True)
    subgroup = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedSubgroup)
    _superGroup = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='superGroup', transient=True)

    def __init__(self, containedEdge=None, containedNode=None,
                 inActivity=None, subgroup=None, superGroup=None, **kwargs):

        super(ActivityGroup, self).__init__(**kwargs)

        if containedEdge:
            self.containedEdge.extend(containedEdge)

        if containedNode:
            self.containedNode.extend(containedNode)

        if inActivity is not None:
            self.inActivity = inActivity

        if subgroup:
            self.subgroup.extend(subgroup)

        if superGroup is not None:
            self.superGroup = superGroup


@abstract
class ActivityEdge(_user_module.ActivityEdgeMixin, RedefinableElement):
    """An ActivityEdge is an abstract class for directed connections between two ActivityNodes.
<p>From package UML::Activities.</p>"""
    activity = EReference(ordered=False, unique=True,
                          containment=False, derived=False)
    guard = EReference(ordered=False, unique=True,
                       containment=True, derived=False)
    inPartition = EReference(ordered=False, unique=True,
                             containment=False, derived=False, upper=-1)
    interrupts = EReference(ordered=False, unique=True,
                            containment=False, derived=False)
    inStructuredNode = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    target = EReference(ordered=False, unique=True,
                        containment=False, derived=False)
    source = EReference(ordered=False, unique=True,
                        containment=False, derived=False)
    redefinedEdge = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    weight = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    inGroup = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedIngroup)

    def __init__(
            self, activity=None, guard=None, inPartition=None,
            interrupts=None, inStructuredNode=None, target=None, source=None,
            redefinedEdge=None, weight=None, inGroup=None, **kwargs):

        super(ActivityEdge, self).__init__(**kwargs)

        if activity is not None:
            self.activity = activity

        if guard is not None:
            self.guard = guard

        if inPartition:
            self.inPartition.extend(inPartition)

        if interrupts is not None:
            self.interrupts = interrupts

        if inStructuredNode is not None:
            self.inStructuredNode = inStructuredNode

        if target is not None:
            self.target = target

        if source is not None:
            self.source = source

        if redefinedEdge:
            self.redefinedEdge.extend(redefinedEdge)

        if weight is not None:
            self.weight = weight

        if inGroup:
            self.inGroup.extend(inGroup)


class InteractionUse(_user_module.InteractionUseMixin, InteractionFragment):
    """An InteractionUse refers to an Interaction. The InteractionUse is a shorthand for copying the contents of the referenced Interaction where the InteractionUse is. To be accurate the copying must take into account substituting parameters with arguments and connect the formal Gates with the actual ones.
<p>From package UML::Interactions.</p>"""
    actualGate = EReference(ordered=False, unique=True,
                            containment=True, derived=False, upper=-1)
    argument = EReference(ordered=True, unique=True,
                          containment=True, derived=False, upper=-1)
    refersTo = EReference(ordered=False, unique=True,
                          containment=False, derived=False)
    returnValue = EReference(ordered=False, unique=True,
                             containment=True, derived=False)
    returnValueRecipient = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, actualGate=None, argument=None, refersTo=None,
                 returnValue=None, returnValueRecipient=None, **kwargs):

        super(InteractionUse, self).__init__(**kwargs)

        if actualGate:
            self.actualGate.extend(actualGate)

        if argument:
            self.argument.extend(argument)

        if refersTo is not None:
            self.refersTo = refersTo

        if returnValue is not None:
            self.returnValue = returnValue

        if returnValueRecipient is not None:
            self.returnValueRecipient = returnValueRecipient


class Gate(_user_module.GateMixin, MessageEnd):
    """A Gate is a MessageEnd which serves as a connection point for relating a Message which has a MessageEnd (sendEvent / receiveEvent) outside an InteractionFragment with another Message which has a MessageEnd (receiveEvent / sendEvent)  inside that InteractionFragment.
<p>From package UML::Interactions.</p>"""

    def __init__(self, **kwargs):

        super(Gate, self).__init__(**kwargs)


class OccurrenceSpecification(
        _user_module.OccurrenceSpecificationMixin, InteractionFragment):
    """An OccurrenceSpecification is the basic semantic unit of Interactions. The sequences of occurrences specified by them are the meanings of Interactions.
<p>From package UML::Interactions.</p>"""
    toAfter = EReference(ordered=False, unique=True,
                         containment=False, derived=False, upper=-1)
    toBefore = EReference(ordered=False, unique=True,
                          containment=False, derived=False, upper=-1)

    def __init__(self, toAfter=None, toBefore=None, **kwargs):

        super(OccurrenceSpecification, self).__init__(**kwargs)

        if toAfter:
            self.toAfter.extend(toAfter)

        if toBefore:
            self.toBefore.extend(toBefore)


@abstract
class ExecutionSpecification(
        _user_module.ExecutionSpecificationMixin, InteractionFragment):
    """An ExecutionSpecification is a specification of the execution of a unit of Behavior or Action within the Lifeline. The duration of an ExecutionSpecification is represented by two OccurrenceSpecifications, the start OccurrenceSpecification and the finish OccurrenceSpecification.
<p>From package UML::Interactions.</p>"""
    finish = EReference(ordered=False, unique=True,
                        containment=False, derived=False)
    start = EReference(ordered=False, unique=True,
                       containment=False, derived=False)

    def __init__(self, finish=None, start=None, **kwargs):

        super(ExecutionSpecification, self).__init__(**kwargs)

        if finish is not None:
            self.finish = finish

        if start is not None:
            self.start = start


class CombinedFragment(
        _user_module.CombinedFragmentMixin, InteractionFragment):
    """A CombinedFragment defines an expression of InteractionFragments. A CombinedFragment is defined by an interaction operator and corresponding InteractionOperands. Through the use of CombinedFragments the user will be able to describe a number of traces in a compact and concise manner.
<p>From package UML::Interactions.</p>"""
    interactionOperator = EAttribute(
        eType=InteractionOperatorKind, derived=False, changeable=True,
        default_value=InteractionOperatorKind.seq)
    cfragmentGate = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    operand = EReference(ordered=True, unique=True,
                         containment=True, derived=False, upper=-1)

    def __init__(
            self, cfragmentGate=None, interactionOperator=None,
            operand=None, **kwargs):

        super(CombinedFragment, self).__init__(**kwargs)

        if interactionOperator is not None:
            self.interactionOperator = interactionOperator

        if cfragmentGate:
            self.cfragmentGate.extend(cfragmentGate)

        if operand:
            self.operand.extend(operand)


class Continuation(_user_module.ContinuationMixin, InteractionFragment):
    """A Continuation is a syntactic way to define continuations of different branches of an alternative CombinedFragment. Continuations are intuitively similar to labels representing intermediate points in a flow of control.
<p>From package UML::Interactions.</p>"""
    setting = EAttribute(eType=Boolean, derived=False,
                         changeable=True, default_value=True)

    def __init__(self, setting=None, **kwargs):

        super(Continuation, self).__init__(**kwargs)

        if setting is not None:
            self.setting = setting


class StateInvariant(_user_module.StateInvariantMixin, InteractionFragment):
    """A StateInvariant is a runtime constraint on the participants of the Interaction. It may be used to specify a variety of different kinds of Constraints, such as values of Attributes or Variables, internal or external States, and so on. A StateInvariant is an InteractionFragment and it is placed on a Lifeline.
<p>From package UML::Interactions.</p>"""
    invariant = EReference(ordered=False, unique=True,
                           containment=True, derived=False)

    def __init__(self, invariant=None, **kwargs):

        super(StateInvariant, self).__init__(**kwargs)

        if invariant is not None:
            self.invariant = invariant


@abstract
class Type(_user_module.TypeMixin, PackageableElement):
    """A Type constrains the values represented by a TypedElement.
<p>From package UML::CommonStructure.</p>"""
    _package = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='package', transient=True)

    def __init__(self, package=None, **kwargs):

        super(Type, self).__init__(**kwargs)

        if package is not None:
            self.package = package


@abstract
class ConnectableElement(
        _user_module.ConnectableElementMixin, TypedElement, ParameterableElement):
    """ConnectableElement is an abstract metaclass representing a set of instances that play roles of a StructuredClassifier. ConnectableElements may be joined by attached Connectors and specify configurations of linked instances to be created within an instance of the containing StructuredClassifier.
<p>From package UML::StructuredClassifiers.</p>"""
    end = EReference(ordered=False, unique=True, containment=False,
                     derived=True, upper=-1, transient=True,
                     derived_class=_user_module.DerivedEnd)

    def __init__(self, end=None, **kwargs):

        super(ConnectableElement, self).__init__(**kwargs)

        if end:
            self.end.extend(end)


class Constraint(_user_module.ConstraintMixin, PackageableElement):
    """A Constraint is a condition or restriction expressed in natural language text or in a machine readable language for the purpose of declaring some of the semantics of an Element or set of Elements.
<p>From package UML::CommonStructure.</p>"""
    constrainedElement = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)
    context = EReference(ordered=False, unique=True,
                         containment=False, derived=False)
    specification = EReference(
        ordered=False, unique=True, containment=True, derived=False)

    def __init__(self, constrainedElement=None, context=None,
                 specification=None, **kwargs):

        super(Constraint, self).__init__(**kwargs)

        if constrainedElement:
            self.constrainedElement.extend(constrainedElement)

        if context is not None:
            self.context = context

        if specification is not None:
            self.specification = specification


class Region(_user_module.RegionMixin, Namespace, RedefinableElement):
    """A Region is a top-level part of a StateMachine or a composite State, that serves as a container for the Vertices and Transitions of the StateMachine. A StateMachine or composite State may contain multiple Regions representing behaviors that may occur in parallel.
<p>From package UML::StateMachines.</p>"""
    extendedRegion = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    state = EReference(ordered=False, unique=True,
                       containment=False, derived=False)
    stateMachine = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    transition = EReference(ordered=False, unique=True,
                            containment=True, derived=False, upper=-1)
    subvertex = EReference(ordered=False, unique=True,
                           containment=True, derived=False, upper=-1)

    def __init__(
            self, extendedRegion=None, state=None, stateMachine=None,
            transition=None, subvertex=None, **kwargs):

        super(Region, self).__init__(**kwargs)

        if extendedRegion is not None:
            self.extendedRegion = extendedRegion

        if state is not None:
            self.state = state

        if stateMachine is not None:
            self.stateMachine = stateMachine

        if transition:
            self.transition.extend(transition)

        if subvertex:
            self.subvertex.extend(subvertex)


@abstract
class Event(_user_module.EventMixin, PackageableElement):
    """An Event is the specification of some occurrence that may potentially trigger effects by an object.
<p>From package UML::CommonBehavior.</p>"""

    def __init__(self, **kwargs):

        super(Event, self).__init__(**kwargs)


class Transition(_user_module.TransitionMixin, Namespace, RedefinableElement):
    """A Transition represents an arc between exactly one source Vertex and exactly one Target vertex (the source and targets may be the same Vertex). It may form part of a compound transition, which takes the StateMachine from one steady State configuration to another, representing the full response of the StateMachine to an occurrence of an Event that triggered it.
<p>From package UML::StateMachines.</p>"""
    kind = EAttribute(
        eType=TransitionKind, derived=False, changeable=True,
        default_value=TransitionKind.external)
    effect = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    guard = EReference(ordered=False, unique=True,
                       containment=False, derived=False)
    redefinedTransition = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    source = EReference(ordered=False, unique=True,
                        containment=False, derived=False)
    target = EReference(ordered=False, unique=True,
                        containment=False, derived=False)
    trigger = EReference(ordered=False, unique=True,
                         containment=True, derived=False, upper=-1)
    container = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(self, effect=None, guard=None, kind=None,
                 redefinedTransition=None, source=None, target=None,
                 trigger=None, container=None, **kwargs):

        super(Transition, self).__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if effect is not None:
            self.effect = effect

        if guard is not None:
            self.guard = guard

        if redefinedTransition is not None:
            self.redefinedTransition = redefinedTransition

        if source is not None:
            self.source = source

        if target is not None:
            self.target = target

        if trigger:
            self.trigger.extend(trigger)

        if container is not None:
            self.container = container


class Connector(_user_module.ConnectorMixin, Feature):
    """A Connector specifies links that enables communication between two or more instances. In contrast to Associations, which specify links between any instance of the associated Classifiers, Connectors specify links between instances playing the connected parts only.
<p>From package UML::StructuredClassifiers.</p>"""
    _kind = EAttribute(eType=ConnectorKind, derived=True,
                       changeable=False, name='kind', transient=True)
    contract = EReference(ordered=False, unique=True,
                          containment=False, derived=False, upper=-1)
    end = EReference(ordered=True, unique=True,
                     containment=True, derived=False, upper=-1)
    redefinedConnector = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    type = EReference(ordered=False, unique=True,
                      containment=False, derived=False)

    def __init__(self, contract=None, end=None, kind=None,
                 redefinedConnector=None, type=None, **kwargs):

        super(Connector, self).__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if contract:
            self.contract.extend(contract)

        if end:
            self.end.extend(end)

        if redefinedConnector:
            self.redefinedConnector.extend(redefinedConnector)

        if type is not None:
            self.type = type


class GeneralizationSet(
        _user_module.GeneralizationSetMixin, PackageableElement):
    """A GeneralizationSet is a PackageableElement whose instances represent sets of Generalization relationships.
<p>From package UML::Classification.</p>"""
    isCovering = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=False)
    isDisjoint = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=False)
    powertype = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    generalization = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(
            self, isCovering=None, isDisjoint=None, powertype=None,
            generalization=None, **kwargs):

        super(GeneralizationSet, self).__init__(**kwargs)

        if isCovering is not None:
            self.isCovering = isCovering

        if isDisjoint is not None:
            self.isDisjoint = isDisjoint

        if powertype is not None:
            self.powertype = powertype

        if generalization:
            self.generalization.extend(generalization)


class RedefinableTemplateSignature(
        _user_module.RedefinableTemplateSignatureMixin, RedefinableElement,
        TemplateSignature):
    """A RedefinableTemplateSignature supports the addition of formal template parameters in a specialization of a template classifier.
<p>From package UML::Classification.</p>"""
    extendedSignature = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    inheritedParameter = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedInheritedparameter)
    classifier = EReference(ordered=False, unique=True,
                            containment=False, derived=False, transient=True)

    def __init__(
            self, extendedSignature=None, inheritedParameter=None,
            classifier=None, **kwargs):

        super(RedefinableTemplateSignature, self).__init__(**kwargs)

        if extendedSignature:
            self.extendedSignature.extend(extendedSignature)

        if inheritedParameter:
            self.inheritedParameter.extend(inheritedParameter)

        if classifier is not None:
            self.classifier = classifier


class Extend(_user_module.ExtendMixin, NamedElement, DirectedRelationship):
    """A relationship from an extending UseCase to an extended UseCase that specifies how and when the behavior defined in the extending UseCase can be inserted into the behavior defined in the extended UseCase.
<p>From package UML::UseCases.</p>"""
    condition = EReference(ordered=False, unique=True,
                           containment=True, derived=False)
    extendedCase = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    extensionLocation = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)
    extension = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(self, condition=None, extendedCase=None,
                 extensionLocation=None, extension=None, **kwargs):

        super(Extend, self).__init__(**kwargs)

        if condition is not None:
            self.condition = condition

        if extendedCase is not None:
            self.extendedCase = extendedCase

        if extensionLocation:
            self.extensionLocation.extend(extensionLocation)

        if extension is not None:
            self.extension = extension


class Include(_user_module.IncludeMixin, NamedElement, DirectedRelationship):
    """An Include relationship specifies that a UseCase contains the behavior defined in another UseCase.
<p>From package UML::UseCases.</p>"""
    addition = EReference(ordered=False, unique=True,
                          containment=False, derived=False)
    includingCase = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, addition=None, includingCase=None, **kwargs):

        super(Include, self).__init__(**kwargs)

        if addition is not None:
            self.addition = addition

        if includingCase is not None:
            self.includingCase = includingCase


class ActivityPartition(_user_module.ActivityPartitionMixin, ActivityGroup):
    """An ActivityPartition is a kind of ActivityGroup for identifying ActivityNodes that have some characteristic in common.
<p>From package UML::Activities.</p>"""
    isDimension = EAttribute(eType=Boolean, derived=False,
                             changeable=True, default_value=False)
    isExternal = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=False)
    node = EReference(ordered=False, unique=True,
                      containment=False, derived=False, upper=-1)
    represents = EReference(ordered=False, unique=True,
                            containment=False, derived=False)
    subpartition = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    superPartition = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    edge = EReference(ordered=False, unique=True,
                      containment=False, derived=False, upper=-1)

    def __init__(
            self, isDimension=None, isExternal=None, node=None,
            represents=None, subpartition=None, superPartition=None, edge=None,
            **kwargs):

        super(ActivityPartition, self).__init__(**kwargs)

        if isDimension is not None:
            self.isDimension = isDimension

        if isExternal is not None:
            self.isExternal = isExternal

        if node:
            self.node.extend(node)

        if represents is not None:
            self.represents = represents

        if subpartition:
            self.subpartition.extend(subpartition)

        if superPartition is not None:
            self.superPartition = superPartition

        if edge:
            self.edge.extend(edge)


@abstract
class ActivityNode(
        _user_module.ActivityNodeMixin, RedefinableElement, ActivityContent):
    """ActivityNode is an abstract class for points in the flow of an Activity connected by ActivityEdges.
<p>From package UML::Activities.</p>"""
    _activity = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='activity', transient=True)
    inGroup = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedIngroup)
    inInterruptibleRegion = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    inStructuredNode = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    incoming = EReference(ordered=False, unique=True,
                          containment=False, derived=False, upper=-1)
    outgoing = EReference(ordered=False, unique=True,
                          containment=False, derived=False, upper=-1)
    redefinedNode = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    inPartition = EReference(ordered=False, unique=True,
                             containment=False, derived=False, upper=-1)

    def __init__(self, activity=None, inGroup=None,
                 inInterruptibleRegion=None, inStructuredNode=None,
                 incoming=None, outgoing=None, redefinedNode=None,
                 inPartition=None, **kwargs):

        super(ActivityNode, self).__init__(**kwargs)

        if activity is not None:
            self.activity = activity

        if inGroup:
            self.inGroup.extend(inGroup)

        if inInterruptibleRegion:
            self.inInterruptibleRegion.extend(inInterruptibleRegion)

        if inStructuredNode is not None:
            self.inStructuredNode = inStructuredNode

        if incoming:
            self.incoming.extend(incoming)

        if outgoing:
            self.outgoing.extend(outgoing)

        if redefinedNode:
            self.redefinedNode.extend(redefinedNode)

        if inPartition:
            self.inPartition.extend(inPartition)


class InterruptibleActivityRegion(
        _user_module.InterruptibleActivityRegionMixin, ActivityGroup):
    """An InterruptibleActivityRegion is an ActivityGroup that supports the termination of tokens flowing in the portions of an activity within it.
<p>From package UML::Activities.</p>"""
    interruptingEdge = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    node = EReference(ordered=False, unique=True,
                      containment=False, derived=False, upper=-1)

    def __init__(self, interruptingEdge=None, node=None, **kwargs):

        super(InterruptibleActivityRegion, self).__init__(**kwargs)

        if interruptingEdge:
            self.interruptingEdge.extend(interruptingEdge)

        if node:
            self.node.extend(node)


class ControlFlow(_user_module.ControlFlowMixin, ActivityEdge):
    """A ControlFlow is an ActivityEdge traversed by control tokens or object tokens of control type, which are use to control the execution of ExecutableNodes.
<p>From package UML::Activities.</p>"""

    def __init__(self, **kwargs):

        super(ControlFlow, self).__init__(**kwargs)


class ObjectFlow(_user_module.ObjectFlowMixin, ActivityEdge):
    """An ObjectFlow is an ActivityEdge that is traversed by object tokens that may hold values. Object flows also support multicast/receive, token selection from object nodes, and transformation of tokens.
<p>From package UML::Activities.</p>"""
    isMulticast = EAttribute(eType=Boolean, derived=False,
                             changeable=True, default_value=False)
    isMultireceive = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    selection = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    transformation = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, isMulticast=None, isMultireceive=None,
                 selection=None, transformation=None, **kwargs):

        super(ObjectFlow, self).__init__(**kwargs)

        if isMulticast is not None:
            self.isMulticast = isMulticast

        if isMultireceive is not None:
            self.isMultireceive = isMultireceive

        if selection is not None:
            self.selection = selection

        if transformation is not None:
            self.transformation = transformation


@abstract
class Observation(_user_module.ObservationMixin, PackageableElement):
    """Observation specifies a value determined by observing an event or events that occur relative to other model Elements.
<p>From package UML::Values.</p>"""

    def __init__(self, **kwargs):

        super(Observation, self).__init__(**kwargs)


class PartDecomposition(_user_module.PartDecompositionMixin, InteractionUse):
    """A PartDecomposition is a description of the internal Interactions of one Lifeline relative to an Interaction.
<p>From package UML::Interactions.</p>"""

    def __init__(self, **kwargs):

        super(PartDecomposition, self).__init__(**kwargs)


class InteractionOperand(
        _user_module.InteractionOperandMixin, Namespace, InteractionFragment):
    """An InteractionOperand is contained in a CombinedFragment. An InteractionOperand represents one operand of the expression given by the enclosing CombinedFragment.
<p>From package UML::Interactions.</p>"""
    fragment = EReference(ordered=True, unique=True,
                          containment=True, derived=False, upper=-1)
    guard = EReference(ordered=False, unique=True,
                       containment=True, derived=False)

    def __init__(self, fragment=None, guard=None, **kwargs):

        super(InteractionOperand, self).__init__(**kwargs)

        if fragment:
            self.fragment.extend(fragment)

        if guard is not None:
            self.guard = guard


class ActionExecutionSpecification(
        _user_module.ActionExecutionSpecificationMixin, ExecutionSpecification):
    """An ActionExecutionSpecification is a kind of ExecutionSpecification representing the execution of an Action.
<p>From package UML::Interactions.</p>"""
    action = EReference(ordered=False, unique=True,
                        containment=False, derived=False)

    def __init__(self, action=None, **kwargs):

        super(ActionExecutionSpecification, self).__init__(**kwargs)

        if action is not None:
            self.action = action


class BehaviorExecutionSpecification(
        _user_module.BehaviorExecutionSpecificationMixin, ExecutionSpecification):
    """A BehaviorExecutionSpecification is a kind of ExecutionSpecification representing the execution of a Behavior.
<p>From package UML::Interactions.</p>"""
    behavior = EReference(ordered=False, unique=True,
                          containment=False, derived=False)

    def __init__(self, behavior=None, **kwargs):

        super(BehaviorExecutionSpecification, self).__init__(**kwargs)

        if behavior is not None:
            self.behavior = behavior


class ConsiderIgnoreFragment(
        _user_module.ConsiderIgnoreFragmentMixin, CombinedFragment):
    """A ConsiderIgnoreFragment is a kind of CombinedFragment that is used for the consider and ignore cases, which require lists of pertinent Messages to be specified.
<p>From package UML::Interactions.</p>"""
    message = EReference(ordered=False, unique=True,
                         containment=False, derived=False, upper=-1)

    def __init__(self, message=None, **kwargs):

        super(ConsiderIgnoreFragment, self).__init__(**kwargs)

        if message:
            self.message.extend(message)


class ExecutionOccurrenceSpecification(
        _user_module.ExecutionOccurrenceSpecificationMixin,
        OccurrenceSpecification):
    """An ExecutionOccurrenceSpecification represents moments in time at which Actions or Behaviors start or finish.
<p>From package UML::Interactions.</p>"""
    execution = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(self, execution=None, **kwargs):

        super(ExecutionOccurrenceSpecification, self).__init__(**kwargs)

        if execution is not None:
            self.execution = execution


@abstract
class ValueSpecification(
        _user_module.ValueSpecificationMixin, PackageableElement, TypedElement):
    """A ValueSpecification is the specification of a (possibly empty) set of values. A ValueSpecification is a ParameterableElement that may be exposed as a formal TemplateParameter and provided as the actual parameter in the binding of a template.
<p>From package UML::Values.</p>"""

    def __init__(self, **kwargs):

        super(ValueSpecification, self).__init__(**kwargs)


@abstract
class BehavioralFeature(
        _user_module.BehavioralFeatureMixin, Namespace, Feature):
    """A BehavioralFeature is a feature of a Classifier that specifies an aspect of the behavior of its instances.  A BehavioralFeature is implemented (realized) by a Behavior. A BehavioralFeature specifies that a Classifier will respond to a designated request by invoking its implementing method.
<p>From package UML::Classification.</p>"""
    concurrency = EAttribute(
        eType=CallConcurrencyKind, derived=False, changeable=True,
        default_value=CallConcurrencyKind.sequential)
    isAbstract = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=False)
    method = EReference(ordered=False, unique=True,
                        containment=False, derived=False, upper=-1)
    ownedParameter = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedParameterSet = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    raisedException = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(
            self, concurrency=None, isAbstract=None, method=None,
            ownedParameter=None, ownedParameterSet=None, raisedException=None,
            **kwargs):

        super(BehavioralFeature, self).__init__(**kwargs)

        if concurrency is not None:
            self.concurrency = concurrency

        if isAbstract is not None:
            self.isAbstract = isAbstract

        if method:
            self.method.extend(method)

        if ownedParameter:
            self.ownedParameter.extend(ownedParameter)

        if ownedParameterSet:
            self.ownedParameterSet.extend(ownedParameterSet)

        if raisedException:
            self.raisedException.extend(raisedException)


class State(_user_module.StateMixin, Namespace, RedefinableElement, Vertex):
    """A State models a situation during which some (usually implicit) invariant condition holds.
<p>From package UML::StateMachines.</p>"""
    _isComposite = EAttribute(
        eType=Boolean, derived=True, changeable=False, name='isComposite',
        transient=True)
    _isOrthogonal = EAttribute(
        eType=Boolean, derived=True, changeable=False, name='isOrthogonal',
        transient=True)
    _isSimple = EAttribute(
        eType=Boolean, derived=True, changeable=False, name='isSimple',
        default_value=True, transient=True)
    _isSubmachineState = EAttribute(
        eType=Boolean, derived=True, changeable=False,
        name='isSubmachineState', transient=True)
    connection = EReference(ordered=False, unique=True,
                            containment=True, derived=False, upper=-1)
    connectionPoint = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    deferrableTrigger = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    doActivity = EReference(ordered=False, unique=True,
                            containment=True, derived=False)
    entry = EReference(ordered=False, unique=True,
                       containment=True, derived=False)
    exit = EReference(ordered=False, unique=True,
                      containment=True, derived=False)
    redefinedState = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    stateInvariant = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    submachine = EReference(ordered=False, unique=True,
                            containment=False, derived=False)
    region = EReference(ordered=False, unique=True,
                        containment=True, derived=False, upper=-1)

    def __init__(self, connection=None, connectionPoint=None,
                 deferrableTrigger=None, doActivity=None, entry=None,
                 exit=None, isComposite=None, isOrthogonal=None, isSimple=None,
                 isSubmachineState=None, redefinedState=None,
                 stateInvariant=None, submachine=None, region=None, **kwargs):

        super(State, self).__init__(**kwargs)

        if isComposite is not None:
            self.isComposite = isComposite

        if isOrthogonal is not None:
            self.isOrthogonal = isOrthogonal

        if isSimple is not None:
            self.isSimple = isSimple

        if isSubmachineState is not None:
            self.isSubmachineState = isSubmachineState

        if connection:
            self.connection.extend(connection)

        if connectionPoint:
            self.connectionPoint.extend(connectionPoint)

        if deferrableTrigger:
            self.deferrableTrigger.extend(deferrableTrigger)

        if doActivity is not None:
            self.doActivity = doActivity

        if entry is not None:
            self.entry = entry

        if exit is not None:
            self.exit = exit

        if redefinedState is not None:
            self.redefinedState = redefinedState

        if stateInvariant is not None:
            self.stateInvariant = stateInvariant

        if submachine is not None:
            self.submachine = submachine

        if region:
            self.region.extend(region)


@abstract
class ExecutableNode(_user_module.ExecutableNodeMixin, ActivityNode):
    """An ExecutableNode is an abstract class for ActivityNodes whose execution may be controlled using ControlFlows and to which ExceptionHandlers may be attached.
<p>From package UML::Activities.</p>"""
    handler = EReference(ordered=False, unique=True,
                         containment=True, derived=False, upper=-1)

    def __init__(self, handler=None, **kwargs):

        super(ExecutableNode, self).__init__(**kwargs)

        if handler:
            self.handler.extend(handler)


@abstract
class ControlNode(_user_module.ControlNodeMixin, ActivityNode):
    """A ControlNode is an abstract ActivityNode that coordinates flows in an Activity.
<p>From package UML::Activities.</p>"""

    def __init__(self, **kwargs):

        super(ControlNode, self).__init__(**kwargs)


@abstract
class MessageEvent(_user_module.MessageEventMixin, Event):
    """A MessageEvent specifies the receipt by an object of either an Operation call or a Signal instance.
<p>From package UML::CommonBehavior.</p>"""

    def __init__(self, **kwargs):

        super(MessageEvent, self).__init__(**kwargs)


class ChangeEvent(_user_module.ChangeEventMixin, Event):
    """A ChangeEvent models a change in the system configuration that makes a condition true.
<p>From package UML::CommonBehavior.</p>"""
    changeExpression = EReference(
        ordered=False, unique=True, containment=True, derived=False)

    def __init__(self, changeExpression=None, **kwargs):

        super(ChangeEvent, self).__init__(**kwargs)

        if changeExpression is not None:
            self.changeExpression = changeExpression


class TimeEvent(_user_module.TimeEventMixin, Event):
    """A TimeEvent is an Event that occurs at a specific point in time.
<p>From package UML::CommonBehavior.</p>"""
    isRelative = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=False)
    when = EReference(ordered=False, unique=True,
                      containment=True, derived=False)

    def __init__(self, isRelative=None, when=None, **kwargs):

        super(TimeEvent, self).__init__(**kwargs)

        if isRelative is not None:
            self.isRelative = isRelative

        if when is not None:
            self.when = when


class InteractionConstraint(
        _user_module.InteractionConstraintMixin, Constraint):
    """An InteractionConstraint is a Boolean expression that guards an operand in a CombinedFragment.
<p>From package UML::Interactions.</p>"""
    maxint = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    minint = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, maxint=None, minint=None, **kwargs):

        super(InteractionConstraint, self).__init__(**kwargs)

        if maxint is not None:
            self.maxint = maxint

        if minint is not None:
            self.minint = minint


class MessageOccurrenceSpecification(
        _user_module.MessageOccurrenceSpecificationMixin, OccurrenceSpecification,
        MessageEnd):
    """A MessageOccurrenceSpecification specifies the occurrence of Message events, such as sending and receiving of Signals or invoking or receiving of Operation calls. A MessageOccurrenceSpecification is a kind of MessageEnd. Messages are generated either by synchronous Operation calls or asynchronous Signal sends. They are received by the execution of corresponding AcceptEventActions.
<p>From package UML::Interactions.</p>"""

    def __init__(self, **kwargs):

        super(MessageOccurrenceSpecification, self).__init__(**kwargs)


class ProtocolTransition(_user_module.ProtocolTransitionMixin, Transition):
    """A ProtocolTransition specifies a legal Transition for an Operation. Transitions of ProtocolStateMachines have the following information: a pre-condition (guard), a Trigger, and a post-condition. Every ProtocolTransition is associated with at most one BehavioralFeature belonging to the context Classifier of the ProtocolStateMachine.
<p>From package UML::StateMachines.</p>"""
    postCondition = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    preCondition = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    referred = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedReferred)

    def __init__(
            self, postCondition=None, preCondition=None, referred=None, **
            kwargs):

        super(ProtocolTransition, self).__init__(**kwargs)

        if postCondition is not None:
            self.postCondition = postCondition

        if preCondition is not None:
            self.preCondition = preCondition

        if referred:
            self.referred.extend(referred)


class IntervalConstraint(_user_module.IntervalConstraintMixin, Constraint):
    """An IntervalConstraint is a Constraint that is specified by an Interval.
<p>From package UML::Values.</p>"""

    def __init__(self, **kwargs):

        super(IntervalConstraint, self).__init__(**kwargs)


class DurationObservation(_user_module.DurationObservationMixin, Observation):
    """A DurationObservation is a reference to a duration during an execution. It points out the NamedElement(s) in the model to observe and whether the observations are when this NamedElement is entered or when it is exited.
<p>From package UML::Values.</p>"""
    firstEvent = EAttribute(eType=Boolean, derived=False,
                            changeable=True, upper=-1)
    event = EReference(ordered=True, unique=True,
                       containment=False, derived=False)

    def __init__(self, event=None, firstEvent=None, **kwargs):

        super(DurationObservation, self).__init__(**kwargs)

        if firstEvent:
            self.firstEvent.extend(firstEvent)

        if event:
            self.event.extend(event)


class TimeObservation(_user_module.TimeObservationMixin, Observation):
    """A TimeObservation is a reference to a time instant during an execution. It points out the NamedElement in the model to observe and whether the observation is when this NamedElement is entered or when it is exited.
<p>From package UML::Values.</p>"""
    firstEvent = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=True)
    event = EReference(ordered=False, unique=True,
                       containment=False, derived=False)

    def __init__(self, event=None, firstEvent=None, **kwargs):

        super(TimeObservation, self).__init__(**kwargs)

        if firstEvent is not None:
            self.firstEvent = firstEvent

        if event is not None:
            self.event = event


class Package(
        _user_module.PackageMixin, Namespace, PackageableElement,
        TemplateableElement):
    """A package can have one or more profile applications to indicate which profiles have been applied. Because a profile is a package, it is possible to apply a profile not only to packages, but also to profiles.
Package specializes TemplateableElement and PackageableElement specializes ParameterableElement to specify that a package can be used as a template and a PackageableElement as a template parameter.
A package is used to group elements, and provides a namespace for the grouped elements.
<p>From package UML::Packages.</p>"""
    URI = EAttribute(eType=String, derived=False, changeable=True)
    nestedPackage = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedNestedpackage)
    _nestingPackage = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='nestingPackage', transient=True)
    ownedStereotype = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedOwnedstereotype)
    ownedType = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedOwnedtype)
    packageMerge = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    packagedElement = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    profileApplication = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)

    def __init__(
            self, URI=None, nestedPackage=None, nestingPackage=None,
            ownedStereotype=None, ownedType=None, packageMerge=None,
            packagedElement=None, profileApplication=None, **kwargs):

        super(Package, self).__init__(**kwargs)

        if URI is not None:
            self.URI = URI

        if nestedPackage:
            self.nestedPackage.extend(nestedPackage)

        if nestingPackage is not None:
            self.nestingPackage = nestingPackage

        if ownedStereotype:
            self.ownedStereotype.extend(ownedStereotype)

        if ownedType:
            self.ownedType.extend(ownedType)

        if packageMerge:
            self.packageMerge.extend(packageMerge)

        if packagedElement:
            self.packagedElement.extend(packagedElement)

        if profileApplication:
            self.profileApplication.extend(profileApplication)


class Dependency(_user_module.DependencyMixin, PackageableElement,
                 DirectedRelationship):
    """A Dependency is a Relationship that signifies that a single model Element or a set of model Elements requires other model Elements for their specification or implementation. This means that the complete semantics of the client Element(s) are either semantically or structurally dependent on the definition of the supplier Element(s).
<p>From package UML::CommonStructure.</p>"""
    client = EReference(ordered=False, unique=True,
                        containment=False, derived=False, upper=-1)
    supplier = EReference(ordered=False, unique=True,
                          containment=False, derived=False, upper=-1)

    def __init__(self, client=None, supplier=None, **kwargs):

        super(Dependency, self).__init__(**kwargs)

        if client:
            self.client.extend(client)

        if supplier:
            self.supplier.extend(supplier)


class OpaqueExpression(_user_module.OpaqueExpressionMixin, ValueSpecification):
    """An OpaqueExpression is a ValueSpecification that specifies the computation of a collection of values either in terms of a UML Behavior or based on a textual statement in a language other than UML
<p>From package UML::Values.</p>"""
    body = EAttribute(eType=String, derived=False, changeable=True, upper=-1)
    language = EAttribute(eType=String, derived=False,
                          changeable=True, upper=-1)
    behavior = EReference(ordered=False, unique=True,
                          containment=False, derived=False)
    _result = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='result', transient=True)

    def __init__(
            self, behavior=None, body=None, language=None, result=None, **
            kwargs):

        super(OpaqueExpression, self).__init__(**kwargs)

        if body:
            self.body.extend(body)

        if language:
            self.language.extend(language)

        if behavior is not None:
            self.behavior = behavior

        if result is not None:
            self.result = result


class Parameter(_user_module.ParameterMixin, ConnectableElement,
                MultiplicityElement):
    """A Parameter is a specification of an argument used to pass information into or out of an invocation of a BehavioralFeature.  Parameters can be treated as ConnectableElements within Collaborations.
<p>From package UML::Classification.</p>"""
    _default = EAttribute(eType=String, derived=True,
                          changeable=True, name='default', transient=True)
    direction = EAttribute(
        eType=ParameterDirectionKind, derived=False, changeable=True,
        default_value=ParameterDirectionKind.in_)
    effect = EAttribute(eType=ParameterEffectKind,
                        derived=False, changeable=True)
    isException = EAttribute(eType=Boolean, derived=False,
                             changeable=True, default_value=False)
    isStream = EAttribute(eType=Boolean, derived=False,
                          changeable=True, default_value=False)
    defaultValue = EReference(
        ordered=False, unique=True, containment=True, derived=False)
    operation = EReference(ordered=False, unique=True,
                           containment=False, derived=False, transient=True)
    parameterSet = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(
            self, default=None, defaultValue=None, direction=None,
            effect=None, isException=None, isStream=None, operation=None,
            parameterSet=None, **kwargs):

        super(Parameter, self).__init__(**kwargs)

        if default is not None:
            self.default = default

        if direction is not None:
            self.direction = direction

        if effect is not None:
            self.effect = effect

        if isException is not None:
            self.isException = isException

        if isStream is not None:
            self.isStream = isStream

        if defaultValue is not None:
            self.defaultValue = defaultValue

        if operation is not None:
            self.operation = operation

        if parameterSet:
            self.parameterSet.extend(parameterSet)


class Reception(_user_module.ReceptionMixin, BehavioralFeature):
    """A Reception is a declaration stating that a Classifier is prepared to react to the receipt of a Signal.
<p>From package UML::SimpleClassifiers.</p>"""
    signal = EReference(ordered=False, unique=True,
                        containment=False, derived=False)

    def __init__(self, signal=None, **kwargs):

        super(Reception, self).__init__(**kwargs)

        if signal is not None:
            self.signal = signal


@abstract
class StructuralFeature(
        _user_module.StructuralFeatureMixin, Feature, TypedElement,
        MultiplicityElement):
    """A StructuralFeature is a typed feature of a Classifier that specifies the structure of instances of the Classifier.
<p>From package UML::Classification.</p>"""
    isReadOnly = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=False)

    def __init__(self, isReadOnly=None, **kwargs):

        super(StructuralFeature, self).__init__(**kwargs)

        if isReadOnly is not None:
            self.isReadOnly = isReadOnly


class InstanceSpecification(
        _user_module.InstanceSpecificationMixin, DeploymentTarget,
        PackageableElement, DeployedArtifact):
    """An InstanceSpecification is a model element that represents an instance in a modeled system. An InstanceSpecification can act as a DeploymentTarget in a Deployment relationship, in the case that it represents an instance of a Node. It can also act as a DeployedArtifact, if it represents an instance of an Artifact.
<p>From package UML::Classification.</p>"""
    classifier = EReference(ordered=False, unique=True,
                            containment=False, derived=False, upper=-1)
    slot = EReference(ordered=False, unique=True,
                      containment=True, derived=False, upper=-1)
    specification = EReference(
        ordered=False, unique=True, containment=True, derived=False)

    def __init__(
            self, classifier=None, slot=None, specification=None, **kwargs):

        super(InstanceSpecification, self).__init__(**kwargs)

        if classifier:
            self.classifier.extend(classifier)

        if slot:
            self.slot.extend(slot)

        if specification is not None:
            self.specification = specification


class Expression(_user_module.ExpressionMixin, ValueSpecification):
    """An Expression represents a node in an expression tree, which may be non-terminal or terminal. It defines a symbol, and has a possibly empty sequence of operands that are ValueSpecifications. It denotes a (possibly empty) set of values when evaluated in a context.
<p>From package UML::Values.</p>"""
    symbol = EAttribute(eType=String, derived=False, changeable=True)
    operand = EReference(ordered=True, unique=True,
                         containment=True, derived=False, upper=-1)

    def __init__(self, operand=None, symbol=None, **kwargs):

        super(Expression, self).__init__(**kwargs)

        if symbol is not None:
            self.symbol = symbol

        if operand:
            self.operand.extend(operand)


@abstract
class Action(_user_module.ActionMixin, ExecutableNode):
    """An Action is the fundamental unit of executable functionality. The execution of an Action represents some transformation or processing in the modeled system. Actions provide the ExecutableNodes within Activities and may also be used within Interactions.
<p>From package UML::Actions.</p>"""
    isLocallyReentrant = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    _context = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='context', transient=True)
    input = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedInput)
    localPostcondition = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    localPrecondition = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    output = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedOutput)

    def __init__(
            self, context=None, input=None, isLocallyReentrant=None,
            localPostcondition=None, localPrecondition=None, output=None, **
            kwargs):

        super(Action, self).__init__(**kwargs)

        if isLocallyReentrant is not None:
            self.isLocallyReentrant = isLocallyReentrant

        if context is not None:
            self.context = context

        if input:
            self.input.extend(input)

        if localPostcondition:
            self.localPostcondition.extend(localPostcondition)

        if localPrecondition:
            self.localPrecondition.extend(localPrecondition)

        if output:
            self.output.extend(output)


@abstract
class ObjectNode(_user_module.ObjectNodeMixin, ActivityNode, TypedElement):
    """An ObjectNode is an abstract ActivityNode that may hold tokens within the object flow in an Activity. ObjectNodes also support token selection, limitation on the number of tokens held, specification of the state required for tokens being held, and carrying control values.
<p>From package UML::Activities.</p>"""
    isControlType = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    ordering = EAttribute(
        eType=ObjectNodeOrderingKind, derived=False, changeable=True,
        default_value=ObjectNodeOrderingKind.FIFO)
    inState = EReference(ordered=False, unique=True,
                         containment=False, derived=False, upper=-1)
    selection = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    upperBound = EReference(ordered=False, unique=True,
                            containment=True, derived=False)

    def __init__(
            self, inState=None, isControlType=None, ordering=None,
            selection=None, upperBound=None, **kwargs):

        super(ObjectNode, self).__init__(**kwargs)

        if isControlType is not None:
            self.isControlType = isControlType

        if ordering is not None:
            self.ordering = ordering

        if inState:
            self.inState.extend(inState)

        if selection is not None:
            self.selection = selection

        if upperBound is not None:
            self.upperBound = upperBound


class Variable(_user_module.VariableMixin, ConnectableElement,
               MultiplicityElement):
    """A Variable is a ConnectableElement that may store values during the execution of an Activity. Reading and writing the values of a Variable provides an alternative means for passing data than the use of ObjectFlows. A Variable may be owned directly by an Activity, in which case it is accessible from anywhere within that activity, or it may be owned by a StructuredActivityNode, in which case it is only accessible within that node.
<p>From package UML::Activities.</p>"""
    activityScope = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    scope = EReference(ordered=False, unique=True,
                       containment=False, derived=False)

    def __init__(self, activityScope=None, scope=None, **kwargs):

        super(Variable, self).__init__(**kwargs)

        if activityScope is not None:
            self.activityScope = activityScope

        if scope is not None:
            self.scope = scope


@abstract
class FinalNode(_user_module.FinalNodeMixin, ControlNode):
    """A FinalNode is an abstract ControlNode at which a flow in an Activity stops.
<p>From package UML::Activities.</p>"""

    def __init__(self, **kwargs):

        super(FinalNode, self).__init__(**kwargs)


class DecisionNode(_user_module.DecisionNodeMixin, ControlNode):
    """A DecisionNode is a ControlNode that chooses between outgoing ActivityEdges for the routing of tokens.
<p>From package UML::Activities.</p>"""
    decisionInput = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    decisionInputFlow = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, decisionInput=None, decisionInputFlow=None, **kwargs):

        super(DecisionNode, self).__init__(**kwargs)

        if decisionInput is not None:
            self.decisionInput = decisionInput

        if decisionInputFlow is not None:
            self.decisionInputFlow = decisionInputFlow


class ForkNode(_user_module.ForkNodeMixin, ControlNode):
    """A ForkNode is a ControlNode that splits a flow into multiple concurrent flows.
<p>From package UML::Activities.</p>"""

    def __init__(self, **kwargs):

        super(ForkNode, self).__init__(**kwargs)


class InitialNode(_user_module.InitialNodeMixin, ControlNode):
    """An InitialNode is a ControlNode that offers a single control token when initially enabled.
<p>From package UML::Activities.</p>"""

    def __init__(self, **kwargs):

        super(InitialNode, self).__init__(**kwargs)


class JoinNode(_user_module.JoinNodeMixin, ControlNode):
    """A JoinNode is a ControlNode that synchronizes multiple flows.
<p>From package UML::Activities.</p>"""
    isCombineDuplicate = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=True)
    joinSpec = EReference(ordered=False, unique=True,
                          containment=True, derived=False)

    def __init__(self, isCombineDuplicate=None, joinSpec=None, **kwargs):

        super(JoinNode, self).__init__(**kwargs)

        if isCombineDuplicate is not None:
            self.isCombineDuplicate = isCombineDuplicate

        if joinSpec is not None:
            self.joinSpec = joinSpec


class MergeNode(_user_module.MergeNodeMixin, ControlNode):
    """A merge node is a control node that brings together multiple alternate flows. It is not used to synchronize concurrent flows but to accept one among several alternate flows.
<p>From package UML::Activities.</p>"""

    def __init__(self, **kwargs):

        super(MergeNode, self).__init__(**kwargs)


class InstanceValue(_user_module.InstanceValueMixin, ValueSpecification):
    """An InstanceValue is a ValueSpecification that identifies an instance.
<p>From package UML::Classification.</p>"""
    instance = EReference(ordered=False, unique=True,
                          containment=False, derived=False)

    def __init__(self, instance=None, **kwargs):

        super(InstanceValue, self).__init__(**kwargs)

        if instance is not None:
            self.instance = instance


class AnyReceiveEvent(_user_module.AnyReceiveEventMixin, MessageEvent):
    """A trigger for an AnyReceiveEvent is triggered by the receipt of any message that is not explicitly handled by any related trigger.
<p>From package UML::CommonBehavior.</p>"""

    def __init__(self, **kwargs):

        super(AnyReceiveEvent, self).__init__(**kwargs)


class CallEvent(_user_module.CallEventMixin, MessageEvent):
    """A CallEvent models the receipt by an object of a message invoking a call of an Operation.
<p>From package UML::CommonBehavior.</p>"""
    operation = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(self, operation=None, **kwargs):

        super(CallEvent, self).__init__(**kwargs)

        if operation is not None:
            self.operation = operation


class SignalEvent(_user_module.SignalEventMixin, MessageEvent):
    """A SignalEvent represents the receipt of an asynchronous Signal instance.
<p>From package UML::CommonBehavior.</p>"""
    signal = EReference(ordered=False, unique=True,
                        containment=False, derived=False)

    def __init__(self, signal=None, **kwargs):

        super(SignalEvent, self).__init__(**kwargs)

        if signal is not None:
            self.signal = signal


class TimeExpression(_user_module.TimeExpressionMixin, ValueSpecification):
    """A TimeExpression is a ValueSpecification that represents a time value.
<p>From package UML::Values.</p>"""
    expr = EReference(ordered=False, unique=True,
                      containment=True, derived=False)
    observation = EReference(ordered=False, unique=True,
                             containment=False, derived=False, upper=-1)

    def __init__(self, expr=None, observation=None, **kwargs):

        super(TimeExpression, self).__init__(**kwargs)

        if expr is not None:
            self.expr = expr

        if observation:
            self.observation.extend(observation)


class InformationFlow(
        _user_module.InformationFlowMixin, PackageableElement,
        DirectedRelationship):
    """InformationFlows describe circulation of information through a system in a general manner. They do not specify the nature of the information, mechanisms by which it is conveyed, sequences of exchange or any control conditions. During more detailed modeling, representation and realization links may be added to specify which model elements implement an InformationFlow and to show how information is conveyed.  InformationFlows require some kind of “information channel” for unidirectional transmission of information items from sources to targets.  They specify the information channel’s realizations, if any, and identify the information that flows along them.  Information moving along the information channel may be represented by abstract InformationItems and by concrete Classifiers.
<p>From package UML::InformationFlows.</p>"""
    conveyed = EReference(ordered=False, unique=True,
                          containment=False, derived=False, upper=-1)
    informationSource = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    informationTarget = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    realization = EReference(ordered=False, unique=True,
                             containment=False, derived=False, upper=-1)
    realizingActivityEdge = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    realizingConnector = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    realizingMessage = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(
            self, conveyed=None, informationSource=None,
            informationTarget=None, realization=None,
            realizingActivityEdge=None, realizingConnector=None,
            realizingMessage=None, **kwargs):

        super(InformationFlow, self).__init__(**kwargs)

        if conveyed:
            self.conveyed.extend(conveyed)

        if informationSource:
            self.informationSource.extend(informationSource)

        if informationTarget:
            self.informationTarget.extend(informationTarget)

        if realization:
            self.realization.extend(realization)

        if realizingActivityEdge:
            self.realizingActivityEdge.extend(realizingActivityEdge)

        if realizingConnector:
            self.realizingConnector.extend(realizingConnector)

        if realizingMessage:
            self.realizingMessage.extend(realizingMessage)


class DestructionOccurrenceSpecification(
        _user_module.DestructionOccurrenceSpecificationMixin,
        MessageOccurrenceSpecification):
    """A DestructionOccurenceSpecification models the destruction of an object.
<p>From package UML::Interactions.</p>"""

    def __init__(self, **kwargs):

        super(DestructionOccurrenceSpecification, self).__init__(**kwargs)


class FinalState(_user_module.FinalStateMixin, State):
    """A special kind of State, which, when entered, signifies that the enclosing Region has completed. If the enclosing Region is directly contained in a StateMachine and all other Regions in that StateMachine also are completed, then it means that the entire StateMachine behavior is completed.
<p>From package UML::StateMachines.</p>"""

    def __init__(self, **kwargs):

        super(FinalState, self).__init__(**kwargs)


class Duration(_user_module.DurationMixin, ValueSpecification):
    """A Duration is a ValueSpecification that specifies the temporal distance between two time instants.
<p>From package UML::Values.</p>"""
    expr = EReference(ordered=False, unique=True,
                      containment=True, derived=False)
    observation = EReference(ordered=False, unique=True,
                             containment=False, derived=False, upper=-1)

    def __init__(self, expr=None, observation=None, **kwargs):

        super(Duration, self).__init__(**kwargs)

        if expr is not None:
            self.expr = expr

        if observation:
            self.observation.extend(observation)


class DurationConstraint(
        _user_module.DurationConstraintMixin, IntervalConstraint):
    """A DurationConstraint is a Constraint that refers to a DurationInterval.
<p>From package UML::Values.</p>"""
    firstEvent = EAttribute(eType=Boolean, derived=False,
                            changeable=True, upper=-1)

    def __init__(self, firstEvent=None, **kwargs):

        super(DurationConstraint, self).__init__(**kwargs)

        if firstEvent:
            self.firstEvent.extend(firstEvent)


class Interval(_user_module.IntervalMixin, ValueSpecification):
    """An Interval defines the range between two ValueSpecifications.
<p>From package UML::Values.</p>"""
    max = EReference(ordered=False, unique=True,
                     containment=False, derived=False)
    min = EReference(ordered=False, unique=True,
                     containment=False, derived=False)

    def __init__(self, max=None, min=None, **kwargs):

        super(Interval, self).__init__(**kwargs)

        if max is not None:
            self.max = max

        if min is not None:
            self.min = min


@abstract
class LiteralSpecification(
        _user_module.LiteralSpecificationMixin, ValueSpecification):
    """A LiteralSpecification identifies a literal constant being modeled.
<p>From package UML::Values.</p>"""

    def __init__(self, **kwargs):

        super(LiteralSpecification, self).__init__(**kwargs)


class TimeConstraint(_user_module.TimeConstraintMixin, IntervalConstraint):
    """A TimeConstraint is a Constraint that refers to a TimeInterval.
<p>From package UML::Values.</p>"""
    firstEvent = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=True)

    def __init__(self, firstEvent=None, **kwargs):

        super(TimeConstraint, self).__init__(**kwargs)

        if firstEvent is not None:
            self.firstEvent = firstEvent


class Profile(_user_module.ProfileMixin, Package):
    """A profile defines limited extensions to a reference metamodel with the purpose of adapting the metamodel to a specific platform or domain.
<p>From package UML::Packages.</p>"""
    metaclassReference = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    metamodelReference = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(
            self, metaclassReference=None, metamodelReference=None, **
            kwargs):

        super(Profile, self).__init__(**kwargs)

        if metaclassReference:
            self.metaclassReference.extend(metaclassReference)

        if metamodelReference:
            self.metamodelReference.extend(metamodelReference)


class Deployment(_user_module.DeploymentMixin, Dependency):
    """A deployment is the allocation of an artifact or artifact instance to a deployment target.
A component deployment is the deployment of one or more artifacts or artifact instances to a deployment target, optionally parameterized by a deployment specification. Examples are executables and configuration files.
<p>From package UML::Deployments.</p>"""
    configuration = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    deployedArtifact = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    location = EReference(ordered=False, unique=True,
                          containment=False, derived=False)

    def __init__(
            self, configuration=None, deployedArtifact=None, location=None,
            **kwargs):

        super(Deployment, self).__init__(**kwargs)

        if configuration:
            self.configuration.extend(configuration)

        if deployedArtifact:
            self.deployedArtifact.extend(deployedArtifact)

        if location is not None:
            self.location = location


class Abstraction(_user_module.AbstractionMixin, Dependency):
    """An Abstraction is a Relationship that relates two Elements or sets of Elements that represent the same concept at different levels of abstraction or from different viewpoints.
<p>From package UML::CommonStructure.</p>"""
    mapping = EReference(ordered=False, unique=True,
                         containment=True, derived=False)

    def __init__(self, mapping=None, **kwargs):

        super(Abstraction, self).__init__(**kwargs)

        if mapping is not None:
            self.mapping = mapping


class EnumerationLiteral(
        _user_module.EnumerationLiteralMixin, InstanceSpecification):
    """An EnumerationLiteral is a user-defined data value for an Enumeration.
<p>From package UML::SimpleClassifiers.</p>"""
    enumeration = EReference(ordered=False, unique=True,
                             containment=False, derived=False)

    def __init__(self, enumeration=None, **kwargs):

        super(EnumerationLiteral, self).__init__(**kwargs)

        if enumeration is not None:
            self.enumeration = enumeration


class Model(_user_module.ModelMixin, Package):
    """A model captures a view of a physical system. It is an abstraction of the physical system, with a certain purpose. This purpose determines what is to be included in the model and what is irrelevant. Thus the model completely describes those aspects of the physical system that are relevant to the purpose of the model, at the appropriate level of detail.
<p>From package UML::Packages.</p>"""
    viewpoint = EAttribute(eType=String, derived=False, changeable=True)

    def __init__(self, viewpoint=None, **kwargs):

        super(Model, self).__init__(**kwargs)

        if viewpoint is not None:
            self.viewpoint = viewpoint


class Usage(_user_module.UsageMixin, Dependency):
    """A Usage is a Dependency in which the client Element requires the supplier Element (or set of Elements) for its full implementation or operation.
<p>From package UML::CommonStructure.</p>"""

    def __init__(self, **kwargs):

        super(Usage, self).__init__(**kwargs)


class ValueSpecificationAction(
        _user_module.ValueSpecificationActionMixin, Action):
    """A ValueSpecificationAction is an Action that evaluates a ValueSpecification and provides a result.
<p>From package UML::Actions.</p>"""
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    value = EReference(ordered=False, unique=True,
                       containment=True, derived=False)

    def __init__(self, result=None, value=None, **kwargs):

        super(ValueSpecificationAction, self).__init__(**kwargs)

        if result is not None:
            self.result = result

        if value is not None:
            self.value = value


@abstract
class VariableAction(_user_module.VariableActionMixin, Action):
    """VariableAction is an abstract class for Actions that operate on a specified Variable.
<p>From package UML::Actions.</p>"""
    variable = EReference(ordered=False, unique=True,
                          containment=False, derived=False)

    def __init__(self, variable=None, **kwargs):

        super(VariableAction, self).__init__(**kwargs)

        if variable is not None:
            self.variable = variable


@abstract
class LinkAction(_user_module.LinkActionMixin, Action):
    """LinkAction is an abstract class for all Actions that identify the links to be acted on using LinkEndData.
<p>From package UML::Actions.</p>"""
    endData = EReference(ordered=False, unique=True,
                         containment=True, derived=False, upper=-1)
    inputValue = EReference(ordered=False, unique=True,
                            containment=True, derived=False, upper=-1)

    def __init__(self, endData=None, inputValue=None, **kwargs):

        super(LinkAction, self).__init__(**kwargs)

        if endData:
            self.endData.extend(endData)

        if inputValue:
            self.inputValue.extend(inputValue)


@abstract
class StructuralFeatureAction(
        _user_module.StructuralFeatureActionMixin, Action):
    """StructuralFeatureAction is an abstract class for all Actions that operate on StructuralFeatures.
<p>From package UML::Actions.</p>"""
    object = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    structuralFeature = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, object=None, structuralFeature=None, **kwargs):

        super(StructuralFeatureAction, self).__init__(**kwargs)

        if object is not None:
            self.object = object

        if structuralFeature is not None:
            self.structuralFeature = structuralFeature


class AcceptEventAction(_user_module.AcceptEventActionMixin, Action):
    """An AcceptEventAction is an Action that waits for the occurrence of one or more specific Events.
<p>From package UML::Actions.</p>"""
    isUnmarshall = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    result = EReference(ordered=True, unique=True,
                        containment=True, derived=False, upper=-1)
    trigger = EReference(ordered=False, unique=True,
                         containment=True, derived=False, upper=-1)

    def __init__(
            self, isUnmarshall=None, result=None, trigger=None, **kwargs):

        super(AcceptEventAction, self).__init__(**kwargs)

        if isUnmarshall is not None:
            self.isUnmarshall = isUnmarshall

        if result:
            self.result.extend(result)

        if trigger:
            self.trigger.extend(trigger)


@abstract
class InvocationAction(_user_module.InvocationActionMixin, Action):
    """InvocationAction is an abstract class for the various actions that request Behavior invocation.
<p>From package UML::Actions.</p>"""
    argument = EReference(ordered=True, unique=True,
                          containment=True, derived=False, upper=-1)
    onPort = EReference(ordered=False, unique=True,
                        containment=False, derived=False)

    def __init__(self, argument=None, onPort=None, **kwargs):

        super(InvocationAction, self).__init__(**kwargs)

        if argument:
            self.argument.extend(argument)

        if onPort is not None:
            self.onPort = onPort


class ClearAssociationAction(_user_module.ClearAssociationActionMixin, Action):
    """A ClearAssociationAction is an Action that destroys all links of an Association in which a particular object participates.
<p>From package UML::Actions.</p>"""
    association = EReference(ordered=False, unique=True,
                             containment=False, derived=False)
    object = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, association=None, object=None, **kwargs):

        super(ClearAssociationAction, self).__init__(**kwargs)

        if association is not None:
            self.association = association

        if object is not None:
            self.object = object


class CreateObjectAction(_user_module.CreateObjectActionMixin, Action):
    """A CreateObjectAction is an Action that creates an instance of the specified Classifier.
<p>From package UML::Actions.</p>"""
    classifier = EReference(ordered=False, unique=True,
                            containment=False, derived=False)
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, classifier=None, result=None, **kwargs):

        super(CreateObjectAction, self).__init__(**kwargs)

        if classifier is not None:
            self.classifier = classifier

        if result is not None:
            self.result = result


class DestroyObjectAction(_user_module.DestroyObjectActionMixin, Action):
    """A DestroyObjectAction is an Action that destroys objects.
<p>From package UML::Actions.</p>"""
    isDestroyLinks = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    isDestroyOwnedObjects = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    target = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(
            self, isDestroyLinks=None, isDestroyOwnedObjects=None,
            target=None, **kwargs):

        super(DestroyObjectAction, self).__init__(**kwargs)

        if isDestroyLinks is not None:
            self.isDestroyLinks = isDestroyLinks

        if isDestroyOwnedObjects is not None:
            self.isDestroyOwnedObjects = isDestroyOwnedObjects

        if target is not None:
            self.target = target


class ExpansionNode(_user_module.ExpansionNodeMixin, ObjectNode):
    """An ExpansionNode is an ObjectNode used to indicate a collection input or output for an ExpansionRegion. A collection input of an ExpansionRegion contains a collection that is broken into its individual elements inside the region, whose content is executed once per element. A collection output of an ExpansionRegion combines individual elements produced by the execution of the region into a collection for use outside the region.
<p>From package UML::Actions.</p>"""
    regionAsInput = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    regionAsOutput = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, regionAsInput=None, regionAsOutput=None, **kwargs):

        super(ExpansionNode, self).__init__(**kwargs)

        if regionAsInput is not None:
            self.regionAsInput = regionAsInput

        if regionAsOutput is not None:
            self.regionAsOutput = regionAsOutput


class OpaqueAction(_user_module.OpaqueActionMixin, Action):
    """An OpaqueAction is an Action whose functionality is not specified within UML.
<p>From package UML::Actions.</p>"""
    body = EAttribute(eType=String, derived=False, changeable=True, upper=-1)
    language = EAttribute(eType=String, derived=False,
                          changeable=True, upper=-1)
    inputValue = EReference(ordered=False, unique=True,
                            containment=True, derived=False, upper=-1)
    outputValue = EReference(ordered=False, unique=True,
                             containment=True, derived=False, upper=-1)

    def __init__(
            self, body=None, inputValue=None, language=None,
            outputValue=None, **kwargs):

        super(OpaqueAction, self).__init__(**kwargs)

        if body:
            self.body.extend(body)

        if language:
            self.language.extend(language)

        if inputValue:
            self.inputValue.extend(inputValue)

        if outputValue:
            self.outputValue.extend(outputValue)


class RaiseExceptionAction(_user_module.RaiseExceptionActionMixin, Action):
    """A RaiseExceptionAction is an Action that causes an exception to occur. The input value becomes the exception object.
<p>From package UML::Actions.</p>"""
    exception = EReference(ordered=False, unique=True,
                           containment=True, derived=False)

    def __init__(self, exception=None, **kwargs):

        super(RaiseExceptionAction, self).__init__(**kwargs)

        if exception is not None:
            self.exception = exception


class ReadExtentAction(_user_module.ReadExtentActionMixin, Action):
    """A ReadExtentAction is an Action that retrieves the current instances of a Classifier.
<p>From package UML::Actions.</p>"""
    classifier = EReference(ordered=False, unique=True,
                            containment=False, derived=False)
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, classifier=None, result=None, **kwargs):

        super(ReadExtentAction, self).__init__(**kwargs)

        if classifier is not None:
            self.classifier = classifier

        if result is not None:
            self.result = result


class ReadIsClassifiedObjectAction(
        _user_module.ReadIsClassifiedObjectActionMixin, Action):
    """A ReadIsClassifiedObjectAction is an Action that determines whether an object is classified by a given Classifier.
<p>From package UML::Actions.</p>"""
    isDirect = EAttribute(eType=Boolean, derived=False,
                          changeable=True, default_value=False)
    classifier = EReference(ordered=False, unique=True,
                            containment=False, derived=False)
    object = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(
            self, classifier=None, isDirect=None, object=None, result=None,
            **kwargs):

        super(ReadIsClassifiedObjectAction, self).__init__(**kwargs)

        if isDirect is not None:
            self.isDirect = isDirect

        if classifier is not None:
            self.classifier = classifier

        if object is not None:
            self.object = object

        if result is not None:
            self.result = result


class ReadLinkObjectEndAction(
        _user_module.ReadLinkObjectEndActionMixin, Action):
    """A ReadLinkObjectEndAction is an Action that retrieves an end object from a link object.
<p>From package UML::Actions.</p>"""
    end = EReference(ordered=False, unique=True,
                     containment=False, derived=False)
    object = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, end=None, object=None, result=None, **kwargs):

        super(ReadLinkObjectEndAction, self).__init__(**kwargs)

        if end is not None:
            self.end = end

        if object is not None:
            self.object = object

        if result is not None:
            self.result = result


class ReadLinkObjectEndQualifierAction(
        _user_module.ReadLinkObjectEndQualifierActionMixin, Action):
    """A ReadLinkObjectEndQualifierAction is an Action that retrieves a qualifier end value from a link object.
<p>From package UML::Actions.</p>"""
    object = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    qualifier = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, object=None, qualifier=None, result=None, **kwargs):

        super(ReadLinkObjectEndQualifierAction, self).__init__(**kwargs)

        if object is not None:
            self.object = object

        if qualifier is not None:
            self.qualifier = qualifier

        if result is not None:
            self.result = result


class ReadSelfAction(_user_module.ReadSelfActionMixin, Action):
    """A ReadSelfAction is an Action that retrieves the context object of the Behavior execution within which the ReadSelfAction execution is taking place.
<p>From package UML::Actions.</p>"""
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, result=None, **kwargs):

        super(ReadSelfAction, self).__init__(**kwargs)

        if result is not None:
            self.result = result


class ReclassifyObjectAction(_user_module.ReclassifyObjectActionMixin, Action):
    """A ReclassifyObjectAction is an Action that changes the Classifiers that classify an object.
<p>From package UML::Actions.</p>"""
    isReplaceAll = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    newClassifier = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    object = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    oldClassifier = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(
            self, isReplaceAll=None, newClassifier=None, object=None,
            oldClassifier=None, **kwargs):

        super(ReclassifyObjectAction, self).__init__(**kwargs)

        if isReplaceAll is not None:
            self.isReplaceAll = isReplaceAll

        if newClassifier:
            self.newClassifier.extend(newClassifier)

        if object is not None:
            self.object = object

        if oldClassifier:
            self.oldClassifier.extend(oldClassifier)


class ReduceAction(_user_module.ReduceActionMixin, Action):
    """A ReduceAction is an Action that reduces a collection to a single value by repeatedly combining the elements of the collection using a reducer Behavior.
<p>From package UML::Actions.</p>"""
    isOrdered = EAttribute(eType=Boolean, derived=False,
                           changeable=True, default_value=False)
    collection = EReference(ordered=False, unique=True,
                            containment=True, derived=False)
    reducer = EReference(ordered=False, unique=True,
                         containment=False, derived=False)
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(
            self, collection=None, isOrdered=None, reducer=None,
            result=None, **kwargs):

        super(ReduceAction, self).__init__(**kwargs)

        if isOrdered is not None:
            self.isOrdered = isOrdered

        if collection is not None:
            self.collection = collection

        if reducer is not None:
            self.reducer = reducer

        if result is not None:
            self.result = result


class ReplyAction(_user_module.ReplyActionMixin, Action):
    """A ReplyAction is an Action that accepts a set of reply values and a value containing return information produced by a previous AcceptCallAction. The ReplyAction returns the values to the caller of the previous call, completing execution of the call.
<p>From package UML::Actions.</p>"""
    replyToCall = EReference(ordered=False, unique=True,
                             containment=False, derived=False)
    replyValue = EReference(ordered=True, unique=True,
                            containment=True, derived=False, upper=-1)
    returnInformation = EReference(
        ordered=False, unique=True, containment=True, derived=False)

    def __init__(self, replyToCall=None, replyValue=None,
                 returnInformation=None, **kwargs):

        super(ReplyAction, self).__init__(**kwargs)

        if replyToCall is not None:
            self.replyToCall = replyToCall

        if replyValue:
            self.replyValue.extend(replyValue)

        if returnInformation is not None:
            self.returnInformation = returnInformation


class StartClassifierBehaviorAction(
        _user_module.StartClassifierBehaviorActionMixin, Action):
    """A StartClassifierBehaviorAction is an Action that starts the classifierBehavior of the input object.
<p>From package UML::Actions.</p>"""
    object = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, object=None, **kwargs):

        super(StartClassifierBehaviorAction, self).__init__(**kwargs)

        if object is not None:
            self.object = object


class TestIdentityAction(_user_module.TestIdentityActionMixin, Action):
    """A TestIdentityAction is an Action that tests if two values are identical objects.
<p>From package UML::Actions.</p>"""
    first = EReference(ordered=False, unique=True,
                       containment=True, derived=False)
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    second = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, first=None, result=None, second=None, **kwargs):

        super(TestIdentityAction, self).__init__(**kwargs)

        if first is not None:
            self.first = first

        if result is not None:
            self.result = result

        if second is not None:
            self.second = second


class UnmarshallAction(_user_module.UnmarshallActionMixin, Action):
    """An UnmarshallAction is an Action that retrieves the values of the StructuralFeatures of an object and places them on OutputPins.
<p>From package UML::Actions.</p>"""
    object = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    result = EReference(ordered=True, unique=True,
                        containment=True, derived=False, upper=-1)
    unmarshallType = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(
            self, object=None, result=None, unmarshallType=None, **kwargs):

        super(UnmarshallAction, self).__init__(**kwargs)

        if object is not None:
            self.object = object

        if result:
            self.result.extend(result)

        if unmarshallType is not None:
            self.unmarshallType = unmarshallType


class ActivityFinalNode(_user_module.ActivityFinalNodeMixin, FinalNode):
    """An ActivityFinalNode is a FinalNode that terminates the execution of its owning Activity or StructuredActivityNode.
<p>From package UML::Activities.</p>"""

    def __init__(self, **kwargs):

        super(ActivityFinalNode, self).__init__(**kwargs)


class ActivityParameterNode(
        _user_module.ActivityParameterNodeMixin, ObjectNode):
    """An ActivityParameterNode is an ObjectNode for accepting values from the input Parameters or providing values to the output Parameters of an Activity.
<p>From package UML::Activities.</p>"""
    parameter = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(self, parameter=None, **kwargs):

        super(ActivityParameterNode, self).__init__(**kwargs)

        if parameter is not None:
            self.parameter = parameter


class CentralBufferNode(_user_module.CentralBufferNodeMixin, ObjectNode):
    """A CentralBufferNode is an ObjectNode for managing flows from multiple sources and targets.
<p>From package UML::Activities.</p>"""

    def __init__(self, **kwargs):

        super(CentralBufferNode, self).__init__(**kwargs)


class FlowFinalNode(_user_module.FlowFinalNodeMixin, FinalNode):
    """A FlowFinalNode is a FinalNode that terminates a flow by consuming the tokens offered to it.
<p>From package UML::Activities.</p>"""

    def __init__(self, **kwargs):

        super(FlowFinalNode, self).__init__(**kwargs)


class DurationInterval(_user_module.DurationIntervalMixin, Interval):
    """A DurationInterval defines the range between two Durations.
<p>From package UML::Values.</p>"""

    def __init__(self, **kwargs):

        super(DurationInterval, self).__init__(**kwargs)


class LiteralBoolean(_user_module.LiteralBooleanMixin, LiteralSpecification):
    """A LiteralBoolean is a specification of a Boolean value.
<p>From package UML::Values.</p>"""
    value = EAttribute(eType=Boolean, derived=False,
                       changeable=True, default_value=False)

    def __init__(self, value=None, **kwargs):

        super(LiteralBoolean, self).__init__(**kwargs)

        if value is not None:
            self.value = value


class LiteralInteger(_user_module.LiteralIntegerMixin, LiteralSpecification):
    """A LiteralInteger is a specification of an Integer value.
<p>From package UML::Values.</p>"""
    value = EAttribute(eType=Integer, derived=False,
                       changeable=True, default_value=0)

    def __init__(self, value=None, **kwargs):

        super(LiteralInteger, self).__init__(**kwargs)

        if value is not None:
            self.value = value


class LiteralNull(_user_module.LiteralNullMixin, LiteralSpecification):
    """A LiteralNull specifies the lack of a value.
<p>From package UML::Values.</p>"""

    def __init__(self, **kwargs):

        super(LiteralNull, self).__init__(**kwargs)


class LiteralReal(_user_module.LiteralRealMixin, LiteralSpecification):
    """A LiteralReal is a specification of a Real value.
<p>From package UML::Values.</p>"""
    value = EAttribute(eType=Real, derived=False, changeable=True)

    def __init__(self, value=None, **kwargs):

        super(LiteralReal, self).__init__(**kwargs)

        if value is not None:
            self.value = value


class LiteralString(_user_module.LiteralStringMixin, LiteralSpecification):
    """A LiteralString is a specification of a String value.
<p>From package UML::Values.</p>"""
    value = EAttribute(eType=String, derived=False, changeable=True)

    def __init__(self, value=None, **kwargs):

        super(LiteralString, self).__init__(**kwargs)

        if value is not None:
            self.value = value


class LiteralUnlimitedNatural(
        _user_module.LiteralUnlimitedNaturalMixin, LiteralSpecification):
    """A LiteralUnlimitedNatural is a specification of an UnlimitedNatural number.
<p>From package UML::Values.</p>"""
    value = EAttribute(eType=UnlimitedNatural, derived=False,
                       changeable=True, default_value=0)

    def __init__(self, value=None, **kwargs):

        super(LiteralUnlimitedNatural, self).__init__(**kwargs)

        if value is not None:
            self.value = value


class TimeInterval(_user_module.TimeIntervalMixin, Interval):
    """A TimeInterval defines the range between two TimeExpressions.
<p>From package UML::Values.</p>"""

    def __init__(self, **kwargs):

        super(TimeInterval, self).__init__(**kwargs)


@abstract
class Classifier(
        _user_module.ClassifierMixin, Namespace, RedefinableElement, Type,
        TemplateableElement):
    """A Classifier represents a classification of instances according to their Features.
<p>From package UML::Classification.</p>"""
    isAbstract = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=False)
    isFinalSpecialization = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    feature = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedFeature)
    attribute = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedAttribute)
    collaborationUse = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    general = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedGeneral)
    generalization = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    powertypeExtent = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    inheritedMember = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedInheritedmember)
    ownedUseCase = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    useCase = EReference(ordered=False, unique=True,
                         containment=False, derived=False, upper=-1)
    redefinedClassifier = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    representation = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    substitution = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)

    def __init__(
            self, feature=None, attribute=None, collaborationUse=None,
            general=None, generalization=None, powertypeExtent=None,
            inheritedMember=None, isAbstract=None, isFinalSpecialization=None,
            ownedUseCase=None, useCase=None, redefinedClassifier=None,
            representation=None, substitution=None, **kwargs):

        super(Classifier, self).__init__(**kwargs)

        if isAbstract is not None:
            self.isAbstract = isAbstract

        if isFinalSpecialization is not None:
            self.isFinalSpecialization = isFinalSpecialization

        if feature:
            self.feature.extend(feature)

        if attribute:
            self.attribute.extend(attribute)

        if collaborationUse:
            self.collaborationUse.extend(collaborationUse)

        if general:
            self.general.extend(general)

        if generalization:
            self.generalization.extend(generalization)

        if powertypeExtent:
            self.powertypeExtent.extend(powertypeExtent)

        if inheritedMember:
            self.inheritedMember.extend(inheritedMember)

        if ownedUseCase:
            self.ownedUseCase.extend(ownedUseCase)

        if useCase:
            self.useCase.extend(useCase)

        if redefinedClassifier:
            self.redefinedClassifier.extend(redefinedClassifier)

        if representation is not None:
            self.representation = representation

        if substitution:
            self.substitution.extend(substitution)


class Manifestation(_user_module.ManifestationMixin, Abstraction):
    """A manifestation is the concrete physical rendering of one or more model elements by an artifact.
<p>From package UML::Deployments.</p>"""
    utilizedElement = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, utilizedElement=None, **kwargs):

        super(Manifestation, self).__init__(**kwargs)

        if utilizedElement is not None:
            self.utilizedElement = utilizedElement


class Operation(_user_module.OperationMixin, BehavioralFeature,
                ParameterableElement, TemplateableElement):
    """An Operation is a BehavioralFeature of a Classifier that specifies the name, type, parameters, and constraints for invoking an associated Behavior. An Operation may invoke both the execution of method behaviors as well as other behavioral responses. Operation specializes TemplateableElement in order to support specification of template operations and bound operations. Operation specializes ParameterableElement to specify that an operation can be exposed as a formal template parameter, and provided as an actual parameter in a binding of a template.
<p>From package UML::Classification.</p>"""
    _isOrdered = EAttribute(
        eType=Boolean, derived=True, changeable=False, name='isOrdered',
        transient=True)
    isQuery = EAttribute(eType=Boolean, derived=False,
                         changeable=True, default_value=False)
    _isUnique = EAttribute(
        eType=Boolean, derived=True, changeable=False, name='isUnique',
        default_value=True, transient=True)
    _lower = EAttribute(
        eType=Integer, derived=True, changeable=False, name='lower',
        default_value=1, transient=True)
    _upper = EAttribute(
        eType=UnlimitedNatural, derived=True, changeable=False, name='upper',
        default_value=1, transient=True)
    bodyCondition = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    class_ = EReference(ordered=False, unique=True,
                        containment=False, derived=False)
    datatype = EReference(ordered=False, unique=True,
                          containment=False, derived=False)
    interface = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    postcondition = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    precondition = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    redefinedOperation = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    _type = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='type', transient=True)

    def __init__(
            self, bodyCondition=None, class_=None, datatype=None,
            interface=None, isOrdered=None, isQuery=None, isUnique=None,
            lower=None, postcondition=None, precondition=None,
            redefinedOperation=None, type=None, upper=None, **kwargs):

        super(Operation, self).__init__(**kwargs)

        if isOrdered is not None:
            self.isOrdered = isOrdered

        if isQuery is not None:
            self.isQuery = isQuery

        if isUnique is not None:
            self.isUnique = isUnique

        if lower is not None:
            self.lower = lower

        if upper is not None:
            self.upper = upper

        if bodyCondition is not None:
            self.bodyCondition = bodyCondition

        if class_ is not None:
            self.class_ = class_

        if datatype is not None:
            self.datatype = datatype

        if interface is not None:
            self.interface = interface

        if postcondition:
            self.postcondition.extend(postcondition)

        if precondition:
            self.precondition.extend(precondition)

        if redefinedOperation:
            self.redefinedOperation.extend(redefinedOperation)

        if type is not None:
            self.type = type


class StringExpression(
        _user_module.StringExpressionMixin, Expression, TemplateableElement):
    """A StringExpression is an Expression that specifies a String value that is derived by concatenating a sequence of operands with String values or a sequence of subExpressions, some of which might be template parameters.
<p>From package UML::Values.</p>"""
    owningExpression = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    subExpression = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, owningExpression=None, subExpression=None, **kwargs):

        super(StringExpression, self).__init__(**kwargs)

        if owningExpression is not None:
            self.owningExpression = owningExpression

        if subExpression:
            self.subExpression.extend(subExpression)


class Realization(_user_module.RealizationMixin, Abstraction):
    """Realization is a specialized Abstraction relationship between two sets of model Elements, one representing a specification (the supplier) and the other represents an implementation of the latter (the client). Realization can be used to model stepwise refinement, optimizations, transformations, templates, model synthesis, framework composition, etc.
<p>From package UML::CommonStructure.</p>"""

    def __init__(self, **kwargs):

        super(Realization, self).__init__(**kwargs)


@abstract
class Pin(_user_module.PinMixin, ObjectNode, MultiplicityElement):
    """A Pin is an ObjectNode and MultiplicityElement that provides input values to an Action or accepts output values from an Action.
<p>From package UML::Actions.</p>"""
    isControl = EAttribute(eType=Boolean, derived=False,
                           changeable=True, default_value=False)

    def __init__(self, isControl=None, **kwargs):

        super(Pin, self).__init__(**kwargs)

        if isControl is not None:
            self.isControl = isControl


@abstract
class WriteLinkAction(_user_module.WriteLinkActionMixin, LinkAction):
    """WriteLinkAction is an abstract class for LinkActions that create and destroy links.
<p>From package UML::Actions.</p>"""

    def __init__(self, **kwargs):

        super(WriteLinkAction, self).__init__(**kwargs)


@abstract
class WriteStructuralFeatureAction(
        _user_module.WriteStructuralFeatureActionMixin, StructuralFeatureAction):
    """WriteStructuralFeatureAction is an abstract class for StructuralFeatureActions that change StructuralFeature values.
<p>From package UML::Actions.</p>"""
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)
    value = EReference(ordered=False, unique=True,
                       containment=True, derived=False)

    def __init__(self, result=None, value=None, **kwargs):

        super(WriteStructuralFeatureAction, self).__init__(**kwargs)

        if result is not None:
            self.result = result

        if value is not None:
            self.value = value


@abstract
class WriteVariableAction(
        _user_module.WriteVariableActionMixin, VariableAction):
    """WriteVariableAction is an abstract class for VariableActions that change Variable values.
<p>From package UML::Actions.</p>"""
    value = EReference(ordered=False, unique=True,
                       containment=True, derived=False)

    def __init__(self, value=None, **kwargs):

        super(WriteVariableAction, self).__init__(**kwargs)

        if value is not None:
            self.value = value


class AcceptCallAction(_user_module.AcceptCallActionMixin, AcceptEventAction):
    """An AcceptCallAction is an AcceptEventAction that handles the receipt of a synchronous call request. In addition to the values from the Operation input parameters, the Action produces an output that is needed later to supply the information to the ReplyAction necessary to return control to the caller. An AcceptCallAction is for synchronous calls. If it is used to handle an asynchronous call, execution of the subsequent ReplyAction will complete immediately with no effect.
<p>From package UML::Actions.</p>"""
    returnInformation = EReference(
        ordered=False, unique=True, containment=True, derived=False)

    def __init__(self, returnInformation=None, **kwargs):

        super(AcceptCallAction, self).__init__(**kwargs)

        if returnInformation is not None:
            self.returnInformation = returnInformation


class BroadcastSignalAction(
        _user_module.BroadcastSignalActionMixin, InvocationAction):
    """A BroadcastSignalAction is an InvocationAction that transmits a Signal instance to all the potential target objects in the system. Values from the argument InputPins are used to provide values for the attributes of the Signal. The requestor continues execution immediately after the Signal instances are sent out and cannot receive reply values.
<p>From package UML::Actions.</p>"""
    signal = EReference(ordered=False, unique=True,
                        containment=False, derived=False)

    def __init__(self, signal=None, **kwargs):

        super(BroadcastSignalAction, self).__init__(**kwargs)

        if signal is not None:
            self.signal = signal


@abstract
class CallAction(_user_module.CallActionMixin, InvocationAction):
    """CallAction is an abstract class for Actions that invoke a Behavior with given argument values and (if the invocation is synchronous) receive reply values.
<p>From package UML::Actions.</p>"""
    isSynchronous = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=True)
    result = EReference(ordered=True, unique=True,
                        containment=True, derived=False, upper=-1)

    def __init__(self, isSynchronous=None, result=None, **kwargs):

        super(CallAction, self).__init__(**kwargs)

        if isSynchronous is not None:
            self.isSynchronous = isSynchronous

        if result:
            self.result.extend(result)


class ClearStructuralFeatureAction(
        _user_module.ClearStructuralFeatureActionMixin, StructuralFeatureAction):
    """A ClearStructuralFeatureAction is a StructuralFeatureAction that removes all values of a StructuralFeature.
<p>From package UML::Actions.</p>"""
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, result=None, **kwargs):

        super(ClearStructuralFeatureAction, self).__init__(**kwargs)

        if result is not None:
            self.result = result


class ClearVariableAction(
        _user_module.ClearVariableActionMixin, VariableAction):
    """A ClearVariableAction is a VariableAction that removes all values of a Variable.
<p>From package UML::Actions.</p>"""

    def __init__(self, **kwargs):

        super(ClearVariableAction, self).__init__(**kwargs)


class ReadLinkAction(_user_module.ReadLinkActionMixin, LinkAction):
    """A ReadLinkAction is a LinkAction that navigates across an Association to retrieve the objects on one end.
<p>From package UML::Actions.</p>"""
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, result=None, **kwargs):

        super(ReadLinkAction, self).__init__(**kwargs)

        if result is not None:
            self.result = result


class ReadStructuralFeatureAction(
        _user_module.ReadStructuralFeatureActionMixin, StructuralFeatureAction):
    """A ReadStructuralFeatureAction is a StructuralFeatureAction that retrieves the values of a StructuralFeature.
<p>From package UML::Actions.</p>"""
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, result=None, **kwargs):

        super(ReadStructuralFeatureAction, self).__init__(**kwargs)

        if result is not None:
            self.result = result


class ReadVariableAction(_user_module.ReadVariableActionMixin, VariableAction):
    """A ReadVariableAction is a VariableAction that retrieves the values of a Variable.
<p>From package UML::Actions.</p>"""
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, result=None, **kwargs):

        super(ReadVariableAction, self).__init__(**kwargs)

        if result is not None:
            self.result = result


class SendObjectAction(_user_module.SendObjectActionMixin, InvocationAction):
    """A SendObjectAction is an InvocationAction that transmits an input object to the target object, which is handled as a request message by the target object. The requestor continues execution immediately after the object is sent out and cannot receive reply values.
<p>From package UML::Actions.</p>"""
    request = EReference(ordered=False, unique=True,
                         containment=True, derived=False)
    target = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, request=None, target=None, **kwargs):

        super(SendObjectAction, self).__init__(**kwargs)

        if request is not None:
            self.request = request

        if target is not None:
            self.target = target


class SendSignalAction(_user_module.SendSignalActionMixin, InvocationAction):
    """A SendSignalAction is an InvocationAction that creates a Signal instance and transmits it to the target object. Values from the argument InputPins are used to provide values for the attributes of the Signal. The requestor continues execution immediately after the Signal instance is sent out and cannot receive reply values.
<p>From package UML::Actions.</p>"""
    signal = EReference(ordered=False, unique=True,
                        containment=False, derived=False)
    target = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, signal=None, target=None, **kwargs):

        super(SendSignalAction, self).__init__(**kwargs)

        if signal is not None:
            self.signal = signal

        if target is not None:
            self.target = target


class DataStoreNode(_user_module.DataStoreNodeMixin, CentralBufferNode):
    """A DataStoreNode is a CentralBufferNode for persistent data.
<p>From package UML::Activities.</p>"""

    def __init__(self, **kwargs):

        super(DataStoreNode, self).__init__(**kwargs)


@abstract
class BehavioredClassifier(_user_module.BehavioredClassifierMixin, Classifier):
    """A BehavioredClassifier may have InterfaceRealizations, and owns a set of Behaviors one of which may specify the behavior of the BehavioredClassifier itself.
<p>From package UML::SimpleClassifiers.</p>"""
    classifierBehavior = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    interfaceRealization = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    ownedBehavior = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)

    def __init__(
            self, classifierBehavior=None, interfaceRealization=None,
            ownedBehavior=None, **kwargs):

        super(BehavioredClassifier, self).__init__(**kwargs)

        if classifierBehavior is not None:
            self.classifierBehavior = classifierBehavior

        if interfaceRealization:
            self.interfaceRealization.extend(interfaceRealization)

        if ownedBehavior:
            self.ownedBehavior.extend(ownedBehavior)


class DataType(_user_module.DataTypeMixin, Classifier):
    """A DataType is a type whose instances are identified only by their value.
<p>From package UML::SimpleClassifiers.</p>"""
    ownedAttribute = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedOperation = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, ownedAttribute=None, ownedOperation=None, **kwargs):

        super(DataType, self).__init__(**kwargs)

        if ownedAttribute:
            self.ownedAttribute.extend(ownedAttribute)

        if ownedOperation:
            self.ownedOperation.extend(ownedOperation)


class Interface(_user_module.InterfaceMixin, Classifier):
    """Interfaces declare coherent services that are implemented by BehavioredClassifiers that implement the Interfaces via InterfaceRealizations.
<p>From package UML::SimpleClassifiers.</p>"""
    nestedClassifier = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedAttribute = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedReception = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    protocol = EReference(ordered=False, unique=True,
                          containment=True, derived=False)
    redefinedInterface = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    ownedOperation = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(
            self, nestedClassifier=None, ownedAttribute=None,
            ownedReception=None, protocol=None, redefinedInterface=None,
            ownedOperation=None, **kwargs):

        super(Interface, self).__init__(**kwargs)

        if nestedClassifier:
            self.nestedClassifier.extend(nestedClassifier)

        if ownedAttribute:
            self.ownedAttribute.extend(ownedAttribute)

        if ownedReception:
            self.ownedReception.extend(ownedReception)

        if protocol is not None:
            self.protocol = protocol

        if redefinedInterface:
            self.redefinedInterface.extend(redefinedInterface)

        if ownedOperation:
            self.ownedOperation.extend(ownedOperation)


class Signal(_user_module.SignalMixin, Classifier):
    """A Signal is a specification of a kind of communication between objects in which a reaction is asynchronously triggered in the receiver without a reply.
<p>From package UML::SimpleClassifiers.</p>"""
    ownedAttribute = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, ownedAttribute=None, **kwargs):

        super(Signal, self).__init__(**kwargs)

        if ownedAttribute:
            self.ownedAttribute.extend(ownedAttribute)


@abstract
class StructuredClassifier(_user_module.StructuredClassifierMixin, Classifier):
    """StructuredClassifiers may contain an internal structure of connected elements each of which plays a role in the overall Behavior modeled by the StructuredClassifier.
<p>From package UML::StructuredClassifiers.</p>"""
    ownedAttribute = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedConnector = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    part = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedPart)
    role = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedRole)

    def __init__(
            self, ownedAttribute=None, ownedConnector=None, part=None,
            role=None, **kwargs):

        super(StructuredClassifier, self).__init__(**kwargs)

        if ownedAttribute:
            self.ownedAttribute.extend(ownedAttribute)

        if ownedConnector:
            self.ownedConnector.extend(ownedConnector)

        if part:
            self.part.extend(part)

        if role:
            self.role.extend(role)


class Substitution(_user_module.SubstitutionMixin, Realization):
    """A substitution is a relationship between two classifiers signifying that the substituting classifier complies with the contract specified by the contract classifier. This implies that instances of the substituting classifier are runtime substitutable where instances of the contract classifier are expected.
<p>From package UML::Classification.</p>"""
    contract = EReference(ordered=False, unique=True,
                          containment=False, derived=False)
    substitutingClassifier = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, contract=None, substitutingClassifier=None, **kwargs):

        super(Substitution, self).__init__(**kwargs)

        if contract is not None:
            self.contract = contract

        if substitutingClassifier is not None:
            self.substitutingClassifier = substitutingClassifier


class InterfaceRealization(
        _user_module.InterfaceRealizationMixin, Realization):
    """An InterfaceRealization is a specialized realization relationship between a BehavioredClassifier and an Interface. This relationship signifies that the realizing BehavioredClassifier conforms to the contract specified by the Interface.
<p>From package UML::SimpleClassifiers.</p>"""
    contract = EReference(ordered=False, unique=True,
                          containment=False, derived=False)
    implementingClassifier = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, contract=None, implementingClassifier=None, **kwargs):

        super(InterfaceRealization, self).__init__(**kwargs)

        if contract is not None:
            self.contract = contract

        if implementingClassifier is not None:
            self.implementingClassifier = implementingClassifier


class StructuredActivityNode(_user_module.StructuredActivityNodeMixin, Action,
                             Namespace, ActivityGroup):
    """A StructuredActivityNode is an Action that is also an ActivityGroup and whose behavior is specified by the ActivityNodes and ActivityEdges it so contains. Unlike other kinds of ActivityGroup, a StructuredActivityNode owns the ActivityNodes and ActivityEdges it contains, and so a node or edge can only be directly contained in one StructuredActivityNode, though StructuredActivityNodes may be nested.
<p>From package UML::Actions.</p>"""
    mustIsolate = EAttribute(eType=Boolean, derived=False,
                             changeable=True, default_value=False)
    edge = EReference(ordered=False, unique=True,
                      containment=True, derived=False, upper=-1)
    structuredNodeInput = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    structuredNodeOutput = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    variable = EReference(ordered=False, unique=True,
                          containment=True, derived=False, upper=-1)
    node = EReference(ordered=False, unique=True,
                      containment=True, derived=False, upper=-1)

    def __init__(self, edge=None, mustIsolate=None,
                 structuredNodeInput=None, structuredNodeOutput=None,
                 variable=None, node=None, **kwargs):

        super(StructuredActivityNode, self).__init__(**kwargs)

        if mustIsolate is not None:
            self.mustIsolate = mustIsolate

        if edge:
            self.edge.extend(edge)

        if structuredNodeInput:
            self.structuredNodeInput.extend(structuredNodeInput)

        if structuredNodeOutput:
            self.structuredNodeOutput.extend(structuredNodeOutput)

        if variable:
            self.variable.extend(variable)

        if node:
            self.node.extend(node)


class InputPin(_user_module.InputPinMixin, Pin):
    """An InputPin is a Pin that holds input values to be consumed by an Action.
<p>From package UML::Actions.</p>"""

    def __init__(self, **kwargs):

        super(InputPin, self).__init__(**kwargs)


class OutputPin(_user_module.OutputPinMixin, Pin):
    """An OutputPin is a Pin that holds output values produced by an Action.
<p>From package UML::Actions.</p>"""

    def __init__(self, **kwargs):

        super(OutputPin, self).__init__(**kwargs)


class AddStructuralFeatureValueAction(
        _user_module.AddStructuralFeatureValueActionMixin,
        WriteStructuralFeatureAction):
    """An AddStructuralFeatureValueAction is a WriteStructuralFeatureAction for adding values to a StructuralFeature.
<p>From package UML::Actions.</p>"""
    isReplaceAll = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    insertAt = EReference(ordered=False, unique=True,
                          containment=True, derived=False)

    def __init__(self, insertAt=None, isReplaceAll=None, **kwargs):

        super(AddStructuralFeatureValueAction, self).__init__(**kwargs)

        if isReplaceAll is not None:
            self.isReplaceAll = isReplaceAll

        if insertAt is not None:
            self.insertAt = insertAt


class AddVariableValueAction(
        _user_module.AddVariableValueActionMixin, WriteVariableAction):
    """An AddVariableValueAction is a WriteVariableAction for adding values to a Variable.
<p>From package UML::Actions.</p>"""
    isReplaceAll = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    insertAt = EReference(ordered=False, unique=True,
                          containment=True, derived=False)

    def __init__(self, insertAt=None, isReplaceAll=None, **kwargs):

        super(AddVariableValueAction, self).__init__(**kwargs)

        if isReplaceAll is not None:
            self.isReplaceAll = isReplaceAll

        if insertAt is not None:
            self.insertAt = insertAt


class CallBehaviorAction(_user_module.CallBehaviorActionMixin, CallAction):
    """A CallBehaviorAction is a CallAction that invokes a Behavior directly. The argument values of the CallBehaviorAction are passed on the input Parameters of the invoked Behavior. If the call is synchronous, the execution of the CallBehaviorAction waits until the execution of the invoked Behavior completes and the values of output Parameters of the Behavior are placed on the result OutputPins. If the call is asynchronous, the CallBehaviorAction completes immediately and no results values can be provided.
<p>From package UML::Actions.</p>"""
    behavior = EReference(ordered=False, unique=True,
                          containment=False, derived=False)

    def __init__(self, behavior=None, **kwargs):

        super(CallBehaviorAction, self).__init__(**kwargs)

        if behavior is not None:
            self.behavior = behavior


class CallOperationAction(_user_module.CallOperationActionMixin, CallAction):
    """A CallOperationAction is a CallAction that transmits an Operation call request to the target object, where it may cause the invocation of associated Behavior. The argument values of the CallOperationAction are passed on the input Parameters of the Operation. If call is synchronous, the execution of the CallOperationAction waits until the execution of the invoked Operation completes and the values of output Parameters of the Operation are placed on the result OutputPins. If the call is asynchronous, the CallOperationAction completes immediately and no results values can be provided.
<p>From package UML::Actions.</p>"""
    operation = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    target = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, operation=None, target=None, **kwargs):

        super(CallOperationAction, self).__init__(**kwargs)

        if operation is not None:
            self.operation = operation

        if target is not None:
            self.target = target


class CreateLinkAction(_user_module.CreateLinkActionMixin, WriteLinkAction):
    """A CreateLinkAction is a WriteLinkAction for creating links.
<p>From package UML::Actions.</p>"""

    def __init__(self, **kwargs):

        super(CreateLinkAction, self).__init__(**kwargs)


class DestroyLinkAction(_user_module.DestroyLinkActionMixin, WriteLinkAction):
    """A DestroyLinkAction is a WriteLinkAction that destroys links (including link objects).
<p>From package UML::Actions.</p>"""

    def __init__(self, **kwargs):

        super(DestroyLinkAction, self).__init__(**kwargs)


class RemoveStructuralFeatureValueAction(
        _user_module.RemoveStructuralFeatureValueActionMixin,
        WriteStructuralFeatureAction):
    """A RemoveStructuralFeatureValueAction is a WriteStructuralFeatureAction that removes values from a StructuralFeature.
<p>From package UML::Actions.</p>"""
    isRemoveDuplicates = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    removeAt = EReference(ordered=False, unique=True,
                          containment=True, derived=False)

    def __init__(self, isRemoveDuplicates=None, removeAt=None, **kwargs):

        super(RemoveStructuralFeatureValueAction, self).__init__(**kwargs)

        if isRemoveDuplicates is not None:
            self.isRemoveDuplicates = isRemoveDuplicates

        if removeAt is not None:
            self.removeAt = removeAt


class RemoveVariableValueAction(
        _user_module.RemoveVariableValueActionMixin, WriteVariableAction):
    """A RemoveVariableValueAction is a WriteVariableAction that removes values from a Variables.
<p>From package UML::Actions.</p>"""
    isRemoveDuplicates = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    removeAt = EReference(ordered=False, unique=True,
                          containment=True, derived=False)

    def __init__(self, isRemoveDuplicates=None, removeAt=None, **kwargs):

        super(RemoveVariableValueAction, self).__init__(**kwargs)

        if isRemoveDuplicates is not None:
            self.isRemoveDuplicates = isRemoveDuplicates

        if removeAt is not None:
            self.removeAt = removeAt


class StartObjectBehaviorAction(
        _user_module.StartObjectBehaviorActionMixin, CallAction):
    """A StartObjectBehaviorAction is an InvocationAction that starts the execution either of a directly instantiated Behavior or of the classifierBehavior of an object. Argument values may be supplied for the input Parameters of the Behavior. If the Behavior is invoked synchronously, then output values may be obtained for output Parameters.
<p>From package UML::Actions.</p>"""
    object = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, object=None, **kwargs):

        super(StartObjectBehaviorAction, self).__init__(**kwargs)

        if object is not None:
            self.object = object


class InformationItem(_user_module.InformationItemMixin, Classifier):
    """InformationItems represent many kinds of information that can flow from sources to targets in very abstract ways.  They represent the kinds of information that may move within a system, but do not elaborate details of the transferred information.  Details of transferred information are the province of other Classifiers that may ultimately define InformationItems.  Consequently, InformationItems cannot be instantiated and do not themselves have features, generalizations, or associations. An important use of InformationItems is to represent information during early design stages, possibly before the detailed modeling decisions that will ultimately define them have been made. Another purpose of InformationItems is to abstract portions of complex models in less precise, but perhaps more general and communicable, ways.
<p>From package UML::InformationFlows.</p>"""
    represented = EReference(ordered=False, unique=True,
                             containment=False, derived=False, upper=-1)

    def __init__(self, represented=None, **kwargs):

        super(InformationItem, self).__init__(**kwargs)

        if represented:
            self.represented.extend(represented)


class ComponentRealization(
        _user_module.ComponentRealizationMixin, Realization):
    """Realization is specialized to (optionally) define the Classifiers that realize the contract offered by a Component in terms of its provided and required Interfaces. The Component forms an abstraction from these various Classifiers.
<p>From package UML::StructuredClassifiers.</p>"""
    realizingClassifier = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    abstraction = EReference(ordered=False, unique=True,
                             containment=False, derived=False)

    def __init__(self, realizingClassifier=None, abstraction=None, **kwargs):

        super(ComponentRealization, self).__init__(**kwargs)

        if realizingClassifier:
            self.realizingClassifier.extend(realizingClassifier)

        if abstraction is not None:
            self.abstraction = abstraction


class Association(_user_module.AssociationMixin, Classifier, Relationship):
    """A link is a tuple of values that refer to typed objects.  An Association classifies a set of links, each of which is an instance of the Association.  Each value in the link refers to an instance of the type of the corresponding end of the Association.
<p>From package UML::StructuredClassifiers.</p>"""
    isDerived = EAttribute(eType=Boolean, derived=False,
                           changeable=True, default_value=False)
    endType = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedEndtype)
    memberEnd = EReference(ordered=True, unique=True,
                           containment=False, derived=False, upper=-1)
    ownedEnd = EReference(ordered=True, unique=True,
                          containment=True, derived=False, upper=-1)
    navigableOwnedEnd = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, endType=None, isDerived=None, memberEnd=None,
                 ownedEnd=None, navigableOwnedEnd=None, **kwargs):

        super(Association, self).__init__(**kwargs)

        if isDerived is not None:
            self.isDerived = isDerived

        if endType:
            self.endType.extend(endType)

        if memberEnd:
            self.memberEnd.extend(memberEnd)

        if ownedEnd:
            self.ownedEnd.extend(ownedEnd)

        if navigableOwnedEnd:
            self.navigableOwnedEnd.extend(navigableOwnedEnd)


class Property(_user_module.PropertyMixin, StructuralFeature,
               ConnectableElement, DeploymentTarget):
    """A Property is a StructuralFeature. A Property related by ownedAttribute to a Classifier (other than an association) represents an attribute and might also represent an association end. It relates an instance of the Classifier to a value or set of values of the type of the attribute. A Property related by memberEnd to an Association represents an end of the Association. The type of the Property is the type of the end of the Association. A Property has the capability of being a DeploymentTarget in a Deployment relationship. This enables modeling the deployment to hierarchical nodes that have Properties functioning as internal parts.  Property specializes ParameterableElement to specify that a Property can be exposed as a formal template parameter, and provided as an actual parameter in a binding of a template.
<p>From package UML::Classification.</p>"""
    _default = EAttribute(eType=String, derived=True,
                          changeable=True, name='default', transient=True)
    aggregation = EAttribute(
        eType=AggregationKind, derived=False, changeable=True,
        default_value=AggregationKind.none)
    _isComposite = EAttribute(
        eType=Boolean, derived=True, changeable=True, name='isComposite',
        default_value=False, transient=True)
    isDerived = EAttribute(eType=Boolean, derived=False,
                           changeable=True, default_value=False)
    isDerivedUnion = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    isID = EAttribute(eType=Boolean, derived=False,
                      changeable=True, default_value=False)
    datatype = EReference(ordered=False, unique=True,
                          containment=False, derived=False)
    interface = EReference(ordered=False, unique=True,
                           containment=False, derived=False)
    associationEnd = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    qualifier = EReference(ordered=True, unique=True,
                           containment=True, derived=False, upper=-1)
    class_ = EReference(ordered=False, unique=True,
                        containment=False, derived=False, transient=True)
    defaultValue = EReference(
        ordered=False, unique=True, containment=True, derived=False)
    _opposite = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='opposite', transient=True)
    owningAssociation = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    redefinedProperty = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    subsettedProperty = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    association = EReference(ordered=False, unique=True,
                             containment=False, derived=False)

    def __init__(
            self, datatype=None, interface=None, default=None,
            aggregation=None, associationEnd=None, qualifier=None, class_=None,
            defaultValue=None, isComposite=None, isDerived=None,
            isDerivedUnion=None, isID=None, opposite=None,
            owningAssociation=None, redefinedProperty=None,
            subsettedProperty=None, association=None, **kwargs):

        super(Property, self).__init__(**kwargs)

        if default is not None:
            self.default = default

        if aggregation is not None:
            self.aggregation = aggregation

        if isComposite is not None:
            self.isComposite = isComposite

        if isDerived is not None:
            self.isDerived = isDerived

        if isDerivedUnion is not None:
            self.isDerivedUnion = isDerivedUnion

        if isID is not None:
            self.isID = isID

        if datatype is not None:
            self.datatype = datatype

        if interface is not None:
            self.interface = interface

        if associationEnd is not None:
            self.associationEnd = associationEnd

        if qualifier:
            self.qualifier.extend(qualifier)

        if class_ is not None:
            self.class_ = class_

        if defaultValue is not None:
            self.defaultValue = defaultValue

        if opposite is not None:
            self.opposite = opposite

        if owningAssociation is not None:
            self.owningAssociation = owningAssociation

        if redefinedProperty:
            self.redefinedProperty.extend(redefinedProperty)

        if subsettedProperty:
            self.subsettedProperty.extend(subsettedProperty)

        if association is not None:
            self.association = association


class Artifact(_user_module.ArtifactMixin, Classifier, DeployedArtifact):
    """An artifact is the specification of a physical piece of information that is used or produced by a software development process, or by deployment and operation of a system. Examples of artifacts include model files, source files, scripts, and binary executable files, a table in a database system, a development deliverable, or a word-processing document, a mail message.
An artifact is the source of a deployment to a node.
<p>From package UML::Deployments.</p>"""
    fileName = EAttribute(eType=String, derived=False, changeable=True)
    manifestation = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    nestedArtifact = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    ownedAttribute = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedOperation = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(
            self, fileName=None, manifestation=None, nestedArtifact=None,
            ownedAttribute=None, ownedOperation=None, **kwargs):

        super(Artifact, self).__init__(**kwargs)

        if fileName is not None:
            self.fileName = fileName

        if manifestation:
            self.manifestation.extend(manifestation)

        if nestedArtifact:
            self.nestedArtifact.extend(nestedArtifact)

        if ownedAttribute:
            self.ownedAttribute.extend(ownedAttribute)

        if ownedOperation:
            self.ownedOperation.extend(ownedOperation)


class Enumeration(_user_module.EnumerationMixin, DataType):
    """An Enumeration is a DataType whose values are enumerated in the model as EnumerationLiterals.
<p>From package UML::SimpleClassifiers.</p>"""
    ownedLiteral = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, ownedLiteral=None, **kwargs):

        super(Enumeration, self).__init__(**kwargs)

        if ownedLiteral:
            self.ownedLiteral.extend(ownedLiteral)


class PrimitiveType(_user_module.PrimitiveTypeMixin, DataType):
    """A PrimitiveType defines a predefined DataType, without any substructure. A PrimitiveType may have an algebra and operations defined outside of UML, for example, mathematically.
<p>From package UML::SimpleClassifiers.</p>"""

    def __init__(self, **kwargs):

        super(PrimitiveType, self).__init__(**kwargs)


class UseCase(_user_module.UseCaseMixin, BehavioredClassifier):
    """A UseCase specifies a set of actions performed by its subjects, which yields an observable result that is of value for one or more Actors or other stakeholders of each subject.
<p>From package UML::UseCases.</p>"""
    extend = EReference(ordered=False, unique=True,
                        containment=True, derived=False, upper=-1)
    extensionPoint = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    include = EReference(ordered=False, unique=True,
                         containment=True, derived=False, upper=-1)
    subject = EReference(ordered=False, unique=True,
                         containment=False, derived=False, upper=-1)

    def __init__(
            self, extend=None, extensionPoint=None, include=None,
            subject=None, **kwargs):

        super(UseCase, self).__init__(**kwargs)

        if extend:
            self.extend.extend(extend)

        if extensionPoint:
            self.extensionPoint.extend(extensionPoint)

        if include:
            self.include.extend(include)

        if subject:
            self.subject.extend(subject)


@abstract
class EncapsulatedClassifier(
        _user_module.EncapsulatedClassifierMixin, StructuredClassifier):
    """An EncapsulatedClassifier may own Ports to specify typed interaction points.
<p>From package UML::StructuredClassifiers.</p>"""
    ownedPort = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedOwnedport)

    def __init__(self, ownedPort=None, **kwargs):

        super(EncapsulatedClassifier, self).__init__(**kwargs)

        if ownedPort:
            self.ownedPort.extend(ownedPort)


class ActionInputPin(_user_module.ActionInputPinMixin, InputPin):
    """An ActionInputPin is a kind of InputPin that executes an Action to determine the values to input to another Action.
<p>From package UML::Actions.</p>"""
    fromAction = EReference(ordered=False, unique=True,
                            containment=True, derived=False)

    def __init__(self, fromAction=None, **kwargs):

        super(ActionInputPin, self).__init__(**kwargs)

        if fromAction is not None:
            self.fromAction = fromAction


class ConditionalNode(_user_module.ConditionalNodeMixin,
                      StructuredActivityNode):
    """A ConditionalNode is a StructuredActivityNode that chooses one among some number of alternative collections of ExecutableNodes to execute.
<p>From package UML::Actions.</p>"""
    isAssured = EAttribute(eType=Boolean, derived=False,
                           changeable=True, default_value=False)
    isDeterminate = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    clause = EReference(ordered=False, unique=True,
                        containment=True, derived=False, upper=-1)
    result = EReference(ordered=True, unique=True,
                        containment=True, derived=False, upper=-1)

    def __init__(
            self, clause=None, isAssured=None, isDeterminate=None,
            result=None, **kwargs):

        super(ConditionalNode, self).__init__(**kwargs)

        if isAssured is not None:
            self.isAssured = isAssured

        if isDeterminate is not None:
            self.isDeterminate = isDeterminate

        if clause:
            self.clause.extend(clause)

        if result:
            self.result.extend(result)


class CreateLinkObjectAction(
        _user_module.CreateLinkObjectActionMixin, CreateLinkAction):
    """A CreateLinkObjectAction is a CreateLinkAction for creating link objects (AssociationClasse instances).
<p>From package UML::Actions.</p>"""
    result = EReference(ordered=False, unique=True,
                        containment=True, derived=False)

    def __init__(self, result=None, **kwargs):

        super(CreateLinkObjectAction, self).__init__(**kwargs)

        if result is not None:
            self.result = result


class ExpansionRegion(_user_module.ExpansionRegionMixin,
                      StructuredActivityNode):
    """An ExpansionRegion is a StructuredActivityNode that executes its content multiple times corresponding to elements of input collection(s).
<p>From package UML::Actions.</p>"""
    mode = EAttribute(
        eType=ExpansionKind, derived=False, changeable=True,
        default_value=ExpansionKind.iterative)
    outputElement = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    inputElement = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(
            self, mode=None, outputElement=None, inputElement=None, **
            kwargs):

        super(ExpansionRegion, self).__init__(**kwargs)

        if mode is not None:
            self.mode = mode

        if outputElement:
            self.outputElement.extend(outputElement)

        if inputElement:
            self.inputElement.extend(inputElement)


class LoopNode(_user_module.LoopNodeMixin, StructuredActivityNode):
    """A LoopNode is a StructuredActivityNode that represents an iterative loop with setup, test, and body sections.
<p>From package UML::Actions.</p>"""
    isTestedFirst = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    bodyOutput = EReference(ordered=True, unique=True,
                            containment=False, derived=False, upper=-1)
    bodyPart = EReference(ordered=False, unique=True,
                          containment=False, derived=False, upper=-1)
    decider = EReference(ordered=False, unique=True,
                         containment=False, derived=False)
    loopVariable = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    loopVariableInput = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    result = EReference(ordered=True, unique=True,
                        containment=True, derived=False, upper=-1)
    setupPart = EReference(ordered=False, unique=True,
                           containment=False, derived=False, upper=-1)
    test = EReference(ordered=False, unique=True,
                      containment=False, derived=False, upper=-1)

    def __init__(
            self, bodyOutput=None, bodyPart=None, decider=None,
            isTestedFirst=None, loopVariable=None, loopVariableInput=None,
            result=None, setupPart=None, test=None, **kwargs):

        super(LoopNode, self).__init__(**kwargs)

        if isTestedFirst is not None:
            self.isTestedFirst = isTestedFirst

        if bodyOutput:
            self.bodyOutput.extend(bodyOutput)

        if bodyPart:
            self.bodyPart.extend(bodyPart)

        if decider is not None:
            self.decider = decider

        if loopVariable:
            self.loopVariable.extend(loopVariable)

        if loopVariableInput:
            self.loopVariableInput.extend(loopVariableInput)

        if result:
            self.result.extend(result)

        if setupPart:
            self.setupPart.extend(setupPart)

        if test:
            self.test.extend(test)


class SequenceNode(_user_module.SequenceNodeMixin, StructuredActivityNode):
    """A SequenceNode is a StructuredActivityNode that executes a sequence of ExecutableNodes in order.
<p>From package UML::Actions.</p>"""
    executableNode = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, executableNode=None, **kwargs):

        super(SequenceNode, self).__init__(**kwargs)

        if executableNode:
            self.executableNode.extend(executableNode)


class ValuePin(_user_module.ValuePinMixin, InputPin):
    """A ValuePin is an InputPin that provides a value by evaluating a ValueSpecification.
<p>From package UML::Actions.</p>"""
    value = EReference(ordered=False, unique=True,
                       containment=True, derived=False)

    def __init__(self, value=None, **kwargs):

        super(ValuePin, self).__init__(**kwargs)

        if value is not None:
            self.value = value


class Actor(_user_module.ActorMixin, BehavioredClassifier):
    """An Actor specifies a role played by a user or any other system that interacts with the subject.
<p>From package UML::UseCases.</p>"""

    def __init__(self, **kwargs):

        super(Actor, self).__init__(**kwargs)


class DeploymentSpecification(
        _user_module.DeploymentSpecificationMixin, Artifact):
    """A deployment specification specifies a set of properties that determine execution parameters of a component artifact that is deployed on a node. A deployment specification can be aimed at a specific type of container. An artifact that reifies or implements deployment specification properties is a deployment descriptor.
<p>From package UML::Deployments.</p>"""
    deploymentLocation = EAttribute(
        eType=String, derived=False, changeable=True)
    executionLocation = EAttribute(
        eType=String, derived=False, changeable=True)
    deployment = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(
            self, deploymentLocation=None, executionLocation=None,
            deployment=None, **kwargs):

        super(DeploymentSpecification, self).__init__(**kwargs)

        if deploymentLocation is not None:
            self.deploymentLocation = deploymentLocation

        if executionLocation is not None:
            self.executionLocation = executionLocation

        if deployment is not None:
            self.deployment = deployment


class Port(_user_module.PortMixin, Property):
    """A Port is a property of an EncapsulatedClassifier that specifies a distinct interaction point between that EncapsulatedClassifier and its environment or between the (behavior of the) EncapsulatedClassifier and its internal parts. Ports are connected to Properties of the EncapsulatedClassifier by Connectors through which requests can be made to invoke BehavioralFeatures. A Port may specify the services an EncapsulatedClassifier provides (offers) to its environment as well as the services that an EncapsulatedClassifier expects (requires) of its environment.  A Port may have an associated ProtocolStateMachine.
<p>From package UML::StructuredClassifiers.</p>"""
    isBehavior = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=False)
    isConjugated = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    isService = EAttribute(eType=Boolean, derived=False,
                           changeable=True, default_value=True)
    protocol = EReference(ordered=False, unique=True,
                          containment=False, derived=False)
    provided = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedProvided)
    redefinedPort = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    required = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedRequired)

    def __init__(
            self, isBehavior=None, isConjugated=None, isService=None,
            protocol=None, provided=None, redefinedPort=None, required=None, **
            kwargs):

        super(Port, self).__init__(**kwargs)

        if isBehavior is not None:
            self.isBehavior = isBehavior

        if isConjugated is not None:
            self.isConjugated = isConjugated

        if isService is not None:
            self.isService = isService

        if protocol is not None:
            self.protocol = protocol

        if provided:
            self.provided.extend(provided)

        if redefinedPort:
            self.redefinedPort.extend(redefinedPort)

        if required:
            self.required.extend(required)


class Extension(_user_module.ExtensionMixin, Association):
    """An extension is used to indicate that the properties of a metaclass are extended through a stereotype, and gives the ability to flexibly add (and later remove) stereotypes to classes.
<p>From package UML::Packages.</p>"""
    _isRequired = EAttribute(
        eType=Boolean, derived=True, changeable=False, name='isRequired',
        transient=True)
    _metaclass = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='metaclass', transient=True)

    def __init__(self, isRequired=None, metaclass=None, **kwargs):

        super(Extension, self).__init__(**kwargs)

        if isRequired is not None:
            self.isRequired = isRequired

        if metaclass is not None:
            self.metaclass = metaclass


class ExtensionEnd(_user_module.ExtensionEndMixin, Property):
    """An extension end is used to tie an extension to a stereotype when extending a metaclass.
The default multiplicity of an extension end is 0..1.
<p>From package UML::Packages.</p>"""

    def __init__(self, **kwargs):

        super(ExtensionEnd, self).__init__(**kwargs)


class Collaboration(
        _user_module.CollaborationMixin, StructuredClassifier,
        BehavioredClassifier):
    """A Collaboration describes a structure of collaborating elements (roles), each performing a specialized function, which collectively accomplish some desired functionality.
<p>From package UML::StructuredClassifiers.</p>"""
    collaborationRole = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, collaborationRole=None, **kwargs):

        super(Collaboration, self).__init__(**kwargs)

        if collaborationRole:
            self.collaborationRole.extend(collaborationRole)


class CommunicationPath(_user_module.CommunicationPathMixin, Association):
    """A communication path is an association between two deployment targets, through which they are able to exchange signals and messages.
<p>From package UML::Deployments.</p>"""

    def __init__(self, **kwargs):

        super(CommunicationPath, self).__init__(**kwargs)


class Class(_user_module.ClassMixin, EncapsulatedClassifier,
            BehavioredClassifier):
    """A Class classifies a set of objects and specifies the features that characterize the structure and behavior of those objects.  A Class may have an internal structure and Ports.
<p>From package UML::StructuredClassifiers.</p>"""
    isActive = EAttribute(eType=Boolean, derived=False,
                          changeable=True, default_value=False)
    ownedOperation = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    extension = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedExtension)
    nestedClassifier = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedReception = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    superClass = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedSuperclass)

    def __init__(
            self, ownedOperation=None, extension=None, isActive=None,
            nestedClassifier=None, ownedReception=None, superClass=None, **
            kwargs):

        super(Class, self).__init__(**kwargs)

        if isActive is not None:
            self.isActive = isActive

        if ownedOperation:
            self.ownedOperation.extend(ownedOperation)

        if extension:
            self.extension.extend(extension)

        if nestedClassifier:
            self.nestedClassifier.extend(nestedClassifier)

        if ownedReception:
            self.ownedReception.extend(ownedReception)

        if superClass:
            self.superClass.extend(superClass)


@abstract
class Behavior(_user_module.BehaviorMixin, Class):
    """Behavior is a specification of how its context BehavioredClassifier changes state over time. This specification may be either a definition of possible behavior execution or emergent behavior, or a selective illustration of an interesting subset of possible executions. The latter form is typically used for capturing examples, such as a trace of a particular execution.
<p>From package UML::CommonBehavior.</p>"""
    isReentrant = EAttribute(eType=Boolean, derived=False,
                             changeable=True, default_value=True)
    specification = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    _context = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='context', transient=True)
    ownedParameter = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedParameterSet = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    postcondition = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    precondition = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    redefinedBehavior = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(
            self, specification=None, context=None, isReentrant=None,
            ownedParameter=None, ownedParameterSet=None, postcondition=None,
            precondition=None, redefinedBehavior=None, **kwargs):

        super(Behavior, self).__init__(**kwargs)

        if isReentrant is not None:
            self.isReentrant = isReentrant

        if specification is not None:
            self.specification = specification

        if context is not None:
            self.context = context

        if ownedParameter:
            self.ownedParameter.extend(ownedParameter)

        if ownedParameterSet:
            self.ownedParameterSet.extend(ownedParameterSet)

        if postcondition:
            self.postcondition.extend(postcondition)

        if precondition:
            self.precondition.extend(precondition)

        if redefinedBehavior:
            self.redefinedBehavior.extend(redefinedBehavior)


class Stereotype(_user_module.StereotypeMixin, Class):
    """A stereotype defines how an existing metaclass may be extended, and enables the use of platform or domain specific terminology or notation in place of, or in addition to, the ones used for the extended metaclass.
<p>From package UML::Packages.</p>"""
    icon = EReference(ordered=False, unique=True,
                      containment=True, derived=False, upper=-1)
    _profile = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='profile', transient=True)

    def __init__(self, icon=None, profile=None, **kwargs):

        super(Stereotype, self).__init__(**kwargs)

        if icon:
            self.icon.extend(icon)

        if profile is not None:
            self.profile = profile


class Component(_user_module.ComponentMixin, Class):
    """A Component represents a modular part of a system that encapsulates its contents and whose manifestation is replaceable within its environment.
<p>From package UML::StructuredClassifiers.</p>"""
    isIndirectlyInstantiated = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=True)
    packagedElement = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    provided = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedProvided)
    realization = EReference(ordered=False, unique=True,
                             containment=True, derived=False, upper=-1)
    required = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedRequired)

    def __init__(
            self, isIndirectlyInstantiated=None, packagedElement=None,
            provided=None, realization=None, required=None, **kwargs):

        super(Component, self).__init__(**kwargs)

        if isIndirectlyInstantiated is not None:
            self.isIndirectlyInstantiated = isIndirectlyInstantiated

        if packagedElement:
            self.packagedElement.extend(packagedElement)

        if provided:
            self.provided.extend(provided)

        if realization:
            self.realization.extend(realization)

        if required:
            self.required.extend(required)


class Activity(_user_module.ActivityMixin, Behavior):
    """An Activity is the specification of parameterized Behavior as the coordinated sequencing of subordinate units.
<p>From package UML::Activities.</p>"""
    isReadOnly = EAttribute(eType=Boolean, derived=False,
                            changeable=True, default_value=False)
    isSingleExecution = EAttribute(
        eType=Boolean, derived=False, changeable=True, default_value=False)
    ownedGroup = EReference(ordered=False, unique=True,
                            containment=True, derived=False, upper=-1)
    edge = EReference(ordered=False, unique=True,
                      containment=True, derived=False, upper=-1)
    node = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedNode)
    variable = EReference(ordered=False, unique=True,
                          containment=True, derived=False, upper=-1)
    group = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedGroup)
    ownedNode = EReference(ordered=False, unique=True,
                           containment=True, derived=False, upper=-1)
    partition = EReference(ordered=False, unique=True,
                           containment=False, derived=False, upper=-1)
    structuredNode = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)

    def __init__(
            self, ownedGroup=None, edge=None, node=None, variable=None,
            group=None, ownedNode=None, isReadOnly=None,
            isSingleExecution=None, partition=None, structuredNode=None, **
            kwargs):

        super(Activity, self).__init__(**kwargs)

        if isReadOnly is not None:
            self.isReadOnly = isReadOnly

        if isSingleExecution is not None:
            self.isSingleExecution = isSingleExecution

        if ownedGroup:
            self.ownedGroup.extend(ownedGroup)

        if edge:
            self.edge.extend(edge)

        if node:
            self.node.extend(node)

        if variable:
            self.variable.extend(variable)

        if group:
            self.group.extend(group)

        if ownedNode:
            self.ownedNode.extend(ownedNode)

        if partition:
            self.partition.extend(partition)

        if structuredNode:
            self.structuredNode.extend(structuredNode)


class StateMachine(_user_module.StateMachineMixin, Behavior):
    """StateMachines can be used to express event-driven behaviors of parts of a system. Behavior is modeled as a traversal of a graph of Vertices interconnected by one or more joined Transition arcs that are triggered by the dispatching of successive Event occurrences. During this traversal, the StateMachine may execute a sequence of Behaviors associated with various elements of the StateMachine.
<p>From package UML::StateMachines.</p>"""
    connectionPoint = EReference(
        ordered=False, unique=True, containment=True, derived=False, upper=-1)
    submachineState = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)
    region = EReference(ordered=False, unique=True,
                        containment=True, derived=False, upper=-1)
    extendedStateMachine = EReference(
        ordered=False, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, connectionPoint=None, submachineState=None,
                 region=None, extendedStateMachine=None, **kwargs):

        super(StateMachine, self).__init__(**kwargs)

        if connectionPoint:
            self.connectionPoint.extend(connectionPoint)

        if submachineState:
            self.submachineState.extend(submachineState)

        if region:
            self.region.extend(region)

        if extendedStateMachine:
            self.extendedStateMachine.extend(extendedStateMachine)


class OpaqueBehavior(_user_module.OpaqueBehaviorMixin, Behavior):
    """An OpaqueBehavior is a Behavior whose specification is given in a textual language other than UML.
<p>From package UML::CommonBehavior.</p>"""
    body = EAttribute(eType=String, derived=False, changeable=True, upper=-1)
    language = EAttribute(eType=String, derived=False,
                          changeable=True, upper=-1)

    def __init__(self, body=None, language=None, **kwargs):

        super(OpaqueBehavior, self).__init__(**kwargs)

        if body:
            self.body.extend(body)

        if language:
            self.language.extend(language)


class Node(_user_module.NodeMixin, Class, DeploymentTarget):
    """A Node is computational resource upon which artifacts may be deployed for execution. Nodes can be interconnected through communication paths to define network structures.
<p>From package UML::Deployments.</p>"""
    nestedNode = EReference(ordered=False, unique=True,
                            containment=True, derived=False, upper=-1)

    def __init__(self, nestedNode=None, **kwargs):

        super(Node, self).__init__(**kwargs)

        if nestedNode:
            self.nestedNode.extend(nestedNode)


class ProtocolStateMachine(
        _user_module.ProtocolStateMachineMixin, StateMachine):
    """A ProtocolStateMachine is always defined in the context of a Classifier. It specifies which BehavioralFeatures of the Classifier can be called in which State and under which conditions, thus specifying the allowed invocation sequences on the Classifier's BehavioralFeatures. A ProtocolStateMachine specifies the possible and permitted Transitions on the instances of its context Classifier, together with the BehavioralFeatures that carry the Transitions. In this manner, an instance lifecycle can be specified for a Classifier, by defining the order in which the BehavioralFeatures can be activated and the States through which an instance progresses during its existence.
<p>From package UML::StateMachines.</p>"""
    conformance = EReference(ordered=False, unique=True,
                             containment=True, derived=False, upper=-1)

    def __init__(self, conformance=None, **kwargs):

        super(ProtocolStateMachine, self).__init__(**kwargs)

        if conformance:
            self.conformance.extend(conformance)


class FunctionBehavior(_user_module.FunctionBehaviorMixin, OpaqueBehavior):
    """A FunctionBehavior is an OpaqueBehavior that does not access or modify any objects or other external data.
<p>From package UML::CommonBehavior.</p>"""

    def __init__(self, **kwargs):

        super(FunctionBehavior, self).__init__(**kwargs)


class Device(_user_module.DeviceMixin, Node):
    """A device is a physical computational resource with processing capability upon which artifacts may be deployed for execution. Devices may be complex (i.e., they may consist of other devices).
<p>From package UML::Deployments.</p>"""

    def __init__(self, **kwargs):

        super(Device, self).__init__(**kwargs)


class ExecutionEnvironment(_user_module.ExecutionEnvironmentMixin, Node):
    """An execution environment is a node that offers an execution environment for specific types of components that are deployed on it in the form of executable artifacts.
<p>From package UML::Deployments.</p>"""

    def __init__(self, **kwargs):

        super(ExecutionEnvironment, self).__init__(**kwargs)


class Interaction(
        _user_module.InteractionMixin, Behavior, InteractionFragment):
    """An Interaction is a unit of Behavior that focuses on the observable exchange of information between connectable elements.
<p>From package UML::Interactions.</p>"""
    lifeline = EReference(ordered=False, unique=True,
                          containment=True, derived=False, upper=-1)
    fragment = EReference(ordered=True, unique=True,
                          containment=True, derived=False, upper=-1)
    action = EReference(ordered=False, unique=True,
                        containment=True, derived=False, upper=-1)
    formalGate = EReference(ordered=False, unique=True,
                            containment=True, derived=False, upper=-1)
    message = EReference(ordered=False, unique=True,
                         containment=True, derived=False, upper=-1)

    def __init__(self, lifeline=None, fragment=None, action=None,
                 formalGate=None, message=None, **kwargs):

        super(Interaction, self).__init__(**kwargs)

        if lifeline:
            self.lifeline.extend(lifeline)

        if fragment:
            self.fragment.extend(fragment)

        if action:
            self.action.extend(action)

        if formalGate:
            self.formalGate.extend(formalGate)

        if message:
            self.message.extend(message)


class AssociationClass(_user_module.AssociationClassMixin, Class, Association):
    """A model element that has both Association and Class properties. An AssociationClass can be seen as an Association that also has Class properties, or as a Class that also has Association properties. It not only connects a set of Classifiers but also defines a set of Features that belong to the Association itself and not to any of the associated Classifiers.
<p>From package UML::StructuredClassifiers.</p>"""

    def __init__(self, **kwargs):

        super(AssociationClass, self).__init__(**kwargs)
