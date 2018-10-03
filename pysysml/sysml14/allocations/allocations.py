"""Definition of meta model 'allocations'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from ..blocks import DirectedRelationshipPropertyPath
import pysysml.allocations_mixins as _user_module


name = 'allocations'
nsURI = 'http://www.eclipse.org/papyrus/sysml/1.4/SysML/Allocations'
nsPrefix = 'Allocations'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class AllocateActivityPartition(_user_module.AllocateActivityPartitionMixin,
                                EObject, metaclass=MetaEClass):
    """AllocateActivityPartition is used to depict an «allocate» relationship on an Activity diagram. The AllocateActivityPartition is a standard UML2::ActivityPartition, with modified constraints as stated in the paragraph below."""
    base_ActivityPartition = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_ActivityPartition=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_ActivityPartition is not None:
            self.base_ActivityPartition = base_ActivityPartition


class Allocate(_user_module.AllocateMixin, DirectedRelationshipPropertyPath):
    """
            Allocate is a dependency based on UML::abstraction. It is a mechanism for associating elements of different types, or in different hierarchies, at an abstract level. Allocate is used for assessing user model consistency and directing future design activity. It is expected that an «allocate» relationship between model elements is a precursor to a more concrete relationship between the elements, their properties, operations, attributes, or sub-classes.
          """
    base_Abstraction = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Abstraction=None, **kwargs):

        super().__init__(**kwargs)

        if base_Abstraction is not None:
            self.base_Abstraction = base_Abstraction
