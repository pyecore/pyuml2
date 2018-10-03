"""Mixins to be implemented by user."""


class AcceptChangeStructuralFeatureEventActionMixin:
    """User defined mixin class for AcceptChangeStructuralFeatureEventAction."""

    def __init__(self, *, base_AcceptEventAction=None, **kwargs):
        super().__init__()


class ChangeStructuralFeatureEventMixin:
    """User defined mixin class for ChangeStructuralFeatureEvent."""

    def __init__(
            self, *, base_ChangeEvent=None, structuralFeature=None, **kwargs):
        super().__init__()


class DirectedFeatureMixin:
    """User defined mixin class for DirectedFeature."""

    def __init__(self, *, base_Feature=None, featureDirection=None, **kwargs):
        super().__init__()


class FlowPropertyMixin:
    """User defined mixin class for FlowProperty."""

    def __init__(self, *, base_Property=None, direction=None, **kwargs):
        super().__init__()

    def get_icon(self):

        raise NotImplementedError(
            'operation get_icon(...) not yet implemented')


class FullPortMixin:
    """User defined mixin class for FullPort."""

    def __init__(self, *, base_Port=None, **kwargs):
        super().__init__()


class ItemFlowMixin:
    """User defined mixin class for ItemFlow."""

    def __init__(
            self, *, base_InformationFlow=None, itemProperty=None, **kwargs):
        super().__init__()


class ProxyPortMixin:
    """User defined mixin class for ProxyPort."""

    def __init__(self, *, base_Port=None, **kwargs):
        super().__init__()


class InterfaceBlockMixin:
    """User defined mixin class for InterfaceBlock."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class InvocationOnNestedPortActionMixin:
    """User defined mixin class for InvocationOnNestedPortAction."""

    def __init__(
            self, *, base_InvocationAction=None, onNestedPort=None, **kwargs):
        super().__init__(**kwargs)


class TriggerOnNestedPortMixin:
    """User defined mixin class for TriggerOnNestedPort."""

    def __init__(self, *, base_Trigger=None, onNestedPort=None, **kwargs):
        super().__init__(**kwargs)
