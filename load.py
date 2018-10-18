from pyecore.resources import ResourceSet
from pyuml2 import profile_utils as utils
import pyuml2.uml as uml
import pyuml2.types as types
import pyuml2.standard as standard
import pysysml.sysml14 as sysml14
import pyecore.ecore as ecore


def get_resourceSet():
    """
    Setup a Resource Set with all the required depencencies to load models
    with Codegen profile applied.
    """
    rset = ResourceSet()
    registry = rset.metamodel_registry

    # register UML metamodel, types metamodel and standard metamodel
    registry[uml.nsURI] = uml
    registry[types.nsURI] = types
    ecore_uri = 'http://www.eclipse.org/uml2/schemas/Ecore/5'
    registry[ecore_uri] = ecore
    registry[standard.nsURI] = standard

    # register UML primitives types
    resource = rset.get_resource('profiles/UMLPrimitiveTypes.library.uml')
    resource.uri = 'pathmap://UML_LIBRARIES/UMLPrimitiveTypes.library.uml'

    # register SysML metamodel (with subpackages)
    registry[sysml14.nsURI] = sysml14
    for subpackage in sysml14.eSubpackages:
        registry[subpackage.nsURI] = subpackage

    # load the tomasys profile and registers the tomasys metamodel
    # (when a profile is 'defined', it creates a metamodel of the profile)
    # it also means that the python code of the tomasys metamodel could be
    # generated. 
    profile_resource = rset.get_resource('tomasys.profile.uml')
    profile = profile_resource.contents[0]
    static = profile.getEAnnotation(utils.UML_20_URI).contents[0]
    registry[static.nsURI] = static

    return rset


def get_application(element, stereotype_name):
    """
    Returns the stereotype application of an element using the stereotype name.
    """
    for o, r in element._inverse_rels:
        if r.name.startswith('base_') and o.eClass.name == stereotype_name:
            return o


def get_applications(element):
    """
    Returns all the stereotype applications applied to an element.
    """
    return [o for o, r in element._inverse_rels if r.name.startswith('base_')]


def print_stereotype_summary(element):
    """
    Displays a summary of the applied stereotypes (shows navigation between)
    an element, the stereotype application and how getting information from the
    meta-structure.
    """
    applications = get_applications(element)
    print('Object', element, 'of type', element.eClass.name)
    print('has', len(applications), 'applied stereotypes:')
    for application in applications:
        print('+- Stereotype', application.eClass.name)
        print('+-- Features:')
        for feature in application.eClass.eStructuralFeatures:
            print('+---', feature.name, 'of type', feature.eType.eClass.name)
            try:
                print('    `- feature value set to:', application.eGet(feature))
            except NotImplementedError:
                print('    `- feature NOT IMPLEMENTED (YET)')

# informat entry point
# load the input model
rset = get_resourceSet()

model_root = rset.get_resource('ux1_submarine_v01.uml').contents[0]

i = 0
for x in model_root.eAllContents():
    print_stereotype_summary(x)
    i = i + 1

print('Nb elements', len(model_root.eResource.contents) + i)
