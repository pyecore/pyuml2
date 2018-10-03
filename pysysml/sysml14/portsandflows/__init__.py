
from .portsandflows import getEClassifier, eClassifiers
from .portsandflows import name, nsURI, nsPrefix, eClass
from .portsandflows import FeatureDirection, AcceptChangeStructuralFeatureEventAction, ChangeStructuralFeatureEvent, DirectedFeature, FlowProperty, FullPort, InterfaceBlock, InvocationOnNestedPortAction, ItemFlow, ProxyPort, TriggerOnNestedPort, FlowDirection

from pyuml2.uml import AcceptEventAction, Trigger, Port, Class, ChangeEvent, StructuralFeature, Feature, InvocationAction, InformationFlow, Property, Element

from . import portsandflows
from .. import sysml14


__all__ = ['FeatureDirection', 'AcceptChangeStructuralFeatureEventAction',
           'ChangeStructuralFeatureEvent', 'DirectedFeature', 'FlowProperty',
           'FullPort', 'InterfaceBlock', 'InvocationOnNestedPortAction',
           'ItemFlow', 'ProxyPort', 'TriggerOnNestedPort', 'FlowDirection']

eSubpackages = []
eSuperPackage = sysml14
portsandflows.eSubpackages = eSubpackages
portsandflows.eSuperPackage = eSuperPackage


otherClassifiers = [FeatureDirection, FlowDirection]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
