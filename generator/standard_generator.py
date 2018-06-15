import patch_generator
from pyecore.resources import ResourceSet
from pyecoregen.ecore import EcoreGenerator
import sys


def import_pyuml2_types():
    sys.path.append('../pyuml2')


def setup_resourceset():
    import pyuml2.types as types
    import pyuml2.uml as uml

    types_URI = 'platform:/plugin/org.eclipse.uml2.types/model/Types.ecore'
    uml_plateform_URI = 'platform:/plugin/org.eclipse.uml2.uml/model/UML.ecore'

    rset = ResourceSet()
    rset.metamodel_registry[types_URI] = types
    rset.metamodel_registry[uml_plateform_URI] = uml
    return rset


def generate_code():
    def format_autopep8(raw: str) -> str:
        import autopep8
        return autopep8.fix_code(raw, options={'experimental': True})

    rset = setup_resourceset()
    uml_root = rset.get_resource('model/standard.ecore').contents[0]
    generator = EcoreGenerator(user_module='pyuml2.standard_mixins')
    for task in generator.tasks:
        task.formatter = format_autopep8
    generator.generate(uml_root, 'pyuml2')


if __name__ == '__main__':
    import_pyuml2_types()
    generate_code()
