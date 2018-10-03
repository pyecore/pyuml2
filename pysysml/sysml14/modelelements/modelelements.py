"""Definition of meta model 'modelelements'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from pyuml2.types import Integer, String
import pysysml.modelelements_mixins as _user_module


name = 'modelelements'
nsURI = 'http://www.eclipse.org/papyrus/sysml/1.4/SysML/ModelElements'
nsPrefix = 'ModelElements'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class Conform(_user_module.ConformMixin, EObject, metaclass=MetaEClass):
    """
            A Conform relationship is a dependency between a view and a viewpoint. The view conforms to the specified rules and conventions detailed in the viewpoint. Conform is a specialization of the UML dependency, and as with other dependencies the arrow direction points from the (client/source) to the (supplier/target).
          """
    base_Generalization = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Generalization=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Generalization is not None:
            self.base_Generalization = base_Generalization


class ElementGroup(_user_module.ElementGroupMixin, EObject,
                   metaclass=MetaEClass):

    _criterion = EAttribute(eType=String, derived=True,
                            changeable=False, name='criterion', transient=True)
    name = EAttribute(eType=String, derived=False, changeable=True)
    _size = EAttribute(eType=Integer, derived=True,
                       changeable=False, name='size', transient=True)
    base_Comment = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    member = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedMember)
    orderedMemeber = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, base_Comment=None, criterion=None, member=None,
                 name=None, orderedMemeber=None, size=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if criterion is not None:
            self.criterion = criterion

        if name is not None:
            self.name = name

        if size is not None:
            self.size = size

        if base_Comment is not None:
            self.base_Comment = base_Comment

        if member:
            self.member.extend(member)

        if orderedMemeber:
            self.orderedMemeber.extend(orderedMemeber)


class Expose(_user_module.ExposeMixin, EObject, metaclass=MetaEClass):

    base_Dependency = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Dependency=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Dependency is not None:
            self.base_Dependency = base_Dependency


class Problem(_user_module.ProblemMixin, EObject, metaclass=MetaEClass):
    """
            A Problem documents a deficiency, limitation, or failure of one or more model elements to satisfy a requirement or need, or other undesired outcome. It may be used to capture problems identified during analysis, design, verification, or manufacture and associate the problem with the relevant model elements. Problem is a stereotype of comment and may be attached to any other model element in the same manner as a comment.
          """
    base_Comment = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Comment=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Comment is not None:
            self.base_Comment = base_Comment


class Rationale(_user_module.RationaleMixin, EObject, metaclass=MetaEClass):
    """
            A Rationale documents the justification for decisions and the requirements, design, and other decisions. A Rationale can be attached to any model element including relationships. It allows the user, for example, to specify a rationale that may reference more detailed documentation such as a trade study or analysis report. Rationale is a stereotype of comment and may be attached to any other model element in the same manner as a comment.
          """
    base_Comment = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Comment=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Comment is not None:
            self.base_Comment = base_Comment


class Stakeholder(
        _user_module.StakeholderMixin, EObject, metaclass=MetaEClass):

    concern = EAttribute(
        eType=String, derived=True, changeable=False, upper=-1, transient=True,
        derived_class=_user_module.DerivedConcern)
    base_Classifier = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    concernList = EReference(ordered=False, unique=True,
                             containment=False, derived=False, upper=-1)

    def __init__(
            self, *, base_Classifier=None, concernList=None, concern=None, **
            kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if concern:
            self.concern.extend(concern)

        if base_Classifier is not None:
            self.base_Classifier = base_Classifier

        if concernList:
            self.concernList.extend(concernList)


class View(_user_module.ViewMixin, EObject, metaclass=MetaEClass):
    """A View is a representation of a whole system or subsystem from the perspective of a single viewpoint. Views are allowed to import other elements including other packages and other views that conform to the viewpoint."""
    base_Class = EReference(ordered=False, unique=True,
                            containment=False, derived=False)
    stakeholder = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedStakeholder)
    _viewPoint = EReference(
        ordered=False, unique=True, containment=False, derived=True,
        name='viewPoint', transient=True)

    def __init__(
            self, *, base_Class=None, stakeholder=None, viewPoint=None, **
            kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Class is not None:
            self.base_Class = base_Class

        if stakeholder:
            self.stakeholder.extend(stakeholder)

        if viewPoint is not None:
            self.viewPoint = viewPoint


class Viewpoint(_user_module.ViewpointMixin, EObject, metaclass=MetaEClass):
    """
            A Viewpoint is a specification of the conventions and rules for constructing and using a view for the purpose of addressing a set of stakeholder concerns. The languages and methods for specifying a view may reference languages and methods in another viewpoint. They specify the elements expected to be represented in the view, and may be formally or informally defined. For example, the security viewpoint may require the security requirements, security functional and physical architecture, and security test cases.
          """
    concern = EAttribute(
        eType=String, derived=True, changeable=False, upper=-1, transient=True,
        derived_class=_user_module.DerivedConcern)
    language = EAttribute(eType=String, derived=False,
                          changeable=True, upper=-1)
    presentation = EAttribute(
        eType=String, derived=False, changeable=True, upper=-1)
    purpose = EAttribute(eType=String, derived=False, changeable=True)
    base_Class = EReference(ordered=False, unique=True,
                            containment=False, derived=False)
    concernList = EReference(ordered=False, unique=True,
                             containment=False, derived=False, upper=-1)
    method = EReference(
        ordered=False, unique=True, containment=False, derived=True, upper=-1,
        transient=True, derived_class=_user_module.DerivedMethod)
    stakeholder = EReference(ordered=False, unique=True,
                             containment=False, derived=False, upper=-1)

    def __init__(
            self, *, base_Class=None, concern=None, concernList=None,
            language=None, method=None, presentation=None, purpose=None,
            stakeholder=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if concern:
            self.concern.extend(concern)

        if language:
            self.language.extend(language)

        if presentation:
            self.presentation.extend(presentation)

        if purpose is not None:
            self.purpose = purpose

        if base_Class is not None:
            self.base_Class = base_Class

        if concernList:
            self.concernList.extend(concernList)

        if method:
            self.method.extend(method)

        if stakeholder:
            self.stakeholder.extend(stakeholder)
