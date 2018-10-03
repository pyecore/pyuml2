"""Definition of meta model 'blocks'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from pyuml2.types import UnlimitedNatural, Integer, Boolean
import pysysml.blocks_mixins as _user_module


name = 'blocks'
nsURI = 'http://www.eclipse.org/papyrus/sysml/1.4/SysML/Blocks'
nsPrefix = 'Blocks'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class AdjunctProperty(
        _user_module.AdjunctPropertyMixin, EObject, metaclass=MetaEClass):
    """
            The AdjunctProperty stereotype can be applied to properties to constrain their values to the values of connectors typed by association blocks, call actions, object nodes, variables, or parameters, interaction uses, and submachine states.  The values of connectors typed by association blocks are the instances of the association block typing a connector in the block having the stereotyped property.  The values of call actions are the executions of behaviors invoked by the behavior having the call action and the stereotyped property (see Subclause 11.3.1.1.1 for more about this use of the stereotype).  The values of object nodes are the values of tokens in the object nodes of the behavior having the stereotyped property (see Subclause 11.3.1.4.1 for more about this use of the stereotype).  The values of variables are those assigned by executions of activities that have the stereotyped property.  The values of parameters are those assigned by executions of behaviors that have the stereotyped property.  The keyword «adjunct» before a property name indicates the property is stereotyped by AdjunctProperty.
          """
    base_Property = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    principal = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(self, *, base_Property=None, principal=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Property is not None:
            self.base_Property = base_Property

        if principal is not None:
            self.principal = principal


class BindingConnector(
        _user_module.BindingConnectorMixin, EObject, metaclass=MetaEClass):
    """
            A Binding Connector is a connector which specifies that the properties at both ends of the connector have equal values. If the properties at the ends of a binding connector are typed by a DataType or ValueType, the connector specifies that the instances of the properties must hold equal values, recursively through any nested properties within the connected properties. If the properties at the ends of a binding connector are typed by a Block, the connector specifies that the instances of the properties must refer to the same block instance. As with any connector owned by a SysML Block, the ends of a binding connector may be nested within a multi-level path of properties accessible from the owning block. The NestedConnectorEnd stereotype is used to represent such nested ends just as for nested ends of other SysML connectors.
          """
    base_Connector = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Connector=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Connector is not None:
            self.base_Connector = base_Connector


class Block(_user_module.BlockMixin, EObject, metaclass=MetaEClass):
    """
            A Block is a modular unit that describes the structure of a system or element. It may include both structural and behavioral features, such as properties and operations, that represent the state of the system and behavior that the system may exhibit. Some of these properties may hold parts of a system, which can also be described by blocks. A block may include a structure of connectors between its properties to indicate how its parts or other properties relate to one another. SysML blocks provide a general-purpose capability to describe the architecture of a system. They provide the ability to represent a system hierarchy, in which a system at one level is composed of systems at a more basic level. They can describe not only the connectivity relationships between the systems at any level, but also quantitative values or other information about a system. SysML does not restrict the kind of system or system element that may be described by a block. Any reusable form of description that may be applied to a system or a set of system characteristics may be described by a block. Such reusable descriptions, for example, may be applied to purely conceptual aspects of a system design, such as relationships that hold between parts or properties of a system. Connectors owned by SysML blocks may be used to define relationships between parts or other properties of the same containing block. The type of a connector or its connected ends may specify the semantic interpretation of a specific connector.
          """
    isEncapsulated = EAttribute(eType=Boolean, derived=False, changeable=True)
    base_Class = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Class=None, isEncapsulated=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if isEncapsulated is not None:
            self.isEncapsulated = isEncapsulated

        if base_Class is not None:
            self.base_Class = base_Class


class EndPathMultiplicity(
        _user_module.EndPathMultiplicityMixin, EObject, metaclass=MetaEClass):

    lower = EAttribute(eType=Integer, derived=False,
                       changeable=True, default_value='0')
    upper = EAttribute(eType=UnlimitedNatural, derived=False,
                       changeable=True, default_value='-1')
    base_Property = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Property=None, lower=None, upper=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if lower is not None:
            self.lower = lower

        if upper is not None:
            self.upper = upper

        if base_Property is not None:
            self.base_Property = base_Property


class ClassifierBehaviorProperty(
        _user_module.ClassifierBehaviorPropertyMixin, EObject,
        metaclass=MetaEClass):
    """
            The ClassifierBehaviorProperty stereotype can be applied to properties to constrain their values to be the executions of classifier behaviors.  The value of properties with ClassifierBehaviorProperty  applied are the executions of classifier behaviors invoked by instantiation of the block that owns the stereotyped property or one of its specializations.
          """
    base_Property = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Property=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Property is not None:
            self.base_Property = base_Property


class ConnectorProperty(
        _user_module.ConnectorPropertyMixin, EObject, metaclass=MetaEClass):
    """
            Connectors can be typed by association classes that are stereotyped by Block (association blocks). These connectors specify instances (links) of the association block that exist due to instantiation of the block owning or inheriting the connector. The value of a connector property on an instance of a block will be exactly those link objects that are instances of the association block typing the connector referred to by the connector property.
          """
    base_Property = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    connector = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(self, *, base_Property=None, connector=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Property is not None:
            self.base_Property = base_Property

        if connector is not None:
            self.connector = connector


class DistributedProperty(
        _user_module.DistributedPropertyMixin, EObject, metaclass=MetaEClass):
    """
            DistributedProperty is a stereotype of Property used to apply a probability distribution to the values of the property. Specific distributions should be defined as subclasses of the DistributedProperty stereotype with the operands of the distributions represented by properties of those stereotype subclasses.
          """
    base_Property = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Property=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Property is not None:
            self.base_Property = base_Property


@abstract
class ElementPropertyPath(
        _user_module.ElementPropertyPathMixin, EObject, metaclass=MetaEClass):

    base_Element = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    propertyPath = EReference(
        ordered=True, unique=False, containment=False, derived=False, upper=-1)

    def __init__(self, *, base_Element=None, propertyPath=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Element is not None:
            self.base_Element = base_Element

        if propertyPath:
            self.propertyPath.extend(propertyPath)


class ParticipantProperty(
        _user_module.ParticipantPropertyMixin, EObject, metaclass=MetaEClass):
    """
            The Block stereotype extends Class, so it can be applied to any specialization of Class, including Association Classes. These are informally called “association blocks.” An association block can own properties and connectors, like any other block. Each instance of an association block can link together instances of the end classifiers of the association. To refer to linked objects and values of an instance of an association block, it is necessary for the modeler to specify which (participant) properties of the association block identify the instances being linked at which end of the association. The value of a participant property on an instance (link) of the association block is the value or object at the end of the link corresponding to this end of the association.
          """
    base_Property = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    end = EReference(ordered=False, unique=True,
                     containment=False, derived=False)

    def __init__(self, *, base_Property=None, end=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Property is not None:
            self.base_Property = base_Property

        if end is not None:
            self.end = end


class PropertySpecificType(
        _user_module.PropertySpecificTypeMixin, EObject, metaclass=MetaEClass):
    """The PropertySpecificType stereotype should automatically be applied to the classifier which types a property with a propertyspecific type. This classifier can contain definitions of new or redefined features which extend the original classifier referenced by the property-specific type."""
    base_Classifier = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Classifier=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Classifier is not None:
            self.base_Classifier = base_Classifier


class ValueType(_user_module.ValueTypeMixin, EObject, metaclass=MetaEClass):
    """
            A ValueType defines types of values that may be used to express information about a system, but cannot be identified as the target of any reference. Since a value cannot be identified except by means of the value itself, each such value within a model is independent of any other, unless other forms of constraints are imposed. Value types may be used to type properties, operation parameters, or potentially other elements within SysML. SysML defines ValueType as a stereotype of UML DataType to establish a more neutral term for system values that may never be given a concrete data representation.
          """
    base_DataType = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    quantityKind = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    unit = EReference(ordered=False, unique=True,
                      containment=False, derived=False)

    def __init__(
            self, *, base_DataType=None, quantityKind=None, unit=None, **
            kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_DataType is not None:
            self.base_DataType = base_DataType

        if quantityKind is not None:
            self.quantityKind = quantityKind

        if unit is not None:
            self.unit = unit


@abstract
class DirectedRelationshipPropertyPath(
        _user_module.DirectedRelationshipPropertyPathMixin, EObject,
        metaclass=MetaEClass):

    base_DirectedRelationship = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    sourceContext = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    sourcePropertyPath = EReference(
        ordered=True, unique=False, containment=False, derived=False, upper=-1)
    targetContext = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    targetPropertyPath = EReference(
        ordered=True, unique=False, containment=False, derived=False, upper=-1)

    def __init__(
            self, *, base_DirectedRelationship=None, sourceContext=None,
            sourcePropertyPath=None, targetContext=None,
            targetPropertyPath=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_DirectedRelationship is not None:
            self.base_DirectedRelationship = base_DirectedRelationship

        if sourceContext is not None:
            self.sourceContext = sourceContext

        if sourcePropertyPath:
            self.sourcePropertyPath.extend(sourcePropertyPath)

        if targetContext is not None:
            self.targetContext = targetContext

        if targetPropertyPath:
            self.targetPropertyPath.extend(targetPropertyPath)


class BoundReference(_user_module.BoundReferenceMixin, EndPathMultiplicity):

    bindingPath = EReference(
        ordered=True, unique=False, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedBindingpath)
    boundEnd = EReference(ordered=False, unique=True,
                          containment=False, derived=False)

    def __init__(self, *, bindingPath=None, boundEnd=None, **kwargs):

        super().__init__(**kwargs)

        if bindingPath:
            self.bindingPath.extend(bindingPath)

        if boundEnd is not None:
            self.boundEnd = boundEnd


class NestedConnectorEnd(
        _user_module.NestedConnectorEndMixin, ElementPropertyPath):
    """The NestedConnectorEnd stereotype of UML ConnectorEnd extends a UML ConnectorEnd so that the connected property may be identified by a multi-level path of accessible properties from the block that owns the connector."""
    base_ConnectorEnd = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_ConnectorEnd=None, **kwargs):

        super().__init__(**kwargs)

        if base_ConnectorEnd is not None:
            self.base_ConnectorEnd = base_ConnectorEnd
