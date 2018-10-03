"""Definition of meta model 'constraintblocks'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from ..blocks import Block
import pysysml.constraintblocks_mixins as _user_module


name = 'constraintblocks'
nsURI = 'http://www.eclipse.org/papyrus/sysml/1.4/SysML/ConstraintBlocks'
nsPrefix = 'ConstraintBlocks'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class ConstraintBlock(_user_module.ConstraintBlockMixin, Block):
    """
            A constraint block is a block that packages the statement of a constraint so it may be applied in a reusable way to constrain properties of other blocks. A constraint block typically defines one or more constraint parameters, which are bound to properties of other blocks in a surrounding context where the constraint is used. Binding connectors, as defined in Chapter 8: Blocks, are used to bind each parameter of the constraint block to a property in the surrounding context. All properties of a constraint block are constraint parameters, with the exception of constraint properties that hold internally nested usages of other constraint blocks.
          """

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
