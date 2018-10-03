"""Definition of meta model 'deprecatedelements'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from pyuml2.types import Boolean
from ..portsandflows import FlowDirection
import pysysml.deprecatedelements_mixins as _user_module


name = 'deprecatedelements'
nsURI = 'http://www.eclipse.org/papyrus/sysml/1.4/SysML/DeprecatedElements'
nsPrefix = 'DeprecatedElements'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class FlowPort(_user_module.FlowPortMixin, EObject, metaclass=MetaEClass):
    """
            A FlowPort is an interaction point through which input and/or output of items such as data, material, or energy may flow. This enables the owning block to declare which items it may exchange with its environment and the interaction points through which the exchange is made. We distinguish between atomic flow port and a nonatomic flow port. Atomic flow ports relay items that are classified by a single Block, ValueType, DataType, or Signal classifier. A nonatomic flow port relays items of several types as specified by a FlowSpecification. Flow ports and associated flow specifications define “what can flow” between the block and its environment, whereas item flows specify “what does flow” in a specific usage context. Flow ports relay items to their owning block or to a connector that connects them with their owner’s internal parts (internal connector).
          """
    direction = EAttribute(
        eType=FlowDirection, derived=False, changeable=True,
        default_value=FlowDirection.inout)
    _isAtomic = EAttribute(eType=Boolean, derived=True,
                           changeable=False, name='isAtomic', transient=True)
    base_Port = EReference(ordered=False, unique=True,
                           containment=False, derived=False)

    def __init__(
            self, *, base_Port=None, direction=None, isAtomic=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if direction is not None:
            self.direction = direction

        if isAtomic is not None:
            self.isAtomic = isAtomic

        if base_Port is not None:
            self.base_Port = base_Port


class FlowSpecification(
        _user_module.FlowSpecificationMixin, EObject, metaclass=MetaEClass):
    """A FlowSpecification specifies inputs and outputs as a set of flow properties. A flow specification is used by flow ports to specify what items can flow via the port."""
    base_Interface = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Interface=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Interface is not None:
            self.base_Interface = base_Interface
