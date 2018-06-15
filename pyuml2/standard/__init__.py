
from .standard import getEClassifier, eClassifiers
from .standard import name, nsURI, nsPrefix, eClass
from .standard import Auxiliary, Call, Create, Derive, Destroy, Document, File, Entity, Executable, Focus, Framework, Implement, ImplementationClass, Instantiate, Library, Metaclass, ModelLibrary, Process, Realization, Refine, Responsibility, Script, Send, Service, Source, Specification, Subsystem, Trace, Type, Utility, BuildComponent, Metamodel, SystemModel

from ..uml import Class, Classifier, Artifact, Component, Usage, BehavioralFeature, Package, ValueSpecification, Abstraction, Model

from . import standard

__all__ = [
    'Auxiliary', 'Call', 'Create', 'Derive', 'Destroy', 'Document', 'File',
    'Entity', 'Executable', 'Focus', 'Framework', 'Implement',
    'ImplementationClass', 'Instantiate', 'Library', 'Metaclass',
    'ModelLibrary', 'Process', 'Realization', 'Refine', 'Responsibility',
    'Script', 'Send', 'Service', 'Source', 'Specification', 'Subsystem',
    'Trace', 'Type', 'Utility', 'BuildComponent', 'Metamodel', 'SystemModel']

eSubpackages = []
eSuperPackage = None
standard.eSubpackages = eSubpackages
standard.eSuperPackage = eSuperPackage

Auxiliary.base_Class.eType = Class
Call.base_Usage.eType = Usage
Create.base_BehavioralFeature.eType = BehavioralFeature
Create.base_Usage.eType = Usage
Derive.computation.eType = ValueSpecification
Derive.base_Abstraction.eType = Abstraction
Destroy.base_BehavioralFeature.eType = BehavioralFeature
File.base_Artifact.eType = Artifact
Entity.base_Component.eType = Component
Focus.base_Class.eType = Class
Framework.base_Package.eType = Package
Implement.base_Component.eType = Component
ImplementationClass.base_Class.eType = Class
Instantiate.base_Usage.eType = Usage
Metaclass.base_Class.eType = Class
ModelLibrary.base_Package.eType = Package
Process.base_Component.eType = Component
Realization.base_Classifier.eType = Classifier
Refine.base_Abstraction.eType = Abstraction
Responsibility.base_Usage.eType = Usage
Send.base_Usage.eType = Usage
Service.base_Component.eType = Component
Specification.base_Classifier.eType = Classifier
Subsystem.base_Component.eType = Component
Trace.base_Abstraction.eType = Abstraction
Type.base_Class.eType = Class
Utility.base_Class.eType = Class
BuildComponent.base_Component.eType = Component
Metamodel.base_Model.eType = Model
SystemModel.base_Model.eType = Model

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
