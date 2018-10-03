"""Definition of meta model 'types'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'types'
nsURI = 'http://www.eclipse.org/uml2/5.0.0/Types'
nsPrefix = 'types'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)

Boolean = EDataType('Boolean', instanceClassName='boolean')

Integer = EDataType('Integer', instanceClassName='int')

Real = EDataType('Real', instanceClassName='double')

String = EDataType('String', instanceClassName='java.lang.String')

UnlimitedNatural = EDataType('UnlimitedNatural', instanceClassName='int')
