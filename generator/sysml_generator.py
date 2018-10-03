import patch_generator
from pyecore.resources import ResourceSet
import pyecore.ecore as ecore
from pyecoregen.ecore import EcoreGenerator
import sys


def import_pyuml2_types():
    sys.path.append('../pyuml2')


def setup_resourceset():
    import pyuml2.types as types
    import pyuml2.uml as uml
    import pyuml2.standard as standard

    rset = ResourceSet()
    rset.metamodel_registry[types.nsURI] = types
    rset.metamodel_registry[uml.nsURI] = uml
    rset.metamodel_registry[standard.nsURI] = standard
    return rset


def generate_code():
    def format_autopep8(raw: str) -> str:
        import autopep8
        return autopep8.fix_code(raw, options={'experimental': True})

    rset = setup_resourceset()
    sysml_root = rset.get_resource('sysml-resources/sysml.ecore').contents[0]
    generator = EcoreGenerator(user_module='pysysml.sysml_mixins')
    for task in generator.tasks:
        task.formatter = format_autopep8
    generator.generate(sysml_root, 'pysysml')


if __name__ == '__main__':
    import_pyuml2_types()
    generate_code()
