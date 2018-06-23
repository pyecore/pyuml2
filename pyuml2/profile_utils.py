from pyecore.ecore import (EClassifier, EAnnotation, EClass,
                           EPackage, EAttribute)
import pyecore.ecore as ecore
from pyecore.innerutils import ignored
from .uml import Element


UML_20_URI = 'http://www.eclipse.org/uml2/2.0.0/UML'
EXTENSION_PREFIX = 'base_'


def patch_ecore_metamodel():
    pass


def get_stereotype_from_application(obj):
    eclass = obj.eClass
    for ref in eclass.eAllReferences():
        if ref.name.startswith(EXTENSION_PREFIX) and \
                issubclass(ref.eType, Element):
            return get_stereotype(eclass, obj)


def get_stereotype(definition, application):
    if isinstance(definition, EClassifier):
        with ignored(Exception):
            return definition.getEAnnotation(UML_20_URI).references[0]


def get_definition_reference_matching(stereotype, element):
    for o, r in stereotype._inverse_rels:
        if r is EAnnotation.references:
            classifier = o.eModelElement
            for reference in classifier.eAllReferences():
                if reference.name.startswith(EXTENSION_PREFIX) and \
                        isinstance(element, reference.eType):
                    return (classifier, reference)
    return (None, None)


def get_application_for(element, definition):
    for o, r in element._inverse_rels:
        if isinstance(o, definition) and r.name.startswith(EXTENSION_PREFIX):
            return o
    return None


def define_profile(profile):
    epackage = _profile2epackage(profile)
    for stereotype in profile.ownedStereotype:
        eclass = _stereotype2eclass(stereotype)
        epackage.eClassifiers.append(eclass)
    return epackage


def _profile2epackage(profile):
    epackage = EPackage(profile.name)
    epackage.nsURI = profile.URI
    epackage.nsPrefix = profile.name
    return epackage


def _stereotype2eclass(stereotype):
    eclass = EClass(stereotype.name)
    eclass.abstract = stereotype.isAbstract
    estruct_append = eclass.eStructuralFeatures.append
    for tvalue in stereotype.ownedAttribute:
        estruct_append(_taggedValue2eattribute(tvalue))
    return eclass


def _taggedValue2eattribute(tvalue):
    eattribute = EAttribute(tvalue.name)
    eattribute.lowerBound = tvalue.lower
    eattribute.upperBound = tvalue.upper
    with ignored(Exception):
        tvalue_type = tvalue.type
        model = tvalue_type.get_model()
        p = get_application_for(model, EPackage)
        metamodel = p.eResource.resource_set.get_resource(p.nsURI).contents[0]
        eattribute.eType = metamodel.getEClassifier(tvalue_type.name)
    return eattribute
