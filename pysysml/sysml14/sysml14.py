"""Definition of meta model 'sysml14'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
import pysysml.sysml14_mixins as _user_module


name = 'sysml14'
nsURI = 'http://www.eclipse.org/papyrus/sysml/1.4/SysML'
nsPrefix = 'SysML'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
Dummy = EEnum('Dummy', literals=[])
