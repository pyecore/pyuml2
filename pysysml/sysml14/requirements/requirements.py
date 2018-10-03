"""Definition of meta model 'requirements'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from ..blocks import DirectedRelationshipPropertyPath
from pyuml2.standard import Trace, Refine
from pyuml2.types import String
import pysysml.requirements_mixins as _user_module


name = 'requirements'
nsURI = 'http://www.eclipse.org/papyrus/sysml/1.4/SysML/Requirements'
nsPrefix = 'Requirements'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class Requirement(
        _user_module.RequirementMixin, EObject, metaclass=MetaEClass):
    """
            A requirement specifies a capability or condition that must (or should) be satisfied. A requirement may specify a function that a system must perform or a performance condition that a system must satisfy. Requirements are used to establish a contract between the customer (or other stakeholder) and those responsible for designing and implementing the system.
          """
    id = EAttribute(eType=String, derived=False, changeable=True)
    text = EAttribute(eType=String, derived=False, changeable=True)
    base_Class = EReference(ordered=False, unique=True,
                            containment=False, derived=False)
    derived = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedDerived)
    derivedFrom = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedDerivedfrom)
    _master = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='master', transient=True)
    refinedBy = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedRefinedby)
    satisfiedBy = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedSatisfiedby)
    tracedTo = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedTracedto)
    verifiedBy = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedVerifiedby)

    def __init__(
            self, *, base_Class=None, derived=None, derivedFrom=None, id=None,
            master=None, refinedBy=None, satisfiedBy=None, text=None,
            tracedTo=None, verifiedBy=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if text is not None:
            self.text = text

        if base_Class is not None:
            self.base_Class = base_Class

        if derived:
            self.derived.extend(derived)

        if derivedFrom:
            self.derivedFrom.extend(derivedFrom)

        if master is not None:
            self.master = master

        if refinedBy:
            self.refinedBy.extend(refinedBy)

        if satisfiedBy:
            self.satisfiedBy.extend(satisfiedBy)

        if tracedTo:
            self.tracedTo.extend(tracedTo)

        if verifiedBy:
            self.verifiedBy.extend(verifiedBy)


class TestCase(_user_module.TestCaseMixin, EObject, metaclass=MetaEClass):
    """A test case is a method for verifying a requirement is satisfied."""
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


class Trace(_user_module.TraceMixin, DirectedRelationshipPropertyPath, Trace):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Refine(
        _user_module.RefineMixin, DirectedRelationshipPropertyPath, Refine):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Copy(_user_module.CopyMixin, Trace):
    """A Copy relationship is a dependency between a supplier requirement and a client requirement that specifies that the text of the client requirement is a read-only copy of the text of the supplier requirement."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DeriveReqt(_user_module.DeriveReqtMixin, Trace):
    """
            A DeriveReqt relationship is a dependency between two requirements in which a client requirement can be derived from the supplier requirement. As with other dependencies, the arrow direction points from the derived (client) requirement to the (supplier) requirement from which it is derived.
          """

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Satisfy(_user_module.SatisfyMixin, Trace):
    """A Satisfy relationship is a dependency between a requirement and a model element that fulfills the requirement. As with other dependencies, the arrow direction points from the satisfying (client) model element to the (supplier) requirement that is satisfied."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Verify(_user_module.VerifyMixin, Trace):
    """A Verify relationship is a dependency between a requirement and a test case or other model element that can determine whether a system fulfills the requirement. As with other dependencies, the arrow direction points from the (client) element to the (supplier) requirement."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
