# -*- coding: utf-8 -*-
"""Mixins to be implemented by user."""

import pyecore.ecore as ecore
from pyecore.ecore import EDerivedCollection
from pyecore.valuecontainer import EcoreUtils, BadValueError
from pyecore.innerutils import ignored


def check(value, etype):
    if not EcoreUtils.isinstance(value, etype):
        raise BadValueError(value, etype)


class ActivityContentMixin(object):
    """User defined mixin class for ActivityContent."""

    def __init__(self, **kwargs):
        super(ActivityContentMixin, self).__init__()

    def containing_activity(self):

        raise NotImplementedError(
            'operation containing_activity(...) not yet implemented')


class DerivedOwnedelement(EDerivedCollection):
    def __len__(self):
        return len(self.owner.eContents)

    def __contains__(self, x):
        return x in self.owner.eContents

    def __iter__(self):
        return iter(self.owner.eContents)

    def __repr__(self):
        return repr(self.owner.eContents)


class ElementMixin(object):
    """User defined mixin class for Element."""

    @property
    def owner(self):
        return self.eContainer()

    def __init__(
            self, ownedComment=None, ownedElement=None, owner=None, **
            kwargs):
        super(ElementMixin, self).__init__(**kwargs)

    def has_owner(self, diagnostics=None, context=None):
        """Elements that must be owned must have an owner.
mustBeOwned() implies owner->notEmpty()"""
        return self.owner is not None

    def not_own_self(self, diagnostics=None, context=None):
        """An element may not directly or indirectly own itself.
not allOwnedElements()->includes(self)"""
        return self not in self.all_owned_elements()

    def add_keyword(self, keyword=None):
        """Adds the specified keyword to this element."""
        raise NotImplementedError(
            'operation add_keyword(...) not yet implemented')

    def apply_stereotype(self, stereotype):
        """Applies the specified stereotype to this element."""
        from .profile_utils import get_definition_reference_matching
        gdrm = get_definition_reference_matching
        definition, base_reference = gdrm(stereotype, self)
        if definition is None:
            return
        application = definition()
        setattr(application, base_reference.name, self)
        self.eResource.append(application)

    def create_EAnnotation(self, source=None):
        """Creates an annotation with the specified source and this element as its model element."""
        annotation = ecore.EAnnotation(source=source)
        self.eAnnotations.append(annotation)
        return annotation

    def destroy(self):
        """Destroys this element by removing all cross references to/from it and removing it from its containing resource or object."""
        self.delete()

    def get_keywords(self):
        """Retrieves the keywords for this element."""
        raise NotImplementedError(
            'operation get_keywords(...) not yet implemented')

    def get_applicable_stereotype(self, qualifiedName=None):
        """Retrieves the stereotype with the specified qualified name that is applicable to this element, or null if no such stereotype is applicable."""
        raise NotImplementedError(
            'operation get_applicable_stereotype(...) not yet implemented')

    def get_applicable_stereotypes(self):
        """Retrieves the stereotypes that are applicable to this element, including those that are required and/or may already be applied."""
        raise NotImplementedError(
            'operation get_applicable_stereotypes(...) not yet implemented')

    def get_applied_stereotype(self, qualifiedName):
        """Retrieves the stereotype with the specified qualified name that is applied to this element, or null if no such stereotype is  applied."""
        from .profile_utils import get_stereotype_from_application
        for o, r in self._inverse_rels:
            if r.name.startswith('base_'):
                stereotype = get_stereotype_from_application(o)
                with ignored(Exception):
                    if stereotype.qualifiedName == qualifiedName:
                        return stereotype
        return None

    def get_applied_stereotypes(self):
        """Retrieves the stereotypes that are applied to this element."""
        from .profile_utils import get_stereotype_from_application
        result = set()
        for o, r in self._inverse_rels:
            if r.name.startswith('base_'):
                stereotype = get_stereotype_from_application(o)
                if stereotype:
                    result.add(stereotype)
        return tuple(result)

    def get_applied_substereotype(self, stereotype=None, qualifiedName=None):
        """Retrieves the substereotype of the specified stereotype with the specified qualified name that is applied to this element, or null if no such stereotype is applied."""
        raise NotImplementedError(
            'operation get_applied_substereotype(...) not yet implemented')

    def get_applied_substereotypes(self, stereotype=None):
        """Retrieves the substereotypes of the specified stereotype that are applied to this element."""
        raise NotImplementedError(
            'operation get_applied_substereotypes(...) not yet implemented')

    def get_model(self):
        """Retrieves the model that owns (either directly or indirectly) this element."""
        from .uml import Model
        parent = self.eContainer()
        while parent is not None and not isinstance(parent, Model):
            parent = parent.eContainer()
        return parent

    def get_nearest_package(self):
        """Retrieves the nearest package that owns (either directly or indirectly) this element, or the element itself (if it is a package)."""
        from .uml import Package
        parent = self.eContainer()
        while parent is not None and not isinstance(parent, Package):
            parent = parent.eContainer()
        return parent

    def get_relationships(self):
        """Retrieves the relationships in which this element is involved."""
        raise NotImplementedError(
            'operation get_relationships(...) not yet implemented')

    def get_relationships(self, eClass=None):
        """Retrieves the relationships of the specified type in which this element is involved."""
        raise NotImplementedError(
            'operation get_relationships(...) not yet implemented')

    def get_required_stereotype(self, qualifiedName=None):
        """Retrieves the stereotype with the specified qualified name that is required for this element, or null if no such stereotype is required."""
        raise NotImplementedError(
            'operation get_required_stereotype(...) not yet implemented')

    def get_required_stereotypes(self):
        """Retrieves the stereotypes that are required for this element."""
        raise NotImplementedError(
            'operation get_required_stereotypes(...) not yet implemented')

    def get_source_directed_relationships(self):
        """Retrieves the directed relationships for which this element is a source."""
        raise NotImplementedError(
            'operation get_source_directed_relationships(...) not yet implemented')

    def get_source_directed_relationships(self, eClass=None):
        """Retrieves the directed relationships of the specified type for which this element is a source."""
        raise NotImplementedError(
            'operation get_source_directed_relationships(...) not yet implemented')

    def get_stereotype_application(self, stereotype=None):
        """Retrieves the application of the specified stereotype for this element, or null if no such stereotype application exists."""
        raise NotImplementedError(
            'operation get_stereotype_application(...) not yet implemented')

    def get_stereotype_applications(self):
        """Retrieves the stereotype applications for this element."""
        from .profile_utils import get_stereotype_from_application
        return tuple(o for o, r in self._inverse_rels
                     if r.name.startswith('base_') and
                     get_stereotype_from_application(o))

    def get_target_directed_relationships(self):
        """Retrieves the directed relationships for which this element is a target."""
        raise NotImplementedError(
            'operation get_target_directed_relationships(...) not yet implemented')

    def get_target_directed_relationships(self, eClass=None):
        """Retrieves the directed relationships of the specified type for which this element is a target."""
        raise NotImplementedError(
            'operation get_target_directed_relationships(...) not yet implemented')

    def get_value(self, stereotype=None, propertyName=None):
        """Retrieves the value of the property with the specified name in the specified stereotype for this element."""
        raise NotImplementedError(
            'operation get_value(...) not yet implemented')

    def has_keyword(self, keyword=None):
        """Determines whether this element has the specified keyword."""
        raise NotImplementedError(
            'operation has_keyword(...) not yet implemented')

    def has_value(self, stereotype=None, propertyName=None):
        """Determines whether this element has a (non-default) value for the property with the specified name in the specified stereotype."""
        raise NotImplementedError(
            'operation has_value(...) not yet implemented')

    def is_stereotype_applicable(self, stereotype=None):
        """Determines whether the specified stereotype is applicable to this element."""
        raise NotImplementedError(
            'operation is_stereotype_applicable(...) not yet implemented')

    def is_stereotype_applied(self, stereotype=None):
        """Determines whether the specified stereotype is applied to this element."""
        stereotype = self.get_applied_stereotype(stereotype.qualifiedName)
        return stereotype is not None

    def is_stereotype_required(self, stereotype=None):
        """Determines whether the specified stereotype is required for this element."""
        raise NotImplementedError(
            'operation is_stereotype_required(...) not yet implemented')

    def remove_keyword(self, keyword=None):
        """Removes the specified keyword from this element."""
        raise NotImplementedError(
            'operation remove_keyword(...) not yet implemented')

    def set_value(self, stereotype=None, propertyName=None, newValue=None):
        """Sets the value of the property with the specified name in the specified stereotype for this element."""
        raise NotImplementedError(
            'operation set_value(...) not yet implemented')

    def unapply_stereotype(self, stereotype=None):
        """Unapplies the specified stereotype from this element."""
        raise NotImplementedError(
            'operation unapply_stereotype(...) not yet implemented')

    def all_owned_elements(self):
        """The query allOwnedElements() gives all of the direct and indirect ownedElements of an Element.
result = (ownedElement->union(ownedElement->collect(e | e.allOwnedElements()))->asSet())
<p>From package UML::CommonStructure.</p>"""
        return self.eAllContents()

    def must_be_owned(self):
        """The query mustBeOwned() indicates whether Elements of this type must have an owner. Subclasses of Element that do not require an owner must override this operation.
result = (true)
<p>From package UML::CommonStructure.</p>"""
        return True


class DerivedClientdependency(EDerivedCollection):
    pass


class NamedElementMixin(object):
    """User defined mixin class for NamedElement."""

    @property
    def namespace(self):
        raise NotImplementedError('Missing implementation for namespace')

    @property
    def qualifiedName(self):
        qualified_name = self.name
        element = self
        separator = self.separator()
        while element.eContainer():
            element = element.eContainer()
            qualified_name = element.name + separator + qualified_name
        return qualified_name

    def __init__(self, clientDependency=None, name=None,
                 nameExpression=None, namespace=None, qualifiedName=None,
                 visibility=None, **kwargs):
        super(NamedElementMixin, self).__init__(**kwargs)

    def visibility_needs_ownership(self, diagnostics=None, context=None):
        """If a NamedElement is owned by something other than a Namespace, it does not have a visibility. One that is not owned by anything (and hence must be a Package, as this is the only kind of NamedElement that overrides mustBeOwned()) may have a visibility.
(namespace = null and owner <> null) implies visibility = null"""
        raise NotImplementedError(
            'operation visibility_needs_ownership(...) not yet implemented')

    def has_qualified_name(self, diagnostics=None, context=None):
        """When there is a name, and all of the containing Namespaces have a name, the qualifiedName is constructed from the name of the NamedElement and the names of the containing Namespaces.
(name <> null and allNamespaces()->select(ns | ns.name = null)->isEmpty()) implies
  qualifiedName = allNamespaces()->iterate( ns : Namespace; agg: String = name | ns.name.concat(self.separator()).concat(agg))"""
        raise NotImplementedError(
            'operation has_qualified_name(...) not yet implemented')

    def has_no_qualified_name(self, diagnostics=None, context=None):
        """If there is no name, or one of the containing Namespaces has no name, there is no qualifiedName.
name=null or allNamespaces()->select( ns | ns.name=null )->notEmpty() implies qualifiedName = null"""
        raise NotImplementedError(
            'operation has_no_qualified_name(...) not yet implemented')

    def create_dependency(self, supplier=None):
        """Creates a dependency between this named element and the specified supplier, owned by this named element's nearest package."""
        raise NotImplementedError(
            'operation create_dependency(...) not yet implemented')

    def create_usage(self, supplier=None):
        """Creates a usage between this named element and the specified supplier, owned by this named element's nearest package."""
        raise NotImplementedError(
            'operation create_usage(...) not yet implemented')

    def get_label(self):
        """Retrieves a localized label for this named element."""
        raise NotImplementedError(
            'operation get_label(...) not yet implemented')

    def get_label(self, localize=None):
        """Retrieves a label for this named element, localized if indicated."""
        raise NotImplementedError(
            'operation get_label(...) not yet implemented')

    def get_namespace(self):

        raise NotImplementedError(
            'operation get_namespace(...) not yet implemented')

    def all_namespaces(self):
        """The query allNamespaces() gives the sequence of Namespaces in which the NamedElement is nested, working outwards.
result = (
if owner = null
  then OrderedSet{}
else
  let enclosingNamespace : Namespace =
    if owner.oclIsKindOf(TemplateParameter) and owner.oclAsType(TemplateParameter).signature.template.oclIsKindOf(Namespace)
      then owner.oclAsType(TemplateParameter).signature.template.oclAsType(Namespace)
    else
      namespace
    endif
  in enclosingNamespace.allNamespaces()->prepend(enclosingNamespace)
endif)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation all_namespaces(...) not yet implemented')

    def all_owning_packages(self):
        """The query allOwningPackages() returns the set of all the enclosing Namespaces of this NamedElement, working outwards, that are Packages, up to but not including the first such Namespace that is not a Package.
result = (if namespace.oclIsKindOf(Package)
then
  let owningPackage : Package = namespace.oclAsType(Package) in
    owningPackage->union(owningPackage.allOwningPackages())
else
  null
endif)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation all_owning_packages(...) not yet implemented')

    def is_distinguishable_from(self, n=None, ns=None):
        """The query isDistinguishableFrom() determines whether two NamedElements may logically co-exist within a Namespace. By default, two named elements are distinguishable if (a) they have types neither of which is a kind of the other or (b) they have different names.
result = ((self.oclIsKindOf(n.oclType()) or n.oclIsKindOf(self.oclType())) implies
    ns.getNamesOfMember(self)->intersection(ns.getNamesOfMember(n))->isEmpty()
)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation is_distinguishable_from(...) not yet implemented')

    def get_qualified_name(self):
        """When a NamedElement has a name, and all of its containing Namespaces have a name, the qualifiedName is constructed from the name of the NamedElement and the names of the containing Namespaces.
result = (if self.name <> null and self.allNamespaces()->select( ns | ns.name=null )->isEmpty()
then
    self.allNamespaces()->iterate( ns : Namespace; agg: String = self.name | ns.name.concat(self.separator()).concat(agg))
else
   null
endif)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation get_qualified_name(...) not yet implemented')

    def separator(self):
        """The query separator() gives the string that is used to separate names when constructing a qualifiedName.
result = ('::')
<p>From package UML::CommonStructure.</p>"""
        return '::'

    def get_client_dependencies(self):
        """result = (Dependency.allInstances()->select(d | d.client->includes(self)))
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation get_client_dependencies(...) not yet implemented')


class CommentMixin(object):
    """User defined mixin class for Comment."""

    def __init__(self, annotatedElement=None, body=None, **kwargs):
        super(CommentMixin, self).__init__(**kwargs)


class ImageMixin(object):
    """User defined mixin class for Image."""

    def __init__(self, content=None, format=None, location=None, **kwargs):
        super(ImageMixin, self).__init__(**kwargs)


class ParameterableElementMixin(object):
    """User defined mixin class for ParameterableElement."""

    def __init__(
            self, owningTemplateParameter=None, templateParameter=None, **
            kwargs):
        super(ParameterableElementMixin, self).__init__(**kwargs)

    def is_compatible_with(self, p=None):
        """The query isCompatibleWith() determines if this ParameterableElement is compatible with the specified ParameterableElement. By default, this ParameterableElement is compatible with another ParameterableElement p if the kind of this ParameterableElement is the same as or a subtype of the kind of p. Subclasses of ParameterableElement should override this operation to specify different compatibility constraints.
result = (self.oclIsKindOf(p.oclType()))
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation is_compatible_with(...) not yet implemented')

    def is_template_parameter(self):
        """The query isTemplateParameter() determines if this ParameterableElement is exposed as a formal TemplateParameter.
result = (templateParameter->notEmpty())
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation is_template_parameter(...) not yet implemented')


class TemplateParameterMixin(object):
    """User defined mixin class for TemplateParameter."""

    def __init__(self, default=None, ownedDefault=None,
                 parameteredElement=None, signature=None,
                 ownedParameteredElement=None, **kwargs):
        super(TemplateParameterMixin, self).__init__(**kwargs)

    def must_be_compatible(self, diagnostics=None, context=None):
        """The default must be compatible with the formal TemplateParameter.
default <> null implies default.isCompatibleWith(parameteredElement)"""
        raise NotImplementedError(
            'operation must_be_compatible(...) not yet implemented')


class TemplateSignatureMixin(object):
    """User defined mixin class for TemplateSignature."""

    def __init__(
            self, parameter=None, template=None, ownedParameter=None, **
            kwargs):
        super(TemplateSignatureMixin, self).__init__(**kwargs)

    def own_elements(self, diagnostics=None, context=None):
        """Parameters must own the ParameterableElements they parameter or those ParameterableElements must be owned by the TemplateableElement being templated.
template.ownedElement->includesAll(parameter.parameteredElement->asSet() - parameter.ownedParameteredElement->asSet())"""
        raise NotImplementedError(
            'operation own_elements(...) not yet implemented')

    def unique_parameters(self, diagnostics=None, context=None):
        """The names of the parameters of a TemplateSignature are unique.
parameter->forAll( p1, p2 | (p1 <> p2 and p1.parameteredElement.oclIsKindOf(NamedElement) and p2.parameteredElement.oclIsKindOf(NamedElement) ) implies
   p1.parameteredElement.oclAsType(NamedElement).name <> p2.parameteredElement.oclAsType(NamedElement).name)"""
        raise NotImplementedError(
            'operation unique_parameters(...) not yet implemented')


class TemplateableElementMixin(object):
    """User defined mixin class for TemplateableElement."""

    def __init__(
            self, templateBinding=None, ownedTemplateSignature=None, **
            kwargs):
        super(TemplateableElementMixin, self).__init__(**kwargs)

    def is_template(self):
        """The query isTemplate() returns whether this TemplateableElement is actually a template.
result = (ownedTemplateSignature <> null)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation is_template(...) not yet implemented')

    def parameterable_elements(self):
        """The query parameterableElements() returns the set of ParameterableElements that may be used as the parameteredElements for a TemplateParameter of this TemplateableElement. By default, this set includes all the ownedElements. Subclasses may override this operation if they choose to restrict the set of ParameterableElements.
result = (self.allOwnedElements()->select(oclIsKindOf(ParameterableElement)).oclAsType(ParameterableElement)->asSet())
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation parameterable_elements(...) not yet implemented')


class DerivedRelatedelement(EDerivedCollection):
    pass


class RelationshipMixin(object):
    """User defined mixin class for Relationship."""

    def __init__(self, relatedElement=None, **kwargs):
        super(RelationshipMixin, self).__init__(**kwargs)


class TemplateParameterSubstitutionMixin(object):
    """User defined mixin class for TemplateParameterSubstitution."""

    def __init__(
            self, actual=None, formal=None, ownedActual=None,
            templateBinding=None, **kwargs):
        super(TemplateParameterSubstitutionMixin, self).__init__(**kwargs)

    def must_be_compatible(self, diagnostics=None, context=None):
        """The actual ParameterableElement must be compatible with the formal TemplateParameter, e.g., the actual ParameterableElement for a Class TemplateParameter must be a Class.
actual->forAll(a | a.isCompatibleWith(formal.parameteredElement))"""
        raise NotImplementedError(
            'operation must_be_compatible(...) not yet implemented')


class MultiplicityElementMixin(object):
    """User defined mixin class for MultiplicityElement."""

    @property
    def lower(self):
        return self._lower

    @lower.setter
    def lower(self, value):
        self._lower = value

    @property
    def upper(self):
        return self._upper

    @upper.setter
    def upper(self, value):
        self._upper = value

    def __init__(self, isOrdered=None, isUnique=None, lower=None,
                 lowerValue=None, upper=None, upperValue=None, **kwargs):
        super(MultiplicityElementMixin, self).__init__(**kwargs)

    def upper_ge_lower(self, diagnostics=None, context=None):
        """The upper bound must be greater than or equal to the lower bound.
upperBound() >= lowerBound()"""
        raise NotImplementedError(
            'operation upper_ge_lower(...) not yet implemented')

    def lower_ge_0(self, diagnostics=None, context=None):
        """The lower bound must be a non-negative integer literal.
lowerBound() >= 0"""
        raise NotImplementedError(
            'operation lower_ge_0(...) not yet implemented')

    def value_specification_no_side_effects(
            self, diagnostics=None, context=None):
        """If a non-literal ValueSpecification is used for lowerValue or upperValue, then evaluating that specification must not have side effects."""
        raise NotImplementedError(
            'operation value_specification_no_side_effects(...) not yet implemented')

    def value_specification_constant(self, diagnostics=None, context=None):
        """If a non-literal ValueSpecification is used for lowerValue or upperValue, then that specification must be a constant expression."""
        raise NotImplementedError(
            'operation value_specification_constant(...) not yet implemented')

    def lower_is_integer(self, diagnostics=None, context=None):
        """If it is not empty, then lowerValue must have an Integer value.
lowerValue <> null implies lowerValue.integerValue() <> null"""
        raise NotImplementedError(
            'operation lower_is_integer(...) not yet implemented')

    def upper_is_unlimited_natural(self, diagnostics=None, context=None):
        """If it is not empty, then upperValue must have an UnlimitedNatural value.
upperValue <> null implies upperValue.unlimitedValue() <> null"""
        raise NotImplementedError(
            'operation upper_is_unlimited_natural(...) not yet implemented')

    def set_lower(self, newLower=None):

        raise NotImplementedError(
            'operation set_lower(...) not yet implemented')

    def set_upper(self, newUpper=None):

        raise NotImplementedError(
            'operation set_upper(...) not yet implemented')

    def compatible_with(self, other=None):
        """The operation compatibleWith takes another multiplicity as input. It returns true if the other multiplicity is wider than, or the same as, self.
result = ((other.lowerBound() <= self.lowerBound()) and ((other.upperBound() = *) or (self.upperBound() <= other.upperBound())))
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation compatible_with(...) not yet implemented')

    def includes_multiplicity(self, M=None):
        """The query includesMultiplicity() checks whether this multiplicity includes all the cardinalities allowed by the specified multiplicity.
self.upperBound()->notEmpty() and self.lowerBound()->notEmpty() and M.upperBound()->notEmpty() and M.lowerBound()->notEmpty()
result = ((self.lowerBound() <= M.lowerBound()) and (self.upperBound() >= M.upperBound()))
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation includes_multiplicity(...) not yet implemented')

    def is_(self, lowerbound=None, upperbound=None):
        """The operation is determines if the upper and lower bound of the ranges are the ones given.
result = (lowerbound = self.lowerBound() and upperbound = self.upperBound())
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError('operation is_(...) not yet implemented')

    def is_multivalued(self):
        """The query isMultivalued() checks whether this multiplicity has an upper bound greater than one.
upperBound()->notEmpty()
result = (upperBound() > 1)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation is_multivalued(...) not yet implemented')

    def get_lower(self):
        """The derived lower attribute must equal the lowerBound.
result = (lowerBound())
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation get_lower(...) not yet implemented')

    def lower_bound(self):
        """The query lowerBound() returns the lower bound of the multiplicity as an integer, which is the integerValue of lowerValue, if this is given, and 1 otherwise.
result = (if (lowerValue=null or lowerValue.integerValue()=null) then 1 else lowerValue.integerValue() endif)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation lower_bound(...) not yet implemented')

    def get_upper(self):
        """The derived upper attribute must equal the upperBound.
result = (upperBound())
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation get_upper(...) not yet implemented')

    def upper_bound(self):
        """The query upperBound() returns the upper bound of the multiplicity for a bounded multiplicity as an unlimited natural, which is the unlimitedNaturalValue of upperValue, if given, and 1, otherwise.
result = (if (upperValue=null or upperValue.unlimitedValue()=null) then 1 else upperValue.unlimitedValue() endif)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation upper_bound(...) not yet implemented')


class SlotMixin(object):
    """User defined mixin class for Slot."""

    def __init__(self, definingFeature=None, value=None,
                 owningInstance=None, **kwargs):
        super(SlotMixin, self).__init__(**kwargs)


class ExceptionHandlerMixin(object):
    """User defined mixin class for ExceptionHandler."""

    def __init__(self, exceptionInput=None, exceptionType=None,
                 handlerBody=None, protectedNode=None, **kwargs):
        super(ExceptionHandlerMixin, self).__init__(**kwargs)

    def handler_body_edges(self, diagnostics=None, context=None):
        """The handlerBody has no incoming or outgoing ActivityEdges and the exceptionInput has no incoming ActivityEdges.
handlerBody.incoming->isEmpty() and handlerBody.outgoing->isEmpty() and exceptionInput.incoming->isEmpty()"""
        raise NotImplementedError(
            'operation handler_body_edges(...) not yet implemented')

    def output_pins(self, diagnostics=None, context=None):
        """If the protectedNode is an Action with OutputPins, then the handlerBody must also be an Action with the same number of OutputPins, which are compatible in type, ordering, and multiplicity to those of the protectedNode.
(protectedNode.oclIsKindOf(Action) and protectedNode.oclAsType(Action).output->notEmpty()) implies
(
  handlerBody.oclIsKindOf(Action) and
  let protectedNodeOutput : OrderedSet(OutputPin) = protectedNode.oclAsType(Action).output,
        handlerBodyOutput : OrderedSet(OutputPin) =  handlerBody.oclAsType(Action).output in
    protectedNodeOutput->size() = handlerBodyOutput->size() and
    Sequence{1..protectedNodeOutput->size()}->forAll(i |
        handlerBodyOutput->at(i).type.conformsTo(protectedNodeOutput->at(i).type) and
        handlerBodyOutput->at(i).isOrdered=protectedNodeOutput->at(i).isOrdered and
        handlerBodyOutput->at(i).compatibleWith(protectedNodeOutput->at(i)))
)"""
        raise NotImplementedError(
            'operation output_pins(...) not yet implemented')

    def one_input(self, diagnostics=None, context=None):
        """The handlerBody is an Action with one InputPin, and that InputPin is the same as the exceptionInput.
handlerBody.oclIsKindOf(Action) and
let inputs: OrderedSet(InputPin) = handlerBody.oclAsType(Action).input in
inputs->size()=1 and inputs->first()=exceptionInput"""
        raise NotImplementedError(
            'operation one_input(...) not yet implemented')

    def edge_source_target(self, diagnostics=None, context=None):
        """An ActivityEdge that has a source within the handlerBody of an ExceptionHandler must have its target in the handlerBody also, and vice versa.
let nodes:Set(ActivityNode) = handlerBody.oclAsType(Action).allOwnedNodes() in
nodes.outgoing->forAll(nodes->includes(target)) and
nodes.incoming->forAll(nodes->includes(source))"""
        raise NotImplementedError(
            'operation edge_source_target(...) not yet implemented')

    def handler_body_owner(self, diagnostics=None, context=None):
        """The handlerBody must have the same owner as the protectedNode.
handlerBody.owner=protectedNode.owner"""
        raise NotImplementedError(
            'operation handler_body_owner(...) not yet implemented')

    def exception_input_type(self, diagnostics=None, context=None):
        """The exceptionInput must either have no type or every exceptionType must conform to the exceptionInput type.
exceptionInput.type=null or
exceptionType->forAll(conformsTo(exceptionInput.type.oclAsType(Classifier)))"""
        raise NotImplementedError(
            'operation exception_input_type(...) not yet implemented')


class LinkEndDataMixin(object):
    """User defined mixin class for LinkEndData."""

    def __init__(self, end=None, qualifier=None, value=None, **kwargs):
        super(LinkEndDataMixin, self).__init__(**kwargs)

    def same_type(self, diagnostics=None, context=None):
        """The type of the value InputPin conforms to the type of the Association end.
value<>null implies value.type.conformsTo(end.type)"""
        raise NotImplementedError(
            'operation same_type(...) not yet implemented')

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the value InputPin must be 1..1.
value<>null implies value.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def end_object_input_pin(self, diagnostics=None, context=None):
        """The value InputPin is not also the qualifier value InputPin.
value->excludesAll(qualifier.value)"""
        raise NotImplementedError(
            'operation end_object_input_pin(...) not yet implemented')

    def property_is_association_end(self, diagnostics=None, context=None):
        """The Property must be an Association memberEnd.
end.association <> null"""
        raise NotImplementedError(
            'operation property_is_association_end(...) not yet implemented')

    def qualifiers(self, diagnostics=None, context=None):
        """The qualifiers must be qualifiers of the Association end.
end.qualifier->includesAll(qualifier.qualifier)"""
        raise NotImplementedError(
            'operation qualifiers(...) not yet implemented')

    def all_pins(self):
        """Returns all the InputPins referenced by this LinkEndData. By default this includes the value and qualifier InputPins, but subclasses may override the operation to add other InputPins.
result = (value->asBag()->union(qualifier.value))
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation all_pins(...) not yet implemented')


class QualifierValueMixin(object):
    """User defined mixin class for QualifierValue."""

    def __init__(self, qualifier=None, value=None, **kwargs):
        super(QualifierValueMixin, self).__init__(**kwargs)

    def multiplicity_of_qualifier(self, diagnostics=None, context=None):
        """The multiplicity of the value InputPin is 1..1.
value.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_qualifier(...) not yet implemented')

    def type_of_qualifier(self, diagnostics=None, context=None):
        """The type of the value InputPin conforms to the type of the qualifier Property.
value.type.conformsTo(qualifier.type)"""
        raise NotImplementedError(
            'operation type_of_qualifier(...) not yet implemented')

    def qualifier_attribute(self, diagnostics=None, context=None):
        """The qualifier must be a qualifier of the Association end of the linkEndData that owns this QualifierValue.
linkEndData.end.qualifier->includes(qualifier)"""
        raise NotImplementedError(
            'operation qualifier_attribute(...) not yet implemented')


class ClauseMixin(object):
    """User defined mixin class for Clause."""

    def __init__(
            self, body=None, bodyOutput=None, decider=None,
            predecessorClause=None, successorClause=None, test=None, **kwargs):
        super(ClauseMixin, self).__init__(**kwargs)

    def body_output_pins(self, diagnostics=None, context=None):
        """The bodyOutput Pins are OutputPins on Actions in the body of the Clause.
_'body'.oclAsType(Action).allActions().output->includesAll(bodyOutput)"""
        raise NotImplementedError(
            'operation body_output_pins(...) not yet implemented')

    def decider_output(self, diagnostics=None, context=None):
        """The decider Pin must be on an Action in the test section of the Clause and must be of type Boolean with multiplicity 1..1.
test.oclAsType(Action).allActions().output->includes(decider) and
decider.type = Boolean and
decider.is(1,1)"""
        raise NotImplementedError(
            'operation decider_output(...) not yet implemented')

    def test_and_body(self, diagnostics=None, context=None):
        """The test and body parts of a ConditionalNode must be disjoint with each other.
test->intersection(_'body')->isEmpty()"""
        raise NotImplementedError(
            'operation test_and_body(...) not yet implemented')


class DerivedOwnedmember(EDerivedCollection):
    pass


class DerivedImportedmember(EDerivedCollection):
    pass


class DerivedMember(EDerivedCollection):
    pass


class NamespaceMixin(object):
    """User defined mixin class for Namespace."""

    def __init__(self, ownedRule=None, elementImport=None,
                 packageImport=None, ownedMember=None, importedMember=None,
                 member=None, **kwargs):
        super(NamespaceMixin, self).__init__(**kwargs)

    def members_distinguishable(self, diagnostics=None, context=None):
        """All the members of a Namespace are distinguishable within it.
membersAreDistinguishable()"""
        raise NotImplementedError(
            'operation members_distinguishable(...) not yet implemented')

    def cannot_import_self(self, diagnostics=None, context=None):
        """A Namespace cannot have a PackageImport to itself.
packageImport.importedPackage.oclAsType(Namespace)->excludes(self)"""
        raise NotImplementedError(
            'operation cannot_import_self(...) not yet implemented')

    def cannot_import_owned_members(self, diagnostics=None, context=None):
        """A Namespace cannot have an ElementImport to one of its ownedMembers.
elementImport.importedElement.oclAsType(Element)->excludesAll(ownedMember)"""
        raise NotImplementedError(
            'operation cannot_import_owned_members(...) not yet implemented')

    def create_element_import(self, element=None, visibility=None):
        """Creates an import of the specified element into this namespace with the specified visibility."""
        raise NotImplementedError(
            'operation create_element_import(...) not yet implemented')

    def create_package_import(self, package_=None, visibility=None):
        """Creates an import of the specified package into this namespace with the specified visibility."""
        raise NotImplementedError(
            'operation create_package_import(...) not yet implemented')

    def get_imported_elements(self):
        """Retrieves the elements imported by this namespace."""
        raise NotImplementedError(
            'operation get_imported_elements(...) not yet implemented')

    def get_imported_packages(self):
        """Retrieves the packages imported by this namespace."""
        raise NotImplementedError(
            'operation get_imported_packages(...) not yet implemented')

    def get_owned_members(self):

        raise NotImplementedError(
            'operation get_owned_members(...) not yet implemented')

    def exclude_collisions(self, imps=None):
        """The query excludeCollisions() excludes from a set of PackageableElements any that would not be distinguishable from each other in this Namespace.
result = (imps->reject(imp1  | imps->exists(imp2 | not imp1.isDistinguishableFrom(imp2, self))))
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation exclude_collisions(...) not yet implemented')

    def get_names_of_member(self, element=None):
        """The query getNamesOfMember() gives a set of all of the names that a member would have in a Namespace, taking importing into account. In general a member can have multiple names in a Namespace if it is imported more than once with different aliases.
result = (if self.ownedMember ->includes(element)
then Set{element.name}
else let elementImports : Set(ElementImport) = self.elementImport->select(ei | ei.importedElement = element) in
  if elementImports->notEmpty()
  then
     elementImports->collect(el | el.getName())->asSet()
  else
     self.packageImport->select(pi | pi.importedPackage.visibleMembers().oclAsType(NamedElement)->includes(element))-> collect(pi | pi.importedPackage.getNamesOfMember(element))->asSet()
  endif
endif)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation get_names_of_member(...) not yet implemented')

    def import_members(self, imps=None):
        """The query importMembers() defines which of a set of PackageableElements are actually imported into the Namespace. This excludes hidden ones, i.e., those which have names that conflict with names of ownedMembers, and it also excludes PackageableElements that would have the indistinguishable names when imported.
result = (self.excludeCollisions(imps)->select(imp | self.ownedMember->forAll(mem | imp.isDistinguishableFrom(mem, self))))
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation import_members(...) not yet implemented')

    def get_imported_members(self):
        """The importedMember property is derived as the PackageableElements that are members of this Namespace as a result of either PackageImports or ElementImports.
result = (self.importMembers(elementImport.importedElement->asSet()->union(packageImport.importedPackage->collect(p | p.visibleMembers()))->asSet()))
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation get_imported_members(...) not yet implemented')

    def members_are_distinguishable(self):
        """The Boolean query membersAreDistinguishable() determines whether all of the Namespace's members are distinguishable within it.
result = (member->forAll( memb |
   member->excluding(memb)->forAll(other |
       memb.isDistinguishableFrom(other, self))))
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation members_are_distinguishable(...) not yet implemented')


class DerivedSource(EDerivedCollection):
    pass


class DerivedTarget(EDerivedCollection):
    pass


class DirectedRelationshipMixin(object):
    """User defined mixin class for DirectedRelationship."""

    def __init__(self, source=None, target=None, **kwargs):
        super(DirectedRelationshipMixin, self).__init__(**kwargs)


class TypedElementMixin(object):
    """User defined mixin class for TypedElement."""

    def __init__(self, type=None, **kwargs):
        super(TypedElementMixin, self).__init__(**kwargs)


class ConnectorEndMixin(object):
    """User defined mixin class for ConnectorEnd."""

    @property
    def definingEnd(self):
        raise NotImplementedError('Missing implementation for definingEnd')

    def __init__(
            self, definingEnd=None, partWithPort=None, role=None, **kwargs):
        super(ConnectorEndMixin, self).__init__(**kwargs)

    def role_and_part_with_port(self, diagnostics=None, context=None):
        """If a ConnectorEnd references a partWithPort, then the role must be a Port that is defined or inherited by the type of the partWithPort.
partWithPort->notEmpty() implies
  (role.oclIsKindOf(Port) and partWithPort.type.oclAsType(Namespace).member->includes(role))"""
        raise NotImplementedError(
            'operation role_and_part_with_port(...) not yet implemented')

    def part_with_port_empty(self, diagnostics=None, context=None):
        """If a ConnectorEnd is attached to a Port of the containing Classifier, partWithPort will be empty.
(role.oclIsKindOf(Port) and role.owner = connector.owner) implies partWithPort->isEmpty()"""
        raise NotImplementedError(
            'operation part_with_port_empty(...) not yet implemented')

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the ConnectorEnd may not be more general than the multiplicity of the corresponding end of the Association typing the owning Connector, if any.
self.compatibleWith(definingEnd)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def self_part_with_port(self, diagnostics=None, context=None):
        """The Property held in self.partWithPort must not be a Port.
partWithPort->notEmpty() implies not partWithPort.oclIsKindOf(Port)"""
        raise NotImplementedError(
            'operation self_part_with_port(...) not yet implemented')

    def get_defining_end(self):
        """Derivation for ConnectorEnd::/definingEnd : Property
result = (if connector.type = null
then
  null
else
  let index : Integer = connector.end->indexOf(self) in
    connector.type.memberEnd->at(index)
endif)
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_defining_end(...) not yet implemented')


class ConnectableElementTemplateParameterMixin(object):
    """User defined mixin class for ConnectableElementTemplateParameter."""

    def __init__(self, **kwargs):
        super(ConnectableElementTemplateParameterMixin, self).__init__(**kwargs)


class DerivedDeployedelement(EDerivedCollection):
    pass


class DeploymentTargetMixin(object):
    """User defined mixin class for DeploymentTarget."""

    def __init__(self, deployedElement=None, deployment=None, **kwargs):
        super(DeploymentTargetMixin, self).__init__(**kwargs)

    def get_deployed_elements(self):
        """Derivation for DeploymentTarget::/deployedElement
result = (deployment.deployedArtifact->select(oclIsKindOf(Artifact))->collect(oclAsType(Artifact).manifestation)->collect(utilizedElement)->asSet())
<p>From package UML::Deployments.</p>"""
        raise NotImplementedError(
            'operation get_deployed_elements(...) not yet implemented')


class DeployedArtifactMixin(object):
    """User defined mixin class for DeployedArtifact."""

    def __init__(self, **kwargs):
        super(DeployedArtifactMixin, self).__init__(**kwargs)


class DerivedRedefinedelement(EDerivedCollection):
    pass


class DerivedRedefinitioncontext(EDerivedCollection):
    pass


class RedefinableElementMixin(object):
    """User defined mixin class for RedefinableElement."""

    def __init__(self, isLeaf=None, redefinedElement=None,
                 redefinitionContext=None, **kwargs):
        super(RedefinableElementMixin, self).__init__(**kwargs)

    def redefinition_consistent(self, diagnostics=None, context=None):
        """A redefining element must be consistent with each redefined element.
redefinedElement->forAll(re | re.isConsistentWith(self))"""
        raise NotImplementedError(
            'operation redefinition_consistent(...) not yet implemented')

    def non_leaf_redefinition(self, diagnostics=None, context=None):
        """A RedefinableElement can only redefine non-leaf RedefinableElements.
redefinedElement->forAll(re | not re.isLeaf)"""
        raise NotImplementedError(
            'operation non_leaf_redefinition(...) not yet implemented')

    def redefinition_context_valid(self, diagnostics=None, context=None):
        """At least one of the redefinition contexts of the redefining element must be a specialization of at least one of the redefinition contexts for each redefined element.
redefinedElement->forAll(re | self.isRedefinitionContextValid(re))"""
        raise NotImplementedError(
            'operation redefinition_context_valid(...) not yet implemented')

    def is_consistent_with(self, redefiningElement=None):
        """The query isConsistentWith() specifies, for any two RedefinableElements in a context in which redefinition is possible, whether redefinition would be logically consistent. By default, this is false; this operation must be overridden for subclasses of RedefinableElement to define the consistency conditions.
redefiningElement.isRedefinitionContextValid(self)
result = (false)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation is_consistent_with(...) not yet implemented')

    def is_redefinition_context_valid(self, redefinedElement=None):
        """The query isRedefinitionContextValid() specifies whether the redefinition contexts of this RedefinableElement are properly related to the redefinition contexts of the specified RedefinableElement to allow this element to redefine the other. By default at least one of the redefinition contexts of this element must be a specialization of at least one of the redefinition contexts of the specified element.
result = (redefinitionContext->exists(c | c.allParents()->includesAll(redefinedElement.redefinitionContext)))
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation is_redefinition_context_valid(...) not yet implemented')


class ParameterSetMixin(object):
    """User defined mixin class for ParameterSet."""

    def __init__(self, condition=None, parameter=None, **kwargs):
        super(ParameterSetMixin, self).__init__(**kwargs)

    def same_parameterized_entity(self, diagnostics=None, context=None):
        """The Parameters in a ParameterSet must all be inputs or all be outputs of the same parameterized entity, and the ParameterSet is owned by that entity.
parameter->forAll(p1, p2 | self.owner = p1.owner and self.owner = p2.owner and p1.direction = p2.direction)"""
        raise NotImplementedError(
            'operation same_parameterized_entity(...) not yet implemented')

    def input(self, diagnostics=None, context=None):
        """If a parameterized entity has input Parameters that are in a ParameterSet, then any inputs that are not in a ParameterSet must be streaming. Same for output Parameters.
((parameter->exists(direction = ParameterDirectionKind::_'in')) implies
    behavioralFeature.ownedParameter->select(p | p.direction = ParameterDirectionKind::_'in' and p.parameterSet->isEmpty())->forAll(isStream))
    and
((parameter->exists(direction = ParameterDirectionKind::out)) implies
    behavioralFeature.ownedParameter->select(p | p.direction = ParameterDirectionKind::out and p.parameterSet->isEmpty())->forAll(isStream))"""
        raise NotImplementedError('operation input(...) not yet implemented')

    def two_parameter_sets(self, diagnostics=None, context=None):
        """Two ParameterSets cannot have exactly the same set of Parameters.
parameter->forAll(parameterSet->forAll(s1, s2 | s1->size() = s2->size() implies s1.parameter->exists(p | not s2.parameter->includes(p))))"""
        raise NotImplementedError(
            'operation two_parameter_sets(...) not yet implemented')


class DerivedIncoming(EDerivedCollection):
    pass


class DerivedOutgoing(EDerivedCollection):
    pass


class VertexMixin(object):
    """User defined mixin class for Vertex."""

    def __init__(
            self, container=None, incoming=None, outgoing=None, **kwargs):
        super(VertexMixin, self).__init__(**kwargs)

    def containing_state_machine(self):
        """The operation containingStateMachine() returns the StateMachine in which this Vertex is defined.
result = (if container <> null
then
-- the container is a region
   container.containingStateMachine()
else
   if (self.oclIsKindOf(Pseudostate)) and ((self.oclAsType(Pseudostate).kind = PseudostateKind::entryPoint) or (self.oclAsType(Pseudostate).kind = PseudostateKind::exitPoint)) then
      self.oclAsType(Pseudostate).stateMachine
   else
      if (self.oclIsKindOf(ConnectionPointReference)) then
          self.oclAsType(ConnectionPointReference).state.containingStateMachine() -- no other valid cases possible
      else
          null
      endif
   endif
endif
)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation containing_state_machine(...) not yet implemented')

    def get_incomings(self):
        """Derivation for Vertex::/incoming.
result = (Transition.allInstances()->select(target=self))
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation get_incomings(...) not yet implemented')

    def get_outgoings(self):
        """Derivation for Vertex::/outgoing
result = (Transition.allInstances()->select(source=self))
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation get_outgoings(...) not yet implemented')

    def is_contained_in_state(self, s=None):
        """This utility operation returns true if the Vertex is contained in the State s (input argument).
result = (if not s.isComposite() or container->isEmpty() then
        false
else
        if container.state = s then
                true
        else
                container.state.isContainedInState(s)
        endif
endif)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation is_contained_in_state(...) not yet implemented')

    def is_contained_in_region(self, r=None):
        """This utility query returns true if the Vertex is contained in the Region r (input argument).
result = (if (container = r) then
        true
else
        if (r.state->isEmpty()) then
                false
        else
                container.state.isContainedInRegion(r)
        endif
endif)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation is_contained_in_region(...) not yet implemented')


class TriggerMixin(object):
    """User defined mixin class for Trigger."""

    def __init__(self, event=None, port=None, **kwargs):
        super(TriggerMixin, self).__init__(**kwargs)

    def trigger_with_ports(self, diagnostics=None, context=None):
        """If a Trigger specifies one or more ports, the event of the Trigger must be a MessageEvent.
port->notEmpty() implies event.oclIsKindOf(MessageEvent)"""
        raise NotImplementedError(
            'operation trigger_with_ports(...) not yet implemented')


class OperationTemplateParameterMixin(object):
    """User defined mixin class for OperationTemplateParameter."""

    def __init__(self, **kwargs):
        super(OperationTemplateParameterMixin, self).__init__(**kwargs)

    def match_default_signature(self, diagnostics=None, context=None):
        """default->notEmpty() implies (default.oclIsKindOf(Operation) and (let defaultOp : Operation = default.oclAsType(Operation) in
    defaultOp.ownedParameter->size() = parameteredElement.ownedParameter->size() and
    Sequence{1.. defaultOp.ownedParameter->size()}->forAll( ix |
        let p1: Parameter = defaultOp.ownedParameter->at(ix), p2 : Parameter = parameteredElement.ownedParameter->at(ix) in
          p1.type = p2.type and p1.upper = p2.upper and p1.lower = p2.lower and p1.direction = p2.direction and p1.isOrdered = p2.isOrdered and p1.isUnique = p2.isUnique)))"""
        raise NotImplementedError(
            'operation match_default_signature(...) not yet implemented')


class CollaborationUseMixin(object):
    """User defined mixin class for CollaborationUse."""

    def __init__(self, roleBinding=None, type=None, **kwargs):
        super(CollaborationUseMixin, self).__init__(**kwargs)

    def client_elements(self, diagnostics=None, context=None):
        """All the client elements of a roleBinding are in one Classifier and all supplier elements of a roleBinding are in one Collaboration.
roleBinding->collect(client)->forAll(ne1, ne2 |
  ne1.oclIsKindOf(ConnectableElement) and ne2.oclIsKindOf(ConnectableElement) and
    let ce1 : ConnectableElement = ne1.oclAsType(ConnectableElement), ce2 : ConnectableElement = ne2.oclAsType(ConnectableElement) in
      ce1.structuredClassifier = ce2.structuredClassifier)
and
  roleBinding->collect(supplier)->forAll(ne1, ne2 |
  ne1.oclIsKindOf(ConnectableElement) and ne2.oclIsKindOf(ConnectableElement) and
    let ce1 : ConnectableElement = ne1.oclAsType(ConnectableElement), ce2 : ConnectableElement = ne2.oclAsType(ConnectableElement) in
      ce1.collaboration = ce2.collaboration)"""
        raise NotImplementedError(
            'operation client_elements(...) not yet implemented')

    def every_role(self, diagnostics=None, context=None):
        """Every collaborationRole in the Collaboration is bound within the CollaborationUse.
type.collaborationRole->forAll(role | roleBinding->exists(rb | rb.supplier->includes(role)))"""
        raise NotImplementedError(
            'operation every_role(...) not yet implemented')

    def connectors(self, diagnostics=None, context=None):
        """Connectors in a Collaboration typing a CollaborationUse must have corresponding Connectors between elements bound in the context Classifier, and these corresponding Connectors must have the same or more general type than the Collaboration Connectors.
type.ownedConnector->forAll(connector |
  let rolesConnectedInCollab : Set(ConnectableElement) = connector.end.role->asSet(),
        relevantBindings : Set(Dependency) = roleBinding->select(rb | rb.supplier->intersection(rolesConnectedInCollab)->notEmpty()),
        boundRoles : Set(ConnectableElement) = relevantBindings->collect(client.oclAsType(ConnectableElement))->asSet(),
        contextClassifier : StructuredClassifier = boundRoles->any(true).structuredClassifier->any(true) in
          contextClassifier.ownedConnector->exists( correspondingConnector |
              correspondingConnector.end.role->forAll( role | boundRoles->includes(role) )
              and (connector.type->notEmpty() and correspondingConnector.type->notEmpty()) implies connector.type->forAll(conformsTo(correspondingConnector.type)) )
)"""
        raise NotImplementedError(
            'operation connectors(...) not yet implemented')


class ClassifierTemplateParameterMixin(object):
    """User defined mixin class for ClassifierTemplateParameter."""

    def __init__(
            self, allowSubstitutable=None, constrainingClassifier=None, **
            kwargs):
        super(ClassifierTemplateParameterMixin, self).__init__(**kwargs)

    def has_constraining_classifier(self, diagnostics=None, context=None):
        """If allowSubstitutable is true, then there must be a constrainingClassifier.
allowSubstitutable implies constrainingClassifier->notEmpty()"""
        raise NotImplementedError(
            'operation has_constraining_classifier(...) not yet implemented')

    def parametered_element_no_features(self, diagnostics=None, context=None):
        """The parameteredElement has no direct features, and if constrainedElement is empty it has no generalizations.
parameteredElement.feature->isEmpty() and (constrainingClassifier->isEmpty() implies  parameteredElement.allParents()->isEmpty())"""
        raise NotImplementedError(
            'operation parametered_element_no_features(...) not yet implemented')

    def matching_abstract(self, diagnostics=None, context=None):
        """If the parameteredElement is not abstract, then the Classifier used as an argument shall not be abstract.
(not parameteredElement.isAbstract) implies templateParameterSubstitution.actual->forAll(a | not a.oclAsType(Classifier).isAbstract)"""
        raise NotImplementedError(
            'operation matching_abstract(...) not yet implemented')

    def actual_is_classifier(self, diagnostics=None, context=None):
        """The argument to a ClassifierTemplateParameter is a Classifier.
 templateParameterSubstitution.actual->forAll(a | a.oclIsKindOf(Classifier))"""
        raise NotImplementedError(
            'operation actual_is_classifier(...) not yet implemented')

    def constraining_classifiers_constrain_args(
            self, diagnostics=None, context=None):
        """If there are any constrainingClassifiers, then every argument must be the same as or a specialization of them, or if allowSubstitutable is true, then it can also be substitutable.
templateParameterSubstitution.actual->forAll( a |
  let arg : Classifier = a.oclAsType(Classifier) in
    constrainingClassifier->forAll(
      cc |
         arg = cc or arg.conformsTo(cc) or (allowSubstitutable and arg.isSubstitutableFor(cc))
      )
)"""
        raise NotImplementedError(
            'operation constraining_classifiers_constrain_args(...) not yet implemented')

    def constraining_classifiers_constrain_parametered_element(
            self, diagnostics=None, context=None):
        """If there are any constrainingClassifiers, then the parameteredElement must be the same as or a specialization of them, or if allowSubstitutable is true, then it can also be substitutable.
constrainingClassifier->forAll(
     cc |  parameteredElement = cc or parameteredElement.conformsTo(cc) or (allowSubstitutable and parameteredElement.isSubstitutableFor(cc))
)"""
        raise NotImplementedError(
            'operation constraining_classifiers_constrain_parametered_element(...) not yet implemented')


class LinkEndCreationDataMixin(object):
    """User defined mixin class for LinkEndCreationData."""

    def __init__(self, insertAt=None, isReplaceAll=None, **kwargs):
        super(LinkEndCreationDataMixin, self).__init__(**kwargs)

    def insert_at_pin(self, diagnostics=None, context=None):
        """LinkEndCreationData for ordered Association ends must have a single insertAt InputPin for the insertion point with type UnlimitedNatural and multiplicity of 1..1, if isReplaceAll=false, and must have no InputPin for the insertion point when the association ends are unordered.
if  not end.isOrdered
then insertAt = null
else
        not isReplaceAll=false implies
        insertAt <> null and insertAt->forAll(type=UnlimitedNatural and is(1,1))
endif"""
        raise NotImplementedError(
            'operation insert_at_pin(...) not yet implemented')


class LinkEndDestructionDataMixin(object):
    """User defined mixin class for LinkEndDestructionData."""

    def __init__(self, destroyAt=None, isDestroyDuplicates=None, **kwargs):
        super(LinkEndDestructionDataMixin, self).__init__(**kwargs)

    def destroy_at_pin(self, diagnostics=None, context=None):
        """LinkEndDestructionData for ordered, nonunique Association ends must have a single destroyAt InputPin if isDestroyDuplicates is false, which must be of type UnlimitedNatural and have a multiplicity of 1..1. Otherwise, the action has no destroyAt input pin.
if  not end.isOrdered or end.isUnique or isDestroyDuplicates
then destroyAt = null
else
        destroyAt <> null and
        destroyAt->forAll(type=UnlimitedNatural and is(1,1))
endif"""
        raise NotImplementedError(
            'operation destroy_at_pin(...) not yet implemented')


class MessageMixin(object):
    """User defined mixin class for Message."""

    @property
    def messageKind(self):
        raise NotImplementedError('Missing implementation for messageKind')

    def __init__(
            self, argument=None, connector=None, interaction=None,
            messageKind=None, messageSort=None, receiveEvent=None,
            sendEvent=None, signature=None, **kwargs):
        super(MessageMixin, self).__init__(**kwargs)

    def sending_receiving_message_event(self, diagnostics=None, context=None):
        """If the sendEvent and the receiveEvent of the same Message are on the same Lifeline, the sendEvent must be ordered before the receiveEvent.
receiveEvent.oclIsKindOf(MessageOccurrenceSpecification)
implies
let f :  Lifeline = sendEvent->select(oclIsKindOf(MessageOccurrenceSpecification)).oclAsType(MessageOccurrenceSpecification)->asOrderedSet()->first().covered in
f = receiveEvent->select(oclIsKindOf(MessageOccurrenceSpecification)).oclAsType(MessageOccurrenceSpecification)->asOrderedSet()->first().covered  implies
f.events->indexOf(sendEvent.oclAsType(MessageOccurrenceSpecification)->asOrderedSet()->first() ) <
f.events->indexOf(receiveEvent.oclAsType(MessageOccurrenceSpecification)->asOrderedSet()->first() )"""
        raise NotImplementedError(
            'operation sending_receiving_message_event(...) not yet implemented')

    def arguments(self, diagnostics=None, context=None):
        """Arguments of a Message must only be: i) attributes of the sending lifeline, ii) constants, iii) symbolic values (which are wildcard values representing any legal value), iv) explicit parameters of the enclosing Interaction, v) attributes of the class owning the Interaction."""
        raise NotImplementedError(
            'operation arguments(...) not yet implemented')

    def cannot_cross_boundaries(self, diagnostics=None, context=None):
        """Messages cannot cross boundaries of CombinedFragments or their operands.  This is true if and only if both MessageEnds are enclosed within the same InteractionFragment (i.e., an InteractionOperand or an Interaction).
sendEvent->notEmpty() and receiveEvent->notEmpty() implies
let sendEnclosingFrag : Set(InteractionFragment) =
sendEvent->asOrderedSet()->first().enclosingFragment()
in
let receiveEnclosingFrag : Set(InteractionFragment) =
receiveEvent->asOrderedSet()->first().enclosingFragment()
in  sendEnclosingFrag = receiveEnclosingFrag"""
        raise NotImplementedError(
            'operation cannot_cross_boundaries(...) not yet implemented')

    def signature_is_signal(self, diagnostics=None, context=None):
        """In the case when the Message signature is a Signal, the arguments of the Message must correspond to the attributes of the Signal. A Message Argument corresponds to a Signal Attribute if the Argument is of the same Class or a specialization of that of the Attribute.
(messageSort = MessageSort::asynchSignal ) and signature.oclIsKindOf(Signal) implies
   let signalAttributes : OrderedSet(Property) = signature.oclAsType(Signal).inheritedMember()->
             select(n:NamedElement | n.oclIsTypeOf(Property))->collect(oclAsType(Property))->asOrderedSet()
   in signalAttributes->size() = self.argument->size()
   and self.argument->forAll( o: ValueSpecification |
          not (o.oclIsKindOf(Expression)
          and o.oclAsType(Expression).symbol->size()=0
          and o.oclAsType(Expression).operand->isEmpty() ) implies
              let p : Property = signalAttributes->at(self.argument->indexOf(o))
              in o.type.oclAsType(Classifier).conformsTo(p.type.oclAsType(Classifier)))"""
        raise NotImplementedError(
            'operation signature_is_signal(...) not yet implemented')

    def occurrence_specifications(self, diagnostics=None, context=None):
        """If the MessageEnds are both OccurrenceSpecifications, then the connector must go between the Parts represented by the Lifelines of the two MessageEnds."""
        raise NotImplementedError(
            'operation occurrence_specifications(...) not yet implemented')

    def signature_refer_to(self, diagnostics=None, context=None):
        """The signature must either refer an Operation (in which case messageSort is either synchCall or asynchCall or reply) or a Signal (in which case messageSort is asynchSignal). The name of the NamedElement referenced by signature must be the same as that of the Message.
signature->notEmpty() implies
((signature.oclIsKindOf(Operation) and
(messageSort = MessageSort::asynchCall or messageSort = MessageSort::synchCall or messageSort = MessageSort::reply)
) or (signature.oclIsKindOf(Signal)  and messageSort = MessageSort::asynchSignal )
 ) and name = signature.name"""
        raise NotImplementedError(
            'operation signature_refer_to(...) not yet implemented')

    def signature_is_operation_request(self, diagnostics=None, context=None):
        """In the case when a Message with messageSort synchCall or asynchCall has a non empty Operation signature, the arguments of the Message must correspond to the in and inout parameters of the Operation. A Parameter corresponds to an Argument if the Argument is of the same Class or a specialization of that of the Parameter.
(messageSort = MessageSort::asynchCall or messageSort = MessageSort::synchCall) and signature.oclIsKindOf(Operation)  implies
 let requestParms : OrderedSet(Parameter) = signature.oclAsType(Operation).ownedParameter->
 select(direction = ParameterDirectionKind::inout or direction = ParameterDirectionKind::_'in'  )
in requestParms->size() = self.argument->size() and
self.argument->forAll( o: ValueSpecification |
not (o.oclIsKindOf(Expression) and o.oclAsType(Expression).symbol->size()=0 and o.oclAsType(Expression).operand->isEmpty() ) implies
let p : Parameter = requestParms->at(self.argument->indexOf(o)) in
o.type.oclAsType(Classifier).conformsTo(p.type.oclAsType(Classifier))
)"""
        raise NotImplementedError(
            'operation signature_is_operation_request(...) not yet implemented')

    def signature_is_operation_reply(self, diagnostics=None, context=None):
        """In the case when a Message with messageSort reply has a non empty Operation signature, the arguments of the Message must correspond to the out, inout, and return parameters of the Operation. A Parameter corresponds to an Argument if the Argument is of the same Class or a specialization of that of the Parameter.
(messageSort = MessageSort::reply) and signature.oclIsKindOf(Operation) implies
 let replyParms : OrderedSet(Parameter) = signature.oclAsType(Operation).ownedParameter->
select(direction = ParameterDirectionKind::inout or direction = ParameterDirectionKind::out or direction = ParameterDirectionKind::return)
in replyParms->size() = self.argument->size() and
self.argument->forAll( o: ValueSpecification | o.oclIsKindOf(Expression) and let e : Expression = o.oclAsType(Expression) in
e.operand->notEmpty()  implies
let p : Parameter = replyParms->at(self.argument->indexOf(o)) in
e.operand->asSequence()->first().type.oclAsType(Classifier).conformsTo(p.type.oclAsType(Classifier))
)"""
        raise NotImplementedError(
            'operation signature_is_operation_reply(...) not yet implemented')

    def get_message_kind(self):
        """This query returns the MessageKind value for this Message.
result = (messageKind)
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError(
            'operation get_message_kind(...) not yet implemented')


class InteractionFragmentMixin(object):
    """User defined mixin class for InteractionFragment."""

    def __init__(self, covered=None, enclosingOperand=None,
                 enclosingInteraction=None, generalOrdering=None, **kwargs):
        super(InteractionFragmentMixin, self).__init__(**kwargs)


class LifelineMixin(object):
    """User defined mixin class for Lifeline."""

    def __init__(
            self, decomposedAs=None, interaction=None, represents=None,
            selector=None, coveredBy=None, **kwargs):
        super(LifelineMixin, self).__init__(**kwargs)

    def selector_specified(self, diagnostics=None, context=None):
        """The selector for a Lifeline must only be specified if the referenced Part is multivalued.
 self.selector->notEmpty() = (self.represents.oclIsKindOf(MultiplicityElement) and self.represents.oclAsType(MultiplicityElement).isMultivalued())"""
        raise NotImplementedError(
            'operation selector_specified(...) not yet implemented')

    def interaction_uses_share_lifeline(self, diagnostics=None, context=None):
        """If a lifeline is in an Interaction referred to by an InteractionUse in an enclosing Interaction,  and that lifeline is common with another lifeline in an Interaction referred to by another InteractonUse within that same enclosing Interaction, it must be common to a lifeline within that enclosing Interaction. By common Lifelines we mean Lifelines with the same selector and represents associations.
let intUses : Set(InteractionUse) = interaction.interactionUse  in
intUses->forAll
( iuse : InteractionUse |
let usingInteraction : Set(Interaction)  = iuse.enclosingInteraction->asSet()
->union(
iuse.enclosingOperand.combinedFragment->asSet()->closure(enclosingOperand.combinedFragment).enclosingInteraction->asSet()
               )
in
let peerUses : Set(InteractionUse) = usingInteraction.fragment->select(oclIsKindOf(InteractionUse)).oclAsType(InteractionUse)->asSet()
->union(
usingInteraction.fragment->select(oclIsKindOf(CombinedFragment)).oclAsType(CombinedFragment)->asSet()
->closure(operand.fragment->select(oclIsKindOf(CombinedFragment)).oclAsType(CombinedFragment)).operand.fragment->
select(oclIsKindOf(InteractionUse)).oclAsType(InteractionUse)->asSet()
               )->excluding(iuse)
 in
peerUses->forAll( peerUse : InteractionUse |
 peerUse.refersTo.lifeline->forAll( l : Lifeline | (l.represents = self.represents and
 ( self.selector.oclIsKindOf(LiteralString) implies
  l.selector.oclIsKindOf(LiteralString) and
  self.selector.oclAsType(LiteralString).value = l.selector.oclAsType(LiteralString).value )
  and
( self.selector.oclIsKindOf(LiteralInteger) implies
  l.selector.oclIsKindOf(LiteralInteger) and
  self.selector.oclAsType(LiteralInteger).value = l.selector.oclAsType(LiteralInteger).value )
)
implies
 usingInteraction.lifeline->exists(represents = self.represents and
 ( self.selector.oclIsKindOf(LiteralString) implies
  l.selector.oclIsKindOf(LiteralString) and
  self.selector.oclAsType(LiteralString).value = l.selector.oclAsType(LiteralString).value )
and
( self.selector.oclIsKindOf(LiteralInteger) implies
  l.selector.oclIsKindOf(LiteralInteger) and
  self.selector.oclAsType(LiteralInteger).value = l.selector.oclAsType(LiteralInteger).value )
)
                                                )
                    )
)"""
        raise NotImplementedError(
            'operation interaction_uses_share_lifeline(...) not yet implemented')

    def same_classifier(self, diagnostics=None, context=None):
        """The classifier containing the referenced ConnectableElement must be the same classifier, or an ancestor, of the classifier that contains the interaction enclosing this lifeline.
represents.namespace->closure(namespace)->includes(interaction._'context')"""
        raise NotImplementedError(
            'operation same_classifier(...) not yet implemented')

    def selector_int_or_string(self, diagnostics=None, context=None):
        """The selector value, if present, must be a LiteralString or a LiteralInteger
self.selector->notEmpty() implies
self.selector.oclIsKindOf(LiteralInteger) or
self.selector.oclIsKindOf(LiteralString)"""
        raise NotImplementedError(
            'operation selector_int_or_string(...) not yet implemented')


class MessageEndMixin(object):
    """User defined mixin class for MessageEnd."""

    def __init__(self, message=None, **kwargs):
        super(MessageEndMixin, self).__init__(**kwargs)

    def opposite_end(self):
        """This query returns a set including the MessageEnd (if exists) at the opposite end of the Message for this MessageEnd.
message->notEmpty()
result = (message->asSet().messageEnd->asSet()->excluding(self))
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError(
            'operation opposite_end(...) not yet implemented')

    def is_send(self):
        """This query returns value true if this MessageEnd is a sendEvent.
message->notEmpty()
result = (message.sendEvent->asSet()->includes(self))
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError('operation is_send(...) not yet implemented')

    def is_receive(self):
        """This query returns value true if this MessageEnd is a receiveEvent.
message->notEmpty()
result = (message.receiveEvent->asSet()->includes(self))
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError(
            'operation is_receive(...) not yet implemented')

    def enclosing_fragment(self):
        """This query returns a set including the enclosing InteractionFragment this MessageEnd is enclosed within.
result = (if self->select(oclIsKindOf(Gate))->notEmpty()
then -- it is a Gate
let endGate : Gate =
  self->select(oclIsKindOf(Gate)).oclAsType(Gate)->asOrderedSet()->first()
  in
  if endGate.isOutsideCF()
  then endGate.combinedFragment.enclosingInteraction.oclAsType(InteractionFragment)->asSet()->
     union(endGate.combinedFragment.enclosingOperand.oclAsType(InteractionFragment)->asSet())
  else if endGate.isInsideCF()
    then endGate.combinedFragment.oclAsType(InteractionFragment)->asSet()
    else if endGate.isFormal()
      then endGate.interaction.oclAsType(InteractionFragment)->asSet()
      else if endGate.isActual()
        then endGate.interactionUse.enclosingInteraction.oclAsType(InteractionFragment)->asSet()->
     union(endGate.interactionUse.enclosingOperand.oclAsType(InteractionFragment)->asSet())
        else null
        endif
      endif
    endif
  endif
else -- it is a MessageOccurrenceSpecification
let endMOS : MessageOccurrenceSpecification  =
  self->select(oclIsKindOf(MessageOccurrenceSpecification)).oclAsType(MessageOccurrenceSpecification)->asOrderedSet()->first()
  in
  if endMOS.enclosingInteraction->notEmpty()
  then endMOS.enclosingInteraction.oclAsType(InteractionFragment)->asSet()
  else endMOS.enclosingOperand.oclAsType(InteractionFragment)->asSet()
  endif
endif)
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError(
            'operation enclosing_fragment(...) not yet implemented')


class GeneralOrderingMixin(object):
    """User defined mixin class for GeneralOrdering."""

    def __init__(self, after=None, before=None, **kwargs):
        super(GeneralOrderingMixin, self).__init__(**kwargs)

    def irreflexive_transitive_closure(self, diagnostics=None, context=None):
        """An occurrence specification must not be ordered relative to itself through a series of general orderings. (In other words, the transitive closure of the general orderings is irreflexive.)
after->closure(toAfter.after)->excludes(before)"""
        raise NotImplementedError(
            'operation irreflexive_transitive_closure(...) not yet implemented')


class PackageableElementMixin(object):
    """User defined mixin class for PackageableElement."""

    def __init__(self, **kwargs):
        super(PackageableElementMixin, self).__init__(**kwargs)

    def namespace_needs_visibility(self, diagnostics=None, context=None):
        """A PackageableElement owned by a Namespace must have a visibility.
visibility = null implies namespace = null"""
        raise NotImplementedError(
            'operation namespace_needs_visibility(...) not yet implemented')


class TemplateBindingMixin(object):
    """User defined mixin class for TemplateBinding."""

    def __init__(
            self, parameterSubstitution=None, signature=None,
            boundElement=None, **kwargs):
        super(TemplateBindingMixin, self).__init__(**kwargs)

    def parameter_substitution_formal(self, diagnostics=None, context=None):
        """Each parameterSubstitution must refer to a formal TemplateParameter of the target TemplateSignature.
parameterSubstitution->forAll(b | signature.parameter->includes(b.formal))"""
        raise NotImplementedError(
            'operation parameter_substitution_formal(...) not yet implemented')

    def one_parameter_substitution(self, diagnostics=None, context=None):
        """A TemplateBiinding contains at most one TemplateParameterSubstitution for each formal TemplateParameter of the target TemplateSignature.
signature.parameter->forAll(p | parameterSubstitution->select(b | b.formal = p)->size() <= 1)"""
        raise NotImplementedError(
            'operation one_parameter_substitution(...) not yet implemented')


class DerivedFeaturingclassifier(EDerivedCollection):
    pass


class FeatureMixin(object):
    """User defined mixin class for Feature."""

    def __init__(self, featuringClassifier=None, isStatic=None, **kwargs):
        super(FeatureMixin, self).__init__(**kwargs)


class PseudostateMixin(object):
    """User defined mixin class for Pseudostate."""

    def __init__(self, state=None, kind=None, stateMachine=None, **kwargs):
        super(PseudostateMixin, self).__init__(**kwargs)

    def transitions_outgoing(self, diagnostics=None, context=None):
        """All transitions outgoing a fork vertex must target states in different regions of an orthogonal state.
(kind = PseudostateKind::fork) implies

-- for any pair of outgoing transitions there exists an orthogonal state which contains the targets of these transitions
-- such that these targets belong to different regions of that orthogonal state

outgoing->forAll(t1:Transition, t2:Transition | let contState:State = containingStateMachine().LCAState(t1.target, t2.target) in
        ((contState <> null) and (contState.region
                ->exists(r1:Region, r2: Region | (r1 <> r2) and t1.target.isContainedInRegion(r1) and t2.target.isContainedInRegion(r2)))))"""
        raise NotImplementedError(
            'operation transitions_outgoing(...) not yet implemented')

    def choice_vertex(self, diagnostics=None, context=None):
        """In a complete statemachine, a choice Vertex must have at least one incoming and one outgoing Transition.
(kind = PseudostateKind::choice) implies (incoming->size() >= 1 and outgoing->size() >= 1)"""
        raise NotImplementedError(
            'operation choice_vertex(...) not yet implemented')

    def outgoing_from_initial(self, diagnostics=None, context=None):
        """The outgoing Transition from an initial vertex may have a behavior, but not a trigger or a guard.
(kind = PseudostateKind::initial) implies (outgoing.guard = null and outgoing.trigger->isEmpty())"""
        raise NotImplementedError(
            'operation outgoing_from_initial(...) not yet implemented')

    def join_vertex(self, diagnostics=None, context=None):
        """In a complete StateMachine, a join Vertex must have at least two incoming Transitions and exactly one outgoing Transition.
(kind = PseudostateKind::join) implies (outgoing->size() = 1 and incoming->size() >= 2)"""
        raise NotImplementedError(
            'operation join_vertex(...) not yet implemented')

    def junction_vertex(self, diagnostics=None, context=None):
        """In a complete StateMachine, a junction Vertex must have at least one incoming and one outgoing Transition.
(kind = PseudostateKind::junction) implies (incoming->size() >= 1 and outgoing->size() >= 1)"""
        raise NotImplementedError(
            'operation junction_vertex(...) not yet implemented')

    def history_vertices(self, diagnostics=None, context=None):
        """History Vertices can have at most one outgoing Transition.
((kind = PseudostateKind::deepHistory) or (kind = PseudostateKind::shallowHistory)) implies (outgoing->size() <= 1)"""
        raise NotImplementedError(
            'operation history_vertices(...) not yet implemented')

    def initial_vertex(self, diagnostics=None, context=None):
        """An initial Vertex can have at most one outgoing Transition.
(kind = PseudostateKind::initial) implies (outgoing->size() <= 1)"""
        raise NotImplementedError(
            'operation initial_vertex(...) not yet implemented')

    def fork_vertex(self, diagnostics=None, context=None):
        """In a complete StateMachine, a fork Vertex must have at least two outgoing Transitions and exactly one incoming Transition.
(kind = PseudostateKind::fork) implies (incoming->size() = 1 and outgoing->size() >= 2)"""
        raise NotImplementedError(
            'operation fork_vertex(...) not yet implemented')

    def transitions_incoming(self, diagnostics=None, context=None):
        """All Transitions incoming a join Vertex must originate in different Regions of an orthogonal State.
(kind = PseudostateKind::join) implies

-- for any pair of incoming transitions there exists an orthogonal state which contains the source vetices of these transitions
-- such that these source vertices belong to different regions of that orthogonal state

incoming->forAll(t1:Transition, t2:Transition | let contState:State = containingStateMachine().LCAState(t1.source, t2.source) in
        ((contState <> null) and (contState.region
                ->exists(r1:Region, r2: Region | (r1 <> r2) and t1.source.isContainedInRegion(r1) and t2.source.isContainedInRegion(r2)))))"""
        raise NotImplementedError(
            'operation transitions_incoming(...) not yet implemented')


class ConnectionPointReferenceMixin(object):
    """User defined mixin class for ConnectionPointReference."""

    def __init__(self, entry=None, exit=None, state=None, **kwargs):
        super(ConnectionPointReferenceMixin, self).__init__(**kwargs)

    def exit_pseudostates(self, diagnostics=None, context=None):
        """The exit Pseudostates must be Pseudostates with kind exitPoint.
exit->forAll(kind = PseudostateKind::exitPoint)"""
        raise NotImplementedError(
            'operation exit_pseudostates(...) not yet implemented')

    def entry_pseudostates(self, diagnostics=None, context=None):
        """The entry Pseudostates must be Pseudostates with kind entryPoint.
entry->forAll(kind = PseudostateKind::entryPoint)"""
        raise NotImplementedError(
            'operation entry_pseudostates(...) not yet implemented')


class ProtocolConformanceMixin(object):
    """User defined mixin class for ProtocolConformance."""

    def __init__(self, generalMachine=None, specificMachine=None, **kwargs):
        super(ProtocolConformanceMixin, self).__init__(**kwargs)


class PackageMergeMixin(object):
    """User defined mixin class for PackageMerge."""

    def __init__(self, mergedPackage=None, receivingPackage=None, **kwargs):
        super(PackageMergeMixin, self).__init__(**kwargs)


class ProfileApplicationMixin(object):
    """User defined mixin class for ProfileApplication."""

    def __init__(self, appliedProfile=None, isStrict=None,
                 applyingPackage=None, **kwargs):
        super(ProfileApplicationMixin, self).__init__(**kwargs)

    def get_applied_definition(self):
        """Retrieves the definition (Ecore representation) of the profile associated with this profile application."""
        raise NotImplementedError(
            'operation get_applied_definition(...) not yet implemented')

    def get_applied_definition(self, namedElement=None):
        """Retrieves the definition (Ecore representation) of the specified named element in the profile associated with this profile application."""
        raise NotImplementedError(
            'operation get_applied_definition(...) not yet implemented')


class ElementImportMixin(object):
    """User defined mixin class for ElementImport."""

    def __init__(self, alias=None, importedElement=None,
                 importingNamespace=None, visibility=None, **kwargs):
        super(ElementImportMixin, self).__init__(**kwargs)

    def imported_element_is_public(self, diagnostics=None, context=None):
        """An importedElement has either public visibility or no visibility at all.
importedElement.visibility <> null implies importedElement.visibility = VisibilityKind::public"""
        raise NotImplementedError(
            'operation imported_element_is_public(...) not yet implemented')

    def visibility_public_or_private(self, diagnostics=None, context=None):
        """The visibility of an ElementImport is either public or private.
visibility = VisibilityKind::public or visibility = VisibilityKind::private"""
        raise NotImplementedError(
            'operation visibility_public_or_private(...) not yet implemented')

    def get_name(self):
        """The query getName() returns the name under which the imported PackageableElement will be known in the importing namespace.
result = (if alias->notEmpty() then
  alias
else
  importedElement.name
endif)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation get_name(...) not yet implemented')


class PackageImportMixin(object):
    """User defined mixin class for PackageImport."""

    def __init__(
            self, importedPackage=None, importingNamespace=None,
            visibility=None, **kwargs):
        super(PackageImportMixin, self).__init__(**kwargs)

    def public_or_private(self, diagnostics=None, context=None):
        """The visibility of a PackageImport is either public or private.
visibility = VisibilityKind::public or visibility = VisibilityKind::private"""
        raise NotImplementedError(
            'operation public_or_private(...) not yet implemented')


class GeneralizationMixin(object):
    """User defined mixin class for Generalization."""

    def __init__(self, general=None, generalizationSet=None,
                 isSubstitutable=None, specific=None, **kwargs):
        super(GeneralizationMixin, self).__init__(**kwargs)


class ExtensionPointMixin(object):
    """User defined mixin class for ExtensionPoint."""

    def __init__(self, useCase=None, **kwargs):
        super(ExtensionPointMixin, self).__init__(**kwargs)

    def must_have_name(self, diagnostics=None, context=None):
        """An ExtensionPoint must have a name.
name->notEmpty ()"""
        raise NotImplementedError(
            'operation must_have_name(...) not yet implemented')


class DerivedContainededge(EDerivedCollection):
    pass


class DerivedContainednode(EDerivedCollection):
    pass


class DerivedSubgroup(EDerivedCollection):
    pass


class ActivityGroupMixin(object):
    """User defined mixin class for ActivityGroup."""

    @property
    def inActivity(self):
        raise NotImplementedError('Missing implementation for inActivity')

    @inActivity.setter
    def inActivity(self, value):
        raise NotImplementedError('Missing implementation for inActivity')

    @property
    def superGroup(self):
        raise NotImplementedError('Missing implementation for superGroup')

    def __init__(self, containedEdge=None, containedNode=None,
                 inActivity=None, subgroup=None, superGroup=None, **kwargs):
        super(ActivityGroupMixin, self).__init__(**kwargs)

    def nodes_and_edges(self, diagnostics=None, context=None):
        """All containedNodes and containeEdges of an ActivityGroup must be in the same Activity as the group.
containedNode->forAll(activity = self.containingActivity()) and
containedEdge->forAll(activity = self.containingActivity())"""
        raise NotImplementedError(
            'operation nodes_and_edges(...) not yet implemented')

    def not_contained(self, diagnostics=None, context=None):
        """No containedNode or containedEdge of an ActivityGroup may be contained by its subgroups or its superGroups, transitively.
subgroup->closure(subgroup).containedNode->excludesAll(containedNode) and
superGroup->closure(superGroup).containedNode->excludesAll(containedNode) and
subgroup->closure(subgroup).containedEdge->excludesAll(containedEdge) and
superGroup->closure(superGroup).containedEdge->excludesAll(containedEdge)"""
        raise NotImplementedError(
            'operation not_contained(...) not yet implemented')


class DerivedIngroup(EDerivedCollection):
    pass


class ActivityEdgeMixin(object):
    """User defined mixin class for ActivityEdge."""

    def __init__(
            self, activity=None, guard=None, inPartition=None,
            interrupts=None, inStructuredNode=None, target=None, source=None,
            redefinedEdge=None, weight=None, inGroup=None, **kwargs):
        super(ActivityEdgeMixin, self).__init__(**kwargs)

    def source_and_target(self, diagnostics=None, context=None):
        """If an ActivityEdge is directly owned by an Activity, then its source and target must be directly or indirectly contained in the same Activity.
activity<>null implies source.containingActivity() = activity and target.containingActivity() = activity"""
        raise NotImplementedError(
            'operation source_and_target(...) not yet implemented')


class InteractionUseMixin(object):
    """User defined mixin class for InteractionUse."""

    def __init__(self, actualGate=None, argument=None, refersTo=None,
                 returnValue=None, returnValueRecipient=None, **kwargs):
        super(InteractionUseMixin, self).__init__(**kwargs)

    def gates_match(self, diagnostics=None, context=None):
        """Actual Gates of the InteractionUse must match Formal Gates of the referred Interaction. Gates match when their names are equal and their messages correspond.
actualGate->notEmpty() implies
refersTo.formalGate->forAll( fg : Gate | self.actualGate->select(matches(fg))->size()=1) and
self.actualGate->forAll(ag : Gate | refersTo.formalGate->select(matches(ag))->size()=1)"""
        raise NotImplementedError(
            'operation gates_match(...) not yet implemented')

    def arguments_are_constants(self, diagnostics=None, context=None):
        """The arguments must only be constants, parameters of the enclosing Interaction or attributes of the classifier owning the enclosing Interaction."""
        raise NotImplementedError(
            'operation arguments_are_constants(...) not yet implemented')

    def return_value_recipient_coverage(self, diagnostics=None, context=None):
        """The returnValueRecipient must be a Property of a ConnectableElement that is represented by a Lifeline covered by this InteractionUse.
returnValueRecipient->asSet()->notEmpty() implies
let covCE : Set(ConnectableElement) = covered.represents->asSet() in
covCE->notEmpty() and let classes:Set(Classifier) = covCE.type.oclIsKindOf(Classifier).oclAsType(Classifier)->asSet() in
let allProps : Set(Property) = classes.attribute->union(classes.allParents().attribute)->asSet() in
allProps->includes(returnValueRecipient)"""
        raise NotImplementedError(
            'operation return_value_recipient_coverage(...) not yet implemented')

    def arguments_correspond_to_parameters(
            self, diagnostics=None, context=None):
        """The arguments of the InteractionUse must correspond to parameters of the referred Interaction."""
        raise NotImplementedError(
            'operation arguments_correspond_to_parameters(...) not yet implemented')

    def return_value_type_recipient_correspondence(
            self, diagnostics=None, context=None):
        """The type of the returnValue must correspond to the type of the returnValueRecipient.
returnValue.type->asSequence()->notEmpty() implies returnValue.type->asSequence()->first() = returnValueRecipient.type->asSequence()->first()"""
        raise NotImplementedError(
            'operation return_value_type_recipient_correspondence(...) not yet implemented')

    def all_lifelines(self, diagnostics=None, context=None):
        """The InteractionUse must cover all Lifelines of the enclosing Interaction that are common with the lifelines covered by the referred Interaction. Lifelines are common if they have the same selector and represents associationEnd values.
let parentInteraction : Set(Interaction) = enclosingInteraction->asSet()->
union(enclosingOperand.combinedFragment->closure(enclosingOperand.combinedFragment)->
collect(enclosingInteraction).oclAsType(Interaction)->asSet()) in
parentInteraction->size()=1 and let refInteraction : Interaction = refersTo in
parentInteraction.covered-> forAll(intLifeline : Lifeline | refInteraction.covered->
forAll( refLifeline : Lifeline | refLifeline.represents = intLifeline.represents and
(
( refLifeline.selector.oclIsKindOf(LiteralString) implies
  intLifeline.selector.oclIsKindOf(LiteralString) and
  refLifeline.selector.oclAsType(LiteralString).value = intLifeline.selector.oclAsType(LiteralString).value ) and
( refLifeline.selector.oclIsKindOf(LiteralInteger) implies
  intLifeline.selector.oclIsKindOf(LiteralInteger) and
  refLifeline.selector.oclAsType(LiteralInteger).value = intLifeline.selector.oclAsType(LiteralInteger).value )
)
 implies self.covered->asSet()->includes(intLifeline)))"""
        raise NotImplementedError(
            'operation all_lifelines(...) not yet implemented')


class GateMixin(object):
    """User defined mixin class for Gate."""

    def __init__(self, **kwargs):
        super(GateMixin, self).__init__(**kwargs)

    def actual_gate_matched(self, diagnostics=None, context=None):
        """If this Gate is an actualGate, it must have exactly one matching formalGate within the referred Interaction.
interactionUse->notEmpty() implies interactionUse.refersTo.formalGate->select(matches(self))->size()=1"""
        raise NotImplementedError(
            'operation actual_gate_matched(...) not yet implemented')

    def inside_cf_matched(self, diagnostics=None, context=None):
        """If this Gate is inside a CombinedFragment, it must have exactly one matching Gate which is outside of that CombinedFragment.
isInsideCF() implies combinedFragment.cfragmentGate->select(isOutsideCF() and matches(self))->size()=1"""
        raise NotImplementedError(
            'operation inside_cf_matched(...) not yet implemented')

    def outside_cf_matched(self, diagnostics=None, context=None):
        """If this Gate is outside an 'alt' CombinedFragment,  for every InteractionOperator inside that CombinedFragment there must be exactly one matching Gate inside the CombindedFragment with its opposing end enclosed by that InteractionOperator. If this Gate is outside CombinedFragment with operator other than 'alt',   there must be exactly one matching Gate inside that CombinedFragment.
isOutsideCF() implies
 if self.combinedFragment.interactionOperator->asOrderedSet()->first() = InteractionOperatorKind::alt
 then self.combinedFragment.operand->forAll(op : InteractionOperand |
 self.combinedFragment.cfragmentGate->select(isInsideCF() and
 oppositeEnd().enclosingFragment()->includes(self.combinedFragment) and matches(self))->size()=1)
 else  self.combinedFragment.cfragmentGate->select(isInsideCF() and matches(self))->size()=1
 endif"""
        raise NotImplementedError(
            'operation outside_cf_matched(...) not yet implemented')

    def formal_gate_distinguishable(self, diagnostics=None, context=None):
        """isFormal() implies that no other formalGate of the parent Interaction returns the same getName() as returned for self
isFormal() implies interaction.formalGate->select(getName() = self.getName())->size()=1"""
        raise NotImplementedError(
            'operation formal_gate_distinguishable(...) not yet implemented')

    def actual_gate_distinguishable(self, diagnostics=None, context=None):
        """isActual() implies that no other actualGate of the parent InteractionUse returns the same getName() as returned for self
isActual() implies interactionUse.actualGate->select(getName() = self.getName())->size()=1"""
        raise NotImplementedError(
            'operation actual_gate_distinguishable(...) not yet implemented')

    def outside_cf_gate_distinguishable(self, diagnostics=None, context=None):
        """isOutsideCF() implies that no other outside cfragmentGate of the parent CombinedFragment returns the same getName() as returned for self
isOutsideCF() implies combinedFragment.cfragmentGate->select(getName() = self.getName())->size()=1"""
        raise NotImplementedError(
            'operation outside_cf_gate_distinguishable(...) not yet implemented')

    def inside_cf_gate_distinguishable(self, diagnostics=None, context=None):
        """isInsideCF() implies that no other inside cfragmentGate attached to a message with its other end in the same InteractionOperator as self, returns the same getName() as returned for self
isInsideCF() implies
let selfOperand : InteractionOperand = self.getOperand() in
  combinedFragment.cfragmentGate->select(isInsideCF() and getName() = self.getName())->select(getOperand() = selfOperand)->size()=1"""
        raise NotImplementedError(
            'operation inside_cf_gate_distinguishable(...) not yet implemented')

    def is_outside_cf(self):
        """This query returns true if this Gate is attached to the boundary of a CombinedFragment, and its other end (if present)  is outside of the same CombinedFragment.
result = (self.oppositeEnd()-> notEmpty() and combinedFragment->notEmpty() implies
let oppEnd : MessageEnd = self.oppositeEnd()->asOrderedSet()->first() in
if oppEnd.oclIsKindOf(MessageOccurrenceSpecification)
then let oppMOS : MessageOccurrenceSpecification = oppEnd.oclAsType(MessageOccurrenceSpecification)
in  self.combinedFragment.enclosingInteraction.oclAsType(InteractionFragment)->asSet()->
     union(self.combinedFragment.enclosingOperand.oclAsType(InteractionFragment)->asSet()) =
     oppMOS.enclosingInteraction.oclAsType(InteractionFragment)->asSet()->
     union(oppMOS.enclosingOperand.oclAsType(InteractionFragment)->asSet())
else let oppGate : Gate = oppEnd.oclAsType(Gate)
in self.combinedFragment.enclosingInteraction.oclAsType(InteractionFragment)->asSet()->
     union(self.combinedFragment.enclosingOperand.oclAsType(InteractionFragment)->asSet()) =
     oppGate.combinedFragment.enclosingInteraction.oclAsType(InteractionFragment)->asSet()->
     union(oppGate.combinedFragment.enclosingOperand.oclAsType(InteractionFragment)->asSet())
endif)
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError(
            'operation is_outside_cf(...) not yet implemented')

    def is_inside_cf(self):
        """This query returns true if this Gate is attached to the boundary of a CombinedFragment, and its other end (if present) is inside of an InteractionOperator of the same CombinedFragment.
result = (self.oppositeEnd()-> notEmpty() and combinedFragment->notEmpty() implies
let oppEnd : MessageEnd = self.oppositeEnd()->asOrderedSet()->first() in
if oppEnd.oclIsKindOf(MessageOccurrenceSpecification)
then let oppMOS : MessageOccurrenceSpecification
= oppEnd.oclAsType(MessageOccurrenceSpecification)
in combinedFragment = oppMOS.enclosingOperand.combinedFragment
else let oppGate : Gate = oppEnd.oclAsType(Gate)
in combinedFragment = oppGate.combinedFragment.enclosingOperand.combinedFragment
endif)
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError(
            'operation is_inside_cf(...) not yet implemented')

    def is_actual(self):
        """This query returns true value if this Gate is an actualGate of an InteractionUse.
result = (interactionUse->notEmpty())
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError(
            'operation is_actual(...) not yet implemented')

    def is_formal(self):
        """This query returns true if this Gate is a formalGate of an Interaction.
result = (interaction->notEmpty())
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError(
            'operation is_formal(...) not yet implemented')

    def get_name(self):
        """This query returns the name of the gate, either the explicit name (.name) or the constructed name ('out_" or 'in_' concatenated in front of .message.name) if the explicit name is not present.
result = (if name->notEmpty() then name->asOrderedSet()->first()
else  if isActual() or isOutsideCF()
  then if isSend()
    then 'out_'.concat(self.message.name->asOrderedSet()->first())
    else 'in_'.concat(self.message.name->asOrderedSet()->first())
    endif
  else if isSend()
    then 'in_'.concat(self.message.name->asOrderedSet()->first())
    else 'out_'.concat(self.message.name->asOrderedSet()->first())
    endif
  endif
endif)
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError(
            'operation get_name(...) not yet implemented')

    def matches(self, gateToMatch=None):
        """This query returns true if the name of this Gate matches the name of the in parameter Gate, and the messages for the two Gates correspond. The Message for one Gate (say A) corresponds to the Message for another Gate (say B) if (A and B have the same name value) and (if A is a sendEvent then B is a receiveEvent) and (if A is a receiveEvent then B is a sendEvent) and (A and B have the same messageSort value) and (A and B have the same signature value).
result = (self.getName() = gateToMatch.getName() and
self.message.messageSort = gateToMatch.message.messageSort and
self.message.name = gateToMatch.message.name and
self.message.sendEvent->includes(self) implies gateToMatch.message.receiveEvent->includes(gateToMatch)  and
self.message.receiveEvent->includes(self) implies gateToMatch.message.sendEvent->includes(gateToMatch) and
self.message.signature = gateToMatch.message.signature)
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError('operation matches(...) not yet implemented')

    def get_operand(self):
        """If the Gate is an inside Combined Fragment Gate, this operation returns the InteractionOperand that the opposite end of this Gate is included within.
result = (if isInsideCF() then
  let oppEnd : MessageEnd = self.oppositeEnd()->asOrderedSet()->first() in
    if oppEnd.oclIsKindOf(MessageOccurrenceSpecification)
    then let oppMOS : MessageOccurrenceSpecification = oppEnd.oclAsType(MessageOccurrenceSpecification)
        in oppMOS.enclosingOperand->asOrderedSet()->first()
    else let oppGate : Gate = oppEnd.oclAsType(Gate)
        in oppGate.combinedFragment.enclosingOperand->asOrderedSet()->first()
    endif
  else null
endif)
<p>From package UML::Interactions.</p>"""
        raise NotImplementedError(
            'operation get_operand(...) not yet implemented')


class OccurrenceSpecificationMixin(object):
    """User defined mixin class for OccurrenceSpecification."""

    def __init__(self, toAfter=None, toBefore=None, **kwargs):
        super(OccurrenceSpecificationMixin, self).__init__(**kwargs)

    def get_covered(self):
        """Returns the Lifeline on which the OccurrenceSpecification appears."""
        raise NotImplementedError(
            'operation get_covered(...) not yet implemented')

    def set_covered(self, value=None):
        """Sets the Lifeline on which the OccurrenceSpecification appears."""
        raise NotImplementedError(
            'operation set_covered(...) not yet implemented')


class ExecutionSpecificationMixin(object):
    """User defined mixin class for ExecutionSpecification."""

    def __init__(self, finish=None, start=None, **kwargs):
        super(ExecutionSpecificationMixin, self).__init__(**kwargs)

    def same_lifeline(self, diagnostics=None, context=None):
        """The startEvent and the finishEvent must be on the same Lifeline.
start.covered = finish.covered"""
        raise NotImplementedError(
            'operation same_lifeline(...) not yet implemented')


class CombinedFragmentMixin(object):
    """User defined mixin class for CombinedFragment."""

    def __init__(
            self, cfragmentGate=None, interactionOperator=None,
            operand=None, **kwargs):
        super(CombinedFragmentMixin, self).__init__(**kwargs)

    def break_(self, diagnostics=None, context=None):
        """If the interactionOperator is break, the corresponding InteractionOperand must cover all Lifelines covered by the enclosing InteractionFragment.
interactionOperator=InteractionOperatorKind::break  implies
enclosingInteraction.oclAsType(InteractionFragment)->asSet()->union(
   enclosingOperand.oclAsType(InteractionFragment)->asSet()).covered->asSet() = self.covered->asSet()"""
        raise NotImplementedError('operation break_(...) not yet implemented')

    def consider_and_ignore(self, diagnostics=None, context=None):
        """The interaction operators 'consider' and 'ignore' can only be used for the ConsiderIgnoreFragment subtype of CombinedFragment
((interactionOperator = InteractionOperatorKind::consider) or (interactionOperator =  InteractionOperatorKind::ignore)) implies oclIsKindOf(ConsiderIgnoreFragment)"""
        raise NotImplementedError(
            'operation consider_and_ignore(...) not yet implemented')

    def opt_loop_break_neg(self, diagnostics=None, context=None):
        """If the interactionOperator is opt, loop, break, assert or neg, there must be exactly one operand.
(interactionOperator =  InteractionOperatorKind::opt or interactionOperator = InteractionOperatorKind::loop or
interactionOperator = InteractionOperatorKind::break or interactionOperator = InteractionOperatorKind::assert or
interactionOperator = InteractionOperatorKind::neg)
implies operand->size()=1"""
        raise NotImplementedError(
            'operation opt_loop_break_neg(...) not yet implemented')


class ContinuationMixin(object):
    """User defined mixin class for Continuation."""

    def __init__(self, setting=None, **kwargs):
        super(ContinuationMixin, self).__init__(**kwargs)

    def first_or_last_interaction_fragment(
            self, diagnostics=None, context=None):
        """Continuations always occur as the very first InteractionFragment or the very last InteractionFragment of the enclosing InteractionOperand.
 enclosingOperand->notEmpty() and
 let peerFragments : OrderedSet(InteractionFragment) =  enclosingOperand.fragment in
   ( peerFragments->notEmpty() and
   ((peerFragments->first() = self) or  (peerFragments->last() = self)))"""
        raise NotImplementedError(
            'operation first_or_last_interaction_fragment(...) not yet implemented')

    def same_name(self, diagnostics=None, context=None):
        """Across all Interaction instances having the same context value, every Lifeline instance covered by a Continuation (self) must be common with one covered Lifeline instance of all other Continuation instances with the same name as self, and every Lifeline instance covered by a Continuation instance with the same name as self must be common with one covered Lifeline instance of self. Lifeline instances are common if they have the same selector and represents associationEnd values.
enclosingOperand.combinedFragment->notEmpty() and
let parentInteraction : Set(Interaction) =
enclosingOperand.combinedFragment->closure(enclosingOperand.combinedFragment)->
collect(enclosingInteraction).oclAsType(Interaction)->asSet()
in
(parentInteraction->size() = 1)
and let peerInteractions : Set(Interaction) =
 (parentInteraction->union(parentInteraction->collect(_'context')->collect(behavior)->
 select(oclIsKindOf(Interaction)).oclAsType(Interaction)->asSet())->asSet()) in
 (peerInteractions->notEmpty()) and
  let combinedFragments1 : Set(CombinedFragment) = peerInteractions.fragment->
 select(oclIsKindOf(CombinedFragment)).oclAsType(CombinedFragment)->asSet() in
   combinedFragments1->notEmpty() and  combinedFragments1->closure(operand.fragment->
   select(oclIsKindOf(CombinedFragment)).oclAsType(CombinedFragment))->asSet().operand.fragment->
   select(oclIsKindOf(Continuation)).oclAsType(Continuation)->asSet()->
   forAll(c : Continuation |  (c.name = self.name) implies
  (c.covered->asSet()->forAll(cl : Lifeline | --  cl must be common to one lifeline covered by self
  self.covered->asSet()->
  select(represents = cl.represents and selector = cl.selector)->asSet()->size()=1))
   and
 (self.covered->asSet()->forAll(cl : Lifeline | --  cl must be common to one lifeline covered by c
 c.covered->asSet()->
  select(represents = cl.represents and selector = cl.selector)->asSet()->size()=1))
  )"""
        raise NotImplementedError(
            'operation same_name(...) not yet implemented')

    def global_(self, diagnostics=None, context=None):
        """Continuations are always global in the enclosing InteractionFragment e.g., it always covers all Lifelines covered by the enclosing InteractionOperator.
enclosingOperand->notEmpty() and
  let operandLifelines : Set(Lifeline) =  enclosingOperand.covered in
    (operandLifelines->notEmpty() and
    operandLifelines->forAll(ol :Lifeline |self.covered->includes(ol)))"""
        raise NotImplementedError('operation global_(...) not yet implemented')


class StateInvariantMixin(object):
    """User defined mixin class for StateInvariant."""

    def __init__(self, invariant=None, **kwargs):
        super(StateInvariantMixin, self).__init__(**kwargs)


class TypeMixin(object):
    """User defined mixin class for Type."""

    @property
    def package(self):
        raise NotImplementedError('Missing implementation for package')

    @package.setter
    def package(self, value):
        raise NotImplementedError('Missing implementation for package')

    def __init__(self, package=None, **kwargs):
        super(TypeMixin, self).__init__(**kwargs)

    def create_association(
            self, end1IsNavigable=None, end1Aggregation=None, end1Name=None,
            end1Lower=None, end1Upper=None, end1Type=None,
            end2IsNavigable=None, end2Aggregation=None, end2Name=None,
            end2Lower=None, end2Upper=None):
        """Creates a(n) (binary) association between this type and the specified other type, with the specified navigabilities, aggregations, names, lower bounds, and upper bounds, and owned by this type's nearest package."""
        raise NotImplementedError(
            'operation create_association(...) not yet implemented')

    def get_associations(self):
        """Retrieves the associations in which this type is involved."""
        raise NotImplementedError(
            'operation get_associations(...) not yet implemented')

    def conforms_to(self, other=None):
        """The query conformsTo() gives true for a Type that conforms to another. By default, two Types do not conform to each other. This query is intended to be redefined for specific conformance situations.
result = (false)
<p>From package UML::CommonStructure.</p>"""
        raise NotImplementedError(
            'operation conforms_to(...) not yet implemented')


class DerivedEnd(EDerivedCollection):
    pass


class ConnectableElementMixin(object):
    """User defined mixin class for ConnectableElement."""

    def __init__(self, end=None, **kwargs):
        super(ConnectableElementMixin, self).__init__(**kwargs)

    def get_ends(self):
        """Derivation for ConnectableElement::/end : ConnectorEnd
result = (ConnectorEnd.allInstances()->select(role = self))
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_ends(...) not yet implemented')


class ConstraintMixin(object):
    """User defined mixin class for Constraint."""

    def __init__(self, constrainedElement=None, context=None,
                 specification=None, **kwargs):
        super(ConstraintMixin, self).__init__(**kwargs)

    def boolean_value(self, diagnostics=None, context=None):
        """The ValueSpecification for a Constraint must evaluate to a Boolean value."""
        raise NotImplementedError(
            'operation boolean_value(...) not yet implemented')

    def no_side_effects(self, diagnostics=None, context=None):
        """Evaluating the ValueSpecification for a Constraint must not have side effects."""
        raise NotImplementedError(
            'operation no_side_effects(...) not yet implemented')

    def not_apply_to_self(self, diagnostics=None, context=None):
        """A Constraint cannot be applied to itself.
not constrainedElement->includes(self)"""
        raise NotImplementedError(
            'operation not_apply_to_self(...) not yet implemented')


class RegionMixin(object):
    """User defined mixin class for Region."""

    def __init__(
            self, extendedRegion=None, state=None, stateMachine=None,
            transition=None, subvertex=None, **kwargs):
        super(RegionMixin, self).__init__(**kwargs)

    def deep_history_vertex(self, diagnostics=None, context=None):
        """A Region can have at most one deep history Vertex.
self.subvertex->select (oclIsKindOf(Pseudostate))->collect(oclAsType(Pseudostate))->
   select(kind = PseudostateKind::deepHistory)->size() <= 1"""
        raise NotImplementedError(
            'operation deep_history_vertex(...) not yet implemented')

    def shallow_history_vertex(self, diagnostics=None, context=None):
        """A Region can have at most one shallow history Vertex.
subvertex->select(oclIsKindOf(Pseudostate))->collect(oclAsType(Pseudostate))->
  select(kind = PseudostateKind::shallowHistory)->size() <= 1"""
        raise NotImplementedError(
            'operation shallow_history_vertex(...) not yet implemented')

    def owned(self, diagnostics=None, context=None):
        """If a Region is owned by a StateMachine, then it cannot also be owned by a State and vice versa.
(stateMachine <> null implies state = null) and (state <> null implies stateMachine = null)"""
        raise NotImplementedError('operation owned(...) not yet implemented')

    def initial_vertex(self, diagnostics=None, context=None):
        """A Region can have at most one initial Vertex.
self.subvertex->select (oclIsKindOf(Pseudostate))->collect(oclAsType(Pseudostate))->
  select(kind = PseudostateKind::initial)->size() <= 1"""
        raise NotImplementedError(
            'operation initial_vertex(...) not yet implemented')

    def belongs_to_psm(self):
        """The operation belongsToPSM () checks if the Region belongs to a ProtocolStateMachine.
result = (if  stateMachine <> null
then
  stateMachine.oclIsKindOf(ProtocolStateMachine)
else
  state <> null  implies  state.container.belongsToPSM()
endif )
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation belongs_to_psm(...) not yet implemented')

    def containing_state_machine(self):
        """The operation containingStateMachine() returns the StateMachine in which this Region is defined.
result = (if stateMachine = null
then
  state.containingStateMachine()
else
  stateMachine
endif)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation containing_state_machine(...) not yet implemented')

    def redefinition_context(self):
        """The redefinition context of a Region is the nearest containing StateMachine.
result = (let sm : StateMachine = containingStateMachine() in
if sm._'context' = null or sm.general->notEmpty() then
  sm
else
  sm._'context'
endif)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation redefinition_context(...) not yet implemented')


class EventMixin(object):
    """User defined mixin class for Event."""

    def __init__(self, **kwargs):
        super(EventMixin, self).__init__(**kwargs)


class TransitionMixin(object):
    """User defined mixin class for Transition."""

    def __init__(self, effect=None, guard=None, kind=None,
                 redefinedTransition=None, source=None, target=None,
                 trigger=None, container=None, **kwargs):
        super(TransitionMixin, self).__init__(**kwargs)

    def state_is_external(self, diagnostics=None, context=None):
        """A Transition with kind external can source any Vertex except entry points.
(kind = TransitionKind::external) implies
        not (source.oclIsKindOf(Pseudostate) and source.oclAsType(Pseudostate).kind = PseudostateKind::entryPoint)"""
        raise NotImplementedError(
            'operation state_is_external(...) not yet implemented')

    def join_segment_guards(self, diagnostics=None, context=None):
        """A join segment must not have Guards or Triggers.
(target.oclIsKindOf(Pseudostate) and target.oclAsType(Pseudostate).kind = PseudostateKind::join) implies (guard = null and trigger->isEmpty())"""
        raise NotImplementedError(
            'operation join_segment_guards(...) not yet implemented')

    def state_is_internal(self, diagnostics=None, context=None):
        """A Transition with kind internal must have a State as its source, and its source and target must be equal.
(kind = TransitionKind::internal) implies
                (source.oclIsKindOf (State) and source = target)"""
        raise NotImplementedError(
            'operation state_is_internal(...) not yet implemented')

    def outgoing_pseudostates(self, diagnostics=None, context=None):
        """Transitions outgoing Pseudostates may not have a Trigger.
source.oclIsKindOf(Pseudostate) and (source.oclAsType(Pseudostate).kind <> PseudostateKind::initial) implies trigger->isEmpty()"""
        raise NotImplementedError(
            'operation outgoing_pseudostates(...) not yet implemented')

    def join_segment_state(self, diagnostics=None, context=None):
        """A join segment must always originate from a State.
(target.oclIsKindOf(Pseudostate) and target.oclAsType(Pseudostate).kind = PseudostateKind::join) implies (source.oclIsKindOf(State))"""
        raise NotImplementedError(
            'operation join_segment_state(...) not yet implemented')

    def fork_segment_state(self, diagnostics=None, context=None):
        """A fork segment must always target a State.
(source.oclIsKindOf(Pseudostate) and  source.oclAsType(Pseudostate).kind = PseudostateKind::fork) implies (target.oclIsKindOf(State))"""
        raise NotImplementedError(
            'operation fork_segment_state(...) not yet implemented')

    def state_is_local(self, diagnostics=None, context=None):
        """A Transition with kind local must have a composite State or an entry point as its source.
(kind = TransitionKind::local) implies
                ((source.oclIsKindOf (State) and source.oclAsType(State).isComposite) or
                (source.oclIsKindOf (Pseudostate) and source.oclAsType(Pseudostate).kind = PseudostateKind::entryPoint))"""
        raise NotImplementedError(
            'operation state_is_local(...) not yet implemented')

    def initial_transition(self, diagnostics=None, context=None):
        """An initial Transition at the topmost level Region of a StateMachine that has no Trigger.
(source.oclIsKindOf(Pseudostate) and container.stateMachine->notEmpty()) implies
        trigger->isEmpty()"""
        raise NotImplementedError(
            'operation initial_transition(...) not yet implemented')

    def fork_segment_guards(self, diagnostics=None, context=None):
        """A fork segment must not have Guards or Triggers.
(source.oclIsKindOf(Pseudostate) and source.oclAsType(Pseudostate).kind = PseudostateKind::fork) implies (guard = null and trigger->isEmpty())"""
        raise NotImplementedError(
            'operation fork_segment_guards(...) not yet implemented')

    def containing_state_machine(self):
        """The query containingStateMachine() returns the StateMachine that contains the Transition either directly or transitively.
result = (container.containingStateMachine())
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation containing_state_machine(...) not yet implemented')

    def redefinition_context(self):
        """The redefinition context of a Transition is the nearest containing StateMachine.
result = (let sm : StateMachine = containingStateMachine() in
if sm._'context' = null or sm.general->notEmpty() then
  sm
else
  sm._'context'
endif)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation redefinition_context(...) not yet implemented')


class ConnectorMixin(object):
    """User defined mixin class for Connector."""

    @property
    def kind(self):
        raise NotImplementedError('Missing implementation for kind')

    def __init__(self, contract=None, end=None, kind=None,
                 redefinedConnector=None, type=None, **kwargs):
        super(ConnectorMixin, self).__init__(**kwargs)

    def types(self, diagnostics=None, context=None):
        """The types of the ConnectableElements that the ends of a Connector are attached to must conform to the types of the ends of the Association that types the Connector, if any.
type<>null implies
  let noOfEnds : Integer = end->size() in
  (type.memberEnd->size() = noOfEnds) and Sequence{1..noOfEnds}->forAll(i | end->at(i).role.type.conformsTo(type.memberEnd->at(i).type))"""
        raise NotImplementedError('operation types(...) not yet implemented')

    def roles(self, diagnostics=None, context=None):
        """The ConnectableElements attached as roles to each ConnectorEnd owned by a Connector must be owned or inherited roles of the Classifier that owned the Connector, or they must be Ports of such roles.
structuredClassifier <> null
and
  end->forAll( e | structuredClassifier.allRoles()->includes(e.role)
or
  e.role.oclIsKindOf(Port) and structuredClassifier.allRoles()->includes(e.partWithPort))"""
        raise NotImplementedError('operation roles(...) not yet implemented')

    def get_kind(self):
        """Derivation for Connector::/kind : ConnectorKind
result = (if end->exists(
                role.oclIsKindOf(Port)
                and partWithPort->isEmpty()
                and not role.oclAsType(Port).isBehavior)
then ConnectorKind::delegation
else ConnectorKind::assembly
endif)
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_kind(...) not yet implemented')


class GeneralizationSetMixin(object):
    """User defined mixin class for GeneralizationSet."""

    def __init__(
            self, isCovering=None, isDisjoint=None, powertype=None,
            generalization=None, **kwargs):
        super(GeneralizationSetMixin, self).__init__(**kwargs)

    def generalization_same_classifier(self, diagnostics=None, context=None):
        """Every Generalization associated with a particular GeneralizationSet must have the same general Classifier.
generalization->collect(general)->asSet()->size() <= 1"""
        raise NotImplementedError(
            'operation generalization_same_classifier(...) not yet implemented')

    def maps_to_generalization_set(self, diagnostics=None, context=None):
        """The Classifier that maps to a GeneralizationSet may neither be a specific nor a general Classifier in any of the Generalization relationships defined for that GeneralizationSet. In other words, a power type may not be an instance of itself nor may its instances be its subclasses.
powertype <> null implies generalization->forAll( gen |
    not (gen.general = powertype) and not gen.general.allParents()->includes(powertype) and not (gen.specific = powertype) and not powertype.allParents()->includes(gen.specific)
  )"""
        raise NotImplementedError(
            'operation maps_to_generalization_set(...) not yet implemented')


class DerivedInheritedparameter(EDerivedCollection):
    pass


class RedefinableTemplateSignatureMixin(object):
    """User defined mixin class for RedefinableTemplateSignature."""

    def __init__(
            self, extendedSignature=None, inheritedParameter=None,
            classifier=None, **kwargs):
        super(RedefinableTemplateSignatureMixin, self).__init__(**kwargs)

    def redefines_parents(self, diagnostics=None, context=None):
        """If any of the parent Classifiers are a template, then the extendedSignature must include the signature of that Classifier.
classifier.allParents()->forAll(c | c.ownedTemplateSignature->notEmpty() implies self->closure(extendedSignature)->includes(c.ownedTemplateSignature))"""
        raise NotImplementedError(
            'operation redefines_parents(...) not yet implemented')

    def get_inherited_parameters(self):
        """Derivation for RedefinableTemplateSignature::/inheritedParameter
result = (if extendedSignature->isEmpty() then Set{} else extendedSignature.parameter->asSet() endif)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation get_inherited_parameters(...) not yet implemented')


class ExtendMixin(object):
    """User defined mixin class for Extend."""

    def __init__(self, condition=None, extendedCase=None,
                 extensionLocation=None, extension=None, **kwargs):
        super(ExtendMixin, self).__init__(**kwargs)

    def extension_points(self, diagnostics=None, context=None):
        """The ExtensionPoints referenced by the Extend relationship must belong to the UseCase that is being extended.
extensionLocation->forAll (xp | extendedCase.extensionPoint->includes(xp))"""
        raise NotImplementedError(
            'operation extension_points(...) not yet implemented')


class IncludeMixin(object):
    """User defined mixin class for Include."""

    def __init__(self, addition=None, includingCase=None, **kwargs):
        super(IncludeMixin, self).__init__(**kwargs)


class ActivityPartitionMixin(object):
    """User defined mixin class for ActivityPartition."""

    def __init__(
            self, isDimension=None, isExternal=None, node=None,
            represents=None, subpartition=None, superPartition=None, edge=None,
            **kwargs):
        super(ActivityPartitionMixin, self).__init__(**kwargs)

    def represents_classifier(self, diagnostics=None, context=None):
        """If a non-external ActivityPartition represents a Classifier and has a superPartition, then the superPartition must represent a Classifier, and the Classifier of the subpartition must be nested (nestedClassifier or ownedBehavior) in the Classifier represented by the superPartition, or be at the contained end of a composition Association with the Classifier represented by the superPartition.
(not isExternal and represents.oclIsKindOf(Classifier) and superPartition->notEmpty()) implies
(
   let representedClassifier : Classifier = represents.oclAsType(Classifier) in
     superPartition.represents.oclIsKindOf(Classifier) and
      let representedSuperClassifier : Classifier = superPartition.represents.oclAsType(Classifier) in
       (representedSuperClassifier.oclIsKindOf(BehavioredClassifier) and representedClassifier.oclIsKindOf(Behavior) and
        representedSuperClassifier.oclAsType(BehavioredClassifier).ownedBehavior->includes(representedClassifier.oclAsType(Behavior)))
       or
       (representedSuperClassifier.oclIsKindOf(Class) and  representedSuperClassifier.oclAsType(Class).nestedClassifier->includes(representedClassifier))
       or
       (Association.allInstances()->exists(a | a.memberEnd->exists(end1 | end1.isComposite and end1.type = representedClassifier and
                                                                      a.memberEnd->exists(end2 | end1<>end2 and end2.type = representedSuperClassifier))))
)"""
        raise NotImplementedError(
            'operation represents_classifier(...) not yet implemented')

    def represents_property_and_is_contained(
            self, diagnostics=None, context=None):
        """If an ActivityPartition represents a Property and has a superPartition, then the Property must be of a Classifier represented by the superPartition, or of a Classifier that is the type of a Property represented by the superPartition.
(represents.oclIsKindOf(Property) and superPartition->notEmpty()) implies
(
  (superPartition.represents.oclIsKindOf(Classifier) and represents.owner = superPartition.represents) or
  (superPartition.represents.oclIsKindOf(Property) and represents.owner = superPartition.represents.oclAsType(Property).type)
)"""
        raise NotImplementedError(
            'operation represents_property_and_is_contained(...) not yet implemented')

    def represents_property(self, diagnostics=None, context=None):
        """If an ActivityPartition represents a Property and has a superPartition representing a Classifier, then all the other non-external subpartitions of the superPartition must represent Properties directly owned by the same Classifier.
(represents.oclIsKindOf(Property) and superPartition->notEmpty() and superPartition.represents.oclIsKindOf(Classifier)) implies
(
  let representedClassifier : Classifier = superPartition.represents.oclAsType(Classifier)
  in
    superPartition.subpartition->reject(isExternal)->forAll(p |
       p.represents.oclIsKindOf(Property) and p.owner=representedClassifier)
)"""
        raise NotImplementedError(
            'operation represents_property(...) not yet implemented')

    def dimension_not_contained(self, diagnostics=None, context=None):
        """An ActvivityPartition with isDimension = true may not be contained by another ActivityPartition.
isDimension implies superPartition->isEmpty()"""
        raise NotImplementedError(
            'operation dimension_not_contained(...) not yet implemented')


class DerivedIngroup(EDerivedCollection):
    pass


class ActivityNodeMixin(object):
    """User defined mixin class for ActivityNode."""

    @property
    def activity(self):
        raise NotImplementedError('Missing implementation for activity')

    @activity.setter
    def activity(self, value):
        raise NotImplementedError('Missing implementation for activity')

    def __init__(self, activity=None, inGroup=None,
                 inInterruptibleRegion=None, inStructuredNode=None,
                 incoming=None, outgoing=None, redefinedNode=None,
                 inPartition=None, **kwargs):
        super(ActivityNodeMixin, self).__init__(**kwargs)


class InterruptibleActivityRegionMixin(object):
    """User defined mixin class for InterruptibleActivityRegion."""

    def __init__(self, interruptingEdge=None, node=None, **kwargs):
        super(InterruptibleActivityRegionMixin, self).__init__(**kwargs)

    def interrupting_edges(self, diagnostics=None, context=None):
        """The interruptingEdges of an InterruptibleActivityRegion must have their source in the region and their target outside the region, but within the same Activity containing the region.
interruptingEdge->forAll(edge |
  node->includes(edge.source) and node->excludes(edge.target) and edge.target.containingActivity() = inActivity)"""
        raise NotImplementedError(
            'operation interrupting_edges(...) not yet implemented')


class ControlFlowMixin(object):
    """User defined mixin class for ControlFlow."""

    def __init__(self, **kwargs):
        super(ControlFlowMixin, self).__init__(**kwargs)

    def object_nodes(self, diagnostics=None, context=None):
        """ControlFlows may not have ObjectNodes at either end, except for ObjectNodes with control type.
(source.oclIsKindOf(ObjectNode) implies source.oclAsType(ObjectNode).isControlType) and
(target.oclIsKindOf(ObjectNode) implies target.oclAsType(ObjectNode).isControlType)"""
        raise NotImplementedError(
            'operation object_nodes(...) not yet implemented')


class ObjectFlowMixin(object):
    """User defined mixin class for ObjectFlow."""

    def __init__(self, isMulticast=None, isMultireceive=None,
                 selection=None, transformation=None, **kwargs):
        super(ObjectFlowMixin, self).__init__(**kwargs)

    def input_and_output_parameter(self, diagnostics=None, context=None):
        """A selection Behavior has one input Parameter and one output Parameter. The input Parameter must have the same as or a supertype of the type of the source ObjectNode, be non-unique and have multiplicity 0..*. The output Parameter must be the same or a subtype of the type of source ObjectNode. The Behavior cannot have side effects.
selection<>null implies
        selection.inputParameters()->size()=1 and
        selection.inputParameters()->forAll(not isUnique and is(0,*)) and
        selection.outputParameters()->size()=1"""
        raise NotImplementedError(
            'operation input_and_output_parameter(...) not yet implemented')

    def no_executable_nodes(self, diagnostics=None, context=None):
        """ObjectFlows may not have ExecutableNodes at either end.
not (source.oclIsKindOf(ExecutableNode) or target.oclIsKindOf(ExecutableNode))"""
        raise NotImplementedError(
            'operation no_executable_nodes(...) not yet implemented')

    def transformation_behavior(self, diagnostics=None, context=None):
        """A transformation Behavior has one input Parameter and one output Parameter. The input Parameter must be the same as or a supertype of the type of object token coming from the source end. The output Parameter must be the same or a subtype of the type of object token expected downstream. The Behavior cannot have side effects.
transformation<>null implies
        transformation.inputParameters()->size()=1 and
        transformation.outputParameters()->size()=1"""
        raise NotImplementedError(
            'operation transformation_behavior(...) not yet implemented')

    def selection_behavior(self, diagnostics=None, context=None):
        """An ObjectFlow may have a selection Behavior only if it has an ObjectNode as its source.
selection<>null implies source.oclIsKindOf(ObjectNode)"""
        raise NotImplementedError(
            'operation selection_behavior(...) not yet implemented')

    def compatible_types(self, diagnostics=None, context=None):
        """ObjectNodes connected by an ObjectFlow, with optionally intervening ControlNodes, must have compatible types. In particular, the downstream ObjectNode type must be the same or a supertype of the upstream ObjectNode type."""
        raise NotImplementedError(
            'operation compatible_types(...) not yet implemented')

    def same_upper_bounds(self, diagnostics=None, context=None):
        """ObjectNodes connected by an ObjectFlow, with optionally intervening ControlNodes, must have the same upperBounds."""
        raise NotImplementedError(
            'operation same_upper_bounds(...) not yet implemented')

    def target(self, diagnostics=None, context=None):
        """An ObjectFlow with a constant weight may not target an ObjectNode, with optionally intervening ControlNodes, that has an upper bound less than the weight."""
        raise NotImplementedError('operation target(...) not yet implemented')

    def is_multicast_or_is_multireceive(self, diagnostics=None, context=None):
        """isMulticast and isMultireceive cannot both be true.
not (isMulticast and isMultireceive)"""
        raise NotImplementedError(
            'operation is_multicast_or_is_multireceive(...) not yet implemented')


class ObservationMixin(object):
    """User defined mixin class for Observation."""

    def __init__(self, **kwargs):
        super(ObservationMixin, self).__init__(**kwargs)


class PartDecompositionMixin(object):
    """User defined mixin class for PartDecomposition."""

    def __init__(self, **kwargs):
        super(PartDecompositionMixin, self).__init__(**kwargs)

    def commutativity_of_decomposition(self, diagnostics=None, context=None):
        """Assume that within Interaction X, Lifeline L is of class C and decomposed to D. Assume also that there is within X an InteractionUse (say) U that covers L. According to the constraint above U will have a counterpart CU within D. Within the Interaction referenced by U, L should also be decomposed, and the decomposition should reference CU. (This rule is called commutativity of decomposition.)"""
        raise NotImplementedError(
            'operation commutativity_of_decomposition(...) not yet implemented')

    def assume(self, diagnostics=None, context=None):
        """Assume that within Interaction X, Lifeline L is of class C and decomposed to D. Within X there is a sequence of constructs along L (such constructs are CombinedFragments, InteractionUse and (plain) OccurrenceSpecifications). Then a corresponding sequence of constructs must appear within D, matched one-to-one in the same order. i) CombinedFragment covering L are matched with an extra-global CombinedFragment in D. ii) An InteractionUse covering L is matched with a global (i.e., covering all Lifelines) InteractionUse in D. iii) A plain OccurrenceSpecification on L is considered an actualGate that must be matched by a formalGate of D."""
        raise NotImplementedError('operation assume(...) not yet implemented')

    def parts_of_internal_structures(self, diagnostics=None, context=None):
        """PartDecompositions apply only to Parts that are Parts of Internal Structures not to Parts of Collaborations."""
        raise NotImplementedError(
            'operation parts_of_internal_structures(...) not yet implemented')


class InteractionOperandMixin(object):
    """User defined mixin class for InteractionOperand."""

    def __init__(self, fragment=None, guard=None, **kwargs):
        super(InteractionOperandMixin, self).__init__(**kwargs)

    def guard_contain_references(self, diagnostics=None, context=None):
        """The guard must contain only references to values local to the Lifeline on which it resides, or values global to the whole Interaction."""
        raise NotImplementedError(
            'operation guard_contain_references(...) not yet implemented')

    def guard_directly_prior(self, diagnostics=None, context=None):
        """The guard must be placed directly prior to (above) the OccurrenceSpecification that will become the first OccurrenceSpecification within this InteractionOperand."""
        raise NotImplementedError(
            'operation guard_directly_prior(...) not yet implemented')


class ActionExecutionSpecificationMixin(object):
    """User defined mixin class for ActionExecutionSpecification."""

    def __init__(self, action=None, **kwargs):
        super(ActionExecutionSpecificationMixin, self).__init__(**kwargs)

    def action_referenced(self, diagnostics=None, context=None):
        """The Action referenced by the ActionExecutionSpecification must be owned by the Interaction owning that ActionExecutionSpecification.
(enclosingInteraction->notEmpty() or enclosingOperand.combinedFragment->notEmpty()) and
let parentInteraction : Set(Interaction) = enclosingInteraction.oclAsType(Interaction)->asSet()->union(
enclosingOperand.combinedFragment->closure(enclosingOperand.combinedFragment)->
collect(enclosingInteraction).oclAsType(Interaction)->asSet()) in
(parentInteraction->size() = 1) and self.action.interaction->asSet() = parentInteraction"""
        raise NotImplementedError(
            'operation action_referenced(...) not yet implemented')


class BehaviorExecutionSpecificationMixin(object):
    """User defined mixin class for BehaviorExecutionSpecification."""

    def __init__(self, behavior=None, **kwargs):
        super(BehaviorExecutionSpecificationMixin, self).__init__(**kwargs)


class ConsiderIgnoreFragmentMixin(object):
    """User defined mixin class for ConsiderIgnoreFragment."""

    def __init__(self, message=None, **kwargs):
        super(ConsiderIgnoreFragmentMixin, self).__init__(**kwargs)

    def consider_or_ignore(self, diagnostics=None, context=None):
        """The interaction operator of a ConsiderIgnoreFragment must be either 'consider' or 'ignore'.
(interactionOperator =  InteractionOperatorKind::consider) or (interactionOperator =  InteractionOperatorKind::ignore)"""
        raise NotImplementedError(
            'operation consider_or_ignore(...) not yet implemented')

    def type(self, diagnostics=None, context=None):
        """The NamedElements must be of a type of element that can be a signature for a message (i.e.., an Operation, or a Signal).
message->forAll(m | m.oclIsKindOf(Operation) or m.oclIsKindOf(Signal))"""
        raise NotImplementedError('operation type(...) not yet implemented')


class ExecutionOccurrenceSpecificationMixin(object):
    """User defined mixin class for ExecutionOccurrenceSpecification."""

    def __init__(self, execution=None, **kwargs):
        super(ExecutionOccurrenceSpecificationMixin, self).__init__(**kwargs)


class ValueSpecificationMixin(object):
    """User defined mixin class for ValueSpecification."""

    def __init__(self, **kwargs):
        super(ValueSpecificationMixin, self).__init__(**kwargs)

    def boolean_value(self):
        """The query booleanValue() gives a single Boolean value when one can be computed.
result = (null)
<p>From package UML::Values.</p>"""
        raise NotImplementedError(
            'operation boolean_value(...) not yet implemented')

    def integer_value(self):
        """The query integerValue() gives a single Integer value when one can be computed.
result = (null)
<p>From package UML::Values.</p>"""
        raise NotImplementedError(
            'operation integer_value(...) not yet implemented')

    def is_computable(self):
        """The query isComputable() determines whether a value specification can be computed in a model. This operation cannot be fully defined in OCL. A conforming implementation is expected to deliver true for this operation for all ValueSpecifications that it can compute, and to compute all of those for which the operation is true. A conforming implementation is expected to be able to compute at least the value of all LiteralSpecifications.
result = (false)
<p>From package UML::Values.</p>"""
        raise NotImplementedError(
            'operation is_computable(...) not yet implemented')

    def is_null(self):
        """The query isNull() returns true when it can be computed that the value is null.
result = (false)
<p>From package UML::Values.</p>"""
        raise NotImplementedError('operation is_null(...) not yet implemented')

    def real_value(self):
        """The query realValue() gives a single Real value when one can be computed.
result = (null)
<p>From package UML::Values.</p>"""
        raise NotImplementedError(
            'operation real_value(...) not yet implemented')

    def string_value(self):
        """The query stringValue() gives a single String value when one can be computed.
result = (null)
<p>From package UML::Values.</p>"""
        raise NotImplementedError(
            'operation string_value(...) not yet implemented')

    def unlimited_value(self):
        """The query unlimitedValue() gives a single UnlimitedNatural value when one can be computed.
result = (null)
<p>From package UML::Values.</p>"""
        raise NotImplementedError(
            'operation unlimited_value(...) not yet implemented')


class BehavioralFeatureMixin(object):
    """User defined mixin class for BehavioralFeature."""

    def __init__(
            self, concurrency=None, isAbstract=None, method=None,
            ownedParameter=None, ownedParameterSet=None, raisedException=None,
            **kwargs):
        super(BehavioralFeatureMixin, self).__init__(**kwargs)

    def abstract_no_method(self, diagnostics=None, context=None):
        """When isAbstract is true there are no methods.
isAbstract implies method->isEmpty()"""
        raise NotImplementedError(
            'operation abstract_no_method(...) not yet implemented')

    def create_return_result(self, name=None, type=None):
        """Creates a return result parameter with the specified name and type."""
        raise NotImplementedError(
            'operation create_return_result(...) not yet implemented')

    def input_parameters(self):
        """The ownedParameters with direction in and inout.
result = (ownedParameter->select(direction=ParameterDirectionKind::_'in' or direction=ParameterDirectionKind::inout))
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation input_parameters(...) not yet implemented')

    def output_parameters(self):
        """The ownedParameters with direction out, inout, or return.
result = (ownedParameter->select(direction=ParameterDirectionKind::out or direction=ParameterDirectionKind::inout or direction=ParameterDirectionKind::return))
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation output_parameters(...) not yet implemented')


class StateMixin(object):
    """User defined mixin class for State."""

    @property
    def isComposite(self):
        raise NotImplementedError('Missing implementation for isComposite')

    @property
    def isOrthogonal(self):
        raise NotImplementedError('Missing implementation for isOrthogonal')

    @property
    def isSimple(self):
        raise NotImplementedError('Missing implementation for isSimple')

    @property
    def isSubmachineState(self):
        raise NotImplementedError(
            'Missing implementation for isSubmachineState')

    def __init__(self, connection=None, connectionPoint=None,
                 deferrableTrigger=None, doActivity=None, entry=None,
                 exit=None, isComposite=None, isOrthogonal=None, isSimple=None,
                 isSubmachineState=None, redefinedState=None,
                 stateInvariant=None, submachine=None, region=None, **kwargs):
        super(StateMixin, self).__init__(**kwargs)

    def entry_or_exit(self, diagnostics=None, context=None):
        """Only entry or exit Pseudostates can serve as connection points.
connectionPoint->forAll(kind = PseudostateKind::entryPoint or kind = PseudostateKind::exitPoint)"""
        raise NotImplementedError(
            'operation entry_or_exit(...) not yet implemented')

    def submachine_states(self, diagnostics=None, context=None):
        """Only submachine States can have connection point references.
isSubmachineState implies connection->notEmpty( )"""
        raise NotImplementedError(
            'operation submachine_states(...) not yet implemented')

    def composite_states(self, diagnostics=None, context=None):
        """Only composite States can have entry or exit Pseudostates defined.
connectionPoint->notEmpty() implies isComposite"""
        raise NotImplementedError(
            'operation composite_states(...) not yet implemented')

    def destinations_or_sources_of_transitions(
            self, diagnostics=None, context=None):
        """The connection point references used as destinations/sources of Transitions associated with a submachine State must be defined as entry/exit points in the submachine StateMachine.
self.isSubmachineState implies (self.connection->forAll (cp |
  cp.entry->forAll (ps | ps.stateMachine = self.submachine) and
  cp.exit->forAll (ps | ps.stateMachine = self.submachine)))"""
        raise NotImplementedError(
            'operation destinations_or_sources_of_transitions(...) not yet implemented')

    def submachine_or_regions(self, diagnostics=None, context=None):
        """A State is not allowed to have both a submachine and Regions.
isComposite implies not isSubmachineState"""
        raise NotImplementedError(
            'operation submachine_or_regions(...) not yet implemented')

    def is_composite(self):
        """A composite State is a State with at least one Region.
result = (region->notEmpty())
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation is_composite(...) not yet implemented')

    def is_orthogonal(self):
        """An orthogonal State is a composite state with at least 2 regions.
result = (region->size () > 1)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation is_orthogonal(...) not yet implemented')

    def is_simple(self):
        """A simple State is a State without any regions.
result = ((region->isEmpty()) and not isSubmachineState())
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation is_simple(...) not yet implemented')

    def is_submachine_state(self):
        """Only submachine State references another StateMachine.
result = (submachine <> null)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation is_submachine_state(...) not yet implemented')

    def redefinition_context(self):
        """The redefinition context of a State is the nearest containing StateMachine.
result = (let sm : StateMachine = containingStateMachine() in
if sm._'context' = null or sm.general->notEmpty() then
  sm
else
  sm._'context'
endif)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation redefinition_context(...) not yet implemented')


class ExecutableNodeMixin(object):
    """User defined mixin class for ExecutableNode."""

    def __init__(self, handler=None, **kwargs):
        super(ExecutableNodeMixin, self).__init__(**kwargs)


class ControlNodeMixin(object):
    """User defined mixin class for ControlNode."""

    def __init__(self, **kwargs):
        super(ControlNodeMixin, self).__init__(**kwargs)


class MessageEventMixin(object):
    """User defined mixin class for MessageEvent."""

    def __init__(self, **kwargs):
        super(MessageEventMixin, self).__init__(**kwargs)


class ChangeEventMixin(object):
    """User defined mixin class for ChangeEvent."""

    def __init__(self, changeExpression=None, **kwargs):
        super(ChangeEventMixin, self).__init__(**kwargs)


class TimeEventMixin(object):
    """User defined mixin class for TimeEvent."""

    def __init__(self, isRelative=None, when=None, **kwargs):
        super(TimeEventMixin, self).__init__(**kwargs)

    def when_non_negative(self, diagnostics=None, context=None):
        """The ValueSpecification when must return a non-negative Integer.
when.integerValue() >= 0"""
        raise NotImplementedError(
            'operation when_non_negative(...) not yet implemented')


class InteractionConstraintMixin(object):
    """User defined mixin class for InteractionConstraint."""

    def __init__(self, maxint=None, minint=None, **kwargs):
        super(InteractionConstraintMixin, self).__init__(**kwargs)

    def minint_maxint(self, diagnostics=None, context=None):
        """Minint/maxint can only be present if the InteractionConstraint is associated with the operand of a loop CombinedFragment.
maxint->notEmpty() or minint->notEmpty() implies
interactionOperand.combinedFragment.interactionOperator =
InteractionOperatorKind::loop"""
        raise NotImplementedError(
            'operation minint_maxint(...) not yet implemented')

    def minint_non_negative(self, diagnostics=None, context=None):
        """If minint is specified, then the expression must evaluate to a non-negative integer.
minint->notEmpty() implies
minint->asSequence()->first().integerValue() >= 0"""
        raise NotImplementedError(
            'operation minint_non_negative(...) not yet implemented')

    def maxint_positive(self, diagnostics=None, context=None):
        """If maxint is specified, then the expression must evaluate to a positive integer.
maxint->notEmpty() implies
maxint->asSequence()->first().integerValue() > 0"""
        raise NotImplementedError(
            'operation maxint_positive(...) not yet implemented')

    def dynamic_variables(self, diagnostics=None, context=None):
        """The dynamic variables that take part in the constraint must be owned by the ConnectableElement corresponding to the covered Lifeline."""
        raise NotImplementedError(
            'operation dynamic_variables(...) not yet implemented')

    def global_data(self, diagnostics=None, context=None):
        """The constraint may contain references to global data or write-once data."""
        raise NotImplementedError(
            'operation global_data(...) not yet implemented')

    def maxint_greater_equal_minint(self, diagnostics=None, context=None):
        """If maxint is specified, then minint must be specified and the evaluation of maxint must be >= the evaluation of minint.
maxint->notEmpty() implies (minint->notEmpty() and
maxint->asSequence()->first().integerValue() >=
minint->asSequence()->first().integerValue() )"""
        raise NotImplementedError(
            'operation maxint_greater_equal_minint(...) not yet implemented')


class MessageOccurrenceSpecificationMixin(object):
    """User defined mixin class for MessageOccurrenceSpecification."""

    def __init__(self, **kwargs):
        super(MessageOccurrenceSpecificationMixin, self).__init__(**kwargs)


class DerivedReferred(EDerivedCollection):
    pass


class ProtocolTransitionMixin(object):
    """User defined mixin class for ProtocolTransition."""

    def __init__(
            self, postCondition=None, preCondition=None, referred=None, **
            kwargs):
        super(ProtocolTransitionMixin, self).__init__(**kwargs)

    def refers_to_operation(self, diagnostics=None, context=None):
        """If a ProtocolTransition refers to an Operation (i.e., has a CallEvent trigger corresponding to an Operation), then that Operation should apply to the context Classifier of the StateMachine of the ProtocolTransition.
if (referred()->notEmpty() and containingStateMachine()._'context'->notEmpty()) then
    containingStateMachine()._'context'.oclAsType(BehavioredClassifier).allFeatures()->includesAll(referred())
else true endif"""
        raise NotImplementedError(
            'operation refers_to_operation(...) not yet implemented')

    def associated_actions(self, diagnostics=None, context=None):
        """A ProtocolTransition never has associated Behaviors.
effect = null"""
        raise NotImplementedError(
            'operation associated_actions(...) not yet implemented')

    def belongs_to_psm(self, diagnostics=None, context=None):
        """A ProtocolTransition always belongs to a ProtocolStateMachine.
container.belongsToPSM()"""
        raise NotImplementedError(
            'operation belongs_to_psm(...) not yet implemented')

    def get_referreds(self):
        """Derivation for ProtocolTransition::/referred
result = (trigger->collect(event)->select(oclIsKindOf(CallEvent))->collect(oclAsType(CallEvent).operation)->asSet())
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation get_referreds(...) not yet implemented')


class IntervalConstraintMixin(object):
    """User defined mixin class for IntervalConstraint."""

    def __init__(self, **kwargs):
        super(IntervalConstraintMixin, self).__init__(**kwargs)


class DurationObservationMixin(object):
    """User defined mixin class for DurationObservation."""

    def __init__(self, event=None, firstEvent=None, **kwargs):
        super(DurationObservationMixin, self).__init__(**kwargs)

    def first_event_multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of firstEvent must be 2 if the multiplicity of event is 2. Otherwise the multiplicity of firstEvent is 0.
if (event->size() = 2)
  then (firstEvent->size() = 2) else (firstEvent->size() = 0)
endif"""
        raise NotImplementedError(
            'operation first_event_multiplicity(...) not yet implemented')


class TimeObservationMixin(object):
    """User defined mixin class for TimeObservation."""

    def __init__(self, event=None, firstEvent=None, **kwargs):
        super(TimeObservationMixin, self).__init__(**kwargs)


class DerivedNestedpackage(EDerivedCollection):
    def _get_collection(self):
        from .uml import Package
        return [e for e in self.owner.packagedElement
                if isinstance(e, Package)]

    def __len__(self):
        return len(self._get_collection())

    def __getitem__(self, index):
        return self._get_collection()[index]

    def __repr__(self):
        return 'DerivedCollection({})'.format(self._get_collection())


class DerivedOwnedstereotype(EDerivedCollection):
    def _get_collection(self):
        from .uml import Stereotype
        return [e for e in self.owner.packagedElement
                if isinstance(e, Stereotype)]

    def __contains__(self, x):
        return x in self._get_collection()

    def __len__(self):
        return len(self._get_collection())

    def __getitem__(self, index):
        return self._get_collection()[index]

    def __repr__(self):
        return 'DerivedCollection({})'.format(self._get_collection())


class DerivedOwnedtype(EDerivedCollection):
    pass


class PackageMixin(object):
    """User defined mixin class for Package."""

    @property
    def nestingPackage(self):
        from .uml import Package
        if isinstance(self.owner, Package):
            return self.owner
        return None

    @nestingPackage.setter
    def nestingPackage(self, value):
        from .uml import Package
        check(value, Package)
        if value is None and self.nestingPackage:
            self.nestingPackage.packagedElement.remove(self)
        else:
            value.packagedElement.append(self)

    def __init__(
            self, URI=None, nestedPackage=None, nestingPackage=None,
            ownedStereotype=None, ownedType=None, packageMerge=None,
            packagedElement=None, profileApplication=None, **kwargs):
        super(PackageMixin, self).__init__(**kwargs)

    def elements_public_or_private(self, diagnostics=None, context=None):
        """If an element that is owned by a package has visibility, it is public or private.
packagedElement->forAll(e | e.visibility<> null implies e.visibility = VisibilityKind::public or e.visibility = VisibilityKind::private)"""
        raise NotImplementedError(
            'operation elements_public_or_private(...) not yet implemented')

    def apply_profile(self, profile=None):
        """Applies the current definition of the specified profile to this package and automatically applies required stereotypes in the profile to elements within this package's namespace hieararchy. If a different definition is already applied, automatically migrates any associated stereotype values on a "best effort" basis (matching classifiers and structural features by name)."""
        raise NotImplementedError(
            'operation apply_profile(...) not yet implemented')

    def create_owned_class(self, name=None, isAbstract=None):
        """Creates a(n) (abstract) class with the specified name as an owned type of this package."""
        raise NotImplementedError(
            'operation create_owned_class(...) not yet implemented')

    def create_owned_enumeration(self, name=None):
        """Creates a enumeration with the specified name as an owned type of this package."""
        raise NotImplementedError(
            'operation create_owned_enumeration(...) not yet implemented')

    def create_owned_interface(self, name=None):
        """Creates an interface with the specified name as an owned type of this package."""
        raise NotImplementedError(
            'operation create_owned_interface(...) not yet implemented')

    def create_owned_primitive_type(self, name=None):
        """Creates a primitive type with the specified name as an owned type of this package."""
        raise NotImplementedError(
            'operation create_owned_primitive_type(...) not yet implemented')

    def create_owned_stereotype(self, name=None, isAbstract=None):
        """Creates a(n) (abstract) stereotype with the specified name as an owned stereotype of this profile."""
        raise NotImplementedError(
            'operation create_owned_stereotype(...) not yet implemented')

    def get_all_applied_profiles(self):
        """Retrieves all the profiles that are applied to this package, including profiles applied to its nesting package(s)."""
        raise NotImplementedError(
            'operation get_all_applied_profiles(...) not yet implemented')

    def get_all_profile_applications(self):
        """Retrieves all the profile applications for this package, including profile applications for its nesting package(s)."""
        raise NotImplementedError(
            'operation get_all_profile_applications(...) not yet implemented')

    def get_applied_profile(self, qualifiedName=None):
        """Retrieves the profile with the specified qualified name that is applied to this package, or null if no such profile is applied."""
        raise NotImplementedError(
            'operation get_applied_profile(...) not yet implemented')

    def get_applied_profile(self, qualifiedName=None, recurse=None):
        """Retrieves the profile with the specified qualified name that is applied to this package or any of its nesting packages (if indicated), or null if no such profile is applied."""
        raise NotImplementedError(
            'operation get_applied_profile(...) not yet implemented')

    def get_applied_profiles(self):
        """Retrieves the profiles that are applied to this package."""
        raise NotImplementedError(
            'operation get_applied_profiles(...) not yet implemented')

    def get_profile_application(self, profile=None):
        """Retrieves the application of the specified profile to this package, or null if no such profile is applied."""
        raise NotImplementedError(
            'operation get_profile_application(...) not yet implemented')

    def get_profile_application(self, profile=None, recurse=None):
        """Retrieves the application of the specified profile to this package or any of its nesting packages (if indicated), or null if no such profile is applied."""
        raise NotImplementedError(
            'operation get_profile_application(...) not yet implemented')

    def is_model_library(self):
        """Determines whether this package is a model library."""
        raise NotImplementedError(
            'operation is_model_library(...) not yet implemented')

    def is_profile_applied(self, profile=None):
        """Determines whether the specified profile is applied to this package."""
        raise NotImplementedError(
            'operation is_profile_applied(...) not yet implemented')

    def unapply_profile(self, profile=None):
        """Unapplies the specified profile from this package and automatically unapplies stereotypes in the profile from elements within this package's namespace hieararchy."""
        raise NotImplementedError(
            'operation unapply_profile(...) not yet implemented')

    def apply_profiles(self, profiles=None):
        """Applies the current definitions of the specified profiles to this package and automatically applies required stereotypes in the profiles to elements within this package's namespace hieararchy. If different definitions are already applied, automatically migrates any associated stereotype values on a "best effort" basis (matching classifiers and structural features by name)."""
        raise NotImplementedError(
            'operation apply_profiles(...) not yet implemented')

    def all_applicable_stereotypes(self):
        """The query allApplicableStereotypes() returns all the directly or indirectly owned stereotypes, including stereotypes contained in sub-profiles.
result = (let ownedPackages : Bag(Package) = ownedMember->select(oclIsKindOf(Package))->collect(oclAsType(Package)) in
 ownedStereotype->union(ownedPackages.allApplicableStereotypes())->flatten()->asSet()
)
<p>From package UML::Packages.</p>"""
        raise NotImplementedError(
            'operation all_applicable_stereotypes(...) not yet implemented')

    def containing_profile(self):
        """The query containingProfile() returns the closest profile directly or indirectly containing this package (or this package itself, if it is a profile).
result = (if self.oclIsKindOf(Profile) then
        self.oclAsType(Profile)
else
        self.namespace.oclAsType(Package).containingProfile()
endif)
<p>From package UML::Packages.</p>"""
        raise NotImplementedError(
            'operation containing_profile(...) not yet implemented')

    def makes_visible(self, el=None):
        """The query makesVisible() defines whether a Package makes an element visible outside itself. Elements with no visibility and elements with public visibility are made visible.
member->includes(el)
result = (ownedMember->includes(el) or
(elementImport->select(ei|ei.importedElement = VisibilityKind::public)->collect(importedElement.oclAsType(NamedElement))->includes(el)) or
(packageImport->select(visibility = VisibilityKind::public)->collect(importedPackage.member->includes(el))->notEmpty()))
<p>From package UML::Packages.</p>"""
        raise NotImplementedError(
            'operation makes_visible(...) not yet implemented')

    def get_nested_packages(self):
        """Derivation for Package::/nestedPackage
result = (packagedElement->select(oclIsKindOf(Package))->collect(oclAsType(Package))->asSet())
<p>From package UML::Packages.</p>"""
        return self.nestedPackage

    def get_owned_stereotypes(self):
        """Derivation for Package::/ownedStereotype
result = (packagedElement->select(oclIsKindOf(Stereotype))->collect(oclAsType(Stereotype))->asSet())
<p>From package UML::Packages.</p>"""
        return self.ownedStereotype

    def get_owned_types(self):
        """Derivation for Package::/ownedType
result = (packagedElement->select(oclIsKindOf(Type))->collect(oclAsType(Type))->asSet())
<p>From package UML::Packages.</p>"""
        raise NotImplementedError(
            'operation get_owned_types(...) not yet implemented')

    def visible_members(self):
        """The query visibleMembers() defines which members of a Package can be accessed outside it.
result = (member->select( m | m.oclIsKindOf(PackageableElement) and self.makesVisible(m))->collect(oclAsType(PackageableElement))->asSet())
<p>From package UML::Packages.</p>"""
        raise NotImplementedError(
            'operation visible_members(...) not yet implemented')


class DependencyMixin(object):
    """User defined mixin class for Dependency."""

    def __init__(self, client=None, supplier=None, **kwargs):
        super(DependencyMixin, self).__init__(**kwargs)


class OpaqueExpressionMixin(object):
    """User defined mixin class for OpaqueExpression."""

    @property
    def result(self):
        raise NotImplementedError('Missing implementation for result')

    def __init__(
            self, behavior=None, body=None, language=None, result=None, **
            kwargs):
        super(OpaqueExpressionMixin, self).__init__(**kwargs)

    def language_body_size(self, diagnostics=None, context=None):
        """If the language attribute is not empty, then the size of the body and language arrays must be the same.
language->notEmpty() implies (_'body'->size() = language->size())"""
        raise NotImplementedError(
            'operation language_body_size(...) not yet implemented')

    def one_return_result_parameter(self, diagnostics=None, context=None):
        """The behavior must have exactly one return result parameter.
behavior <> null implies
   behavior.ownedParameter->select(direction=ParameterDirectionKind::return)->size() = 1"""
        raise NotImplementedError(
            'operation one_return_result_parameter(...) not yet implemented')

    def only_return_result_parameters(self, diagnostics=None, context=None):
        """The behavior may only have return result parameters.
behavior <> null implies behavior.ownedParameter->select(direction<>ParameterDirectionKind::return)->isEmpty()"""
        raise NotImplementedError(
            'operation only_return_result_parameters(...) not yet implemented')

    def is_integral(self):
        """The query isIntegral() tells whether an expression is intended to produce an Integer.
result = (false)
<p>From package UML::Values.</p>"""
        raise NotImplementedError(
            'operation is_integral(...) not yet implemented')

    def is_non_negative(self):
        """The query isNonNegative() tells whether an integer expression has a non-negative value.
self.isIntegral()
result = (false)
<p>From package UML::Values.</p>"""
        raise NotImplementedError(
            'operation is_non_negative(...) not yet implemented')

    def is_positive(self):
        """The query isPositive() tells whether an integer expression has a positive value.
self.isIntegral()
result = (false)
<p>From package UML::Values.</p>"""
        raise NotImplementedError(
            'operation is_positive(...) not yet implemented')

    def get_result(self):
        """Derivation for OpaqueExpression::/result
result = (if behavior = null then
        null
else
        behavior.ownedParameter->first()
endif)
<p>From package UML::Values.</p>"""
        raise NotImplementedError(
            'operation get_result(...) not yet implemented')

    def value(self):
        """The query value() gives an integer value for an expression intended to produce one.
self.isIntegral()
result = (0)
<p>From package UML::Values.</p>"""
        raise NotImplementedError('operation value(...) not yet implemented')


class ParameterMixin(object):
    """User defined mixin class for Parameter."""

    @property
    def default(self):
        raise NotImplementedError('Missing implementation for default')

    @default.setter
    def default(self, value):
        raise NotImplementedError('Missing implementation for default')

    def __init__(
            self, default=None, defaultValue=None, direction=None,
            effect=None, isException=None, isStream=None, operation=None,
            parameterSet=None, **kwargs):
        super(ParameterMixin, self).__init__(**kwargs)

    def in_and_out(self, diagnostics=None, context=None):
        """Only in and inout Parameters may have a delete effect. Only out, inout, and return Parameters may have a create effect.
(effect = ParameterEffectKind::delete implies (direction = ParameterDirectionKind::_'in' or direction = ParameterDirectionKind::inout))
and
(effect = ParameterEffectKind::create implies (direction = ParameterDirectionKind::out or direction = ParameterDirectionKind::inout or direction = ParameterDirectionKind::return))"""
        raise NotImplementedError(
            'operation in_and_out(...) not yet implemented')

    def not_exception(self, diagnostics=None, context=None):
        """An input Parameter cannot be an exception.
isException implies (direction <> ParameterDirectionKind::_'in' and direction <> ParameterDirectionKind::inout)"""
        raise NotImplementedError(
            'operation not_exception(...) not yet implemented')

    def connector_end(self, diagnostics=None, context=None):
        """A Parameter may only be associated with a Connector end within the context of a Collaboration.
end->notEmpty() implies collaboration->notEmpty()"""
        raise NotImplementedError(
            'operation connector_end(...) not yet implemented')

    def reentrant_behaviors(self, diagnostics=None, context=None):
        """Reentrant behaviors cannot have stream Parameters.
(isStream and behavior <> null) implies not behavior.isReentrant"""
        raise NotImplementedError(
            'operation reentrant_behaviors(...) not yet implemented')

    def stream_and_exception(self, diagnostics=None, context=None):
        """A Parameter cannot be a stream and exception at the same time.
not (isException and isStream)"""
        raise NotImplementedError(
            'operation stream_and_exception(...) not yet implemented')

    def object_effect(self, diagnostics=None, context=None):
        """Parameters typed by DataTypes cannot have an effect.
(type.oclIsKindOf(DataType)) implies (effect = null)"""
        raise NotImplementedError(
            'operation object_effect(...) not yet implemented')

    def is_set_default(self):

        raise NotImplementedError(
            'operation is_set_default(...) not yet implemented')

    def set_boolean_default_value(self, value=None):
        """Sets the default value for this parameter to the specified Boolean value."""
        raise NotImplementedError(
            'operation set_boolean_default_value(...) not yet implemented')

    def set_default(self, newDefault=None):

        raise NotImplementedError(
            'operation set_default(...) not yet implemented')

    def set_integer_default_value(self, value=None):
        """Sets the default value for this parameter to the specified integer value."""
        raise NotImplementedError(
            'operation set_integer_default_value(...) not yet implemented')

    def set_null_default_value(self):
        """Sets the default value for this parameter to the null value."""
        raise NotImplementedError(
            'operation set_null_default_value(...) not yet implemented')

    def set_real_default_value(self, value=None):
        """Sets the default value for this parameter to the specified real value."""
        raise NotImplementedError(
            'operation set_real_default_value(...) not yet implemented')

    def set_string_default_value(self, value=None):
        """Sets the default value for this parameter to the specified string value."""
        raise NotImplementedError(
            'operation set_string_default_value(...) not yet implemented')

    def set_unlimited_natural_default_value(self, value=None):
        """Sets the default value for this parameter to the specified unlimited natural value."""
        raise NotImplementedError(
            'operation set_unlimited_natural_default_value(...) not yet implemented')

    def unset_default(self):

        raise NotImplementedError(
            'operation unset_default(...) not yet implemented')

    def get_default(self):
        """Derivation for Parameter::/default
result = (if self.type = String then defaultValue.stringValue() else null endif)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation get_default(...) not yet implemented')


class ReceptionMixin(object):
    """User defined mixin class for Reception."""

    def __init__(self, signal=None, **kwargs):
        super(ReceptionMixin, self).__init__(**kwargs)

    def same_name_as_signal(self, diagnostics=None, context=None):
        """A Reception has the same name as its signal
name = signal.name"""
        raise NotImplementedError(
            'operation same_name_as_signal(...) not yet implemented')

    def same_structure_as_signal(self, diagnostics=None, context=None):
        """A Reception's parameters match the ownedAttributes of its signal by name, type, and multiplicity
signal.ownedAttribute->size() = ownedParameter->size() and
Sequence{1..signal.ownedAttribute->size()}->forAll( i |
    ownedParameter->at(i).direction = ParameterDirectionKind::_'in' and
    ownedParameter->at(i).name = signal.ownedAttribute->at(i).name and
    ownedParameter->at(i).type = signal.ownedAttribute->at(i).type and
    ownedParameter->at(i).lowerBound() = signal.ownedAttribute->at(i).lowerBound() and
    ownedParameter->at(i).upperBound() = signal.ownedAttribute->at(i).upperBound()
)"""
        raise NotImplementedError(
            'operation same_structure_as_signal(...) not yet implemented')


class StructuralFeatureMixin(object):
    """User defined mixin class for StructuralFeature."""

    def __init__(self, isReadOnly=None, **kwargs):
        super(StructuralFeatureMixin, self).__init__(**kwargs)


class InstanceSpecificationMixin(object):
    """User defined mixin class for InstanceSpecification."""

    def __init__(
            self, classifier=None, slot=None, specification=None, **kwargs):
        super(InstanceSpecificationMixin, self).__init__(**kwargs)

    def deployment_artifact(self, diagnostics=None, context=None):
        """An InstanceSpecification can act as a DeployedArtifact if it represents an instance of an Artifact.
deploymentForArtifact->notEmpty() implies classifier->exists(oclIsKindOf(Artifact))"""
        raise NotImplementedError(
            'operation deployment_artifact(...) not yet implemented')

    def structural_feature(self, diagnostics=None, context=None):
        """No more than one slot in an InstanceSpecification may have the same definingFeature.
classifier->forAll(c | (c.allSlottableFeatures()->forAll(f | slot->select(s | s.definingFeature = f)->size() <= 1)))"""
        raise NotImplementedError(
            'operation structural_feature(...) not yet implemented')

    def defining_feature(self, diagnostics=None, context=None):
        """The definingFeature of each slot is a StructuralFeature related to a classifier of the InstanceSpecification, including direct attributes, inherited attributes, private attributes in generalizations, and memberEnds of Associations, but excluding redefined StructuralFeatures.
slot->forAll(s | classifier->exists (c | c.allSlottableFeatures()->includes (s.definingFeature)))"""
        raise NotImplementedError(
            'operation defining_feature(...) not yet implemented')

    def deployment_target(self, diagnostics=None, context=None):
        """An InstanceSpecification can act as a DeploymentTarget if it represents an instance of a Node and functions as a part in the internal structure of an encompassing Node.
deployment->notEmpty() implies classifier->exists(node | node.oclIsKindOf(Node) and Node.allInstances()->exists(n | n.part->exists(p | p.type = node)))"""
        raise NotImplementedError(
            'operation deployment_target(...) not yet implemented')


class ExpressionMixin(object):
    """User defined mixin class for Expression."""

    def __init__(self, operand=None, symbol=None, **kwargs):
        super(ExpressionMixin, self).__init__(**kwargs)


class DerivedInput(EDerivedCollection):
    pass


class DerivedOutput(EDerivedCollection):
    pass


class ActionMixin(object):
    """User defined mixin class for Action."""

    @property
    def context(self):
        raise NotImplementedError('Missing implementation for context')

    def __init__(
            self, context=None, input=None, isLocallyReentrant=None,
            localPostcondition=None, localPrecondition=None, output=None, **
            kwargs):
        super(ActionMixin, self).__init__(**kwargs)

    def get_context(self):
        """The derivation for the context property.
result = (let behavior: Behavior = self.containingBehavior() in
if behavior=null then null
else if behavior._'context' = null then behavior
else behavior._'context'
endif
endif)
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation get_context(...) not yet implemented')

    def all_actions(self):
        """Return this Action and all Actions contained directly or indirectly in it. By default only the Action itself is returned, but the operation is overridden for StructuredActivityNodes.
result = (self->asSet())
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation all_actions(...) not yet implemented')

    def all_owned_nodes(self):
        """Returns all the ActivityNodes directly or indirectly owned by this Action. This includes at least all the Pins of the Action.
result = (input.oclAsType(Pin)->asSet()->union(output->asSet()))
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation all_owned_nodes(...) not yet implemented')

    def containing_behavior(self):
        """result = (if inStructuredNode<>null then inStructuredNode.containingBehavior()
else if activity<>null then activity
else interaction
endif
endif
)
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation containing_behavior(...) not yet implemented')


class ObjectNodeMixin(object):
    """User defined mixin class for ObjectNode."""

    def __init__(
            self, inState=None, isControlType=None, ordering=None,
            selection=None, upperBound=None, **kwargs):
        super(ObjectNodeMixin, self).__init__(**kwargs)

    def input_output_parameter(self, diagnostics=None, context=None):
        """A selection Behavior has one input Parameter and one output Parameter. The input Parameter must have the same type as  or a supertype of the type of ObjectNode, be non-unique, and have multiplicity 0..*. The output Parameter must be the same or a subtype of the type of ObjectNode. The Behavior cannot have side effects.
selection<>null implies
        selection.inputParameters()->size()=1 and
        selection.inputParameters()->forAll(p | not p.isUnique and p.is(0,*) and self.type.conformsTo(p.type)) and
        selection.outputParameters()->size()=1 and
                selection.inputParameters()->forAll(p | self.type.conformsTo(p.type))"""
        raise NotImplementedError(
            'operation input_output_parameter(...) not yet implemented')

    def selection_behavior(self, diagnostics=None, context=None):
        """If an ObjectNode has a selection Behavior, then the ordering of the object node is ordered, and vice versa.
(selection<>null) = (ordering=ObjectNodeOrderingKind::ordered)"""
        raise NotImplementedError(
            'operation selection_behavior(...) not yet implemented')

    def object_flow_edges(self, diagnostics=None, context=None):
        """If isControlType=false, the ActivityEdges incoming to or outgoing from an ObjectNode must all be ObjectFlows.
(not isControlType) implies incoming->union(outgoing)->forAll(oclIsKindOf(ObjectFlow))"""
        raise NotImplementedError(
            'operation object_flow_edges(...) not yet implemented')


class VariableMixin(object):
    """User defined mixin class for Variable."""

    def __init__(self, activityScope=None, scope=None, **kwargs):
        super(VariableMixin, self).__init__(**kwargs)

    def is_accessible_by(self, a=None):
        """A Variable is accessible by Actions within its scope (the Activity or StructuredActivityNode that owns it).
result = (if scope<>null then scope.allOwnedNodes()->includes(a)
else a.containingActivity()=activityScope
endif)
<p>From package UML::Activities.</p>"""
        raise NotImplementedError(
            'operation is_accessible_by(...) not yet implemented')


class FinalNodeMixin(object):
    """User defined mixin class for FinalNode."""

    def __init__(self, **kwargs):
        super(FinalNodeMixin, self).__init__(**kwargs)

    def no_outgoing_edges(self, diagnostics=None, context=None):
        """A FinalNode has no outgoing ActivityEdges.
outgoing->isEmpty()"""
        raise NotImplementedError(
            'operation no_outgoing_edges(...) not yet implemented')


class DecisionNodeMixin(object):
    """User defined mixin class for DecisionNode."""

    def __init__(self, decisionInput=None, decisionInputFlow=None, **kwargs):
        super(DecisionNodeMixin, self).__init__(**kwargs)

    def zero_input_parameters(self, diagnostics=None, context=None):
        """If the DecisionNode has no decisionInputFlow and an incoming ControlFlow, then any decisionInput Behavior has no in parameters.
(decisionInput<>null and decisionInputFlow=null and incoming->exists(oclIsKindOf(ControlFlow))) implies
   decisionInput.inputParameters()->isEmpty()"""
        raise NotImplementedError(
            'operation zero_input_parameters(...) not yet implemented')

    def edges(self, diagnostics=None, context=None):
        """The ActivityEdges incoming to and outgoing from a DecisionNode, other than the decisionInputFlow (if any), must be either all ObjectFlows or all ControlFlows.
let allEdges: Set(ActivityEdge) = incoming->union(outgoing) in
let allRelevantEdges: Set(ActivityEdge) = if decisionInputFlow->notEmpty() then allEdges->excluding(decisionInputFlow) else allEdges endif in
allRelevantEdges->forAll(oclIsKindOf(ControlFlow)) or allRelevantEdges->forAll(oclIsKindOf(ObjectFlow))
"""
        raise NotImplementedError('operation edges(...) not yet implemented')

    def decision_input_flow_incoming(self, diagnostics=None, context=None):
        """The decisionInputFlow of a DecisionNode must be an incoming ActivityEdge of the DecisionNode.
incoming->includes(decisionInputFlow)"""
        raise NotImplementedError(
            'operation decision_input_flow_incoming(...) not yet implemented')

    def two_input_parameters(self, diagnostics=None, context=None):
        """If the DecisionNode has a decisionInputFlow and an second incoming ObjectFlow, then any decisionInput has two in Parameters, the first of which has a type that is the same as or a supertype of the type of object tokens offered on the non-decisionInputFlow and the second of which has a type that is the same as or a supertype of the type of object tokens offered on the decisionInputFlow.
(decisionInput<>null and decisionInputFlow<>null and incoming->forAll(oclIsKindOf(ObjectFlow))) implies
        decisionInput.inputParameters()->size()=2"""
        raise NotImplementedError(
            'operation two_input_parameters(...) not yet implemented')

    def incoming_outgoing_edges(self, diagnostics=None, context=None):
        """A DecisionNode has one or two incoming ActivityEdges and at least one outgoing ActivityEdge.
(incoming->size() = 1 or incoming->size() = 2) and outgoing->size() > 0"""
        raise NotImplementedError(
            'operation incoming_outgoing_edges(...) not yet implemented')

    def incoming_control_one_input_parameter(
            self, diagnostics=None, context=None):
        """If the DecisionNode has a decisionInputFlow and an incoming ControlFlow, then any decisionInput Behavior has one in Parameter whose type is the same as or a supertype of the type of object tokens offered on the decisionInputFlow.
(decisionInput<>null and decisionInputFlow<>null and incoming->exists(oclIsKindOf(ControlFlow))) implies
        decisionInput.inputParameters()->size()=1"""
        raise NotImplementedError(
            'operation incoming_control_one_input_parameter(...) not yet implemented')

    def parameters(self, diagnostics=None, context=None):
        """A decisionInput Behavior has no out parameters, no inout parameters, and one return parameter.
decisionInput<>null implies
  (decisionInput.ownedParameter->forAll(par |
     par.direction <> ParameterDirectionKind::out and
     par.direction <> ParameterDirectionKind::inout ) and
   decisionInput.ownedParameter->one(par |
     par.direction <> ParameterDirectionKind::return))"""
        raise NotImplementedError(
            'operation parameters(...) not yet implemented')

    def incoming_object_one_input_parameter(
            self, diagnostics=None, context=None):
        """If the DecisionNode has no decisionInputFlow and an incoming ObjectFlow, then any decisionInput Behavior has one in Parameter whose type is the same as or a supertype of the type of object tokens offered on the incoming ObjectFlow.
(decisionInput<>null and decisionInputFlow=null and incoming->forAll(oclIsKindOf(ObjectFlow))) implies
        decisionInput.inputParameters()->size()=1"""
        raise NotImplementedError(
            'operation incoming_object_one_input_parameter(...) not yet implemented')


class ForkNodeMixin(object):
    """User defined mixin class for ForkNode."""

    def __init__(self, **kwargs):
        super(ForkNodeMixin, self).__init__(**kwargs)

    def edges(self, diagnostics=None, context=None):
        """The ActivityEdges incoming to and outgoing from a ForkNode must be either all ObjectFlows or all ControlFlows.
let allEdges : Set(ActivityEdge) = incoming->union(outgoing) in
allEdges->forAll(oclIsKindOf(ControlFlow)) or allEdges->forAll(oclIsKindOf(ObjectFlow))"""
        raise NotImplementedError('operation edges(...) not yet implemented')

    def one_incoming_edge(self, diagnostics=None, context=None):
        """A ForkNode has one incoming ActivityEdge.
incoming->size()=1"""
        raise NotImplementedError(
            'operation one_incoming_edge(...) not yet implemented')


class InitialNodeMixin(object):
    """User defined mixin class for InitialNode."""

    def __init__(self, **kwargs):
        super(InitialNodeMixin, self).__init__(**kwargs)

    def no_incoming_edges(self, diagnostics=None, context=None):
        """An InitialNode has no incoming ActivityEdges.
incoming->isEmpty()"""
        raise NotImplementedError(
            'operation no_incoming_edges(...) not yet implemented')

    def control_edges(self, diagnostics=None, context=None):
        """All the outgoing ActivityEdges from an InitialNode must be ControlFlows.
outgoing->forAll(oclIsKindOf(ControlFlow))"""
        raise NotImplementedError(
            'operation control_edges(...) not yet implemented')


class JoinNodeMixin(object):
    """User defined mixin class for JoinNode."""

    def __init__(self, isCombineDuplicate=None, joinSpec=None, **kwargs):
        super(JoinNodeMixin, self).__init__(**kwargs)

    def one_outgoing_edge(self, diagnostics=None, context=None):
        """A JoinNode has one outgoing ActivityEdge.
outgoing->size() = 1"""
        raise NotImplementedError(
            'operation one_outgoing_edge(...) not yet implemented')

    def incoming_object_flow(self, diagnostics=None, context=None):
        """If one of the incoming ActivityEdges of a JoinNode is an ObjectFlow, then its outgoing ActivityEdge must be an ObjectFlow. Otherwise its outgoing ActivityEdge must be a ControlFlow.
if incoming->exists(oclIsKindOf(ObjectFlow)) then outgoing->forAll(oclIsKindOf(ObjectFlow))
else outgoing->forAll(oclIsKindOf(ControlFlow))
endif"""
        raise NotImplementedError(
            'operation incoming_object_flow(...) not yet implemented')


class MergeNodeMixin(object):
    """User defined mixin class for MergeNode."""

    def __init__(self, **kwargs):
        super(MergeNodeMixin, self).__init__(**kwargs)

    def one_outgoing_edge(self, diagnostics=None, context=None):
        """A MergeNode has one outgoing ActivityEdge.
outgoing->size()=1"""
        raise NotImplementedError(
            'operation one_outgoing_edge(...) not yet implemented')

    def edges(self, diagnostics=None, context=None):
        """The ActivityEdges incoming to and outgoing from a MergeNode must be either all ObjectFlows or all ControlFlows.
let allEdges : Set(ActivityEdge) = incoming->union(outgoing) in
allEdges->forAll(oclIsKindOf(ControlFlow)) or allEdges->forAll(oclIsKindOf(ObjectFlow))"""
        raise NotImplementedError('operation edges(...) not yet implemented')


class InstanceValueMixin(object):
    """User defined mixin class for InstanceValue."""

    def __init__(self, instance=None, **kwargs):
        super(InstanceValueMixin, self).__init__(**kwargs)


class AnyReceiveEventMixin(object):
    """User defined mixin class for AnyReceiveEvent."""

    def __init__(self, **kwargs):
        super(AnyReceiveEventMixin, self).__init__(**kwargs)


class CallEventMixin(object):
    """User defined mixin class for CallEvent."""

    def __init__(self, operation=None, **kwargs):
        super(CallEventMixin, self).__init__(**kwargs)


class SignalEventMixin(object):
    """User defined mixin class for SignalEvent."""

    def __init__(self, signal=None, **kwargs):
        super(SignalEventMixin, self).__init__(**kwargs)


class TimeExpressionMixin(object):
    """User defined mixin class for TimeExpression."""

    def __init__(self, expr=None, observation=None, **kwargs):
        super(TimeExpressionMixin, self).__init__(**kwargs)

    def no_expr_requires_observation(self, diagnostics=None, context=None):
        """If a TimeExpression has no expr, then it must have a single observation that is a TimeObservation.
expr = null implies (observation->size() = 1 and observation->forAll(oclIsKindOf(TimeObservation)))"""
        raise NotImplementedError(
            'operation no_expr_requires_observation(...) not yet implemented')


class InformationFlowMixin(object):
    """User defined mixin class for InformationFlow."""

    def __init__(
            self, conveyed=None, informationSource=None,
            informationTarget=None, realization=None,
            realizingActivityEdge=None, realizingConnector=None,
            realizingMessage=None, **kwargs):
        super(InformationFlowMixin, self).__init__(**kwargs)

    def must_conform(self, diagnostics=None, context=None):
        """The sources and targets of the information flow must conform to the sources and targets or conversely the targets and sources of the realization relationships."""
        raise NotImplementedError(
            'operation must_conform(...) not yet implemented')

    def sources_and_targets_kind(self, diagnostics=None, context=None):
        """The sources and targets of the information flow can only be one of the following kind: Actor, Node, UseCase, Artifact, Class, Component, Port, Property, Interface, Package, ActivityNode, ActivityPartition,
Behavior and InstanceSpecification except when its classifier is a relationship (i.e. it represents a link).
(self.informationSource->forAll( sis |
  oclIsKindOf(Actor) or oclIsKindOf(Node) or oclIsKindOf(UseCase) or oclIsKindOf(Artifact) or
  oclIsKindOf(Class) or oclIsKindOf(Component) or oclIsKindOf(Port) or oclIsKindOf(Property) or
  oclIsKindOf(Interface) or oclIsKindOf(Package) or oclIsKindOf(ActivityNode) or oclIsKindOf(ActivityPartition) or
  (oclIsKindOf(InstanceSpecification) and not sis.oclAsType(InstanceSpecification).classifier->exists(oclIsKindOf(Relationship)))))

and

(self.informationTarget->forAll( sit |
  oclIsKindOf(Actor) or oclIsKindOf(Node) or oclIsKindOf(UseCase) or oclIsKindOf(Artifact) or
  oclIsKindOf(Class) or oclIsKindOf(Component) or oclIsKindOf(Port) or oclIsKindOf(Property) or
  oclIsKindOf(Interface) or oclIsKindOf(Package) or oclIsKindOf(ActivityNode) or oclIsKindOf(ActivityPartition) or
(oclIsKindOf(InstanceSpecification) and not sit.oclAsType(InstanceSpecification).classifier->exists(oclIsKindOf(Relationship)))))"""
        raise NotImplementedError(
            'operation sources_and_targets_kind(...) not yet implemented')

    def convey_classifiers(self, diagnostics=None, context=None):
        """An information flow can only convey classifiers that are allowed to represent an information item.
self.conveyed->forAll(oclIsKindOf(Class) or oclIsKindOf(Interface)
  or oclIsKindOf(InformationItem) or oclIsKindOf(Signal) or oclIsKindOf(Component))"""
        raise NotImplementedError(
            'operation convey_classifiers(...) not yet implemented')


class DestructionOccurrenceSpecificationMixin(object):
    """User defined mixin class for DestructionOccurrenceSpecification."""

    def __init__(self, **kwargs):
        super(DestructionOccurrenceSpecificationMixin, self).__init__(**kwargs)

    def no_occurrence_specifications_below(
            self, diagnostics=None, context=None):
        """No other OccurrenceSpecifications on a given Lifeline in an InteractionOperand may appear below a DestructionOccurrenceSpecification.
let o : InteractionOperand = enclosingOperand in o->notEmpty() and
let peerEvents : OrderedSet(OccurrenceSpecification) = covered.events->select(enclosingOperand = o)
in peerEvents->last() = self"""
        raise NotImplementedError(
            'operation no_occurrence_specifications_below(...) not yet implemented')


class FinalStateMixin(object):
    """User defined mixin class for FinalState."""

    def __init__(self, **kwargs):
        super(FinalStateMixin, self).__init__(**kwargs)

    def no_exit_behavior(self, diagnostics=None, context=None):
        """A FinalState has no exit Behavior.
exit->isEmpty()"""
        raise NotImplementedError(
            'operation no_exit_behavior(...) not yet implemented')

    def no_outgoing_transitions(self, diagnostics=None, context=None):
        """A FinalState cannot have any outgoing Transitions.
outgoing->size() = 0"""
        raise NotImplementedError(
            'operation no_outgoing_transitions(...) not yet implemented')

    def no_regions(self, diagnostics=None, context=None):
        """A FinalState cannot have Regions.
region->size() = 0"""
        raise NotImplementedError(
            'operation no_regions(...) not yet implemented')

    def cannot_reference_submachine(self, diagnostics=None, context=None):
        """A FinalState cannot reference a submachine.
submachine->isEmpty()"""
        raise NotImplementedError(
            'operation cannot_reference_submachine(...) not yet implemented')

    def no_entry_behavior(self, diagnostics=None, context=None):
        """A FinalState has no entry Behavior.
entry->isEmpty()"""
        raise NotImplementedError(
            'operation no_entry_behavior(...) not yet implemented')

    def no_state_behavior(self, diagnostics=None, context=None):
        """A FinalState has no state (doActivity) Behavior.
doActivity->isEmpty()"""
        raise NotImplementedError(
            'operation no_state_behavior(...) not yet implemented')


class DurationMixin(object):
    """User defined mixin class for Duration."""

    def __init__(self, expr=None, observation=None, **kwargs):
        super(DurationMixin, self).__init__(**kwargs)

    def no_expr_requires_observation(self, diagnostics=None, context=None):
        """If a Duration has no expr, then it must have a single observation that is a DurationObservation.
expr = null implies (observation->size() = 1 and observation->forAll(oclIsKindOf(DurationObservation)))"""
        raise NotImplementedError(
            'operation no_expr_requires_observation(...) not yet implemented')


class DurationConstraintMixin(object):
    """User defined mixin class for DurationConstraint."""

    def __init__(self, firstEvent=None, **kwargs):
        super(DurationConstraintMixin, self).__init__(**kwargs)

    def first_event_multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of firstEvent must be 2 if the multiplicity of constrainedElement is 2. Otherwise the multiplicity of firstEvent is 0.
if (constrainedElement->size() = 2)
  then (firstEvent->size() = 2) else (firstEvent->size() = 0)
endif"""
        raise NotImplementedError(
            'operation first_event_multiplicity(...) not yet implemented')

    def has_one_or_two_constrained_elements(
            self, diagnostics=None, context=None):
        """A DurationConstraint has either one or two constrainedElements.
constrainedElement->size() = 1 or constrainedElement->size()=2"""
        raise NotImplementedError(
            'operation has_one_or_two_constrained_elements(...) not yet implemented')


class IntervalMixin(object):
    """User defined mixin class for Interval."""

    def __init__(self, max=None, min=None, **kwargs):
        super(IntervalMixin, self).__init__(**kwargs)


class LiteralSpecificationMixin(object):
    """User defined mixin class for LiteralSpecification."""

    def __init__(self, **kwargs):
        super(LiteralSpecificationMixin, self).__init__(**kwargs)


class TimeConstraintMixin(object):
    """User defined mixin class for TimeConstraint."""

    def __init__(self, firstEvent=None, **kwargs):
        super(TimeConstraintMixin, self).__init__(**kwargs)

    def has_one_constrained_element(self, diagnostics=None, context=None):
        """A TimeConstraint has one constrainedElement.
constrainedElement->size() = 1"""
        raise NotImplementedError(
            'operation has_one_constrained_element(...) not yet implemented')


class ProfileMixin(object):
    """User defined mixin class for Profile."""

    def __init__(
            self, metaclassReference=None, metamodelReference=None, **
            kwargs):
        super(ProfileMixin, self).__init__(**kwargs)

    def metaclass_reference_not_specialized(
            self, diagnostics=None, context=None):
        """An element imported as a metaclassReference is not specialized or generalized in a Profile.
metaclassReference.importedElement->
        select(c | c.oclIsKindOf(Classifier) and
                (c.oclAsType(Classifier).allParents()->collect(namespace)->includes(self)))->isEmpty()
and
packagedElement->
    select(oclIsKindOf(Classifier))->collect(oclAsType(Classifier).allParents())->
       intersection(metaclassReference.importedElement->select(oclIsKindOf(Classifier))->collect(oclAsType(Classifier)))->isEmpty()"""
        raise NotImplementedError(
            'operation metaclass_reference_not_specialized(...) not yet implemented')

    def references_same_metamodel(self, diagnostics=None, context=None):
        """All elements imported either as metaclassReferences or through metamodelReferences are members of the same base reference metamodel.
metamodelReference.importedPackage.elementImport.importedElement.allOwningPackages()->
  union(metaclassReference.importedElement.allOwningPackages() )->notEmpty()"""
        raise NotImplementedError(
            'operation references_same_metamodel(...) not yet implemented')

    def create(self, classifier=None):
        """Creates and returns an instance of (the Ecore representation of) the specified classifier defined in this profile."""
        raise NotImplementedError('operation create(...) not yet implemented')

    def define(self, options=None, diagnostics=None, context=None):
        """Defines this profile by (re)creating Ecore representations of its current contents, using the specified options, diagnostics, and context."""
        from .profile_utils import UML_20_URI, define_profile
        eannotation = self.getEAnnotation(UML_20_URI)
        if not eannotation:
            eannotation = ecore.EAnnotation(source=UML_20_URI)
        eannotation.contents.append(define_profile(self))
        self.eAnnotations.append(eannotation)

    def get_definition(self):
        """Retrieves the current definition (Ecore representation) of this profile."""
        raise NotImplementedError(
            'operation get_definition(...) not yet implemented')

    def get_definition(self, namedElement=None):
        """Retrieves the current definition (Ecore representation) of the specified named element in this profile."""
        raise NotImplementedError(
            'operation get_definition(...) not yet implemented')

    def get_owned_extensions(self, requiredOnly=None):
        """Retrieves the extensions owned by this profile, excluding non-required extensions if indicated."""
        raise NotImplementedError(
            'operation get_owned_extensions(...) not yet implemented')

    def get_referenced_metaclasses(self):
        """Retrieves the metaclasses referenced by this profile."""
        raise NotImplementedError(
            'operation get_referenced_metaclasses(...) not yet implemented')

    def get_referenced_metamodels(self):
        """Retrieves the metamodels referenced by this profile."""
        raise NotImplementedError(
            'operation get_referenced_metamodels(...) not yet implemented')

    def is_defined(self):
        """Determines whether this profile is defined."""
        raise NotImplementedError(
            'operation is_defined(...) not yet implemented')


class DeploymentMixin(object):
    """User defined mixin class for Deployment."""

    def __init__(
            self, configuration=None, deployedArtifact=None, location=None,
            **kwargs):
        super(DeploymentMixin, self).__init__(**kwargs)


class AbstractionMixin(object):
    """User defined mixin class for Abstraction."""

    def __init__(self, mapping=None, **kwargs):
        super(AbstractionMixin, self).__init__(**kwargs)


class EnumerationLiteralMixin(object):
    """User defined mixin class for EnumerationLiteral."""

    def __init__(self, enumeration=None, **kwargs):
        super(EnumerationLiteralMixin, self).__init__(**kwargs)

    def get_classifiers(self):

        raise NotImplementedError(
            'operation get_classifiers(...) not yet implemented')

    def get_classifier(self):
        """Derivation of Enumeration::/classifier
result = (enumeration)
<p>From package UML::SimpleClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_classifier(...) not yet implemented')


class ModelMixin(object):
    """User defined mixin class for Model."""

    def __init__(self, viewpoint=None, **kwargs):
        super(ModelMixin, self).__init__(**kwargs)

    def is_metamodel(self):
        """Determines whether this model is a metamodel."""
        raise NotImplementedError(
            'operation is_metamodel(...) not yet implemented')


class UsageMixin(object):
    """User defined mixin class for Usage."""

    def __init__(self, **kwargs):
        super(UsageMixin, self).__init__(**kwargs)


class ValueSpecificationActionMixin(object):
    """User defined mixin class for ValueSpecificationAction."""

    def __init__(self, result=None, value=None, **kwargs):
        super(ValueSpecificationActionMixin, self).__init__(**kwargs)

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the result OutputPin is 1..1
result.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def compatible_type(self, diagnostics=None, context=None):
        """The type of the value ValueSpecification must conform to the type of the result OutputPin.
value.type.conformsTo(result.type)"""
        raise NotImplementedError(
            'operation compatible_type(...) not yet implemented')


class VariableActionMixin(object):
    """User defined mixin class for VariableAction."""

    def __init__(self, variable=None, **kwargs):
        super(VariableActionMixin, self).__init__(**kwargs)

    def scope_of_variable(self, diagnostics=None, context=None):
        """The VariableAction must be in the scope of the variable.
variable.isAccessibleBy(self)"""
        raise NotImplementedError(
            'operation scope_of_variable(...) not yet implemented')


class LinkActionMixin(object):
    """User defined mixin class for LinkAction."""

    def __init__(self, endData=None, inputValue=None, **kwargs):
        super(LinkActionMixin, self).__init__(**kwargs)

    def same_pins(self, diagnostics=None, context=None):
        """The inputValue InputPins is the same as the union of all the InputPins referenced by the endData.
inputValue->asBag()=endData.allPins()"""
        raise NotImplementedError(
            'operation same_pins(...) not yet implemented')

    def same_association(self, diagnostics=None, context=None):
        """The ends of the endData must all be from the same Association and include all and only the memberEnds of that association.
endData.end = self.association().memberEnd->asBag()"""
        raise NotImplementedError(
            'operation same_association(...) not yet implemented')

    def not_static(self, diagnostics=None, context=None):
        """The ends of the endData must not be static.
endData->forAll(not end.isStatic)"""
        raise NotImplementedError(
            'operation not_static(...) not yet implemented')

    def association(self):
        """Returns the Association acted on by this LinkAction.
result = (endData->asSequence()->first().end.association)
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation association(...) not yet implemented')


class StructuralFeatureActionMixin(object):
    """User defined mixin class for StructuralFeatureAction."""

    def __init__(self, object=None, structuralFeature=None, **kwargs):
        super(StructuralFeatureActionMixin, self).__init__(**kwargs)

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the object InputPin must be 1..1.
object.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def object_type(self, diagnostics=None, context=None):
        """The structuralFeature must either be an owned or inherited feature of the type of the object InputPin, or it must be an owned end of a binary Association whose opposite end had as a type to which the type of the object InputPin conforms.
object.type.oclAsType(Classifier).allFeatures()->includes(structuralFeature) or
        object.type.conformsTo(structuralFeature.oclAsType(Property).opposite.type)"""
        raise NotImplementedError(
            'operation object_type(...) not yet implemented')

    def visibility(self, diagnostics=None, context=None):
        """The visibility of the structuralFeature must allow access from the object performing the ReadStructuralFeatureAction.
structuralFeature.visibility = VisibilityKind::public or
_'context'.allFeatures()->includes(structuralFeature) or
structuralFeature.visibility=VisibilityKind::protected and
_'context'.conformsTo(structuralFeature.oclAsType(Property).opposite.type.oclAsType(Classifier))"""
        raise NotImplementedError(
            'operation visibility(...) not yet implemented')

    def not_static(self, diagnostics=None, context=None):
        """The structuralFeature must not be static.
not structuralFeature.isStatic"""
        raise NotImplementedError(
            'operation not_static(...) not yet implemented')

    def one_featuring_classifier(self, diagnostics=None, context=None):
        """The structuralFeature must have exactly one featuringClassifier.
structuralFeature.featuringClassifier->size() = 1"""
        raise NotImplementedError(
            'operation one_featuring_classifier(...) not yet implemented')


class AcceptEventActionMixin(object):
    """User defined mixin class for AcceptEventAction."""

    def __init__(
            self, isUnmarshall=None, result=None, trigger=None, **kwargs):
        super(AcceptEventActionMixin, self).__init__(**kwargs)

    def one_output_pin(self, diagnostics=None, context=None):
        """If isUnmarshall=false and any of the triggers are for SignalEvents or TimeEvents, there must be exactly one result OutputPin with multiplicity 1..1.
not isUnmarshall and trigger->exists(event.oclIsKindOf(SignalEvent) or event.oclIsKindOf(TimeEvent)) implies
        output->size() = 1 and output->first().is(1,1)"""
        raise NotImplementedError(
            'operation one_output_pin(...) not yet implemented')

    def no_input_pins(self, diagnostics=None, context=None):
        """AcceptEventActions may have no input pins.
input->size() = 0"""
        raise NotImplementedError(
            'operation no_input_pins(...) not yet implemented')

    def no_output_pins(self, diagnostics=None, context=None):
        """There are no OutputPins if the trigger events are only ChangeEvents and/or CallEvents when this action is an instance of AcceptEventAction and not an instance of a descendant of AcceptEventAction (such as AcceptCallAction).
(self.oclIsTypeOf(AcceptEventAction) and
   (trigger->forAll(event.oclIsKindOf(ChangeEvent) or
                             event.oclIsKindOf(CallEvent))))
implies output->size() = 0"""
        raise NotImplementedError(
            'operation no_output_pins(...) not yet implemented')

    def unmarshall_signal_events(self, diagnostics=None, context=None):
        """If isUnmarshall is true (and this is not an AcceptCallAction), there must be exactly one trigger, which is for a SignalEvent. The number of result output pins must be the same as the number of attributes of the signal. The type and ordering of each result output pin must be the same as the corresponding attribute of the signal. The multiplicity of each result output pin must be compatible with the multiplicity of the corresponding attribute.
isUnmarshall and self.oclIsTypeOf(AcceptEventAction) implies
        trigger->size()=1 and
        trigger->asSequence()->first().event.oclIsKindOf(SignalEvent) and
        let attribute: OrderedSet(Property) = trigger->asSequence()->first().event.oclAsType(SignalEvent).signal.allAttributes() in
        attribute->size()>0 and result->size() = attribute->size() and
        Sequence{1..result->size()}->forAll(i |
                result->at(i).type = attribute->at(i).type and
                result->at(i).isOrdered = attribute->at(i).isOrdered and
                result->at(i).includesMultiplicity(attribute->at(i)))"""
        raise NotImplementedError(
            'operation unmarshall_signal_events(...) not yet implemented')

    def conforming_type(self, diagnostics=None, context=None):
        """If isUnmarshall=false and all the triggers are for SignalEvents, then the type of the single result OutputPin must either be null or all the signals must conform to it.
not isUnmarshall implies
        result->isEmpty() or
        let type: Type = result->first().type in
        type=null or
                (trigger->forAll(event.oclIsKindOf(SignalEvent)) and
                 trigger.event.oclAsType(SignalEvent).signal->forAll(s | s.conformsTo(type)))"""
        raise NotImplementedError(
            'operation conforming_type(...) not yet implemented')


class InvocationActionMixin(object):
    """User defined mixin class for InvocationAction."""

    def __init__(self, argument=None, onPort=None, **kwargs):
        super(InvocationActionMixin, self).__init__(**kwargs)


class ClearAssociationActionMixin(object):
    """User defined mixin class for ClearAssociationAction."""

    def __init__(self, association=None, object=None, **kwargs):
        super(ClearAssociationActionMixin, self).__init__(**kwargs)

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the object InputPin is 1..1.
object.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def same_type(self, diagnostics=None, context=None):
        """The type of the InputPin must conform to the type of at least one of the memberEnds of the association.
association.memberEnd->exists(self.object.type.conformsTo(type))"""
        raise NotImplementedError(
            'operation same_type(...) not yet implemented')


class CreateObjectActionMixin(object):
    """User defined mixin class for CreateObjectAction."""

    def __init__(self, classifier=None, result=None, **kwargs):
        super(CreateObjectActionMixin, self).__init__(**kwargs)

    def classifier_not_abstract(self, diagnostics=None, context=None):
        """The classifier cannot be abstract.
not classifier.isAbstract"""
        raise NotImplementedError(
            'operation classifier_not_abstract(...) not yet implemented')

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the result OutputPin is 1..1.
result.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def classifier_not_association_class(self, diagnostics=None, context=None):
        """The classifier cannot be an AssociationClass.
not classifier.oclIsKindOf(AssociationClass)"""
        raise NotImplementedError(
            'operation classifier_not_association_class(...) not yet implemented')

    def same_type(self, diagnostics=None, context=None):
        """The type of the result OutputPin must be the same as the classifier of the CreateObjectAction.
result.type = classifier"""
        raise NotImplementedError(
            'operation same_type(...) not yet implemented')


class DestroyObjectActionMixin(object):
    """User defined mixin class for DestroyObjectAction."""

    def __init__(
            self, isDestroyLinks=None, isDestroyOwnedObjects=None,
            target=None, **kwargs):
        super(DestroyObjectActionMixin, self).__init__(**kwargs)

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the targe IinputPin is 1..1.
target.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def no_type(self, diagnostics=None, context=None):
        """The target InputPin has no type.
target.type= null"""
        raise NotImplementedError('operation no_type(...) not yet implemented')


class ExpansionNodeMixin(object):
    """User defined mixin class for ExpansionNode."""

    def __init__(self, regionAsInput=None, regionAsOutput=None, **kwargs):
        super(ExpansionNodeMixin, self).__init__(**kwargs)

    def region_as_input_or_output(self, diagnostics=None, context=None):
        """One of regionAsInput or regionAsOutput must be non-empty, but not both.
regionAsInput->notEmpty() xor regionAsOutput->notEmpty()"""
        raise NotImplementedError(
            'operation region_as_input_or_output(...) not yet implemented')


class OpaqueActionMixin(object):
    """User defined mixin class for OpaqueAction."""

    def __init__(
            self, body=None, inputValue=None, language=None,
            outputValue=None, **kwargs):
        super(OpaqueActionMixin, self).__init__(**kwargs)

    def language_body_size(self, diagnostics=None, context=None):
        """If the language attribute is not empty, then the size of the body and language lists must be the same.
language->notEmpty() implies (_'body'->size() = language->size())"""
        raise NotImplementedError(
            'operation language_body_size(...) not yet implemented')


class RaiseExceptionActionMixin(object):
    """User defined mixin class for RaiseExceptionAction."""

    def __init__(self, exception=None, **kwargs):
        super(RaiseExceptionActionMixin, self).__init__(**kwargs)


class ReadExtentActionMixin(object):
    """User defined mixin class for ReadExtentAction."""

    def __init__(self, classifier=None, result=None, **kwargs):
        super(ReadExtentActionMixin, self).__init__(**kwargs)

    def type_is_classifier(self, diagnostics=None, context=None):
        """The type of the result OutputPin is the classifier.
result.type = classifier"""
        raise NotImplementedError(
            'operation type_is_classifier(...) not yet implemented')

    def multiplicity_of_result(self, diagnostics=None, context=None):
        """The multiplicity of the result OutputPin is 0..*.
result.is(0,*)"""
        raise NotImplementedError(
            'operation multiplicity_of_result(...) not yet implemented')


class ReadIsClassifiedObjectActionMixin(object):
    """User defined mixin class for ReadIsClassifiedObjectAction."""

    def __init__(
            self, classifier=None, isDirect=None, object=None, result=None,
            **kwargs):
        super(ReadIsClassifiedObjectActionMixin, self).__init__(**kwargs)

    def no_type(self, diagnostics=None, context=None):
        """The object InputPin has no type.
object.type = null"""
        raise NotImplementedError('operation no_type(...) not yet implemented')

    def multiplicity_of_output(self, diagnostics=None, context=None):
        """The multiplicity of the result OutputPin is 1..1.
result.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_output(...) not yet implemented')

    def boolean_result(self, diagnostics=None, context=None):
        """The type of the result OutputPin is Boolean.
result.type = Boolean"""
        raise NotImplementedError(
            'operation boolean_result(...) not yet implemented')

    def multiplicity_of_input(self, diagnostics=None, context=None):
        """The multiplicity of the object InputPin is 1..1.
object.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_input(...) not yet implemented')


class ReadLinkObjectEndActionMixin(object):
    """User defined mixin class for ReadLinkObjectEndAction."""

    def __init__(self, end=None, object=None, result=None, **kwargs):
        super(ReadLinkObjectEndActionMixin, self).__init__(**kwargs)

    def property(self, diagnostics=None, context=None):
        """The end Property must be an Association memberEnd.
end.association <> null"""
        raise NotImplementedError(
            'operation property(...) not yet implemented')

    def multiplicity_of_object(self, diagnostics=None, context=None):
        """The multiplicity of the object InputPin is 1..1.
object.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_object(...) not yet implemented')

    def ends_of_association(self, diagnostics=None, context=None):
        """The ends of the association must not be static.
end.association.memberEnd->forAll(e | not e.isStatic)"""
        raise NotImplementedError(
            'operation ends_of_association(...) not yet implemented')

    def type_of_result(self, diagnostics=None, context=None):
        """The type of the result OutputPin is the same as the type of the end Property.
result.type = end.type"""
        raise NotImplementedError(
            'operation type_of_result(...) not yet implemented')

    def multiplicity_of_result(self, diagnostics=None, context=None):
        """The multiplicity of the result OutputPin is 1..1.
result.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_result(...) not yet implemented')

    def type_of_object(self, diagnostics=None, context=None):
        """The type of the object InputPin is the AssociationClass that owns the end Property.
object.type = end.association"""
        raise NotImplementedError(
            'operation type_of_object(...) not yet implemented')

    def association_of_association(self, diagnostics=None, context=None):
        """The association of the end must be an AssociationClass.
end.association.oclIsKindOf(AssociationClass)"""
        raise NotImplementedError(
            'operation association_of_association(...) not yet implemented')


class ReadLinkObjectEndQualifierActionMixin(object):
    """User defined mixin class for ReadLinkObjectEndQualifierAction."""

    def __init__(self, object=None, qualifier=None, result=None, **kwargs):
        super(ReadLinkObjectEndQualifierActionMixin, self).__init__(**kwargs)

    def multiplicity_of_object(self, diagnostics=None, context=None):
        """The multiplicity of the object InputPin is 1..1.
object.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_object(...) not yet implemented')

    def type_of_object(self, diagnostics=None, context=None):
        """The type of the object InputPin is the AssociationClass that owns the Association end that has the given qualifier Property.
object.type = qualifier.associationEnd.association"""
        raise NotImplementedError(
            'operation type_of_object(...) not yet implemented')

    def multiplicity_of_qualifier(self, diagnostics=None, context=None):
        """The multiplicity of the qualifier Property is 1..1.
qualifier.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_qualifier(...) not yet implemented')

    def ends_of_association(self, diagnostics=None, context=None):
        """The ends of the Association must not be static.
qualifier.associationEnd.association.memberEnd->forAll(e | not e.isStatic)"""
        raise NotImplementedError(
            'operation ends_of_association(...) not yet implemented')

    def multiplicity_of_result(self, diagnostics=None, context=None):
        """The multiplicity of the result OutputPin is 1..1.
result.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_result(...) not yet implemented')

    def same_type(self, diagnostics=None, context=None):
        """The type of the result OutputPin is the same as the type of the qualifier Property.
result.type = qualifier.type"""
        raise NotImplementedError(
            'operation same_type(...) not yet implemented')

    def association_of_association(self, diagnostics=None, context=None):
        """The association of the Association end of the qualifier Property must be an AssociationClass.
qualifier.associationEnd.association.oclIsKindOf(AssociationClass)"""
        raise NotImplementedError(
            'operation association_of_association(...) not yet implemented')

    def qualifier_attribute(self, diagnostics=None, context=None):
        """The qualifier Property must be a qualifier of an Association end.
qualifier.associationEnd <> null"""
        raise NotImplementedError(
            'operation qualifier_attribute(...) not yet implemented')


class ReadSelfActionMixin(object):
    """User defined mixin class for ReadSelfAction."""

    def __init__(self, result=None, **kwargs):
        super(ReadSelfActionMixin, self).__init__(**kwargs)

    def contained(self, diagnostics=None, context=None):
        """A ReadSelfAction must have a context Classifier.
_'context' <> null"""
        raise NotImplementedError(
            'operation contained(...) not yet implemented')

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the result OutputPin is 1..1.
result.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def not_static(self, diagnostics=None, context=None):
        """If the ReadSelfAction is contained in an Behavior that is acting as a method, then the Operation of the method must not be static.
let behavior: Behavior = self.containingBehavior() in
behavior.specification<>null implies not behavior.specification.isStatic"""
        raise NotImplementedError(
            'operation not_static(...) not yet implemented')

    def type(self, diagnostics=None, context=None):
        """The type of the result OutputPin is the context Classifier.
result.type = _'context'"""
        raise NotImplementedError('operation type(...) not yet implemented')


class ReclassifyObjectActionMixin(object):
    """User defined mixin class for ReclassifyObjectAction."""

    def __init__(
            self, isReplaceAll=None, newClassifier=None, object=None,
            oldClassifier=None, **kwargs):
        super(ReclassifyObjectActionMixin, self).__init__(**kwargs)

    def input_pin(self, diagnostics=None, context=None):
        """The object InputPin has no type.
object.type = null"""
        raise NotImplementedError(
            'operation input_pin(...) not yet implemented')

    def classifier_not_abstract(self, diagnostics=None, context=None):
        """None of the newClassifiers may be abstract.
not newClassifier->exists(isAbstract)"""
        raise NotImplementedError(
            'operation classifier_not_abstract(...) not yet implemented')

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the object InputPin is 1..1.
object.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')


class ReduceActionMixin(object):
    """User defined mixin class for ReduceAction."""

    def __init__(
            self, collection=None, isOrdered=None, reducer=None,
            result=None, **kwargs):
        super(ReduceActionMixin, self).__init__(**kwargs)

    def reducer_inputs_output(self, diagnostics=None, context=None):
        """The reducer Behavior must have two input ownedParameters and one output ownedParameter, where the type of the output Parameter and the type of elements of the input collection conform to the types of the input Parameters.
let inputs: OrderedSet(Parameter) = reducer.inputParameters() in
let outputs: OrderedSet(Parameter) = reducer.outputParameters() in
inputs->size()=2 and outputs->size()=1 and
inputs.type->forAll(t |
        outputs.type->forAll(conformsTo(t)) and
        -- Note that the following only checks the case when the collection is via multiple tokens.
        collection.upperBound()>1 implies collection.type.conformsTo(t))"""
        raise NotImplementedError(
            'operation reducer_inputs_output(...) not yet implemented')

    def input_type_is_collection(self, diagnostics=None, context=None):
        """The type of the collection InputPin must be a collection."""
        raise NotImplementedError(
            'operation input_type_is_collection(...) not yet implemented')

    def output_types_are_compatible(self, diagnostics=None, context=None):
        """The type of the output of the reducer Behavior must conform to the type of the result OutputPin.
reducer.outputParameters().type->forAll(conformsTo(result.type))"""
        raise NotImplementedError(
            'operation output_types_are_compatible(...) not yet implemented')


class ReplyActionMixin(object):
    """User defined mixin class for ReplyAction."""

    def __init__(self, replyToCall=None, replyValue=None,
                 returnInformation=None, **kwargs):
        super(ReplyActionMixin, self).__init__(**kwargs)

    def pins_match_parameter(self, diagnostics=None, context=None):
        """The replyValue InputPins must match the output (return, out, and inout) parameters of the operation of the event of the replyToCall Trigger in number, type, ordering, and multiplicity.
let parameter:OrderedSet(Parameter) = replyToCall.event.oclAsType(CallEvent).operation.outputParameters() in
replyValue->size()=parameter->size() and
Sequence{1..replyValue->size()}->forAll(i |
        replyValue->at(i).type.conformsTo(parameter->at(i).type) and
        replyValue->at(i).isOrdered=parameter->at(i).isOrdered and
        replyValue->at(i).compatibleWith(parameter->at(i)))"""
        raise NotImplementedError(
            'operation pins_match_parameter(...) not yet implemented')

    def event_on_reply_to_call_trigger(self, diagnostics=None, context=None):
        """The event of the replyToCall Trigger must be a CallEvent.
replyToCall.event.oclIsKindOf(CallEvent)"""
        raise NotImplementedError(
            'operation event_on_reply_to_call_trigger(...) not yet implemented')


class StartClassifierBehaviorActionMixin(object):
    """User defined mixin class for StartClassifierBehaviorAction."""

    def __init__(self, object=None, **kwargs):
        super(StartClassifierBehaviorActionMixin, self).__init__(**kwargs)

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the object InputPin is 1..1
object.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def type_has_classifier(self, diagnostics=None, context=None):
        """If the InputPin has a type, then the type or one of its ancestors must have a classifierBehavior.
object.type->notEmpty() implies
   (object.type.oclIsKindOf(BehavioredClassifier) and object.type.oclAsType(BehavioredClassifier).classifierBehavior<>null)"""
        raise NotImplementedError(
            'operation type_has_classifier(...) not yet implemented')


class TestIdentityActionMixin(object):
    """User defined mixin class for TestIdentityAction."""

    def __init__(self, first=None, result=None, second=None, **kwargs):
        super(TestIdentityActionMixin, self).__init__(**kwargs)

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the InputPins is 1..1.
first.is(1,1) and second.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def no_type(self, diagnostics=None, context=None):
        """The InputPins have no type.
first.type= null and second.type = null"""
        raise NotImplementedError('operation no_type(...) not yet implemented')

    def result_is_boolean(self, diagnostics=None, context=None):
        """The type of the result OutputPin is Boolean.
result.type=Boolean"""
        raise NotImplementedError(
            'operation result_is_boolean(...) not yet implemented')


class UnmarshallActionMixin(object):
    """User defined mixin class for UnmarshallAction."""

    def __init__(
            self, object=None, result=None, unmarshallType=None, **kwargs):
        super(UnmarshallActionMixin, self).__init__(**kwargs)

    def structural_feature(self, diagnostics=None, context=None):
        """The unmarshallType must have at least one StructuralFeature.
unmarshallType.allAttributes()->size() >= 1"""
        raise NotImplementedError(
            'operation structural_feature(...) not yet implemented')

    def number_of_result(self, diagnostics=None, context=None):
        """The number of result outputPins must be the same as the number of attributes of the unmarshallType.
unmarshallType.allAttributes()->size() = result->size()"""
        raise NotImplementedError(
            'operation number_of_result(...) not yet implemented')

    def type_ordering_and_multiplicity(self, diagnostics=None, context=None):
        """The type, ordering and multiplicity of each attribute of the unmarshallType must be compatible with the type, ordering and multiplicity of the corresponding result OutputPin.
let attribute:OrderedSet(Property) = unmarshallType.allAttributes() in
Sequence{1..result->size()}->forAll(i |
        attribute->at(i).type.conformsTo(result->at(i).type) and
        attribute->at(i).isOrdered=result->at(i).isOrdered and
        attribute->at(i).compatibleWith(result->at(i)))"""
        raise NotImplementedError(
            'operation type_ordering_and_multiplicity(...) not yet implemented')

    def multiplicity_of_object(self, diagnostics=None, context=None):
        """The multiplicity of the object InputPin is 1..1
object.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_object(...) not yet implemented')

    def object_type(self, diagnostics=None, context=None):
        """The type of the object InputPin conform to the unmarshallType.
object.type.conformsTo(unmarshallType)"""
        raise NotImplementedError(
            'operation object_type(...) not yet implemented')


class ActivityFinalNodeMixin(object):
    """User defined mixin class for ActivityFinalNode."""

    def __init__(self, **kwargs):
        super(ActivityFinalNodeMixin, self).__init__(**kwargs)


class ActivityParameterNodeMixin(object):
    """User defined mixin class for ActivityParameterNode."""

    def __init__(self, parameter=None, **kwargs):
        super(ActivityParameterNodeMixin, self).__init__(**kwargs)

    def no_outgoing_edges(self, diagnostics=None, context=None):
        """An ActivityParameterNode with no outgoing ActivityEdges and one or more incoming ActivityEdges must have a parameter with direction out, inout, or return.
(incoming->notEmpty() and outgoing->isEmpty()) implies
        (parameter.direction = ParameterDirectionKind::out or
         parameter.direction = ParameterDirectionKind::inout or
         parameter.direction = ParameterDirectionKind::return)"""
        raise NotImplementedError(
            'operation no_outgoing_edges(...) not yet implemented')

    def has_parameters(self, diagnostics=None, context=None):
        """The parameter of an ActivityParameterNode must be from the containing Activity.
activity.ownedParameter->includes(parameter)"""
        raise NotImplementedError(
            'operation has_parameters(...) not yet implemented')

    def same_type(self, diagnostics=None, context=None):
        """The type of an ActivityParameterNode is the same as the type of its parameter.
type = parameter.type"""
        raise NotImplementedError(
            'operation same_type(...) not yet implemented')

    def no_incoming_edges(self, diagnostics=None, context=None):
        """An ActivityParameterNode with no incoming ActivityEdges and one or more outgoing ActivityEdges must have a parameter with direction in or inout.
(outgoing->notEmpty() and incoming->isEmpty()) implies
        (parameter.direction = ParameterDirectionKind::_'in' or
         parameter.direction = ParameterDirectionKind::inout)"""
        raise NotImplementedError(
            'operation no_incoming_edges(...) not yet implemented')

    def no_edges(self, diagnostics=None, context=None):
        """An ActivityParameterNode may have all incoming ActivityEdges or all outgoing ActivityEdges, but it must not have both incoming and outgoing ActivityEdges.
incoming->isEmpty() or outgoing->isEmpty()"""
        raise NotImplementedError(
            'operation no_edges(...) not yet implemented')


class CentralBufferNodeMixin(object):
    """User defined mixin class for CentralBufferNode."""

    def __init__(self, **kwargs):
        super(CentralBufferNodeMixin, self).__init__(**kwargs)


class FlowFinalNodeMixin(object):
    """User defined mixin class for FlowFinalNode."""

    def __init__(self, **kwargs):
        super(FlowFinalNodeMixin, self).__init__(**kwargs)


class DurationIntervalMixin(object):
    """User defined mixin class for DurationInterval."""

    def __init__(self, **kwargs):
        super(DurationIntervalMixin, self).__init__(**kwargs)


class LiteralBooleanMixin(object):
    """User defined mixin class for LiteralBoolean."""

    def __init__(self, value=None, **kwargs):
        super(LiteralBooleanMixin, self).__init__(**kwargs)


class LiteralIntegerMixin(object):
    """User defined mixin class for LiteralInteger."""

    def __init__(self, value=None, **kwargs):
        super(LiteralIntegerMixin, self).__init__(**kwargs)


class LiteralNullMixin(object):
    """User defined mixin class for LiteralNull."""

    def __init__(self, **kwargs):
        super(LiteralNullMixin, self).__init__(**kwargs)


class LiteralRealMixin(object):
    """User defined mixin class for LiteralReal."""

    def __init__(self, value=None, **kwargs):
        super(LiteralRealMixin, self).__init__(**kwargs)


class LiteralStringMixin(object):
    """User defined mixin class for LiteralString."""

    def __init__(self, value=None, **kwargs):
        super(LiteralStringMixin, self).__init__(**kwargs)


class LiteralUnlimitedNaturalMixin(object):
    """User defined mixin class for LiteralUnlimitedNatural."""

    def __init__(self, value=None, **kwargs):
        super(LiteralUnlimitedNaturalMixin, self).__init__(**kwargs)


class TimeIntervalMixin(object):
    """User defined mixin class for TimeInterval."""

    def __init__(self, **kwargs):
        super(TimeIntervalMixin, self).__init__(**kwargs)


class DerivedFeature(EDerivedCollection):
    pass


class DerivedAttribute(EDerivedCollection):
    pass


class DerivedGeneral(EDerivedCollection):
    pass


class DerivedInheritedmember(EDerivedCollection):
    pass


class ClassifierMixin(object):
    """User defined mixin class for Classifier."""

    def __init__(
            self, feature=None, attribute=None, collaborationUse=None,
            general=None, generalization=None, powertypeExtent=None,
            inheritedMember=None, isAbstract=None, isFinalSpecialization=None,
            ownedUseCase=None, useCase=None, redefinedClassifier=None,
            representation=None, substitution=None, **kwargs):
        super(ClassifierMixin, self).__init__(**kwargs)

    def specialize_type(self, diagnostics=None, context=None):
        """A Classifier may only specialize Classifiers of a valid type.
parents()->forAll(c | self.maySpecializeType(c))"""
        raise NotImplementedError(
            'operation specialize_type(...) not yet implemented')

    def maps_to_generalization_set(self, diagnostics=None, context=None):
        """The Classifier that maps to a GeneralizationSet may neither be a specific nor a general Classifier in any of the Generalization relationships defined for that GeneralizationSet. In other words, a power type may not be an instance of itself nor may its instances also be its subclasses.
powertypeExtent->forAll( gs |
  gs.generalization->forAll( gen |
    not (gen.general = self) and not gen.general.allParents()->includes(self) and not (gen.specific = self) and not self.allParents()->includes(gen.specific)
  ))"""
        raise NotImplementedError(
            'operation maps_to_generalization_set(...) not yet implemented')

    def non_final_parents(self, diagnostics=None, context=None):
        """The parents of a Classifier must be non-final.
parents()->forAll(not isFinalSpecialization)"""
        raise NotImplementedError(
            'operation non_final_parents(...) not yet implemented')

    def no_cycles_in_generalization(self, diagnostics=None, context=None):
        """Generalization hierarchies must be directed and acyclical. A Classifier can not be both a transitively general and transitively specific Classifier of the same Classifier.
not allParents()->includes(self)"""
        raise NotImplementedError(
            'operation no_cycles_in_generalization(...) not yet implemented')

    def get_all_attributes(self):
        """Retrieves all the attributes of this classifier, including those inherited from its parents."""
        raise NotImplementedError(
            'operation get_all_attributes(...) not yet implemented')

    def get_all_operations(self):
        """Retrieves all the operations of this classifier, including those inherited from its parents."""
        raise NotImplementedError(
            'operation get_all_operations(...) not yet implemented')

    def get_all_used_interfaces(self):
        """Retrieves all the interfaces on which this classifier or any of its parents has a usage dependency."""
        raise NotImplementedError(
            'operation get_all_used_interfaces(...) not yet implemented')

    def get_operation(self, name=None, parameterNames=None,
                      parameterTypes=None):
        """Retrieves the first operation with the specified name, parameter names, and parameter types from this classifier."""
        raise NotImplementedError(
            'operation get_operation(...) not yet implemented')

    def get_operation(self, name=None, parameterNames=None,
                      parameterTypes=None, ignoreCase=None):
        """Retrieves the first operation with the specified name, parameter names, and parameter types from this classifier, ignoring case if indicated."""
        raise NotImplementedError(
            'operation get_operation(...) not yet implemented')

    def get_operations(self):
        """Retrieves the operations of this classifier."""
        raise NotImplementedError(
            'operation get_operations(...) not yet implemented')

    def get_used_interfaces(self):
        """Retrieves the interfaces on which this classifier has a usage dependency."""
        raise NotImplementedError(
            'operation get_used_interfaces(...) not yet implemented')

    def all_features(self):
        """The query allFeatures() gives all of the Features in the namespace of the Classifier. In general, through mechanisms such as inheritance, this will be a larger set than feature.
result = (member->select(oclIsKindOf(Feature))->collect(oclAsType(Feature))->asSet())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation all_features(...) not yet implemented')

    def all_parents(self):
        """The query allParents() gives all of the direct and indirect ancestors of a generalized Classifier.
result = (parents()->union(parents()->collect(allParents())->asSet()))
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation all_parents(...) not yet implemented')

    def get_generals(self):
        """The general Classifiers are the ones referenced by the Generalization relationships.
result = (parents())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation get_generals(...) not yet implemented')

    def has_visibility_of(self, n=None):
        """The query hasVisibilityOf() determines whether a NamedElement is visible in the classifier. Non-private members are visible. It is only called when the argument is something owned by a parent.
allParents()->including(self)->collect(member)->includes(n)
result = (n.visibility <> VisibilityKind::private)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation has_visibility_of(...) not yet implemented')

    def inherit(self, inhs=None):
        """The query inherit() defines how to inherit a set of elements passed as its argument.  It excludes redefined elements from the result.
result = (inhs->reject(inh |
  inh.oclIsKindOf(RedefinableElement) and
  ownedMember->select(oclIsKindOf(RedefinableElement))->
    select(redefinedElement->includes(inh.oclAsType(RedefinableElement)))
       ->notEmpty()))
<p>From package UML::Classification.</p>"""
        raise NotImplementedError('operation inherit(...) not yet implemented')

    def inheritable_members(self, c=None):
        """The query inheritableMembers() gives all of the members of a Classifier that may be inherited in one of its descendants, subject to whatever visibility restrictions apply.
c.allParents()->includes(self)
result = (member->select(m | c.hasVisibilityOf(m)))
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation inheritable_members(...) not yet implemented')

    def get_inherited_members(self):
        """The inheritedMember association is derived by inheriting the inheritable members of the parents.
result = (inherit(parents()->collect(inheritableMembers(self))->asSet()))
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation get_inherited_members(...) not yet implemented')

    def may_specialize_type(self, c=None):
        """The query maySpecializeType() determines whether this classifier may have a generalization relationship to classifiers of the specified type. By default a classifier may specialize classifiers of the same or a more general type. It is intended to be redefined by classifiers that have different specialization constraints.
result = (self.oclIsKindOf(c.oclType()))
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation may_specialize_type(...) not yet implemented')

    def parents(self):
        """The query parents() gives all of the immediate ancestors of a generalized Classifier.
result = (generalization.general->asSet())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError('operation parents(...) not yet implemented')

    def directly_realized_interfaces(self):
        """The Interfaces directly realized by this Classifier
result = ((clientDependency->
  select(oclIsKindOf(Realization) and supplier->forAll(oclIsKindOf(Interface))))->
      collect(supplier.oclAsType(Interface))->asSet())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation directly_realized_interfaces(...) not yet implemented')

    def directly_used_interfaces(self):
        """The Interfaces directly used by this Classifier
result = ((supplierDependency->
  select(oclIsKindOf(Usage) and client->forAll(oclIsKindOf(Interface))))->
    collect(client.oclAsType(Interface))->asSet())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation directly_used_interfaces(...) not yet implemented')

    def all_realized_interfaces(self):
        """The Interfaces realized by this Classifier and all of its generalizations
result = (directlyRealizedInterfaces()->union(self.allParents()->collect(directlyRealizedInterfaces()))->asSet())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation all_realized_interfaces(...) not yet implemented')

    def all_used_interfaces(self):
        """The Interfaces used by this Classifier and all of its generalizations
result = (directlyUsedInterfaces()->union(self.allParents()->collect(directlyUsedInterfaces()))->asSet())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation all_used_interfaces(...) not yet implemented')

    def is_substitutable_for(self, contract=None):
        """result = (substitution.contract->includes(contract))
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation is_substitutable_for(...) not yet implemented')

    def all_attributes(self):
        """The query allAttributes gives an ordered set of all owned and inherited attributes of the Classifier. All owned attributes appear before any inherited attributes, and the attributes inherited from any more specific parent Classifier appear before those of any more general parent Classifier. However, if the Classifier has multiple immediate parents, then the relative ordering of the sets of attributes from those parents is not defined.
result = (attribute->asSequence()->union(parents()->asSequence().allAttributes())->select(p | member->includes(p))->asOrderedSet())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation all_attributes(...) not yet implemented')

    def all_slottable_features(self):
        """All StructuralFeatures related to the Classifier that may have Slots, including direct attributes, inherited attributes, private attributes in generalizations, and memberEnds of Associations, but excluding redefined StructuralFeatures.
result = (member->select(oclIsKindOf(StructuralFeature))->
  collect(oclAsType(StructuralFeature))->
   union(self.inherit(self.allParents()->collect(p | p.attribute)->asSet())->
     collect(oclAsType(StructuralFeature)))->asSet())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation all_slottable_features(...) not yet implemented')


class ManifestationMixin(object):
    """User defined mixin class for Manifestation."""

    def __init__(self, utilizedElement=None, **kwargs):
        super(ManifestationMixin, self).__init__(**kwargs)


class OperationMixin(object):
    """User defined mixin class for Operation."""

    @property
    def isOrdered(self):
        raise NotImplementedError('Missing implementation for isOrdered')

    @property
    def isUnique(self):
        raise NotImplementedError('Missing implementation for isUnique')

    @property
    def lower(self):
        raise NotImplementedError('Missing implementation for lower')

    @property
    def type(self):
        raise NotImplementedError('Missing implementation for type')

    @property
    def upper(self):
        raise NotImplementedError('Missing implementation for upper')

    def __init__(
            self, bodyCondition=None, class_=None, datatype=None,
            interface=None, isOrdered=None, isQuery=None, isUnique=None,
            lower=None, postcondition=None, precondition=None,
            redefinedOperation=None, type=None, upper=None, **kwargs):
        super(OperationMixin, self).__init__(**kwargs)

    def at_most_one_return(self, diagnostics=None, context=None):
        """An Operation can have at most one return parameter; i.e., an owned parameter with the direction set to 'return.'
self.ownedParameter->select(direction = ParameterDirectionKind::return)->size() <= 1"""
        raise NotImplementedError(
            'operation at_most_one_return(...) not yet implemented')

    def only_body_for_query(self, diagnostics=None, context=None):
        """A bodyCondition can only be specified for a query Operation.
bodyCondition <> null implies isQuery"""
        raise NotImplementedError(
            'operation only_body_for_query(...) not yet implemented')

    def get_return_result(self):
        """Retrieves the (only) return result parameter for this operation."""
        raise NotImplementedError(
            'operation get_return_result(...) not yet implemented')

    def set_is_ordered(self, newIsOrdered=None):

        raise NotImplementedError(
            'operation set_is_ordered(...) not yet implemented')

    def set_is_unique(self, newIsUnique=None):

        raise NotImplementedError(
            'operation set_is_unique(...) not yet implemented')

    def set_lower(self, newLower=None):

        raise NotImplementedError(
            'operation set_lower(...) not yet implemented')

    def set_type(self, newType=None):

        raise NotImplementedError(
            'operation set_type(...) not yet implemented')

    def set_upper(self, newUpper=None):

        raise NotImplementedError(
            'operation set_upper(...) not yet implemented')

    def is_ordered(self):
        """If this operation has a return parameter, isOrdered equals the value of isOrdered for that parameter. Otherwise isOrdered is false.
result = (if returnResult()->notEmpty() then returnResult()-> exists(isOrdered) else false endif)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation is_ordered(...) not yet implemented')

    def is_unique(self):
        """If this operation has a return parameter, isUnique equals the value of isUnique for that parameter. Otherwise isUnique is true.
result = (if returnResult()->notEmpty() then returnResult()->exists(isUnique) else true endif)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation is_unique(...) not yet implemented')

    def get_lower(self):
        """If this operation has a return parameter, lower equals the value of lower for that parameter. Otherwise lower has no value.
result = (if returnResult()->notEmpty() then returnResult()->any(true).lower else null endif)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation get_lower(...) not yet implemented')

    def return_result(self):
        """The query returnResult() returns the set containing the return parameter of the Operation if one exists, otherwise, it returns an empty set
result = (ownedParameter->select (direction = ParameterDirectionKind::return)->asSet())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation return_result(...) not yet implemented')

    def get_type(self):
        """If this operation has a return parameter, type equals the value of type for that parameter. Otherwise type has no value.
result = (if returnResult()->notEmpty() then returnResult()->any(true).type else null endif)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation get_type(...) not yet implemented')

    def get_upper(self):
        """If this operation has a return parameter, upper equals the value of upper for that parameter. Otherwise upper has no value.
result = (if returnResult()->notEmpty() then returnResult()->any(true).upper else null endif)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation get_upper(...) not yet implemented')


class StringExpressionMixin(object):
    """User defined mixin class for StringExpression."""

    def __init__(self, owningExpression=None, subExpression=None, **kwargs):
        super(StringExpressionMixin, self).__init__(**kwargs)

    def operands(self, diagnostics=None, context=None):
        """All the operands of a StringExpression must be LiteralStrings
operand->forAll (oclIsKindOf (LiteralString))"""
        raise NotImplementedError(
            'operation operands(...) not yet implemented')

    def subexpressions(self, diagnostics=None, context=None):
        """If a StringExpression has sub-expressions, it cannot have operands and vice versa (this avoids the problem of having to define a collating sequence between operands and subexpressions).
if subExpression->notEmpty() then operand->isEmpty() else operand->notEmpty() endif"""
        raise NotImplementedError(
            'operation subexpressions(...) not yet implemented')


class RealizationMixin(object):
    """User defined mixin class for Realization."""

    def __init__(self, **kwargs):
        super(RealizationMixin, self).__init__(**kwargs)


class PinMixin(object):
    """User defined mixin class for Pin."""

    def __init__(self, isControl=None, **kwargs):
        super(PinMixin, self).__init__(**kwargs)

    def control_pins(self, diagnostics=None, context=None):
        """A control Pin has a control type.
isControl implies isControlType"""
        raise NotImplementedError(
            'operation control_pins(...) not yet implemented')

    def not_unique(self, diagnostics=None, context=None):
        """Pin multiplicity is not unique.
not isUnique"""
        raise NotImplementedError(
            'operation not_unique(...) not yet implemented')


class WriteLinkActionMixin(object):
    """User defined mixin class for WriteLinkAction."""

    def __init__(self, **kwargs):
        super(WriteLinkActionMixin, self).__init__(**kwargs)

    def allow_access(self, diagnostics=None, context=None):
        """The visibility of at least one end must allow access from the context Classifier of the WriteLinkAction.
endData.end->exists(end |
  end.type=_'context' or
  end.visibility=VisibilityKind::public or
  end.visibility=VisibilityKind::protected and
  endData.end->exists(other |
    other<>end and _'context'.conformsTo(other.type.oclAsType(Classifier))))"""
        raise NotImplementedError(
            'operation allow_access(...) not yet implemented')


class WriteStructuralFeatureActionMixin(object):
    """User defined mixin class for WriteStructuralFeatureAction."""

    def __init__(self, result=None, value=None, **kwargs):
        super(WriteStructuralFeatureActionMixin, self).__init__(**kwargs)

    def multiplicity_of_result(self, diagnostics=None, context=None):
        """The multiplicity of the result OutputPin must be 1..1.
result <> null implies result.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_result(...) not yet implemented')

    def type_of_value(self, diagnostics=None, context=None):
        """The type of the value InputPin must conform to the type of the structuralFeature.
value <> null implies value.type.conformsTo(structuralFeature.type)"""
        raise NotImplementedError(
            'operation type_of_value(...) not yet implemented')

    def multiplicity_of_value(self, diagnostics=None, context=None):
        """The multiplicity of the value InputPin is 1..1.
value<>null implies value.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_value(...) not yet implemented')

    def type_of_result(self, diagnostics=None, context=None):
        """The type of the result OutputPin is the same as the type of the inherited object InputPin.
result <> null implies result.type = object.type"""
        raise NotImplementedError(
            'operation type_of_result(...) not yet implemented')


class WriteVariableActionMixin(object):
    """User defined mixin class for WriteVariableAction."""

    def __init__(self, value=None, **kwargs):
        super(WriteVariableActionMixin, self).__init__(**kwargs)

    def value_type(self, diagnostics=None, context=None):
        """The type of the value InputPin must conform to the type of the variable.
value <> null implies value.type.conformsTo(variable.type)"""
        raise NotImplementedError(
            'operation value_type(...) not yet implemented')

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the value InputPin is 1..1.
value<>null implies value.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')


class AcceptCallActionMixin(object):
    """User defined mixin class for AcceptCallAction."""

    def __init__(self, returnInformation=None, **kwargs):
        super(AcceptCallActionMixin, self).__init__(**kwargs)

    def result_pins(self, diagnostics=None, context=None):
        """The number of result OutputPins must be the same as the number of input (in and inout) ownedParameters of the Operation specified by the trigger Event. The type, ordering and multiplicity of each result OutputPin must be consistent with the corresponding input Parameter.
let parameter: OrderedSet(Parameter) = trigger.event->asSequence()->first().oclAsType(CallEvent).operation.inputParameters() in
result->size() = parameter->size() and
Sequence{1..result->size()}->forAll(i |
        parameter->at(i).type.conformsTo(result->at(i).type) and
        parameter->at(i).isOrdered = result->at(i).isOrdered and
        parameter->at(i).compatibleWith(result->at(i)))"""
        raise NotImplementedError(
            'operation result_pins(...) not yet implemented')

    def trigger_call_event(self, diagnostics=None, context=None):
        """The action must have exactly one trigger, which must be for a CallEvent.
trigger->size()=1 and
trigger->asSequence()->first().event.oclIsKindOf(CallEvent)"""
        raise NotImplementedError(
            'operation trigger_call_event(...) not yet implemented')

    def unmarshall(self, diagnostics=None, context=None):
        """isUnmrashall must be true for an AcceptCallAction.
isUnmarshall = true"""
        raise NotImplementedError(
            'operation unmarshall(...) not yet implemented')


class BroadcastSignalActionMixin(object):
    """User defined mixin class for BroadcastSignalAction."""

    def __init__(self, signal=None, **kwargs):
        super(BroadcastSignalActionMixin, self).__init__(**kwargs)

    def number_of_arguments(self, diagnostics=None, context=None):
        """The number of argument InputPins must be the same as the number of attributes in the signal.
argument->size() = signal.allAttributes()->size()"""
        raise NotImplementedError(
            'operation number_of_arguments(...) not yet implemented')

    def type_ordering_multiplicity(self, diagnostics=None, context=None):
        """The type, ordering, and multiplicity of an argument InputPin must be the same as the corresponding attribute of the signal.
let attribute: OrderedSet(Property) = signal.allAttributes() in
Sequence{1..argument->size()}->forAll(i |
        argument->at(i).type.conformsTo(attribute->at(i).type) and
        argument->at(i).isOrdered = attribute->at(i).isOrdered and
        argument->at(i).compatibleWith(attribute->at(i)))"""
        raise NotImplementedError(
            'operation type_ordering_multiplicity(...) not yet implemented')

    def no_onport(self, diagnostics=None, context=None):
        """A BroadcaseSignalAction may not specify onPort.
onPort=null"""
        raise NotImplementedError(
            'operation no_onport(...) not yet implemented')


class CallActionMixin(object):
    """User defined mixin class for CallAction."""

    def __init__(self, isSynchronous=None, result=None, **kwargs):
        super(CallActionMixin, self).__init__(**kwargs)

    def argument_pins(self, diagnostics=None, context=None):
        """The number of argument InputPins must be the same as the number of input (in and inout) ownedParameters of the called Behavior or Operation. The type, ordering and multiplicity of each argument InputPin must be consistent with the corresponding input Parameter.
let parameter: OrderedSet(Parameter) = self.inputParameters() in
argument->size() = parameter->size() and
Sequence{1..argument->size()}->forAll(i |
        argument->at(i).type.conformsTo(parameter->at(i).type) and
        argument->at(i).isOrdered = parameter->at(i).isOrdered and
        argument->at(i).compatibleWith(parameter->at(i)))"""
        raise NotImplementedError(
            'operation argument_pins(...) not yet implemented')

    def result_pins(self, diagnostics=None, context=None):
        """The number of result OutputPins must be the same as the number of output (inout, out and return) ownedParameters of the called Behavior or Operation. The type, ordering and multiplicity of each result OutputPin must be consistent with the corresponding input Parameter.
let parameter: OrderedSet(Parameter) = self.outputParameters() in
result->size() = parameter->size() and
Sequence{1..result->size()}->forAll(i |
        parameter->at(i).type.conformsTo(result->at(i).type) and
        parameter->at(i).isOrdered = result->at(i).isOrdered and
        parameter->at(i).compatibleWith(result->at(i)))"""
        raise NotImplementedError(
            'operation result_pins(...) not yet implemented')

    def synchronous_call(self, diagnostics=None, context=None):
        """Only synchronous CallActions can have result OutputPins.
result->notEmpty() implies isSynchronous"""
        raise NotImplementedError(
            'operation synchronous_call(...) not yet implemented')

    def input_parameters(self):
        """Return the in and inout ownedParameters of the Behavior or Operation being called. (This operation is abstract and should be overridden by subclasses of CallAction.)
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation input_parameters(...) not yet implemented')

    def output_parameters(self):
        """Return the inout, out and return ownedParameters of the Behavior or Operation being called. (This operation is abstract and should be overridden by subclasses of CallAction.)
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation output_parameters(...) not yet implemented')


class ClearStructuralFeatureActionMixin(object):
    """User defined mixin class for ClearStructuralFeatureAction."""

    def __init__(self, result=None, **kwargs):
        super(ClearStructuralFeatureActionMixin, self).__init__(**kwargs)

    def type_of_result(self, diagnostics=None, context=None):
        """The type of the result OutputPin is the same as the type of the inherited object InputPin.
result<>null implies result.type = object.type"""
        raise NotImplementedError(
            'operation type_of_result(...) not yet implemented')

    def multiplicity_of_result(self, diagnostics=None, context=None):
        """The multiplicity of the result OutputPin must be 1..1.
result<>null implies result.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_result(...) not yet implemented')


class ClearVariableActionMixin(object):
    """User defined mixin class for ClearVariableAction."""

    def __init__(self, **kwargs):
        super(ClearVariableActionMixin, self).__init__(**kwargs)


class ReadLinkActionMixin(object):
    """User defined mixin class for ReadLinkAction."""

    def __init__(self, result=None, **kwargs):
        super(ReadLinkActionMixin, self).__init__(**kwargs)

    def type_and_ordering(self, diagnostics=None, context=None):
        """The type and ordering of the result OutputPin are same as the type and ordering of the open Association end.
self.openEnd()->forAll(type=result.type and isOrdered=result.isOrdered)"""
        raise NotImplementedError(
            'operation type_and_ordering(...) not yet implemented')

    def compatible_multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the open Association end must be compatible with the multiplicity of the result OutputPin.
self.openEnd()->first().compatibleWith(result)"""
        raise NotImplementedError(
            'operation compatible_multiplicity(...) not yet implemented')

    def visibility(self, diagnostics=None, context=None):
        """Visibility of the open end must allow access from the object performing the action.
let openEnd : Property = self.openEnd()->first() in
  openEnd.visibility = VisibilityKind::public or
  endData->exists(oed |
    oed.end<>openEnd and
    (_'context' = oed.end.type or
      (openEnd.visibility = VisibilityKind::protected and
        _'context'.conformsTo(oed.end.type.oclAsType(Classifier)))))"""
        raise NotImplementedError(
            'operation visibility(...) not yet implemented')

    def one_open_end(self, diagnostics=None, context=None):
        """Exactly one linkEndData specification (corresponding to the "open" end) must not have an value InputPin.
self.openEnd()->size() = 1"""
        raise NotImplementedError(
            'operation one_open_end(...) not yet implemented')

    def navigable_open_end(self, diagnostics=None, context=None):
        """The open end must be navigable.
self.openEnd()->first().isNavigable()"""
        raise NotImplementedError(
            'operation navigable_open_end(...) not yet implemented')

    def open_end(self):
        """Returns the ends corresponding to endData with no value InputPin. (A well-formed ReadLinkAction is constrained to have only one of these.)
result = (endData->select(value=null).end->asOrderedSet())
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation open_end(...) not yet implemented')


class ReadStructuralFeatureActionMixin(object):
    """User defined mixin class for ReadStructuralFeatureAction."""

    def __init__(self, result=None, **kwargs):
        super(ReadStructuralFeatureActionMixin, self).__init__(**kwargs)

    def type_and_ordering(self, diagnostics=None, context=None):
        """The type and ordering of the result OutputPin are the same as the type and ordering of the StructuralFeature.
result.type =structuralFeature.type and
result.isOrdered = structuralFeature.isOrdered"""
        raise NotImplementedError(
            'operation type_and_ordering(...) not yet implemented')


class ReadVariableActionMixin(object):
    """User defined mixin class for ReadVariableAction."""

    def __init__(self, result=None, **kwargs):
        super(ReadVariableActionMixin, self).__init__(**kwargs)

    def type_and_ordering(self, diagnostics=None, context=None):
        """The type and ordering of the result OutputPin are the same as the type and ordering of the variable.
result.type =variable.type and
result.isOrdered = variable.isOrdered"""
        raise NotImplementedError(
            'operation type_and_ordering(...) not yet implemented')

    def compatible_multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the variable must be compatible with the multiplicity of the output pin.
variable.compatibleWith(result)"""
        raise NotImplementedError(
            'operation compatible_multiplicity(...) not yet implemented')


class SendObjectActionMixin(object):
    """User defined mixin class for SendObjectAction."""

    def __init__(self, request=None, target=None, **kwargs):
        super(SendObjectActionMixin, self).__init__(**kwargs)

    def type_target_pin(self, diagnostics=None, context=None):
        """If onPort is not empty, the Port given by onPort must be an owned or inherited feature of the type of the target InputPin.
onPort<>null implies target.type.oclAsType(Classifier).allFeatures()->includes(onPort)"""
        raise NotImplementedError(
            'operation type_target_pin(...) not yet implemented')


class SendSignalActionMixin(object):
    """User defined mixin class for SendSignalAction."""

    def __init__(self, signal=None, target=None, **kwargs):
        super(SendSignalActionMixin, self).__init__(**kwargs)

    def type_ordering_multiplicity(self, diagnostics=None, context=None):
        """The type, ordering, and multiplicity of an argument InputPin must be the same as the corresponding attribute of the signal.
let attribute: OrderedSet(Property) = signal.allAttributes() in
Sequence{1..argument->size()}->forAll(i |
        argument->at(i).type.conformsTo(attribute->at(i).type) and
        argument->at(i).isOrdered = attribute->at(i).isOrdered and
        argument->at(i).compatibleWith(attribute->at(i)))"""
        raise NotImplementedError(
            'operation type_ordering_multiplicity(...) not yet implemented')

    def number_order(self, diagnostics=None, context=None):
        """The number and order of argument InputPins must be the same as the number and order of attributes of the signal.
argument->size()=signal.allAttributes()->size()"""
        raise NotImplementedError(
            'operation number_order(...) not yet implemented')

    def type_target_pin(self, diagnostics=None, context=None):
        """If onPort is not empty, the Port given by onPort must be an owned or inherited feature of the type of the target InputPin.
not onPort->isEmpty() implies target.type.oclAsType(Classifier).allFeatures()->includes(onPort)"""
        raise NotImplementedError(
            'operation type_target_pin(...) not yet implemented')


class DataStoreNodeMixin(object):
    """User defined mixin class for DataStoreNode."""

    def __init__(self, **kwargs):
        super(DataStoreNodeMixin, self).__init__(**kwargs)


class BehavioredClassifierMixin(object):
    """User defined mixin class for BehavioredClassifier."""

    def __init__(
            self, classifierBehavior=None, interfaceRealization=None,
            ownedBehavior=None, **kwargs):
        super(BehavioredClassifierMixin, self).__init__(**kwargs)

    def class_behavior(self, diagnostics=None, context=None):
        """If a behavior is classifier behavior, it does not have a specification.
classifierBehavior->notEmpty() implies classifierBehavior.specification->isEmpty()"""
        raise NotImplementedError(
            'operation class_behavior(...) not yet implemented')

    def get_all_implemented_interfaces(self):
        """Retrieves all the interfaces on which this behaviored classifier or any of its parents has an interface realization dependency."""
        raise NotImplementedError(
            'operation get_all_implemented_interfaces(...) not yet implemented')

    def get_implemented_interfaces(self):
        """Retrieves the interfaces on which this behaviored classifier has an interface realization dependency."""
        raise NotImplementedError(
            'operation get_implemented_interfaces(...) not yet implemented')


class DataTypeMixin(object):
    """User defined mixin class for DataType."""

    def __init__(self, ownedAttribute=None, ownedOperation=None, **kwargs):
        super(DataTypeMixin, self).__init__(**kwargs)

    def create_owned_attribute(
            self, name=None, type=None, lower=None, upper=None):
        """Creates a property with the specified name, type, lower bound, and upper bound as an owned attribute of this data type."""
        raise NotImplementedError(
            'operation create_owned_attribute(...) not yet implemented')

    def create_owned_operation(
            self, name=None, parameterNames=None, parameterTypes=None,
            returnType=None):
        """Creates an operation with the specified name, parameter names, parameter types, and return type (or null) as an owned operation of this data type."""
        raise NotImplementedError(
            'operation create_owned_operation(...) not yet implemented')


class InterfaceMixin(object):
    """User defined mixin class for Interface."""

    def __init__(
            self, nestedClassifier=None, ownedAttribute=None,
            ownedReception=None, protocol=None, redefinedInterface=None,
            ownedOperation=None, **kwargs):
        super(InterfaceMixin, self).__init__(**kwargs)

    def visibility(self, diagnostics=None, context=None):
        """The visibility of all Features owned by an Interface must be public.
feature->forAll(visibility = VisibilityKind::public)"""
        raise NotImplementedError(
            'operation visibility(...) not yet implemented')

    def create_owned_attribute(
            self, name=None, type=None, lower=None, upper=None):
        """Creates a property with the specified name, type, lower bound, and upper bound as an owned attribute of this interface."""
        raise NotImplementedError(
            'operation create_owned_attribute(...) not yet implemented')

    def create_owned_operation(
            self, name=None, parameterNames=None, parameterTypes=None,
            returnType=None):
        """Creates an operation with the specified name, parameter names, parameter types, and return type (or null) as an owned operation of this interface."""
        raise NotImplementedError(
            'operation create_owned_operation(...) not yet implemented')


class SignalMixin(object):
    """User defined mixin class for Signal."""

    def __init__(self, ownedAttribute=None, **kwargs):
        super(SignalMixin, self).__init__(**kwargs)

    def create_owned_attribute(
            self, name=None, type=None, lower=None, upper=None):
        """Creates a property with the specified name, type, lower bound, and upper bound as an owned attribute of this signal."""
        raise NotImplementedError(
            'operation create_owned_attribute(...) not yet implemented')


class DerivedPart(EDerivedCollection):
    pass


class DerivedRole(EDerivedCollection):
    pass


class StructuredClassifierMixin(object):
    """User defined mixin class for StructuredClassifier."""

    def __init__(
            self, ownedAttribute=None, ownedConnector=None, part=None,
            role=None, **kwargs):
        super(StructuredClassifierMixin, self).__init__(**kwargs)

    def create_owned_attribute(
            self, name=None, type=None, lower=None, upper=None):
        """Creates a property with the specified name, type, lower bound, and upper bound as an owned attribute of this structured classifier."""
        raise NotImplementedError(
            'operation create_owned_attribute(...) not yet implemented')

    def get_parts(self):
        """Derivation for StructuredClassifier::/part
result = (ownedAttribute->select(isComposite)->asSet())
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_parts(...) not yet implemented')

    def all_roles(self):
        """All features of type ConnectableElement, equivalent to all direct and inherited roles.
result = (allFeatures()->select(oclIsKindOf(ConnectableElement))->collect(oclAsType(ConnectableElement))->asSet())
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation all_roles(...) not yet implemented')


class SubstitutionMixin(object):
    """User defined mixin class for Substitution."""

    def __init__(self, contract=None, substitutingClassifier=None, **kwargs):
        super(SubstitutionMixin, self).__init__(**kwargs)


class InterfaceRealizationMixin(object):
    """User defined mixin class for InterfaceRealization."""

    def __init__(self, contract=None, implementingClassifier=None, **kwargs):
        super(InterfaceRealizationMixin, self).__init__(**kwargs)


class StructuredActivityNodeMixin(object):
    """User defined mixin class for StructuredActivityNode."""

    def __init__(self, edge=None, mustIsolate=None,
                 structuredNodeInput=None, structuredNodeOutput=None,
                 variable=None, node=None, **kwargs):
        super(StructuredActivityNodeMixin, self).__init__(**kwargs)

    def output_pin_edges(self, diagnostics=None, context=None):
        """The outgoing ActivityEdges of the OutputPins of a StructuredActivityNode must have targets that are not within the StructuredActivityNode.
output.outgoing.target->excludesAll(allOwnedNodes()-input)"""
        raise NotImplementedError(
            'operation output_pin_edges(...) not yet implemented')

    def edges(self, diagnostics=None, context=None):
        """The edges of a StructuredActivityNode are all the ActivityEdges with source and target ActivityNodes contained directly or indirectly within the StructuredActivityNode and at least one of the source or target not contained in any more deeply nested StructuredActivityNode.
edge=self.sourceNodes().outgoing->intersection(self.allOwnedNodes().incoming)->
        union(self.targetNodes().incoming->intersection(self.allOwnedNodes().outgoing))->asSet()"""
        raise NotImplementedError('operation edges(...) not yet implemented')

    def input_pin_edges(self, diagnostics=None, context=None):
        """The incoming ActivityEdges of an InputPin of a StructuredActivityNode must have sources that are not within the StructuredActivityNode.
input.incoming.source->excludesAll(allOwnedNodes()-output)"""
        raise NotImplementedError(
            'operation input_pin_edges(...) not yet implemented')

    def source_nodes(self):
        """Return those ActivityNodes contained immediately within the StructuredActivityNode that may act as sources of edges owned by the StructuredActivityNode.
result = (node->union(input.oclAsType(ActivityNode)->asSet())->
  union(node->select(oclIsKindOf(Action)).oclAsType(Action).output)->asSet())
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation source_nodes(...) not yet implemented')

    def target_nodes(self):
        """Return those ActivityNodes contained immediately within the StructuredActivityNode that may act as targets of edges owned by the StructuredActivityNode.
result = (node->union(output.oclAsType(ActivityNode)->asSet())->
  union(node->select(oclIsKindOf(Action)).oclAsType(Action).input)->asSet())
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation target_nodes(...) not yet implemented')


class InputPinMixin(object):
    """User defined mixin class for InputPin."""

    def __init__(self, **kwargs):
        super(InputPinMixin, self).__init__(**kwargs)

    def outgoing_edges_structured_only(self, diagnostics=None, context=None):
        """An InputPin may have outgoing ActivityEdges only when it is owned by a StructuredActivityNode, and these edges must target a node contained (directly or indirectly) in the owning StructuredActivityNode.
outgoing->notEmpty() implies
        action<>null and
        action.oclIsKindOf(StructuredActivityNode) and
        action.oclAsType(StructuredActivityNode).allOwnedNodes()->includesAll(outgoing.target)"""
        raise NotImplementedError(
            'operation outgoing_edges_structured_only(...) not yet implemented')


class OutputPinMixin(object):
    """User defined mixin class for OutputPin."""

    def __init__(self, **kwargs):
        super(OutputPinMixin, self).__init__(**kwargs)

    def incoming_edges_structured_only(self, diagnostics=None, context=None):
        """An OutputPin may have incoming ActivityEdges only when it is owned by a StructuredActivityNode, and these edges must have sources contained (directly or indirectly) in the owning StructuredActivityNode.
incoming->notEmpty() implies
        action<>null and
        action.oclIsKindOf(StructuredActivityNode) and
        action.oclAsType(StructuredActivityNode).allOwnedNodes()->includesAll(incoming.source)"""
        raise NotImplementedError(
            'operation incoming_edges_structured_only(...) not yet implemented')


class AddStructuralFeatureValueActionMixin(object):
    """User defined mixin class for AddStructuralFeatureValueAction."""

    def __init__(self, insertAt=None, isReplaceAll=None, **kwargs):
        super(AddStructuralFeatureValueActionMixin, self).__init__(**kwargs)

    def required_value(self, diagnostics=None, context=None):
        """A value InputPin is required.
value<>null"""
        raise NotImplementedError(
            'operation required_value(...) not yet implemented')

    def insert_at_pin(self, diagnostics=None, context=None):
        """AddStructuralFeatureActions adding a value to ordered StructuralFeatures must have a single InputPin for the insertion point with type UnlimitedNatural and multiplicity of 1..1 if isReplaceAll=false, and must have no Input Pin for the insertion point when the StructuralFeature is unordered.
if not structuralFeature.isOrdered then insertAt = null
else
  not isReplaceAll implies
        insertAt<>null and
        insertAt->forAll(type=UnlimitedNatural and is(1,1.oclAsType(UnlimitedNatural)))
endif"""
        raise NotImplementedError(
            'operation insert_at_pin(...) not yet implemented')


class AddVariableValueActionMixin(object):
    """User defined mixin class for AddVariableValueAction."""

    def __init__(self, insertAt=None, isReplaceAll=None, **kwargs):
        super(AddVariableValueActionMixin, self).__init__(**kwargs)

    def required_value(self, diagnostics=None, context=None):
        """A value InputPin is required.
value <> null"""
        raise NotImplementedError(
            'operation required_value(...) not yet implemented')

    def insert_at_pin(self, diagnostics=None, context=None):
        """AddVariableValueActions for ordered Variables must have a single InputPin for the insertion point with type UnlimtedNatural and multiplicity of 1..1 if isReplaceAll=false, otherwise the Action has no InputPin for the insertion point.
if not variable.isOrdered then insertAt = null
else
  not isReplaceAll implies
        insertAt<>null and
        insertAt->forAll(type=UnlimitedNatural and is(1,1.oclAsType(UnlimitedNatural)))
endif"""
        raise NotImplementedError(
            'operation insert_at_pin(...) not yet implemented')


class CallBehaviorActionMixin(object):
    """User defined mixin class for CallBehaviorAction."""

    def __init__(self, behavior=None, **kwargs):
        super(CallBehaviorActionMixin, self).__init__(**kwargs)

    def no_onport(self, diagnostics=None, context=None):
        """A CallBehaviorAction may not specify onPort.
onPort=null"""
        raise NotImplementedError(
            'operation no_onport(...) not yet implemented')


class CallOperationActionMixin(object):
    """User defined mixin class for CallOperationAction."""

    def __init__(self, operation=None, target=None, **kwargs):
        super(CallOperationActionMixin, self).__init__(**kwargs)

    def type_target_pin(self, diagnostics=None, context=None):
        """If onPort has no value, the operation must be an owned or inherited feature of the type of the target InputPin, otherwise the Port given by onPort must be an owned or inherited feature of the type of the target InputPin, and the Port must have a required or provided Interface with the operation as an owned or inherited feature.
if onPort=null then  target.type.oclAsType(Classifier).allFeatures()->includes(operation)
else target.type.oclAsType(Classifier).allFeatures()->includes(onPort) and onPort.provided->union(onPort.required).allFeatures()->includes(operation)
endif"""
        raise NotImplementedError(
            'operation type_target_pin(...) not yet implemented')


class CreateLinkActionMixin(object):
    """User defined mixin class for CreateLinkAction."""

    def __init__(self, **kwargs):
        super(CreateLinkActionMixin, self).__init__(**kwargs)

    def association_not_abstract(self, diagnostics=None, context=None):
        """The Association cannot be an abstract Classifier.
not self.association().isAbstract"""
        raise NotImplementedError(
            'operation association_not_abstract(...) not yet implemented')


class DestroyLinkActionMixin(object):
    """User defined mixin class for DestroyLinkAction."""

    def __init__(self, **kwargs):
        super(DestroyLinkActionMixin, self).__init__(**kwargs)


class RemoveStructuralFeatureValueActionMixin(object):
    """User defined mixin class for RemoveStructuralFeatureValueAction."""

    def __init__(self, isRemoveDuplicates=None, removeAt=None, **kwargs):
        super(RemoveStructuralFeatureValueActionMixin, self).__init__(**kwargs)

    def remove_at_and_value(self, diagnostics=None, context=None):
        """RemoveStructuralFeatureValueActions removing a value from ordered, non-unique StructuralFeatures must have a single removeAt InputPin and no value InputPin, if isRemoveDuplicates is false. The removeAt InputPin must be of type Unlimited Natural with multiplicity 1..1. Otherwise, the Action has a value InputPin and no removeAt InputPin.
if structuralFeature.isOrdered and not structuralFeature.isUnique and  not isRemoveDuplicates then
  value = null and
  removeAt <> null and
  removeAt.type = UnlimitedNatural and
  removeAt.is(1,1)
else
  removeAt = null and value <> null
endif"""
        raise NotImplementedError(
            'operation remove_at_and_value(...) not yet implemented')


class RemoveVariableValueActionMixin(object):
    """User defined mixin class for RemoveVariableValueAction."""

    def __init__(self, isRemoveDuplicates=None, removeAt=None, **kwargs):
        super(RemoveVariableValueActionMixin, self).__init__(**kwargs)

    def remove_at_and_value(self, diagnostics=None, context=None):
        """ReadVariableActions removing a value from ordered, non-unique Variables must have a single removeAt InputPin and no value InputPin, if isRemoveDuplicates is false. The removeAt InputPin must be of type Unlimited Natural with multiplicity 1..1. Otherwise, the Action has a value InputPin and no removeAt InputPin.
if  variable.isOrdered and not variable.isUnique and not isRemoveDuplicates then
  value = null and
  removeAt <> null and
  removeAt.type = UnlimitedNatural and
  removeAt.is(1,1)
else
  removeAt = null and value <> null
endif"""
        raise NotImplementedError(
            'operation remove_at_and_value(...) not yet implemented')


class StartObjectBehaviorActionMixin(object):
    """User defined mixin class for StartObjectBehaviorAction."""

    def __init__(self, object=None, **kwargs):
        super(StartObjectBehaviorActionMixin, self).__init__(**kwargs)

    def multiplicity_of_object(self, diagnostics=None, context=None):
        """The multiplicity of the object InputPin must be 1..1.
object.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity_of_object(...) not yet implemented')

    def type_of_object(self, diagnostics=None, context=None):
        """The type of the object InputPin must be either a Behavior or a BehavioredClassifier with a classifierBehavior.
self.behavior()<>null"""
        raise NotImplementedError(
            'operation type_of_object(...) not yet implemented')

    def no_onport(self, diagnostics=None, context=None):
        """A StartObjectBehaviorAction may not specify onPort.
onPort->isEmpty()"""
        raise NotImplementedError(
            'operation no_onport(...) not yet implemented')

    def behavior(self):
        """If the type of the object InputPin is a Behavior, then that Behavior. Otherwise, if the type of the object InputPin is a BehavioredClassifier, then the classifierBehavior of that BehavioredClassifier.
result = (if object.type.oclIsKindOf(Behavior) then
  object.type.oclAsType(Behavior)
else if object.type.oclIsKindOf(BehavioredClassifier) then
  object.type.oclAsType(BehavioredClassifier).classifierBehavior
else
  null
endif
endif)
<p>From package UML::Actions.</p>"""
        raise NotImplementedError(
            'operation behavior(...) not yet implemented')


class InformationItemMixin(object):
    """User defined mixin class for InformationItem."""

    def __init__(self, represented=None, **kwargs):
        super(InformationItemMixin, self).__init__(**kwargs)

    def sources_and_targets(self, diagnostics=None, context=None):
        """The sources and targets of an information item (its related information flows) must designate subsets of the sources and targets of the representation information item, if any. The Classifiers that can realize an information item can only be of the following kind: Class, Interface, InformationItem, Signal, Component.
(self.represented->select(oclIsKindOf(InformationItem))->forAll(p |
  p.conveyingFlow.source->forAll(q | self.conveyingFlow.source->includes(q)) and
    p.conveyingFlow.target->forAll(q | self.conveyingFlow.target->includes(q)))) and
      (self.represented->forAll(oclIsKindOf(Class) or oclIsKindOf(Interface) or
        oclIsKindOf(InformationItem) or oclIsKindOf(Signal) or oclIsKindOf(Component)))"""
        raise NotImplementedError(
            'operation sources_and_targets(...) not yet implemented')

    def has_no(self, diagnostics=None, context=None):
        """An informationItem has no feature, no generalization, and no associations.
self.generalization->isEmpty() and self.feature->isEmpty()"""
        raise NotImplementedError('operation has_no(...) not yet implemented')

    def not_instantiable(self, diagnostics=None, context=None):
        """It is not instantiable.
isAbstract"""
        raise NotImplementedError(
            'operation not_instantiable(...) not yet implemented')


class ComponentRealizationMixin(object):
    """User defined mixin class for ComponentRealization."""

    def __init__(self, realizingClassifier=None, abstraction=None, **kwargs):
        super(ComponentRealizationMixin, self).__init__(**kwargs)


class DerivedEndtype(EDerivedCollection):
    pass


class AssociationMixin(object):
    """User defined mixin class for Association."""

    def __init__(self, endType=None, isDerived=None, memberEnd=None,
                 ownedEnd=None, navigableOwnedEnd=None, **kwargs):
        super(AssociationMixin, self).__init__(**kwargs)

    def specialized_end_number(self, diagnostics=None, context=None):
        """An Association specializing another Association has the same number of ends as the other Association.
parents()->select(oclIsKindOf(Association)).oclAsType(Association)->forAll(p | p.memberEnd->size() = self.memberEnd->size())"""
        raise NotImplementedError(
            'operation specialized_end_number(...) not yet implemented')

    def specialized_end_types(self, diagnostics=None, context=None):
        """When an Association specializes another Association, every end of the specific Association corresponds to an end of the general Association, and the specific end reaches the same type or a subtype of the corresponding general end.
Sequence{1..memberEnd->size()}->
        forAll(i | general->select(oclIsKindOf(Association)).oclAsType(Association)->
                forAll(ga | self.memberEnd->at(i).type.conformsTo(ga.memberEnd->at(i).type)))"""
        raise NotImplementedError(
            'operation specialized_end_types(...) not yet implemented')

    def binary_associations(self, diagnostics=None, context=None):
        """Only binary Associations can be aggregations.
memberEnd->exists(aggregation <> AggregationKind::none) implies (memberEnd->size() = 2 and memberEnd->exists(aggregation = AggregationKind::none))"""
        raise NotImplementedError(
            'operation binary_associations(...) not yet implemented')

    def association_ends(self, diagnostics=None, context=None):
        """Ends of Associations with more than two ends must be owned by the Association itself.
memberEnd->size() > 2 implies ownedEnd->includesAll(memberEnd)"""
        raise NotImplementedError(
            'operation association_ends(...) not yet implemented')

    def ends_must_be_typed(self, diagnostics=None, context=None):
        """memberEnd->forAll(type->notEmpty())"""
        raise NotImplementedError(
            'operation ends_must_be_typed(...) not yet implemented')

    def is_binary(self):
        """Determines whether this association is a binary association, i.e. whether it has exactly two member ends."""
        raise NotImplementedError(
            'operation is_binary(...) not yet implemented')

    def get_end_types(self):
        """endType is derived from the types of the member ends.
result = (memberEnd->collect(type)->asSet())
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_end_types(...) not yet implemented')


class PropertyMixin(object):
    """User defined mixin class for Property."""

    @property
    def default(self):
        raise NotImplementedError('Missing implementation for default')

    @default.setter
    def default(self, value):
        raise NotImplementedError('Missing implementation for default')

    @property
    def isComposite(self):
        from .uml import AggregationKind
        return self.aggregation == AggregationKind.composite

    @isComposite.setter
    def isComposite(self, value):
        from .uml import AggregationKind
        if value:
            self.aggregation = AggregationKind.composite
        else:
            self.aggregation = AggregationKind.none

    @property
    def opposite(self):
        raise NotImplementedError('Missing implementation for opposite')

    @opposite.setter
    def opposite(self, value):
        raise NotImplementedError('Missing implementation for opposite')

    def __init__(
            self, datatype=None, interface=None, default=None,
            aggregation=None, associationEnd=None, qualifier=None, class_=None,
            defaultValue=None, isComposite=None, isDerived=None,
            isDerivedUnion=None, isID=None, opposite=None,
            owningAssociation=None, redefinedProperty=None,
            subsettedProperty=None, association=None, **kwargs):
        super(PropertyMixin, self).__init__(**kwargs)

    def subsetting_context_conforms(self, diagnostics=None, context=None):
        """Subsetting may only occur when the context of the subsetting property conforms to the context of the subsetted property.
subsettedProperty->notEmpty() implies
  (subsettingContext()->notEmpty() and subsettingContext()->forAll (sc |
    subsettedProperty->forAll(sp |
      sp.subsettingContext()->exists(c | sc.conformsTo(c)))))"""
        raise NotImplementedError(
            'operation subsetting_context_conforms(...) not yet implemented')

    def derived_union_is_read_only(self, diagnostics=None, context=None):
        """A derived union is read only.
isDerivedUnion implies isReadOnly"""
        raise NotImplementedError(
            'operation derived_union_is_read_only(...) not yet implemented')

    def multiplicity_of_composite(self, diagnostics=None, context=None):
        """A multiplicity on the composing end of a composite aggregation must not have an upper bound greater than 1.
isComposite and association <> null implies opposite.upperBound() <= 1"""
        raise NotImplementedError(
            'operation multiplicity_of_composite(...) not yet implemented')

    def redefined_property_inherited(self, diagnostics=None, context=None):
        """A redefined Property must be inherited from a more general Classifier.
(redefinedProperty->notEmpty()) implies
  (redefinitionContext->notEmpty() and
      redefinedProperty->forAll(rp|
        ((redefinitionContext->collect(fc|
          fc.allParents()))->asSet())->collect(c| c.allFeatures())->asSet()->includes(rp)))"""
        raise NotImplementedError(
            'operation redefined_property_inherited(...) not yet implemented')

    def subsetting_rules(self, diagnostics=None, context=None):
        """A subsetting Property may strengthen the type of the subsetted Property, and its upper bound may be less.
subsettedProperty->forAll(sp |
  self.type.conformsTo(sp.type) and
    ((self.upperBound()->notEmpty() and sp.upperBound()->notEmpty()) implies
      self.upperBound() <= sp.upperBound() ))"""
        raise NotImplementedError(
            'operation subsetting_rules(...) not yet implemented')

    def binding_to_attribute(self, diagnostics=None, context=None):
        """A binding of a PropertyTemplateParameter representing an attribute must be to an attribute.
(self.isAttribute()
and (templateParameterSubstitution->notEmpty())
implies (templateParameterSubstitution->forAll(ts |
    ts.formal.oclIsKindOf(Property)
    and ts.formal.oclAsType(Property).isAttribute())))"""
        raise NotImplementedError(
            'operation binding_to_attribute(...) not yet implemented')

    def derived_union_is_derived(self, diagnostics=None, context=None):
        """A derived union is derived.
isDerivedUnion implies isDerived"""
        raise NotImplementedError(
            'operation derived_union_is_derived(...) not yet implemented')

    def deployment_target(self, diagnostics=None, context=None):
        """A Property can be a DeploymentTarget if it is a kind of Node and functions as a part in the internal structure of an encompassing Node.
deployment->notEmpty() implies owner.oclIsKindOf(Node) and Node.allInstances()->exists(n | n.part->exists(p | p = self))"""
        raise NotImplementedError(
            'operation deployment_target(...) not yet implemented')

    def subsetted_property_names(self, diagnostics=None, context=None):
        """A Property may not subset a Property with the same name.
subsettedProperty->forAll(sp | sp.name <> name)"""
        raise NotImplementedError(
            'operation subsetted_property_names(...) not yet implemented')

    def type_of_opposite_end(self, diagnostics=None, context=None):
        """If a Property is a classifier-owned end of a binary Association, its owner must be the type of the opposite end.
(opposite->notEmpty() and owningAssociation->isEmpty()) implies classifier = opposite.type"""
        raise NotImplementedError(
            'operation type_of_opposite_end(...) not yet implemented')

    def qualified_is_association_end(self, diagnostics=None, context=None):
        """All qualified Properties must be Association ends
qualifier->notEmpty() implies association->notEmpty()"""
        raise NotImplementedError(
            'operation qualified_is_association_end(...) not yet implemented')

    def get_default(self):
        """Retrieves a string representation of the default value for this property."""
        raise NotImplementedError(
            'operation get_default(...) not yet implemented')

    def get_other_end(self):
        """Retrieves the other end of the (binary) association in which this property is a member end."""
        raise NotImplementedError(
            'operation get_other_end(...) not yet implemented')

    def is_set_default(self):

        raise NotImplementedError(
            'operation is_set_default(...) not yet implemented')

    def set_boolean_default_value(self, value=None):
        """Sets the default value for this property to the specified Boolean value."""
        raise NotImplementedError(
            'operation set_boolean_default_value(...) not yet implemented')

    def set_default(self, newDefault=None):
        """Sets the default value for this property based on the specified string representation."""
        raise NotImplementedError(
            'operation set_default(...) not yet implemented')

    def set_integer_default_value(self, value=None):
        """Sets the default value for this property to the specified integer value."""
        raise NotImplementedError(
            'operation set_integer_default_value(...) not yet implemented')

    def set_is_composite(self, newIsComposite=None):
        self.isComposite = newIsComposite

    def set_is_navigable(self, isNavigable=None):
        """Sets the navigability of this property as indicated."""
        raise NotImplementedError(
            'operation set_is_navigable(...) not yet implemented')

    def set_null_default_value(self):
        """Sets the default value for this property to the null value."""
        raise NotImplementedError(
            'operation set_null_default_value(...) not yet implemented')

    def set_opposite(self, newOpposite=None):

        raise NotImplementedError(
            'operation set_opposite(...) not yet implemented')

    def set_real_default_value(self, value=None):
        """Sets the default value for this property to the specified real value."""
        raise NotImplementedError(
            'operation set_real_default_value(...) not yet implemented')

    def set_string_default_value(self, value=None):
        """Sets the default value for this property to the specified string value."""
        raise NotImplementedError(
            'operation set_string_default_value(...) not yet implemented')

    def set_unlimited_natural_default_value(self, value=None):
        """Sets the default value for this property to the specified unlimited natural value."""
        raise NotImplementedError(
            'operation set_unlimited_natural_default_value(...) not yet implemented')

    def unset_default(self):

        raise NotImplementedError(
            'operation unset_default(...) not yet implemented')

    def is_attribute(self):
        """The query isAttribute() is true if the Property is defined as an attribute of some Classifier.
result = (not classifier->isEmpty())
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation is_attribute(...) not yet implemented')

    def is_composite(self):
        """The value of isComposite is true only if aggregation is composite.
result = (aggregation = AggregationKind::composite)
<p>From package UML::Classification.</p>"""
        return self.isComposite

    def is_navigable(self):
        """The query isNavigable() indicates whether it is possible to navigate across the property.
result = (not classifier->isEmpty() or association.navigableOwnedEnd->includes(self))
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation is_navigable(...) not yet implemented')

    def get_opposite(self):
        """If this property is a memberEnd of a binary association, then opposite gives the other end.
result = (if association <> null and association.memberEnd->size() = 2
then
    association.memberEnd->any(e | e <> self)
else
    null
endif)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation get_opposite(...) not yet implemented')

    def subsetting_context(self):
        """The query subsettingContext() gives the context for subsetting a Property. It consists, in the case of an attribute, of the corresponding Classifier, and in the case of an association end, all of the Classifiers at the other ends.
result = (if association <> null
then association.memberEnd->excluding(self)->collect(type)->asSet()
else
  if classifier<>null
  then classifier->asSet()
  else Set{}
  endif
endif)
<p>From package UML::Classification.</p>"""
        raise NotImplementedError(
            'operation subsetting_context(...) not yet implemented')


class ArtifactMixin(object):
    """User defined mixin class for Artifact."""

    def __init__(
            self, fileName=None, manifestation=None, nestedArtifact=None,
            ownedAttribute=None, ownedOperation=None, **kwargs):
        super(ArtifactMixin, self).__init__(**kwargs)

    def create_owned_attribute(
            self, name=None, type=None, lower=None, upper=None):
        """Creates a property with the specified name, type, lower bound, and upper bound as an owned attribute of this artifact."""
        raise NotImplementedError(
            'operation create_owned_attribute(...) not yet implemented')

    def create_owned_operation(
            self, name=None, parameterNames=None, parameterTypes=None,
            returnType=None):
        """Creates an operation with the specified name, parameter names, parameter types, and return type (or null) as an owned operation of this artifact."""
        raise NotImplementedError(
            'operation create_owned_operation(...) not yet implemented')


class EnumerationMixin(object):
    """User defined mixin class for Enumeration."""

    def __init__(self, ownedLiteral=None, **kwargs):
        super(EnumerationMixin, self).__init__(**kwargs)

    def immutable(self, diagnostics=None, context=None):
        """ownedAttribute->forAll(isReadOnly)"""
        raise NotImplementedError(
            'operation immutable(...) not yet implemented')


class PrimitiveTypeMixin(object):
    """User defined mixin class for PrimitiveType."""

    def __init__(self, **kwargs):
        super(PrimitiveTypeMixin, self).__init__(**kwargs)


class UseCaseMixin(object):
    """User defined mixin class for UseCase."""

    def __init__(
            self, extend=None, extensionPoint=None, include=None,
            subject=None, **kwargs):
        super(UseCaseMixin, self).__init__(**kwargs)

    def binary_associations(self, diagnostics=None, context=None):
        """UseCases can only be involved in binary Associations.
Association.allInstances()->forAll(a | a.memberEnd.type->includes(self) implies a.memberEnd->size() = 2)"""
        raise NotImplementedError(
            'operation binary_associations(...) not yet implemented')

    def no_association_to_use_case(self, diagnostics=None, context=None):
        """UseCases cannot have Associations to UseCases specifying the same subject.
Association.allInstances()->forAll(a | a.memberEnd.type->includes(self) implies
   (
   let usecases: Set(UseCase) = a.memberEnd.type->select(oclIsKindOf(UseCase))->collect(oclAsType(UseCase))->asSet() in
   usecases->size() > 1 implies usecases->collect(subject)->size() > 1
   )
)"""
        raise NotImplementedError(
            'operation no_association_to_use_case(...) not yet implemented')

    def cannot_include_self(self, diagnostics=None, context=None):
        """A UseCase cannot include UseCases that directly or indirectly include it.
not allIncludedUseCases()->includes(self)"""
        raise NotImplementedError(
            'operation cannot_include_self(...) not yet implemented')

    def must_have_name(self, diagnostics=None, context=None):
        """A UseCase must have a name.
name -> notEmpty ()"""
        raise NotImplementedError(
            'operation must_have_name(...) not yet implemented')

    def all_included_use_cases(self):
        """The query allIncludedUseCases() returns the transitive closure of all UseCases (directly or indirectly) included by this UseCase.
result = (self.include.addition->union(self.include.addition->collect(uc | uc.allIncludedUseCases()))->asSet())
<p>From package UML::UseCases.</p>"""
        raise NotImplementedError(
            'operation all_included_use_cases(...) not yet implemented')


class DerivedOwnedport(EDerivedCollection):
    pass


class EncapsulatedClassifierMixin(object):
    """User defined mixin class for EncapsulatedClassifier."""

    def __init__(self, ownedPort=None, **kwargs):
        super(EncapsulatedClassifierMixin, self).__init__(**kwargs)

    def get_owned_ports(self):
        """Derivation for EncapsulatedClassifier::/ownedPort : Port
result = (ownedAttribute->select(oclIsKindOf(Port))->collect(oclAsType(Port))->asOrderedSet())
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_owned_ports(...) not yet implemented')


class ActionInputPinMixin(object):
    """User defined mixin class for ActionInputPin."""

    def __init__(self, fromAction=None, **kwargs):
        super(ActionInputPinMixin, self).__init__(**kwargs)

    def input_pin(self, diagnostics=None, context=None):
        """The fromAction of an ActionInputPin must only have ActionInputPins as InputPins.
fromAction.input->forAll(oclIsKindOf(ActionInputPin))"""
        raise NotImplementedError(
            'operation input_pin(...) not yet implemented')

    def one_output_pin(self, diagnostics=None, context=None):
        """The fromAction of an ActionInputPin must have exactly one OutputPin.
fromAction.output->size() = 1"""
        raise NotImplementedError(
            'operation one_output_pin(...) not yet implemented')

    def no_control_or_object_flow(self, diagnostics=None, context=None):
        """The fromAction of an ActionInputPin cannot have ActivityEdges coming into or out of it or its Pins.
fromAction.incoming->union(outgoing)->isEmpty() and
fromAction.input.incoming->isEmpty() and
fromAction.output.outgoing->isEmpty()"""
        raise NotImplementedError(
            'operation no_control_or_object_flow(...) not yet implemented')


class ConditionalNodeMixin(object):
    """User defined mixin class for ConditionalNode."""

    def __init__(
            self, clause=None, isAssured=None, isDeterminate=None,
            result=None, **kwargs):
        super(ConditionalNodeMixin, self).__init__(**kwargs)

    def result_no_incoming(self, diagnostics=None, context=None):
        """The result OutputPins have no incoming edges.
result.incoming->isEmpty()"""
        raise NotImplementedError(
            'operation result_no_incoming(...) not yet implemented')

    def no_input_pins(self, diagnostics=None, context=None):
        """A ConditionalNode has no InputPins.
input->isEmpty()"""
        raise NotImplementedError(
            'operation no_input_pins(...) not yet implemented')

    def one_clause_with_executable_node(self, diagnostics=None, context=None):
        """No ExecutableNode in the ConditionNode may appear in the test or body part of more than one clause of a ConditionalNode.
node->select(oclIsKindOf(ExecutableNode)).oclAsType(ExecutableNode)->forAll(n |
        self.clause->select(test->union(_'body')->includes(n))->size()=1)"""
        raise NotImplementedError(
            'operation one_clause_with_executable_node(...) not yet implemented')

    def matching_output_pins(self, diagnostics=None, context=None):
        """Each clause of a ConditionalNode must have the same number of bodyOutput pins as the ConditionalNode has result OutputPins, and each clause bodyOutput Pin must be compatible with the corresponding result OutputPin (by positional order) in type, multiplicity, ordering, and uniqueness.
clause->forAll(
        bodyOutput->size()=self.result->size() and
        Sequence{1..self.result->size()}->forAll(i |
                bodyOutput->at(i).type.conformsTo(result->at(i).type) and
                bodyOutput->at(i).isOrdered = result->at(i).isOrdered and
                bodyOutput->at(i).isUnique = result->at(i).isUnique and
                bodyOutput->at(i).compatibleWith(result->at(i))))"""
        raise NotImplementedError(
            'operation matching_output_pins(...) not yet implemented')

    def executable_nodes(self, diagnostics=None, context=None):
        """The union of the ExecutableNodes in the test and body parts of all clauses must be the same as the subset of nodes contained in the ConditionalNode (considered as a StructuredActivityNode) that are ExecutableNodes.
clause.test->union(clause._'body') = node->select(oclIsKindOf(ExecutableNode)).oclAsType(ExecutableNode)"""
        raise NotImplementedError(
            'operation executable_nodes(...) not yet implemented')

    def clause_no_predecessor(self, diagnostics=None, context=None):
        """No two clauses within a ConditionalNode may be predecessorClauses of each other, either directly or indirectly.
clause->closure(predecessorClause)->intersection(clause)->isEmpty()"""
        raise NotImplementedError(
            'operation clause_no_predecessor(...) not yet implemented')


class CreateLinkObjectActionMixin(object):
    """User defined mixin class for CreateLinkObjectAction."""

    def __init__(self, result=None, **kwargs):
        super(CreateLinkObjectActionMixin, self).__init__(**kwargs)

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of the OutputPin is 1..1.
result.is(1,1)"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def type_of_result(self, diagnostics=None, context=None):
        """The type of the result OutputPin must be the same as the Association of the CreateLinkObjectAction.
result.type = association()"""
        raise NotImplementedError(
            'operation type_of_result(...) not yet implemented')

    def association_class(self, diagnostics=None, context=None):
        """The Association must be an AssociationClass.
self.association().oclIsKindOf(AssociationClass)"""
        raise NotImplementedError(
            'operation association_class(...) not yet implemented')


class ExpansionRegionMixin(object):
    """User defined mixin class for ExpansionRegion."""

    def __init__(
            self, mode=None, outputElement=None, inputElement=None, **
            kwargs):
        super(ExpansionRegionMixin, self).__init__(**kwargs)


class LoopNodeMixin(object):
    """User defined mixin class for LoopNode."""

    def __init__(
            self, bodyOutput=None, bodyPart=None, decider=None,
            isTestedFirst=None, loopVariable=None, loopVariableInput=None,
            result=None, setupPart=None, test=None, **kwargs):
        super(LoopNodeMixin, self).__init__(**kwargs)

    def result_no_incoming(self, diagnostics=None, context=None):
        """The result OutputPins have no incoming edges.
result.incoming->isEmpty()"""
        raise NotImplementedError(
            'operation result_no_incoming(...) not yet implemented')

    def input_edges(self, diagnostics=None, context=None):
        """The loopVariableInputs must not have outgoing edges.
loopVariableInput.outgoing->isEmpty()"""
        raise NotImplementedError(
            'operation input_edges(...) not yet implemented')

    def executable_nodes(self, diagnostics=None, context=None):
        """The union of the ExecutableNodes in the setupPart, test and bodyPart of a LoopNode must be the same as the subset of nodes contained in the LoopNode (considered as a StructuredActivityNode) that are ExecutableNodes.
setupPart->union(test)->union(bodyPart)=node->select(oclIsKindOf(ExecutableNode)).oclAsType(ExecutableNode)->asSet()"""
        raise NotImplementedError(
            'operation executable_nodes(...) not yet implemented')

    def body_output_pins(self, diagnostics=None, context=None):
        """The bodyOutput pins are OutputPins on Actions in the body of the LoopNode.
bodyPart.oclAsType(Action).allActions().output->includesAll(bodyOutput)"""
        raise NotImplementedError(
            'operation body_output_pins(...) not yet implemented')

    def setup_test_and_body(self, diagnostics=None, context=None):
        """The test and body parts of a ConditionalNode must be disjoint with each other.
setupPart->intersection(test)->isEmpty() and
setupPart->intersection(bodyPart)->isEmpty() and
test->intersection(bodyPart)->isEmpty()"""
        raise NotImplementedError(
            'operation setup_test_and_body(...) not yet implemented')

    def matching_output_pins(self, diagnostics=None, context=None):
        """A LoopNode must have the same number of bodyOutput Pins as loopVariables, and each bodyOutput Pin must be compatible with the corresponding loopVariable (by positional order) in type, multiplicity, ordering and uniqueness.
bodyOutput->size()=loopVariable->size() and
Sequence{1..loopVariable->size()}->forAll(i |
        bodyOutput->at(i).type.conformsTo(loopVariable->at(i).type) and
        bodyOutput->at(i).isOrdered = loopVariable->at(i).isOrdered and
        bodyOutput->at(i).isUnique = loopVariable->at(i).isUnique and
        loopVariable->at(i).includesMultiplicity(bodyOutput->at(i)))"""
        raise NotImplementedError(
            'operation matching_output_pins(...) not yet implemented')

    def matching_loop_variables(self, diagnostics=None, context=None):
        """A LoopNode must have the same number of loopVariableInputs and loopVariables, and they must match in type, uniqueness and multiplicity.
loopVariableInput->size()=loopVariable->size() and
loopVariableInput.type=loopVariable.type and
loopVariableInput.isUnique=loopVariable.isUnique and
loopVariableInput.lower=loopVariable.lower and
loopVariableInput.upper=loopVariable.upper"""
        raise NotImplementedError(
            'operation matching_loop_variables(...) not yet implemented')

    def matching_result_pins(self, diagnostics=None, context=None):
        """A LoopNode must have the same number of result OutputPins and loopVariables, and they must match in type, uniqueness and multiplicity.
result->size()=loopVariable->size() and
result.type=loopVariable.type and
result.isUnique=loopVariable.isUnique and
result.lower=loopVariable.lower and
result.upper=loopVariable.upper"""
        raise NotImplementedError(
            'operation matching_result_pins(...) not yet implemented')

    def loop_variable_outgoing(self, diagnostics=None, context=None):
        """All ActivityEdges outgoing from loopVariable OutputPins must have targets within the LoopNode.
allOwnedNodes()->includesAll(loopVariable.outgoing.target)"""
        raise NotImplementedError(
            'operation loop_variable_outgoing(...) not yet implemented')


class SequenceNodeMixin(object):
    """User defined mixin class for SequenceNode."""

    def __init__(self, executableNode=None, **kwargs):
        super(SequenceNodeMixin, self).__init__(**kwargs)


class ValuePinMixin(object):
    """User defined mixin class for ValuePin."""

    def __init__(self, value=None, **kwargs):
        super(ValuePinMixin, self).__init__(**kwargs)

    def no_incoming_edges(self, diagnostics=None, context=None):
        """A ValuePin may have no incoming ActivityEdges.
incoming->isEmpty()"""
        raise NotImplementedError(
            'operation no_incoming_edges(...) not yet implemented')

    def compatible_type(self, diagnostics=None, context=None):
        """The type of the value ValueSpecification must conform to the type of the ValuePin.
value.type.conformsTo(type)"""
        raise NotImplementedError(
            'operation compatible_type(...) not yet implemented')


class ActorMixin(object):
    """User defined mixin class for Actor."""

    def __init__(self, **kwargs):
        super(ActorMixin, self).__init__(**kwargs)

    def associations(self, diagnostics=None, context=None):
        """An Actor can only have Associations to UseCases, Components, and Classes. Furthermore these Associations must be binary.
Association.allInstances()->forAll( a |
  a.memberEnd->collect(type)->includes(self) implies
  (
    a.memberEnd->size() = 2 and
    let actorEnd : Property = a.memberEnd->any(type = self) in
      actorEnd.opposite.class.oclIsKindOf(UseCase) or
      ( actorEnd.opposite.class.oclIsKindOf(Class) and not
         actorEnd.opposite.class.oclIsKindOf(Behavior))
      )
  )"""
        raise NotImplementedError(
            'operation associations(...) not yet implemented')

    def must_have_name(self, diagnostics=None, context=None):
        """An Actor must have a name.
name->notEmpty()"""
        raise NotImplementedError(
            'operation must_have_name(...) not yet implemented')


class DeploymentSpecificationMixin(object):
    """User defined mixin class for DeploymentSpecification."""

    def __init__(
            self, deploymentLocation=None, executionLocation=None,
            deployment=None, **kwargs):
        super(DeploymentSpecificationMixin, self).__init__(**kwargs)

    def deployment_target(self, diagnostics=None, context=None):
        """The DeploymentTarget of a DeploymentSpecification is a kind of ExecutionEnvironment.
deployment->forAll (location.oclIsKindOf(ExecutionEnvironment))"""
        raise NotImplementedError(
            'operation deployment_target(...) not yet implemented')

    def deployed_elements(self, diagnostics=None, context=None):
        """The deployedElements of a DeploymentTarget that are involved in a Deployment that has an associated Deployment-Specification is a kind of Component (i.e., the configured components).
deployment->forAll (location.deployedElement->forAll (oclIsKindOf(Component)))"""
        raise NotImplementedError(
            'operation deployed_elements(...) not yet implemented')


class DerivedProvided(EDerivedCollection):
    pass


class DerivedRequired(EDerivedCollection):
    pass


class PortMixin(object):
    """User defined mixin class for Port."""

    def __init__(
            self, isBehavior=None, isConjugated=None, isService=None,
            protocol=None, provided=None, redefinedPort=None, required=None, **
            kwargs):
        super(PortMixin, self).__init__(**kwargs)

    def port_aggregation(self, diagnostics=None, context=None):
        """Port.aggregation must be composite.
aggregation = AggregationKind::composite"""
        raise NotImplementedError(
            'operation port_aggregation(...) not yet implemented')

    def default_value(self, diagnostics=None, context=None):
        """A defaultValue for port cannot be specified when the type of the Port is an Interface.
type.oclIsKindOf(Interface) implies defaultValue->isEmpty()"""
        raise NotImplementedError(
            'operation default_value(...) not yet implemented')

    def encapsulated_owner(self, diagnostics=None, context=None):
        """All Ports are owned by an EncapsulatedClassifier.
owner = encapsulatedClassifier"""
        raise NotImplementedError(
            'operation encapsulated_owner(...) not yet implemented')

    def get_provideds(self):
        """Derivation for Port::/provided
result = (if isConjugated then basicRequired() else basicProvided() endif)
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_provideds(...) not yet implemented')

    def get_requireds(self):
        """Derivation for Port::/required
result = (if isConjugated then basicProvided() else basicRequired() endif)
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_requireds(...) not yet implemented')

    def basic_provided(self):
        """The union of the sets of Interfaces realized by the type of the Port and its supertypes, or directly the type of the Port if the Port is typed by an Interface.
result = (if type.oclIsKindOf(Interface)
then type.oclAsType(Interface)->asSet()
else type.oclAsType(Classifier).allRealizedInterfaces()
endif)
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation basic_provided(...) not yet implemented')

    def basic_required(self):
        """The union of the sets of Interfaces used by the type of the Port and its supertypes.
result = ( type.oclAsType(Classifier).allUsedInterfaces() )
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation basic_required(...) not yet implemented')


class ExtensionMixin(object):
    """User defined mixin class for Extension."""

    @property
    def isRequired(self):
        raise NotImplementedError('Missing implementation for isRequired')

    @property
    def metaclass(self):
        raise NotImplementedError('Missing implementation for metaclass')

    def __init__(self, isRequired=None, metaclass=None, **kwargs):
        super(ExtensionMixin, self).__init__(**kwargs)

    def non_owned_end(self, diagnostics=None, context=None):
        """The non-owned end of an Extension is typed by a Class.
metaclassEnd()->notEmpty() and metaclassEnd().type.oclIsKindOf(Class)"""
        raise NotImplementedError(
            'operation non_owned_end(...) not yet implemented')

    def is_binary(self, diagnostics=None, context=None):
        """An Extension is binary, i.e., it has only two memberEnds.
memberEnd->size() = 2"""
        raise NotImplementedError(
            'operation is_binary(...) not yet implemented')

    def get_stereotype(self):
        """Retrieves the stereotype that extends a metaclass through this extension."""
        raise NotImplementedError(
            'operation get_stereotype(...) not yet implemented')

    def get_stereotype_end(self):
        """Retrieves the extension end that is typed by a stereotype (as opposed to a metaclass)."""
        raise NotImplementedError(
            'operation get_stereotype_end(...) not yet implemented')

    def is_required(self):
        """The query isRequired() is true if the owned end has a multiplicity with the lower bound of 1.
result = (ownedEnd.lowerBound() = 1)
<p>From package UML::Packages.</p>"""
        raise NotImplementedError(
            'operation is_required(...) not yet implemented')

    def get_metaclass(self):
        """The query metaclass() returns the metaclass that is being extended (as opposed to the extending stereotype).
result = (metaclassEnd().type.oclAsType(Class))
<p>From package UML::Packages.</p>"""
        raise NotImplementedError(
            'operation get_metaclass(...) not yet implemented')

    def metaclass_end(self):
        """The query metaclassEnd() returns the Property that is typed by a metaclass (as opposed to a stereotype).
result = (memberEnd->reject(p | ownedEnd->includes(p.oclAsType(ExtensionEnd)))->any(true))
<p>From package UML::Packages.</p>"""
        raise NotImplementedError(
            'operation metaclass_end(...) not yet implemented')


class ExtensionEndMixin(object):
    """User defined mixin class for ExtensionEnd."""

    def __init__(self, **kwargs):
        super(ExtensionEndMixin, self).__init__(**kwargs)

    def multiplicity(self, diagnostics=None, context=None):
        """The multiplicity of ExtensionEnd is 0..1 or 1.
(lowerBound() = 0 or lowerBound() = 1) and upperBound() = 1"""
        raise NotImplementedError(
            'operation multiplicity(...) not yet implemented')

    def aggregation(self, diagnostics=None, context=None):
        """The aggregation of an ExtensionEnd is composite.
self.aggregation = AggregationKind::composite"""
        raise NotImplementedError(
            'operation aggregation(...) not yet implemented')


class CollaborationMixin(object):
    """User defined mixin class for Collaboration."""

    def __init__(self, collaborationRole=None, **kwargs):
        super(CollaborationMixin, self).__init__(**kwargs)


class CommunicationPathMixin(object):
    """User defined mixin class for CommunicationPath."""

    def __init__(self, **kwargs):
        super(CommunicationPathMixin, self).__init__(**kwargs)


class DerivedExtension(EDerivedCollection):
    pass


class DerivedSuperclass(EDerivedCollection):
    def _get_collection(self):
        return [g.general for g in self.owner.generalization]

    def __len__(self):
        return len(self.owner.generalization)

    def __getitem__(self, index):
        return self._get_collection()[index]

    def insert(self, index, item):
        from .uml import Generalization
        self.check(item)
        g = Generalization(general=item)
        self.owner.generalization.append(g)

    def discard(self, item):
        c = [g for g in self.owner.generalization if g.general is item]
        for i in c:
            self.owner.generalization.remove(i)

    def __delitem__(self, index):
        g = self.owner.generalization[index]
        self.owner.generalization.remove(g)

    def __repr__(self):
        return 'DerivedCollection({})'.format(self._get_collection())


class ClassMixin(object):
    """User defined mixin class for Class."""

    def __init__(
            self, ownedOperation=None, extension=None, isActive=None,
            nestedClassifier=None, ownedReception=None, superClass=None, **
            kwargs):
        super(ClassMixin, self).__init__(**kwargs)

    def passive_class(self, diagnostics=None, context=None):
        """Only an active Class may own Receptions and have a classifierBehavior.
not isActive implies (ownedReception->isEmpty() and classifierBehavior = null)"""
        raise NotImplementedError(
            'operation passive_class(...) not yet implemented')

    def create_owned_operation(
            self, name=None, parameterNames=None, parameterTypes=None,
            returnType=None):
        """Creates an operation with the specified name, parameter names, parameter types, and return type (or null) as an owned operation of this class."""
        raise NotImplementedError(
            'operation create_owned_operation(...) not yet implemented')

    def is_metaclass(self):
        from .standard import Metaclass
        """Determines whether this class is a metaclass."""
        for o, r in self._inverse_rels:
            if isinstance(o, Metaclass) and r.name == 'base_Class':
                return True
        return False

    def get_extensions(self):
        """Derivation for Class::/extension : Extension
result = (Extension.allInstances()->select(ext |
  let endTypes : Sequence(Classifier) = ext.memberEnd->collect(type.oclAsType(Classifier)) in
  endTypes->includes(self) or endTypes.allParents()->includes(self) ))
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_extensions(...) not yet implemented')

    def get_super_classes(self):
        """Derivation for Class::/superClass : Class
result = (self.general()->select(oclIsKindOf(Class))->collect(oclAsType(Class))->asSet())
<p>From package UML::StructuredClassifiers.</p>"""
        return self.superClass


class BehaviorMixin(object):
    """User defined mixin class for Behavior."""

    @property
    def context(self):
        raise NotImplementedError('Missing implementation for context')

    def __init__(
            self, specification=None, context=None, isReentrant=None,
            ownedParameter=None, ownedParameterSet=None, postcondition=None,
            precondition=None, redefinedBehavior=None, **kwargs):
        super(BehaviorMixin, self).__init__(**kwargs)

    def most_one_behavior(self, diagnostics=None, context=None):
        """There may be at most one Behavior for a given pairing of BehavioredClassifier (as owner of the Behavior) and BehavioralFeature (as specification of the Behavior).
specification <> null implies _'context'.ownedBehavior->select(specification=self.specification)->size() = 1"""
        raise NotImplementedError(
            'operation most_one_behavior(...) not yet implemented')

    def parameters_match(self, diagnostics=None, context=None):
        """If a Behavior has a specification BehavioralFeature, then it must have the same number of ownedParameters as its specification. The Behavior Parameters must also "match" the BehavioralParameter Parameters, but the exact requirements for this matching are not formalized.
specification <> null implies ownedParameter->size() = specification.ownedParameter->size()"""
        raise NotImplementedError(
            'operation parameters_match(...) not yet implemented')

    def feature_of_context_classifier(self, diagnostics=None, context=None):
        """The specification BehavioralFeature must be a feature (possibly inherited) of the context BehavioredClassifier of the Behavior.
_'context'.feature->includes(specification)"""
        raise NotImplementedError(
            'operation feature_of_context_classifier(...) not yet implemented')

    def get_context(self):
        """A Behavior that is directly owned as a nestedClassifier does not have a context. Otherwise, to determine the context of a Behavior, find the first BehavioredClassifier reached by following the chain of owner relationships from the Behavior, if any. If there is such a BehavioredClassifier, then it is the context, unless it is itself a Behavior with a non-empty context, in which case that is also the context for the original Behavior.
result = (if nestingClass <> null then
    null
else
    let b:BehavioredClassifier = self.behavioredClassifier(self.owner) in
    if b.oclIsKindOf(Behavior) and b.oclAsType(Behavior)._'context' <> null then
        b.oclAsType(Behavior)._'context'
    else
        b
    endif
endif
        )
<p>From package UML::CommonBehavior.</p>"""
        raise NotImplementedError(
            'operation get_context(...) not yet implemented')

    def behaviored_classifier(self, from_=None):
        """The first BehavioredClassifier reached by following the chain of owner relationships from the Behavior, if any.
if from.oclIsKindOf(BehavioredClassifier) then
    from.oclAsType(BehavioredClassifier)
else if from.owner = null then
    null
else
    self.behavioredClassifier(from.owner)
endif
endif
<p>From package UML::CommonBehavior.</p>"""
        raise NotImplementedError(
            'operation behaviored_classifier(...) not yet implemented')

    def input_parameters(self):
        """The in and inout ownedParameters of the Behavior.
result = (ownedParameter->select(direction=ParameterDirectionKind::_'in' or direction=ParameterDirectionKind::inout))
<p>From package UML::CommonBehavior.</p>"""
        raise NotImplementedError(
            'operation input_parameters(...) not yet implemented')

    def output_parameters(self):
        """The out, inout and return ownedParameters.
result = (ownedParameter->select(direction=ParameterDirectionKind::out or direction=ParameterDirectionKind::inout or direction=ParameterDirectionKind::return))
<p>From package UML::CommonBehavior.</p>"""
        raise NotImplementedError(
            'operation output_parameters(...) not yet implemented')


class StereotypeMixin(object):
    """User defined mixin class for Stereotype."""

    @property
    def profile(self):
        raise NotImplementedError('Missing implementation for profile')

    def __init__(self, icon=None, profile=None, **kwargs):
        super(StereotypeMixin, self).__init__(**kwargs)

    def binary_associations_only(self, diagnostics=None, context=None):
        """Stereotypes may only participate in binary associations.
ownedAttribute.association->forAll(memberEnd->size()=2)"""
        raise NotImplementedError(
            'operation binary_associations_only(...) not yet implemented')

    def generalize(self, diagnostics=None, context=None):
        """A Stereotype may only generalize or specialize another Stereotype.
allParents()->forAll(oclIsKindOf(Stereotype))
and Classifier.allInstances()->forAll(c | c.allParents()->exists(oclIsKindOf(Stereotype)) implies c.oclIsKindOf(Stereotype))"""
        raise NotImplementedError(
            'operation generalize(...) not yet implemented')

    def name_not_clash(self, diagnostics=None, context=None):
        """Stereotype names should not clash with keyword names for the extended model element."""
        raise NotImplementedError(
            'operation name_not_clash(...) not yet implemented')

    def association_end_ownership(self, diagnostics=None, context=None):
        """Where a stereotype’s property is an association end for an association other than a kind of extension, and the other end is not a stereotype, the other end must be owned by the association itself.
ownedAttribute
->select(association->notEmpty() and not association.oclIsKindOf(Extension) and not type.oclIsKindOf(Stereotype))
->forAll(opposite.owner = association)"""
        raise NotImplementedError(
            'operation association_end_ownership(...) not yet implemented')

    def base_property_upper_bound(self, diagnostics=None, context=None):
        """The upper bound of base-properties is exactly 1."""
        raise NotImplementedError(
            'operation base_property_upper_bound(...) not yet implemented')

    def base_property_multiplicity_single_extension(
            self, diagnostics=None, context=None):
        """If a Stereotype extends only one metaclass, the multiplicity of the corresponding base-property shall be 1..1."""
        raise NotImplementedError(
            'operation base_property_multiplicity_single_extension(...) not yet implemented')

    def base_property_multiplicity_multiple_extension(
            self, diagnostics=None, context=None):
        """If a Stereotype extends more than one metaclass, the multiplicity of the corresponding base-properties shall be [0..1]. At any point in time, only one of these base-properties can contain a metaclass instance during runtime."""
        raise NotImplementedError(
            'operation base_property_multiplicity_multiple_extension(...) not yet implemented')

    def create_extension(self, metaclass=None, isRequired=None):
        """Creates a(n) (required) extension of the specified metaclass with this stereotype."""
        raise NotImplementedError(
            'operation create_extension(...) not yet implemented')

    def create_icon(self, location=None):
        """Creates an icon with the specified location for this stereotype."""
        raise NotImplementedError(
            'operation create_icon(...) not yet implemented')

    def create_icon(self, format=None, content=None):
        """Creates an icon with the specified format and content for this stereotype."""
        raise NotImplementedError(
            'operation create_icon(...) not yet implemented')

    def get_all_extended_metaclasses(self):
        """Retrieves all the metaclasses extended by this stereotype, including the metaclasses extended by its superstereotypes."""
        raise NotImplementedError(
            'operation get_all_extended_metaclasses(...) not yet implemented')

    def get_definition(self):
        """Retrieves the current definition (Ecore representation) of this stereotype."""
        raise NotImplementedError(
            'operation get_definition(...) not yet implemented')

    def get_extended_metaclasses(self):
        """Retrieves the metaclasses extended by this stereotype."""
        raise NotImplementedError(
            'operation get_extended_metaclasses(...) not yet implemented')

    def get_keyword(self):
        """Retrieves the localized keyword for this stereotype."""
        raise NotImplementedError(
            'operation get_keyword(...) not yet implemented')

    def get_keyword(self, localize=None):
        """Retrieves the keyword for this stereotype, localized if indicated."""
        raise NotImplementedError(
            'operation get_keyword(...) not yet implemented')

    def containing_profile(self):
        """The query containingProfile returns the closest profile directly or indirectly containing this stereotype.
result = (self.namespace.oclAsType(Package).containingProfile())
<p>From package UML::Packages.</p>"""
        raise NotImplementedError(
            'operation containing_profile(...) not yet implemented')

    def get_profile(self):
        """A stereotype must be contained, directly or indirectly, in a profile.
result = (self.containingProfile())
<p>From package UML::Packages.</p>"""
        raise NotImplementedError(
            'operation get_profile(...) not yet implemented')


class DerivedProvided(EDerivedCollection):
    pass


class DerivedRequired(EDerivedCollection):
    pass


class ComponentMixin(object):
    """User defined mixin class for Component."""

    def __init__(
            self, isIndirectlyInstantiated=None, packagedElement=None,
            provided=None, realization=None, required=None, **kwargs):
        super(ComponentMixin, self).__init__(**kwargs)

    def no_nested_classifiers(self, diagnostics=None, context=None):
        """A Component cannot nest Classifiers.
nestedClassifier->isEmpty()"""
        raise NotImplementedError(
            'operation no_nested_classifiers(...) not yet implemented')

    def no_packaged_elements(self, diagnostics=None, context=None):
        """A Component nested in a Class cannot have any packaged elements.
nestingClass <> null implies packagedElement->isEmpty()"""
        raise NotImplementedError(
            'operation no_packaged_elements(...) not yet implemented')

    def create_owned_class(self, name=None, isAbstract=None):
        """Creates a(n) (abstract) class with the specified name as a packaged element of this component."""
        raise NotImplementedError(
            'operation create_owned_class(...) not yet implemented')

    def create_owned_enumeration(self, name=None):
        """Creates a enumeration with the specified name as a packaged element of this component."""
        raise NotImplementedError(
            'operation create_owned_enumeration(...) not yet implemented')

    def create_owned_interface(self, name=None):
        """Creates an interface with the specified name as a packaged element of this component."""
        raise NotImplementedError(
            'operation create_owned_interface(...) not yet implemented')

    def create_owned_primitive_type(self, name=None):
        """Creates a primitive type with the specified name as a packaged element of this component."""
        raise NotImplementedError(
            'operation create_owned_primitive_type(...) not yet implemented')

    def get_provideds(self):
        """Derivation for Component::/provided
result = (let 	ris : Set(Interface) = allRealizedInterfaces(),
        realizingClassifiers : Set(Classifier) =  self.realization.realizingClassifier->union(self.allParents()->collect(realization.realizingClassifier))->asSet(),
        allRealizingClassifiers : Set(Classifier) = realizingClassifiers->union(realizingClassifiers.allParents())->asSet(),
        realizingClassifierInterfaces : Set(Interface) = allRealizingClassifiers->iterate(c; rci : Set(Interface) = Set{} | rci->union(c.allRealizedInterfaces())),
        ports : Set(Port) = self.ownedPort->union(allParents()->collect(ownedPort))->asSet(),
        providedByPorts : Set(Interface) = ports.provided->asSet()
in     ris->union(realizingClassifierInterfaces) ->union(providedByPorts)->asSet())
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_provideds(...) not yet implemented')

    def get_requireds(self):
        """Derivation for Component::/required
result = (let 	uis : Set(Interface) = allUsedInterfaces(),
        realizingClassifiers : Set(Classifier) = self.realization.realizingClassifier->union(self.allParents()->collect(realization.realizingClassifier))->asSet(),
        allRealizingClassifiers : Set(Classifier) = realizingClassifiers->union(realizingClassifiers.allParents())->asSet(),
        realizingClassifierInterfaces : Set(Interface) = allRealizingClassifiers->iterate(c; rci : Set(Interface) = Set{} | rci->union(c.allUsedInterfaces())),
        ports : Set(Port) = self.ownedPort->union(allParents()->collect(ownedPort))->asSet(),
        usedByPorts : Set(Interface) = ports.required->asSet()
in	    uis->union(realizingClassifierInterfaces)->union(usedByPorts)->asSet()
)
<p>From package UML::StructuredClassifiers.</p>"""
        raise NotImplementedError(
            'operation get_requireds(...) not yet implemented')


class DerivedNode(EDerivedCollection):
    pass


class DerivedGroup(EDerivedCollection):
    pass


class ActivityMixin(object):
    """User defined mixin class for Activity."""

    def __init__(
            self, ownedGroup=None, edge=None, node=None, variable=None,
            group=None, ownedNode=None, isReadOnly=None,
            isSingleExecution=None, partition=None, structuredNode=None, **
            kwargs):
        super(ActivityMixin, self).__init__(**kwargs)

    def maximum_one_parameter_node(self, diagnostics=None, context=None):
        """A Parameter with direction other than inout must have exactly one ActivityParameterNode in an Activity.
ownedParameter->forAll(p |
   p.direction <> ParameterDirectionKind::inout implies node->select(
       oclIsKindOf(ActivityParameterNode) and oclAsType(ActivityParameterNode).parameter = p)->size()= 1)"""
        raise NotImplementedError(
            'operation maximum_one_parameter_node(...) not yet implemented')

    def maximum_two_parameter_nodes(self, diagnostics=None, context=None):
        """A Parameter with direction inout must have exactly two ActivityParameterNodes in an Activity, at most one with incoming ActivityEdges and at most one with outgoing ActivityEdges.
ownedParameter->forAll(p |
p.direction = ParameterDirectionKind::inout implies
let associatedNodes : Set(ActivityNode) = node->select(
       oclIsKindOf(ActivityParameterNode) and oclAsType(ActivityParameterNode).parameter = p) in
  associatedNodes->size()=2 and
  associatedNodes->select(incoming->notEmpty())->size()<=1 and
  associatedNodes->select(outgoing->notEmpty())->size()<=1
)"""
        raise NotImplementedError(
            'operation maximum_two_parameter_nodes(...) not yet implemented')


class StateMachineMixin(object):
    """User defined mixin class for StateMachine."""

    def __init__(self, connectionPoint=None, submachineState=None,
                 region=None, extendedStateMachine=None, **kwargs):
        super(StateMachineMixin, self).__init__(**kwargs)

    def connection_points(self, diagnostics=None, context=None):
        """The connection points of a StateMachine are Pseudostates of kind entry point or exit point.
connectionPoint->forAll (kind = PseudostateKind::entryPoint or kind = PseudostateKind::exitPoint)"""
        raise NotImplementedError(
            'operation connection_points(...) not yet implemented')

    def classifier_context(self, diagnostics=None, context=None):
        """The Classifier context of a StateMachine cannot be an Interface.
_'context' <> null implies not _'context'.oclIsKindOf(Interface)"""
        raise NotImplementedError(
            'operation classifier_context(...) not yet implemented')

    def method(self, diagnostics=None, context=None):
        """A StateMachine as the method for a BehavioralFeature cannot have entry/exit connection points.
specification <> null implies connectionPoint->isEmpty()"""
        raise NotImplementedError('operation method(...) not yet implemented')

    def context_classifier(self, diagnostics=None, context=None):
        """The context Classifier of the method StateMachine of a BehavioralFeature must be the Classifier that owns the BehavioralFeature.
specification <> null implies ( _'context' <> null and specification.featuringClassifier->exists(c | c = _'context'))"""
        raise NotImplementedError(
            'operation context_classifier(...) not yet implemented')

    def lca(self, s1=None, s2=None):
        """The operation LCA(s1,s2) returns the Region that is the least common ancestor of Vertices s1 and s2, based on the StateMachine containment hierarchy.
result = (if ancestor(s1, s2) then
    s2.container
else
        if ancestor(s2, s1) then
            s1.container
        else
            LCA(s1.container.state, s2.container.state)
        endif
endif)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError('operation lca(...) not yet implemented')

    def ancestor(self, s1=None, s2=None):
        """The query ancestor(s1, s2) checks whether Vertex s2 is an ancestor of Vertex s1.
result = (if (s2 = s1) then
        true
else
        if s1.container.stateMachine->notEmpty() then
            true
        else
            if s2.container.stateMachine->notEmpty() then
                false
            else
                ancestor(s1, s2.container.state)
             endif
         endif
endif  )
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation ancestor(...) not yet implemented')

    def lca_state(self, v1=None, v2=None):
        """This utility funciton is like the LCA, except that it returns the nearest composite State that contains both input Vertices.
result = (if v2.oclIsTypeOf(State) and ancestor(v1, v2) then
        v2.oclAsType(State)
else if v1.oclIsTypeOf(State) and ancestor(v2, v1) then
        v1.oclAsType(State)
else if (v1.container.state->isEmpty() or v2.container.state->isEmpty()) then
        null.oclAsType(State)
else LCAState(v1.container.state, v2.container.state)
endif endif endif)
<p>From package UML::StateMachines.</p>"""
        raise NotImplementedError(
            'operation lca_state(...) not yet implemented')


class OpaqueBehaviorMixin(object):
    """User defined mixin class for OpaqueBehavior."""

    def __init__(self, body=None, language=None, **kwargs):
        super(OpaqueBehaviorMixin, self).__init__(**kwargs)


class NodeMixin(object):
    """User defined mixin class for Node."""

    def __init__(self, nestedNode=None, **kwargs):
        super(NodeMixin, self).__init__(**kwargs)

    def internal_structure(self, diagnostics=None, context=None):
        """The internal structure of a Node (if defined) consists solely of parts of type Node.
part->forAll(oclIsKindOf(Node))"""
        raise NotImplementedError(
            'operation internal_structure(...) not yet implemented')

    def create_communication_path(
            self, end1IsNavigable=None, end1Aggregation=None, end1Name=None,
            end1Lower=None, end1Upper=None, end1Node=None,
            end2IsNavigable=None, end2Aggregation=None, end2Name=None,
            end2Lower=None, end2Upper=None):
        """Creates a (binary) communication path between this node and the specified other node, with the specified navigabilities, aggregations, names, lower bounds, and upper bounds, and owned by this node's nearest package."""
        raise NotImplementedError(
            'operation create_communication_path(...) not yet implemented')

    def get_communication_paths(self):
        """Retrieves the communication paths in which this node is involved."""
        raise NotImplementedError(
            'operation get_communication_paths(...) not yet implemented')


class ProtocolStateMachineMixin(object):
    """User defined mixin class for ProtocolStateMachine."""

    def __init__(self, conformance=None, **kwargs):
        super(ProtocolStateMachineMixin, self).__init__(**kwargs)

    def deep_or_shallow_history(self, diagnostics=None, context=None):
        """ProtocolStateMachines cannot have deep or shallow history Pseudostates.
region->forAll (r | r.subvertex->forAll (v | v.oclIsKindOf(Pseudostate) implies
((v.oclAsType(Pseudostate).kind <>  PseudostateKind::deepHistory) and (v.oclAsType(Pseudostate).kind <> PseudostateKind::shallowHistory))))"""
        raise NotImplementedError(
            'operation deep_or_shallow_history(...) not yet implemented')

    def entry_exit_do(self, diagnostics=None, context=None):
        """The states of a ProtocolStateMachine cannot have entry, exit, or do activity Behaviors.
region->forAll(r | r.subvertex->forAll(v | v.oclIsKindOf(State) implies
(v.oclAsType(State).entry->isEmpty() and v.oclAsType(State).exit->isEmpty() and v.oclAsType(State).doActivity->isEmpty())))"""
        raise NotImplementedError(
            'operation entry_exit_do(...) not yet implemented')

    def protocol_transitions(self, diagnostics=None, context=None):
        """All Transitions of a ProtocolStateMachine must be ProtocolTransitions.
region->forAll(r | r.transition->forAll(t | t.oclIsTypeOf(ProtocolTransition)))"""
        raise NotImplementedError(
            'operation protocol_transitions(...) not yet implemented')


class FunctionBehaviorMixin(object):
    """User defined mixin class for FunctionBehavior."""

    def __init__(self, **kwargs):
        super(FunctionBehaviorMixin, self).__init__(**kwargs)

    def one_output_parameter(self, diagnostics=None, context=None):
        """A FunctionBehavior has at least one output Parameter.
self.ownedParameter->
  select(p | p.direction = ParameterDirectionKind::out or p.direction= ParameterDirectionKind::inout or p.direction= ParameterDirectionKind::return)->size() >= 1"""
        raise NotImplementedError(
            'operation one_output_parameter(...) not yet implemented')

    def types_of_parameters(self, diagnostics=None, context=None):
        """The types of the ownedParameters are all DataTypes, which may not nest anything but other DataTypes.
ownedParameter->forAll(p | p.type <> null and
  p.type.oclIsTypeOf(DataType) and hasAllDataTypeAttributes(p.type.oclAsType(DataType)))"""
        raise NotImplementedError(
            'operation types_of_parameters(...) not yet implemented')

    def has_all_data_type_attributes(self, d=None):
        """The hasAllDataTypeAttributes query tests whether the types of the attributes of the given DataType are all DataTypes, and similarly for all those DataTypes.
result = (d.ownedAttribute->forAll(a |
    a.type.oclIsKindOf(DataType) and
      hasAllDataTypeAttributes(a.type.oclAsType(DataType))))
<p>From package UML::CommonBehavior.</p>"""
        raise NotImplementedError(
            'operation has_all_data_type_attributes(...) not yet implemented')


class DeviceMixin(object):
    """User defined mixin class for Device."""

    def __init__(self, **kwargs):
        super(DeviceMixin, self).__init__(**kwargs)


class ExecutionEnvironmentMixin(object):
    """User defined mixin class for ExecutionEnvironment."""

    def __init__(self, **kwargs):
        super(ExecutionEnvironmentMixin, self).__init__(**kwargs)


class InteractionMixin(object):
    """User defined mixin class for Interaction."""

    def __init__(self, lifeline=None, fragment=None, action=None,
                 formalGate=None, message=None, **kwargs):
        super(InteractionMixin, self).__init__(**kwargs)

    def not_contained(self, diagnostics=None, context=None):
        """An Interaction instance must not be contained within another Interaction instance.
enclosingInteraction->isEmpty()"""
        raise NotImplementedError(
            'operation not_contained(...) not yet implemented')


class AssociationClassMixin(object):
    """User defined mixin class for AssociationClass."""

    def __init__(self, **kwargs):
        super(AssociationClassMixin, self).__init__(**kwargs)

    def cannot_be_defined(self, diagnostics=None, context=None):
        """An AssociationClass cannot be defined between itself and something else.
self.endType()->excludes(self) and self.endType()->collect(et|et.oclAsType(Classifier).allParents())->flatten()->excludes(self)"""
        raise NotImplementedError(
            'operation cannot_be_defined(...) not yet implemented')

    def disjoint_attributes_ends(self, diagnostics=None, context=None):
        """The owned attributes and owned ends of an AssociationClass are disjoint.
ownedAttribute->intersection(ownedEnd)->isEmpty()"""
        raise NotImplementedError(
            'operation disjoint_attributes_ends(...) not yet implemented')
