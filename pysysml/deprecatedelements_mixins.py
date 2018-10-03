"""Mixins to be implemented by user."""


class FlowPortMixin:
    """User defined mixin class for FlowPort."""

    @property
    def isAtomic(self):
        raise NotImplementedError('Missing implementation for isAtomic')

    def __init__(
            self, *, base_Port=None, direction=None, isAtomic=None, **kwargs):
        super().__init__()

    def get_icon(self):

        raise NotImplementedError(
            'operation get_icon(...) not yet implemented')


class FlowSpecificationMixin:
    """User defined mixin class for FlowSpecification."""

    def __init__(self, *, base_Interface=None, **kwargs):
        super().__init__()

    def get_flow_properties(self):

        raise NotImplementedError(
            'operation get_flow_properties(...) not yet implemented')
