"""Mixins to be implemented by user."""


class AllocateActivityPartitionMixin:
    """User defined mixin class for AllocateActivityPartition."""

    def __init__(self, *, base_ActivityPartition=None, **kwargs):
        super().__init__()


class AllocateMixin:
    """User defined mixin class for Allocate."""

    def __init__(self, *, base_Abstraction=None, **kwargs):
        super().__init__(**kwargs)

    def get_allocated_from(self, ref=None, result=None):

        raise NotImplementedError(
            'operation get_allocated_from(...) not yet implemented')

    def get_allocated_to(self, ref=None, result=None):

        raise NotImplementedError(
            'operation get_allocated_to(...) not yet implemented')
