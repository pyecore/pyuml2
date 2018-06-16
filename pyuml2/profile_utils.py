from pyecore.ecore import EClassifier
from pyecore.innerutils import ignored
from .uml import Element


UML_20_URI = 'http://www.eclipse.org/uml2/2.0.0/UML'


def get_stereotype_from_application(obj):
    eclass = obj.eClass
    for ref in eclass.eAllReferences():
        etype = ref.eType
        if ref.name.startswith('base_') and issubclass(etype, Element):
            return get_stereotype(eclass, obj)


def get_stereotype(definition, application):
    if isinstance(definition, EClassifier):
        with ignored(Exception):
            return definition.getEAnnotation(UML_20_URI).references[0]
