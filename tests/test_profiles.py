import pytest
from os import path
from pyecore.resources import ResourceSet

import pyecore.ecore as ecore
import pyuml2.types as types
import pyuml2.uml as uml
import pyuml2.standard as standard

import pyuml2.profile_utils as utils


@pytest.fixture
def rset():
    rset = ResourceSet()
    rset.metamodel_registry[types.nsURI] = types
    rset.metamodel_registry[uml.nsURI] = uml
    ecore_uri = 'http://www.eclipse.org/uml2/schemas/Ecore/5'
    rset.metamodel_registry[ecore_uri] = ecore
    rset.metamodel_registry[standard.nsURI] = standard
    return rset


def test_class_ismetaclass(rset):
    mm_file = path.join('profiles', 'UML.metamodel.uml')
    uml_resource = rset.get_resource(mm_file)
    uml_root = uml_resource.contents[0]
    for o in uml_root.packagedElement:
        if isinstance(o, uml.Class):
            assert o.is_metaclass() is True


def test_package_ownedstereotype(rset):
    # uml_resource = rset.get_resource('profiles/UML.metamodel.uml')
    profile_file = path.join('profiles', 'Standard.profile.uml')
    standard_prof_resource = rset.get_resource(profile_file)
    standard_prof = standard_prof_resource.contents[0]

    assert len(standard_prof.ownedStereotype) > 0
    assert len(standard_prof.get_owned_stereotypes()) > 0

    stereotypes = [x for x in standard_prof.packagedElement
                   if isinstance(x, uml.Stereotype)]
    for stereotype in stereotypes:
        assert stereotype in standard_prof.ownedStereotype


def test_utils_get_stereotypefromapplication(rset):
    profile_file = path.join('tests', 'profiles', 'testProfile.profile.uml')
    profile_resource = rset.get_resource(profile_file)
    profile = profile_resource.contents[0]
    static = profile.getEAnnotation(utils.UML_20_URI).contents[0]
    rset.metamodel_registry[static.nsURI] = static

    applied_file = path.join('tests', 'profiles', 'applied.uml')
    applied_resource = rset.get_resource(applied_file)
    stereotype_application = applied_resource.contents[-1]
    stereotype = utils.get_stereotype_from_application(stereotype_application)

    assert stereotype is profile.packagedElement[0]


def test_element_get_appliedstereotypes(rset):
    profile_file = path.join('tests', 'profiles', 'testProfile.profile.uml')
    profile_resource = rset.get_resource(profile_file)
    profile = profile_resource.contents[0]
    static = profile.getEAnnotation(utils.UML_20_URI).contents[0]
    rset.metamodel_registry[static.nsURI] = static

    applied_file = path.join('tests', 'profiles', 'applied.uml')
    applied_resource = rset.get_resource(applied_file)
    applied_root = applied_resource.contents[0]

    c = applied_root.packagedElement[0]
    assert len(c.get_applied_stereotypes()) == 1

    stereotype = profile.packagedElement[0]
    assert stereotype in c.get_applied_stereotypes()


def test_element_get_appliedstereotypes_deserialized_profile(rset):
    profile_file = path.join('tests', 'profiles', 'testProfile.profile.uml')
    profile_resource = rset.get_resource(profile_file)
    profile = profile_resource.contents[0]

    applied_file = path.join('tests', 'profiles', 'applied.uml')
    applied_resource = rset.get_resource(applied_file)
    applied_root = applied_resource.contents[0]

    c = applied_root.packagedElement[0]
    assert len(c.get_applied_stereotypes()) == 1

    stereotype = profile.packagedElement[0]
    assert stereotype in c.get_applied_stereotypes()


def test_element_get_appliedstereotypes_schema_location(rset):
    applied_file = path.join('tests', 'profiles', 'applied.uml')
    applied_resource = rset.get_resource(applied_file)
    applied_root = applied_resource.contents[0]

    c = applied_root.packagedElement[0]
    assert len(c.get_applied_stereotypes()) == 1

    stereotype = c.get_applied_stereotypes()[0]
    assert stereotype.name == "FirstStereotype"
    assert isinstance(stereotype, uml.Stereotype)
    assert stereotype.qualifiedName == 'testProfile::FirstStereotype'

    t_value = stereotype.ownedAttribute[1]
    assert t_value.qualifiedName == 'testProfile::FirstStereotype::newName'


def test_element_get_appliedstereotype_qualifiedName(rset):
    applied_file = path.join('tests', 'profiles', 'applied.uml')
    applied_resource = rset.get_resource(applied_file)
    applied_root = applied_resource.contents[0]

    c = applied_root.packagedElement[0]
    assert len(c.get_applied_stereotypes()) == 1

    stereotype = c.get_applied_stereotype('testProfile::FirstStereotype')

    assert stereotype.name == "FirstStereotype"
    assert isinstance(stereotype, uml.Stereotype)
    assert stereotype.qualifiedName == 'testProfile::FirstStereotype'

    assert c.get_applied_stereotype('testProfile::FirstStereotypeAA') is None


def test_element_get_stereotypeapplications(rset):
    profile_file = path.join('tests', 'profiles', 'testProfile.profile.uml')
    profile_resource = rset.get_resource(profile_file)
    profile = profile_resource.contents[0]
    static = profile.getEAnnotation(utils.UML_20_URI).contents[0]
    rset.metamodel_registry[static.nsURI] = static

    applied_file = path.join('tests', 'profiles', 'applied.uml')
    applied_resource = rset.get_resource(applied_file)
    applied_root = applied_resource.contents[0]

    c = applied_root.packagedElement[0]
    assert len(c.get_stereotype_applications()) == 1
    assert c.get_stereotype_applications()


def test_element_get_stereotypeapplications_deserialized_profile(rset):
    profile_file = path.join('tests', 'profiles', 'testProfile.profile.uml')
    rset.get_resource(profile_file)

    applied_file = path.join('tests', 'profiles', 'applied.uml')
    applied_resource = rset.get_resource(applied_file)
    applied_root = applied_resource.contents[0]

    c = applied_root.packagedElement[0]
    assert len(c.get_stereotype_applications()) == 1
    assert c.get_stereotype_applications()
