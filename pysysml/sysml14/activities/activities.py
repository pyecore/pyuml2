"""Definition of meta model 'activities'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
import pysysml.activities_mixins as _user_module


name = 'activities'
nsURI = 'http://www.eclipse.org/papyrus/sysml/1.4/SysML/Activities'
nsPrefix = 'Activities'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class Rate(_user_module.RateMixin, EObject, metaclass=MetaEClass):
    """
            When the «rate» stereotype is applied to an activity edge, it specifies the expected value of the number of objects and values that traverse the edge per time interval, that is, the expected value rate at which they leave the source node and arrive at the target node. It does not refer to the rate at which a value changes over time. When the stereotype is applied to a parameter, the parameter must be streaming, and the stereotype gives the number of objects or values that flow in or out of the parameter per time interval while the behavior or operation is executing. Streaming is a characteristic of UML behavior parameters that supports the input and output of items while a behavior is executing, rather than only when the behavior starts and stops. The flow may be continuous or discrete. The «rate» stereotype has a rate property of type InstanceSpecification. The values of this property must be instances of classifiers stereotyped by «valueType» or «distributionDefinition». In particular, the denominator for units used in the rate property must be time units.
          """
    base_ActivityEdge = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    base_ObjectNode = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    base_Parameter = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    rate = EReference(ordered=False, unique=True,
                      containment=False, derived=False)

    def __init__(
            self, *, base_ActivityEdge=None, base_ObjectNode=None,
            base_Parameter=None, rate=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_ActivityEdge is not None:
            self.base_ActivityEdge = base_ActivityEdge

        if base_ObjectNode is not None:
            self.base_ObjectNode = base_ObjectNode

        if base_Parameter is not None:
            self.base_Parameter = base_Parameter

        if rate is not None:
            self.rate = rate


class ControlOperator(
        _user_module.ControlOperatorMixin, EObject, metaclass=MetaEClass):
    """
            A control operator is a behavior that is intended to represent an arbitrarily complex logical operator that can be used to enable and disable other actions. When this stereotype is applied to behaviors, the behavior takes control values as inputs or provides them as outputs, that is, it treats control as data. When this stereotype is not applied, the behavior may not have a parameter typed by ControlValue. This stereotype also applies to operations with the same semantics.
          """
    base_Behavior = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    base_Operation = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Behavior=None, base_Operation=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Behavior is not None:
            self.base_Behavior = base_Behavior

        if base_Operation is not None:
            self.base_Operation = base_Operation


class NoBuffer(_user_module.NoBufferMixin, EObject, metaclass=MetaEClass):
    """
            When this stereotype is applied to object nodes, tokens arriving at the node are discarded if they are refused by outgoing edges, or refused by actions for object nodes that are input pins. This is typically used with fast or continuously flowing data values, to prevent buffer overrun, or to model transient values, such as electrical signals. For object nodes that are the target of continuous flows, «nobuffer» and «overwrite» have the same effect. The stereotype does not override UML token offering semantics; it just indicates what happens to the token when it is accepted. When the stereotype is not applied, the semantics are as in UML, specifically, tokens arriving at an object node that are refused by outgoing edges, or action for input pins, are held until they can leave the object node.
          """
    base_ObjectNode = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_ObjectNode=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_ObjectNode is not None:
            self.base_ObjectNode = base_ObjectNode


class Optional(_user_module.OptionalMixin, EObject, metaclass=MetaEClass):
    """
            When the «optional» stereotype is applied to parameters, the lower multiplicity must be equal to zero. This means the parameter is not required to have a value for the activity or any behavior to begin or end execution. Otherwise, the lower multiplicity must be greater than zero, which is called “required.”
          """
    base_Parameter = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Parameter=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Parameter is not None:
            self.base_Parameter = base_Parameter


class Overwrite(_user_module.OverwriteMixin, EObject, metaclass=MetaEClass):
    """
            When the «overwrite» stereotype is applied to object nodes, a token arriving at a full object node replaces the ones already there (a full object node has as many tokens as allowed by its upper bound). This is typically used on an input pin with an upper bound of 1 to ensure that stale data is overridden at an input pin. For upper bounds greater than one, the token replaced is the one that would be the last to be selected according to the ordering kind for the node. For FIFO ordering, this is the most recently added token, for LIFO it is the least recently added token. A null token removes all the tokens already there. The number of tokens replaced is equal to the weight of the incoming edge, which defaults to 1. For object nodes that are the target of continuous flows, «overwrite» and «nobuffer» have the same effect. The stereotype does not override UML token offering semantics, just indicates what happens to the token when it is accepted. When the stereotype is not applied, the semantics is as in UML, specifically, tokens arriving at object nodes do not replace ones that are already there.
          """
    base_ObjectNode = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_ObjectNode=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_ObjectNode is not None:
            self.base_ObjectNode = base_ObjectNode


class Probability(
        _user_module.ProbabilityMixin, EObject, metaclass=MetaEClass):
    """
            When the «probability» stereotype is applied to edges coming out of decision nodes and object nodes, it provides an expression for the probability that the edge will be traversed. These must be between zero and one inclusive, and add up to one for edges with same source at the time the probabilities are used.
When the «probability» stereotype is applied to output parameter sets, it gives the probability the parameter set will be given values at runtime. These must be between zero and one inclusive, and add up to one for output parameter sets of the same behavior at the time the probabilities are used.
          """
    base_ActivityEdge = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    base_ParameterSet = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    probability = EReference(ordered=False, unique=True,
                             containment=False, derived=False)

    def __init__(
            self, *, base_ActivityEdge=None, base_ParameterSet=None,
            probability=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_ActivityEdge is not None:
            self.base_ActivityEdge = base_ActivityEdge

        if base_ParameterSet is not None:
            self.base_ParameterSet = base_ParameterSet

        if probability is not None:
            self.probability = probability


class Continuous(_user_module.ContinuousMixin, Rate):
    """
            Continuous rate is a special case of rate of flow (see Rate) where the increment of time between items approaches zero. It is intended to represent continuous flows that may correspond to water flowing through a pipe, a time continuous signal, or continuous energy flow. It is independent from UML streaming. A streaming parameter may or may not apply to continuous flow, and a continuous flow may or may not apply to streaming parameters.
          """

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Discrete(_user_module.DiscreteMixin, Rate):
    """Discrete rate is a special case of rate of flow (see Rate) where the increment of time between items is non-zero."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
