"""Mixins to be implemented by user."""


class AuxiliaryMixin:
    """User defined mixin class for Auxiliary."""

    def __init__(self, base_Class=None, **kwargs):
        super(AuxiliaryMixin, self).__init__()


class CallMixin:
    """User defined mixin class for Call."""

    def __init__(self, base_Usage=None, **kwargs):
        super(CallMixin, self).__init__()

    def client_and_supplier_are_operations(
            self, diagnostics=None, context=None):
        """self.base_Usage.client->forAll(oclIsKindOf(Operation)) and self.base_Usage.supplier->forAll(oclIsKindOf(Operation))"""
        raise NotImplementedError(
            'operation client_and_supplier_are_operations(...) not yet implemented')


class CreateMixin:
    """User defined mixin class for Create."""

    def __init__(self, base_BehavioralFeature=None, base_Usage=None, **kwargs):
        super(CreateMixin, self).__init__()

    def client_and_supplier_are_classifiers(
            self, diagnostics=None, context=None):
        """self.base_Usage->notEmpty() implies (self.base_Usage.client->forAll(oclIsKindOf(Classifier)) and self.base_Usage.supplier->forAll(oclIsKindOf(Classifier)))"""
        raise NotImplementedError(
            'operation client_and_supplier_are_classifiers(...) not yet implemented')


class DeriveMixin:
    """User defined mixin class for Derive."""

    def __init__(self, computation=None, base_Abstraction=None, **kwargs):
        super(DeriveMixin, self).__init__()


class DestroyMixin:
    """User defined mixin class for Destroy."""

    def __init__(self, base_BehavioralFeature=None, **kwargs):
        super(DestroyMixin, self).__init__()


class FileMixin:
    """User defined mixin class for File."""

    def __init__(self, base_Artifact=None, **kwargs):
        super(FileMixin, self).__init__()


class EntityMixin:
    """User defined mixin class for Entity."""

    def __init__(self, base_Component=None, **kwargs):
        super(EntityMixin, self).__init__()


class FocusMixin:
    """User defined mixin class for Focus."""

    def __init__(self, base_Class=None, **kwargs):
        super(FocusMixin, self).__init__()


class FrameworkMixin:
    """User defined mixin class for Framework."""

    def __init__(self, base_Package=None, **kwargs):
        super(FrameworkMixin, self).__init__()


class ImplementMixin:
    """User defined mixin class for Implement."""

    def __init__(self, base_Component=None, **kwargs):
        super(ImplementMixin, self).__init__()

    def implements_specification(self, diagnostics=None, context=None):
        """self.base_Component.clientDependency.supplier->select(oclIsKindOf(Classifier)).oclAsType(Classifier).extension_Specificaiton->notEmpty()"""
        raise NotImplementedError(
            'operation implements_specification(...) not yet implemented')


class ImplementationClassMixin:
    """User defined mixin class for ImplementationClass."""

    def __init__(self, base_Class=None, **kwargs):
        super(ImplementationClassMixin, self).__init__()

    def cannot_be_realization(self, diagnostics=None, context=None):
        """self.base_Class.extension_Realization->isEmpty()"""
        raise NotImplementedError(
            'operation cannot_be_realization(...) not yet implemented')


class InstantiateMixin:
    """User defined mixin class for Instantiate."""

    def __init__(self, base_Usage=None, **kwargs):
        super(InstantiateMixin, self).__init__()

    def client_and_supplier_are_classifiers(
            self, diagnostics=None, context=None):
        """self.base_Usage.client->forAll(oclIsKindOf(Classifier)) and self.base_Usage.supplier->forAll(oclIsKindOf(Classifier))"""
        raise NotImplementedError(
            'operation client_and_supplier_are_classifiers(...) not yet implemented')


class MetaclassMixin:
    """User defined mixin class for Metaclass."""

    def __init__(self, base_Class=None, **kwargs):
        super(MetaclassMixin, self).__init__()


class ModelLibraryMixin:
    """User defined mixin class for ModelLibrary."""

    def __init__(self, base_Package=None, **kwargs):
        super(ModelLibraryMixin, self).__init__()


class ProcessMixin:
    """User defined mixin class for Process."""

    def __init__(self, base_Component=None, **kwargs):
        super(ProcessMixin, self).__init__()


class RealizationMixin:
    """User defined mixin class for Realization."""

    def __init__(self, base_Classifier=None, **kwargs):
        super(RealizationMixin, self).__init__()

    def cannot_be_implementation_class(self, diagnostics=None, context=None):
        """self.base_Classifier.extension_ImplementationClass->isEmpty()"""
        raise NotImplementedError(
            'operation cannot_be_implementation_class(...) not yet implemented')


class RefineMixin:
    """User defined mixin class for Refine."""

    def __init__(self, base_Abstraction=None, **kwargs):
        super(RefineMixin, self).__init__()


class ResponsibilityMixin:
    """User defined mixin class for Responsibility."""

    def __init__(self, base_Usage=None, **kwargs):
        super(ResponsibilityMixin, self).__init__()


class SendMixin:
    """User defined mixin class for Send."""

    def __init__(self, base_Usage=None, **kwargs):
        super(SendMixin, self).__init__()

    def client_operation_sends_supplier_signal(
            self, diagnostics=None, context=None):
        """self.base_Usage.client->forAll(oclIsKindOf(Operation)) and self.base_Usage.supplier->forAll(oclIsKindOf(Signal))"""
        raise NotImplementedError(
            'operation client_operation_sends_supplier_signal(...) not yet implemented')


class ServiceMixin:
    """User defined mixin class for Service."""

    def __init__(self, base_Component=None, **kwargs):
        super(ServiceMixin, self).__init__()


class SpecificationMixin:
    """User defined mixin class for Specification."""

    def __init__(self, base_Classifier=None, **kwargs):
        super(SpecificationMixin, self).__init__()

    def cannot_be_type(self, diagnostics=None, context=None):
        """self.base_Classifier.extension_Type->isEmpty()"""
        raise NotImplementedError(
            'operation cannot_be_type(...) not yet implemented')


class SubsystemMixin:
    """User defined mixin class for Subsystem."""

    def __init__(self, base_Component=None, **kwargs):
        super(SubsystemMixin, self).__init__()


class TraceMixin:
    """User defined mixin class for Trace."""

    def __init__(self, base_Abstraction=None, **kwargs):
        super(TraceMixin, self).__init__()


class TypeMixin:
    """User defined mixin class for Type."""

    def __init__(self, base_Class=None, **kwargs):
        super(TypeMixin, self).__init__()

    def cannot_be_specification(self, diagnostics=None, context=None):
        """self.base_Class.extension_Specification->isEmpty()"""
        raise NotImplementedError(
            'operation cannot_be_specification(...) not yet implemented')


class UtilityMixin:
    """User defined mixin class for Utility."""

    def __init__(self, base_Class=None, **kwargs):
        super(UtilityMixin, self).__init__()

    def is_utility(self, diagnostics=None, context=None):
        """self.base_Class.feature->forAll(isStatic)"""
        raise NotImplementedError(
            'operation is_utility(...) not yet implemented')


class BuildComponentMixin:
    """User defined mixin class for BuildComponent."""

    def __init__(self, base_Component=None, **kwargs):
        super(BuildComponentMixin, self).__init__()


class MetamodelMixin:
    """User defined mixin class for Metamodel."""

    def __init__(self, base_Model=None, **kwargs):
        super(MetamodelMixin, self).__init__()


class SystemModelMixin:
    """User defined mixin class for SystemModel."""

    def __init__(self, base_Model=None, **kwargs):
        super(SystemModelMixin, self).__init__()


class DocumentMixin:
    """User defined mixin class for Document."""

    def __init__(self, **kwargs):
        super(DocumentMixin, self).__init__(**kwargs)


class ExecutableMixin:
    """User defined mixin class for Executable."""

    def __init__(self, **kwargs):
        super(ExecutableMixin, self).__init__(**kwargs)


class LibraryMixin:
    """User defined mixin class for Library."""

    def __init__(self, **kwargs):
        super(LibraryMixin, self).__init__(**kwargs)


class ScriptMixin:
    """User defined mixin class for Script."""

    def __init__(self, **kwargs):
        super(ScriptMixin, self).__init__(**kwargs)


class SourceMixin:
    """User defined mixin class for Source."""

    def __init__(self, **kwargs):
        super(SourceMixin, self).__init__(**kwargs)
