from pyecore.resources import ResourceSet
import pyuml2.uml as uml
import pyuml2.types as types
import pyuml2.standard as standard
import pyecore.ecore as ecore


def get_resourceSet():
    """
    Setup a Resource Set with all the required depencencies to load models
    with Codegen profile applied.
    """
    rset = ResourceSet()

    # register UML metamodel, types metamodel and standard metamodel
    rset.metamodel_registry[uml.nsURI] = uml
    rset.metamodel_registry[types.nsURI] = types
    ecore_uri = 'http://www.eclipse.org/uml2/schemas/Ecore/5'
    rset.metamodel_registry[ecore_uri] = ecore
    rset.metamodel_registry[standard.nsURI] = standard

    # register UML metamodel in a UML format (if required)
    # resource = rset.get_resource('profiles/UML.metamodel.uml')
    # resource.uri = 'pathmap://UML_METAMODELS/UML.metamodel.uml'

    # register UML primitives types
    resource = rset.get_resource('profiles/UMLPrimitiveTypes.library.uml')
    resource.uri = 'pathmap://UML_LIBRARIES/UMLPrimitiveTypes.library.uml'

    # load/register codegen metamodel
    resource = rset.get_resource('codegen-profiles/Codegen.ecore')
    root = resource.contents[0]
    rset.metamodel_registry[root.nsURI] = root

    # load codegen profile (there is some issues with the metamodel/profile binding)
    # resource = rset.get_resource('codegen-profiles/Codegen.profile.uml')
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
            print('+---', feature.name, 'of type', feature.eType.name)
            print('    `- feature value set to:', application.eGet(feature))


# informat entry point
# load the input model
rset = get_resourceSet()
resource = rset.get_resource('testModel.uml')
root = resource.contents[0]


print_stereotype_summary(root.packagedElement[0])
