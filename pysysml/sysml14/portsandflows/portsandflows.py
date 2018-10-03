"""Definition of meta model 'portsandflows'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from ..blocks import ElementPropertyPath, Block
import pysysml.portsandflows_mixins as _user_module


name = 'portsandflows'
nsURI = 'http://www.eclipse.org/papyrus/sysml/1.4/SysML/PortsAndFlows'
nsPrefix = 'PortsAndFlows'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
FeatureDirection = EEnum('FeatureDirection', literals=[
                         'provided', 'providedRequired', 'required'])

FlowDirection = EEnum('FlowDirection', literals=['in_', 'inout', 'out'])


class AcceptChangeStructuralFeatureEventAction(
        _user_module.AcceptChangeStructuralFeatureEventActionMixin, EObject,
        metaclass=MetaEClass):

    base_AcceptEventAction = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_AcceptEventAction=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_AcceptEventAction is not None:
            self.base_AcceptEventAction = base_AcceptEventAction


class ChangeStructuralFeatureEvent(
        _user_module.ChangeStructuralFeatureEventMixin, EObject,
        metaclass=MetaEClass):

    base_ChangeEvent = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    structuralFeature = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(
            self, *, base_ChangeEvent=None, structuralFeature=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_ChangeEvent is not None:
            self.base_ChangeEvent = base_ChangeEvent

        if structuralFeature is not None:
            self.structuralFeature = structuralFeature


class DirectedFeature(
        _user_module.DirectedFeatureMixin, EObject, metaclass=MetaEClass):

    featureDirection = EAttribute(
        eType=FeatureDirection, derived=False, changeable=True)
    base_Feature = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Feature=None, featureDirection=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if featureDirection is not None:
            self.featureDirection = featureDirection

        if base_Feature is not None:
            self.base_Feature = base_Feature


class FlowProperty(_user_module.FlowPropertyMixin, EObject,
                   metaclass=MetaEClass):
    """
            A FlowProperty signifies a single flow element that can flow to/from a block. A flow property’s values are either received from or transmitted to an external block. Flow properties are defined directly on blocks or flow specifications that are those specifications which type the flow ports. Flow properties enable item flows across connectors connecting parts of the corresponding block types, either directly (in case of the property is defined on the block) or via flowPorts. For Block, Data Type, and Value Type properties, setting an “out” FlowProperty value of a block usage on one end of a connector will result in assigning the same value of an “in” FlowProperty of a block usage at the other end of the connector, provided the flow properties are matched. Flow properties of type Signal imply sending and/or receiving of a signal usage. An “out” FlowProperty of type Signal means that the owning Block may broadcast the signal via connectors and an “in” FlowProperty means that the owning block is able to receive the Signal.
          """
    direction = EAttribute(
        eType=FlowDirection, derived=False, changeable=True,
        default_value=FlowDirection.inout)
    base_Property = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Property=None, direction=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if direction is not None:
            self.direction = direction

        if base_Property is not None:
            self.base_Property = base_Property


class FullPort(_user_module.FullPortMixin, EObject, metaclass=MetaEClass):

    base_Port = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(self, *, base_Port=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Port is not None:
            self.base_Port = base_Port


class ItemFlow(_user_module.ItemFlowMixin, EObject, metaclass=MetaEClass):
    """
            An ItemFlow describes the flow of items across a connector or an association. It may constrain the item exchange between blocks, block usages, or flow ports as specified by their flow properties. For example, a pump connected to a tank: the pump has an “out” flow property of type Liquid and the tank has an “in” FlowProperty of type Liquid. To signify that only water flows between the pump and the tank, we can specify an ItemFlow of type Water on the connector.
          """
    base_InformationFlow = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    itemProperty = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(
            self, *, base_InformationFlow=None, itemProperty=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_InformationFlow is not None:
            self.base_InformationFlow = base_InformationFlow

        if itemProperty is not None:
            self.itemProperty = itemProperty


class ProxyPort(_user_module.ProxyPortMixin, EObject, metaclass=MetaEClass):

    base_Port = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(self, *, base_Port=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Port is not None:
            self.base_Port = base_Port


class InterfaceBlock(_user_module.InterfaceBlockMixin, Block):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class InvocationOnNestedPortAction(
        _user_module.InvocationOnNestedPortActionMixin, ElementPropertyPath):

    base_InvocationAction = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    onNestedPort = EReference(
        ordered=True, unique=False, containment=False, derived=False, upper=-1)

    def __init__(
            self, *, base_InvocationAction=None, onNestedPort=None, **kwargs):

        super().__init__(**kwargs)

        if base_InvocationAction is not None:
            self.base_InvocationAction = base_InvocationAction

        if onNestedPort:
            self.onNestedPort.extend(onNestedPort)


class TriggerOnNestedPort(
        _user_module.TriggerOnNestedPortMixin, ElementPropertyPath):

    base_Trigger = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    onNestedPort = EReference(
        ordered=True, unique=False, containment=False, derived=False, upper=-1)

    def __init__(self, *, base_Trigger=None, onNestedPort=None, **kwargs):

        super().__init__(**kwargs)

        if base_Trigger is not None:
            self.base_Trigger = base_Trigger

        if onNestedPort:
            self.onNestedPort.extend(onNestedPort)
