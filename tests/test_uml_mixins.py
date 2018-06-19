import pytest
from pyecore.ecore import BadValueError
from pyuml2.uml import Class, Property, Package, AggregationKind, Model


def test_owner():
    c = Class()
    p = Property()
    c.ownedAttribute.append(p)

    assert c.owner is None
    assert p.owner is c


def test_ownedElement():
    c = Class()
    p = Property()
    assert len(c.ownedElement) == 0

    c.ownedAttribute.append(p)
    assert p in c.ownedElement


def test_has_owner():
    c = Class()
    p = Property()
    c.ownedAttribute.append(p)
    assert c.has_owner() is False
    assert p.has_owner() is True


def test_all_owned_elements():
    p = Package()
    c = Class()
    sub = Package()
    p.packagedElement.append(sub)
    sub.packagedElement.append(c)

    assert len(list(p.all_owned_elements())) == 2
    assert c in p.all_owned_elements()
    assert sub in p.all_owned_elements()
    assert c in sub.all_owned_elements()
    assert c.not_own_self() is True


def test_create_EAnnotation():
    c = Class()
    assert c.eAnnotations == []

    annotation = c.create_EAnnotation(source='testsrc')
    assert annotation in c.eAnnotations
    assert annotation.source == 'testsrc'


# def test_delete():
#     c = Class()
#     p = Property()
#     c.ownedAttribute.append(p)
#     p.destroy()
#     assert c.ownedAttribute == []


def test_qualified_name():
    p = Package(name='p')
    c = Class(name='c')
    sub = Package(name='sub')
    p.packagedElement.append(sub)
    sub.packagedElement.append(c)

    assert c.qualifiedName == 'p::sub::c'


def test_class_superclass_derived():
    c1 = Class()
    c2 = Class()
    assert len(c1.superClass) == 0

    c1.superClass.append(c2)
    assert len(c1.superClass) == 1
    assert c2 in c1.superClass

    c1.superClass.remove(c2)
    assert len(c1.superClass) == 0

    c1.superClass.insert(0, c2)
    assert len(c1.superClass) == 1
    assert c2 in c1.superClass

    del c1.superClass[0]
    assert len(c1.superClass) == 0

    assert repr(c1.superClass)

    assert len(c1.get_super_classes()) == 0

    c1.get_super_classes().append(c2)
    assert c2 in c1.get_super_classes()
    assert c2 in c1.superClass


def test_property_iscomposite():
    p = Property()
    assert p.isComposite is False
    assert p.aggregation is not AggregationKind.composite

    p.isComposite = True
    assert p.isComposite is True
    assert p.aggregation is AggregationKind.composite
    assert p.is_composite() is True

    p.isComposite = False
    assert p.isComposite is False
    assert p.aggregation is not AggregationKind.composite
    assert p.is_composite() is False

    p.set_is_composite(True)
    assert p.isComposite is True
    assert p.aggregation is AggregationKind.composite
    assert p.is_composite() is True

    p.set_is_composite(False)
    assert p.isComposite is False
    assert p.aggregation is not AggregationKind.composite
    assert p.is_composite() is False


def test_package_nestedPackages():
    p1, p2 = Package(), Package()
    assert len(p1.nestedPackage) == 0

    p1.packagedElement.append(p2)
    assert len(p1.nestedPackage) == 1
    assert p2 in p1.nestedPackage
    assert p1.nestedPackage[0] is p2


def test_package_nestingPackage():
    p1, p2 = Package(), Package()
    assert p1.nestingPackage is None

    p2.nestingPackage = p1
    assert p2.nestingPackage is p1
    assert p2 in p1.packagedElement
    assert p2 in p1.nestedPackage

    p2.nestingPackage = None
    assert p2.nestingPackage is None
    assert p2 not in p1.packagedElement
    assert p2 not in p1.nestedPackage

    with pytest.raises(BadValueError):
        p1.nestingPackage = Class()


def test_element_get_model():
    m1, p1, c1 = Model(), Package(), Class()
    p1.packagedElement.append(c1)
    m1.packagedElement.append(p1)

    assert c1.get_model() is m1
    assert p1.get_model() is m1
    assert m1.get_model() is None


def test_element_get_nearesPackage():
    m1, p1, c1, prop1 = Model(), Package(), Class(), Property()
    c1.ownedAttribute.append(prop1)
    p1.packagedElement.append(c1)
    m1.packagedElement.append(p1)

    assert prop1.get_nearest_package() is p1
    assert c1.get_nearest_package() is p1
    assert p1.get_nearest_package() is m1
    assert m1.get_nearest_package() is None
