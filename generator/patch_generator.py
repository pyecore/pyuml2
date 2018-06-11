"""Monkey patch pythonic_names to get snake name for each EOperation"""
import re
import pyecoregen.adapter
from pyecoregen.adapter import fix_name_clash
import contextlib
import pyecore.ecore as ecore


def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@contextlib.contextmanager
def snake_pythonic_names():
    original_get_attribute = ecore.ENamedElement.__getattribute__

    def get_attribute(self, name):
        value = original_get_attribute(self, name)

        if name == 'name':
            value = fix_name_clash(value)
            if isinstance(self, ecore.EOperation):
                value = to_snake_case(value)

        return value

    ecore.ENamedElement.__getattribute__ = get_attribute
    yield
    ecore.ENamedElement.__getattribute__ = original_get_attribute


pyecoregen.adapter.pythonic_names = snake_pythonic_names
