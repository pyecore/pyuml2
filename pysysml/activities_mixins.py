"""Mixins to be implemented by user."""


class RateMixin:
    """User defined mixin class for Rate."""

    def __init__(
            self, *, base_ActivityEdge=None, base_ObjectNode=None,
            base_Parameter=None, rate=None, **kwargs):
        super().__init__()


class ControlOperatorMixin:
    """User defined mixin class for ControlOperator."""

    def __init__(self, *, base_Behavior=None, base_Operation=None, **kwargs):
        super().__init__()


class NoBufferMixin:
    """User defined mixin class for NoBuffer."""

    def __init__(self, *, base_ObjectNode=None, **kwargs):
        super().__init__()


class OptionalMixin:
    """User defined mixin class for Optional."""

    def __init__(self, *, base_Parameter=None, **kwargs):
        super().__init__()


class OverwriteMixin:
    """User defined mixin class for Overwrite."""

    def __init__(self, *, base_ObjectNode=None, **kwargs):
        super().__init__()


class ProbabilityMixin:
    """User defined mixin class for Probability."""

    def __init__(
            self, *, base_ActivityEdge=None, base_ParameterSet=None,
            probability=None, **kwargs):
        super().__init__()


class ContinuousMixin:
    """User defined mixin class for Continuous."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DiscreteMixin:
    """User defined mixin class for Discrete."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
