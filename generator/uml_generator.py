import patch_generator
from pyecore.resources import ResourceSet
import pyecore.ecore as ecore
from pyecoregen.ecore import EcoreGenerator
import sys


def import_pyuml2_types():
    sys.path.append('../pyuml2')


def setup_resourceset():
    import pyuml2.types as types

    types_URI = 'platform:/plugin/org.eclipse.uml2.types/model/Types.ecore'
    ecore_UML_URI = 'platform:/plugin/org.eclipse.emf.ecore/model/Ecore.ecore'

    rset = ResourceSet()
    rset.metamodel_registry[types_URI] = types
    rset.metamodel_registry[ecore_UML_URI] = ecore
    return rset


def generate_code():
    def format_autopep8(raw: str) -> str:
        import autopep8
        return autopep8.fix_code(raw, options={'experimental': True})

    rset = setup_resourceset()
    uml_root = rset.get_resource('model/uml.ecore').contents[0]
    generator = EcoreGenerator(user_module='pyuml2.uml_mixins')
    for task in generator.tasks:
        task.formatter = format_autopep8
    generator.generate(uml_root, 'pyuml2')


if __name__ == '__main__':
    import_pyuml2_types()
    generate_code()
