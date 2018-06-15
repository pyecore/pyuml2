"""Definition of meta model 'standard'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
import pyuml2.standard_mixins as _user_module


name = 'standard'
nsURI = 'http://www.eclipse.org/uml2/5.0.0/UML/Profile/Standard'
nsPrefix = 'standard'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class Auxiliary(_user_module.AuxiliaryMixin, EObject, metaclass=MetaEClass):
    """A class that supports another more central or fundamental class, typically by implementing secondary logic or control flow. Auxiliary classes are typically used together with Focus classes, and are particularly useful for specifying the secondary business logic or control flow of components during design. See also: «Focus».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Class = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Class=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Class is not None:
            self.base_Class = base_Class


class Call(_user_module.CallMixin, EObject, metaclass=MetaEClass):
    """A usage dependency whose source is an operation and whose target is an operation. The relationship may also be subsumed to the class containing an operation, with the meaning that there exists an operation in the class to which the dependency applies. A call dependency specifies that the source operation or an operation in the source class invokes the target operation or an operation in the target class. A call dependency may connect a source operation to any target operation that is within scope including, but not limited to, operations of the enclosing classifier and operations of other visible classifiers.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Usage = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Usage=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Usage is not None:
            self.base_Usage = base_Usage


class Create(_user_module.CreateMixin, EObject, metaclass=MetaEClass):
    """When applied to a Usage, denotes that the client classifier creates instances of the supplier classifier. When applied to a BehavioralFeature, specifies that the designated feature creates an instance of the classifier to which the feature is attached.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_BehavioralFeature = EReference(
        ordered=False, unique=True, containment=False, derived=False)
    base_Usage = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(
            self, *, base_BehavioralFeature=None, base_Usage=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_BehavioralFeature is not None:
            self.base_BehavioralFeature = base_BehavioralFeature

        if base_Usage is not None:
            self.base_Usage = base_Usage


class Derive(_user_module.DeriveMixin, EObject, metaclass=MetaEClass):
    """Specifies a derivation relationship among model elements that are usually, but not necessarily, of the same type. A derived dependency specifies that the client may be computed from the supplier. The mapping specifies the computation. The client may be implemented for design reasons, such as efficiency, even though it is logically redundant.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    computation = EReference(ordered=False, unique=True,
                             containment=True, derived=False)
    base_Abstraction = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, computation=None, base_Abstraction=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if computation is not None:
            self.computation = computation

        if base_Abstraction is not None:
            self.base_Abstraction = base_Abstraction


class Destroy(_user_module.DestroyMixin, EObject, metaclass=MetaEClass):
    """Specifies that the designated feature destroys an instance of the classifier to which the feature is attached.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_BehavioralFeature = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_BehavioralFeature=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_BehavioralFeature is not None:
            self.base_BehavioralFeature = base_BehavioralFeature


@abstract
class File(_user_module.FileMixin, EObject, metaclass=MetaEClass):
    """A physical file in the context of the system developed.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Artifact = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Artifact=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Artifact is not None:
            self.base_Artifact = base_Artifact


class Entity(_user_module.EntityMixin, EObject, metaclass=MetaEClass):
    """A persistent information component representing a business concept.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Component = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Component=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Component is not None:
            self.base_Component = base_Component


class Focus(_user_module.FocusMixin, EObject, metaclass=MetaEClass):
    """A class that defines the core logic or control flow for one or more auxiliary classes that support it. Focus classes are typically used together with one or more Auxiliary classes, and are particularly useful for specifying the core business logic or control flow of components during design. See also: «Auxiliary».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Class = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Class=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Class is not None:
            self.base_Class = base_Class


class Framework(_user_module.FrameworkMixin, EObject, metaclass=MetaEClass):
    """A package that contains model elements that specify a reusable architecture for all or part of a system. Frameworks typically include classes, patterns, or templates. When frameworks are specialized for an application domain they are sometimes referred to as application frameworks.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Package = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Package=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Package is not None:
            self.base_Package = base_Package


class Implement(_user_module.ImplementMixin, EObject, metaclass=MetaEClass):
    """A component definition that is not intended to have a specification itself. Rather, it is an implementation for a separate «Specification» to which it has a Dependency.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Component = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Component=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Component is not None:
            self.base_Component = base_Component


class ImplementationClass(
        _user_module.ImplementationClassMixin, EObject, metaclass=MetaEClass):
    """The implementation of a class in some programming language (e.g., C++, Smalltalk, Java) in which an instance may not have more than one class. This is in contrast to Class, for which an instance may have multiple classes at one time and may gain or lose classes over time, and an object may dynamically have multiple classes. An Implementation class is said to realize a Classifier if it provides all of the operations defined for the Classifier with the same behavior as specified for the Classifier's operations. An Implementation Class may realize a number of different Types. The physical attributes and associations of the Implementation class do not have to be the same as those of any Classifier it realizes and the Implementation Class may provide methods for its operations in terms of its physical attributes and associations. See also: «Type».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Class = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Class=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Class is not None:
            self.base_Class = base_Class


class Instantiate(
        _user_module.InstantiateMixin, EObject, metaclass=MetaEClass):
    """A usage dependency among classifiers indicating that operations on the client create instances of the supplier.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Usage = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Usage=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Usage is not None:
            self.base_Usage = base_Usage


class Metaclass(_user_module.MetaclassMixin, EObject, metaclass=MetaEClass):
    """A class whose instances are also classes.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Class = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Class=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Class is not None:
            self.base_Class = base_Class


class ModelLibrary(_user_module.ModelLibraryMixin, EObject,
                   metaclass=MetaEClass):
    """A package that contains model elements that are intended to be reused by other packages. It is analogous to a class library in some programming languages. The model library may not include instances of the metamodel extension metaclasses specified in Clause 12.3, such as Profiles and Stereotypes. However it may include ProfileApplications and Stereotype applications, and a model library is often used in conjunction with an applied Profile.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Package = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Package=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Package is not None:
            self.base_Package = base_Package


class Process(_user_module.ProcessMixin, EObject, metaclass=MetaEClass):
    """A transaction based component.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Component = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Component=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Component is not None:
            self.base_Component = base_Component


class Realization(
        _user_module.RealizationMixin, EObject, metaclass=MetaEClass):
    """A classifier that specifies a domain of objects and that also defines the physical implementation of those objects. For example, a Component stereotyped by «Realization» will only have realizing Classifiers that implement behavior specified by a separate «Specification» Component. See «Specification». This differs from «ImplementationClass» because an «ImplementationClass» is a realization of a Class that can have features such as attributes and methods that are useful to system designers.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Classifier = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Classifier=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Classifier is not None:
            self.base_Classifier = base_Classifier


class Refine(_user_module.RefineMixin, EObject, metaclass=MetaEClass):
    """Specifies a refinement relationship between model elements at different semantic levels, such as analysis and design. The mapping specifies the relationship between the two elements or sets of elements. The mapping may or may not be computable, and it may be unidirectional or bidirectional. Refinement can be used to model transformations from analysis to design and other such changes.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Abstraction = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Abstraction=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Abstraction is not None:
            self.base_Abstraction = base_Abstraction


class Responsibility(
        _user_module.ResponsibilityMixin, EObject, metaclass=MetaEClass):
    """A contract or an obligation of an element in its relationship to other elements.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Usage = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Usage=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Usage is not None:
            self.base_Usage = base_Usage


class Send(_user_module.SendMixin, EObject, metaclass=MetaEClass):
    """A Usage whose client is an Operation and whose supplier is a Signal, specifying that the Operation sends the Signal.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Usage = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Usage=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Usage is not None:
            self.base_Usage = base_Usage


class Service(_user_module.ServiceMixin, EObject, metaclass=MetaEClass):
    """A stateless, functional component.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Component = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Component=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Component is not None:
            self.base_Component = base_Component


class Specification(_user_module.SpecificationMixin, EObject,
                    metaclass=MetaEClass):
    """A classifier that specifies a domain of objects without defining the physical implementation of those objects. For example, a Component stereotyped by «Specification» will only have provided and required interfaces, and is not intended to have any realizingClassifiers as part of its definition. This differs from «Type» because a «Type» can have features such as attributes and methods that are useful to analysts modeling systems. Also see: «Realization».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Classifier = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Classifier=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Classifier is not None:
            self.base_Classifier = base_Classifier


class Subsystem(_user_module.SubsystemMixin, EObject, metaclass=MetaEClass):
    """A unit of hierarchical decomposition for large systems. A subsystem is commonly instantiated indirectly. Definitions of subsystems vary widely among domains and methods, and it is expected that domain and method profiles will specialize this construct. A subsystem may be defined to have specification and realization elements. See also: «Specification» and «Realization».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Component = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Component=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Component is not None:
            self.base_Component = base_Component


class Trace(_user_module.TraceMixin, EObject, metaclass=MetaEClass):
    """Specifies a trace relationship between model elements or sets of model elements that represent the same concept in different models. Traces are mainly used for tracking requirements and changes across models. As model changes can occur in both directions, the directionality of the dependency can often be ignored. The mapping specifies the relationship between the two, but it is rarely computable and is usually informal.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Abstraction = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Abstraction=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Abstraction is not None:
            self.base_Abstraction = base_Abstraction


class Type(_user_module.TypeMixin, EObject, metaclass=MetaEClass):
    """A class that specifies a domain of objects together with the operations applicable to the objects, without defining the physical implementation of those objects. However, it may have attributes and associations. Behavioral specifications for type operations may be expressed using, for example, activity diagrams. An object may have at most one implementation class, however it may conform to multiple different types. See also: «ImplementationClass».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Class = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Class=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Class is not None:
            self.base_Class = base_Class


class Utility(_user_module.UtilityMixin, EObject, metaclass=MetaEClass):
    """A class that has no instances, but rather denotes a named collection of attributes and operations, all of which are static.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Class = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Class=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Class is not None:
            self.base_Class = base_Class


class BuildComponent(
        _user_module.BuildComponentMixin, EObject, metaclass=MetaEClass):
    """A collection of elements defined for the purpose of system level development activities, such as compilation and versioning.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Component = EReference(
        ordered=False, unique=True, containment=False, derived=False)

    def __init__(self, *, base_Component=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Component is not None:
            self.base_Component = base_Component


class Metamodel(_user_module.MetamodelMixin, EObject, metaclass=MetaEClass):
    """A model that specifies the modeling concepts of some modeling language (e.g., a MOF model). See «Metaclass».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Model = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Model=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Model is not None:
            self.base_Model = base_Model


class SystemModel(
        _user_module.SystemModelMixin, EObject, metaclass=MetaEClass):
    """A SystemModel is a stereotyped model that contains a collection of models of the same system. A SystemModel also contains all relationships and constraints between model elements contained in different models.
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""
    base_Model = EReference(ordered=False, unique=True,
                            containment=False, derived=False)

    def __init__(self, *, base_Model=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if base_Model is not None:
            self.base_Model = base_Model


class Document(_user_module.DocumentMixin, File):
    """A human-readable file. Subclass of «File».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Executable(_user_module.ExecutableMixin, File):
    """A program file that can be executed on a computer system. Subclass of «File».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Library(_user_module.LibraryMixin, File):
    """A static or dynamic library file. Subclass of «File».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Script(_user_module.ScriptMixin, File):
    """A script file that can be interpreted by a computer system. Subclass of «File».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Source(_user_module.SourceMixin, File):
    """A source file that can be compiled into an executable file. Subclass of «File».
<p>From package StandardProfile (URI {@literal http://www.omg.org/spec/UML/20131001/StandardProfile}).</p>"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
