======================================================
PyUML2: A Pythonic Implementation of the UML Metamodel
======================================================

|master-build| |coverage| |license|

.. |master-build| image:: https://travis-ci.org/pyecore/pyuml2.svg?branch=master
    :target: https://travis-ci.org/pyecore/pyuml2

.. |coverage| image:: https://coveralls.io/repos/github/pyecore/pyuml2/badge.svg?branch=master
    :target: https://coveralls.io/github/pyecore/pyuml2?branch=master

.. |license| image:: https://img.shields.io/badge/license-New%20BSD-blue.svg
    :target: https://raw.githubusercontent.com/pyecore/pyuml2/master/LICENSE

PyUML2 is an implementation of the UML2 metamodel for Python 2.7, >=3.4,
relying on PyEcore. The goal of this project is to provide an almost-full
implementation of the UML-2.5 standard in Python with Profile support and
compatibility with the Eclipse UML2 project.


Installation
============

There is not yet a pypi package, you can manually install the project using:

.. code-block:: shell

    $ pip install -e .

Documentation
=============

Here is how to load a UML2 model using the implementation.

.. code-block:: python

    from pyecore.resources import ResourceSet
    import pyuml2.uml as uml

    rset = ResourceSet()
    rset.metamodel_registry[uml.nsURI] = uml
    resource = rset.get_resource('path/to/my/model.uml')
    model = resource.contents[0]

    print(model.name)
    print(model.packagedElement)
    print(model.nestedPackage)


Project State
=============

Available:

* Generated UML2 Metamodel (using the awesome `pyecoregen <https://github.com/pyecore/pyecoregen>`_)
* Generated Type Metamodel (used by the UML2 metamodel)
* Some derived features implementation

On the roadmap:

* Add default primitive type library
* Derived features implementation
* Profiles support

  * Open an existing Profile (currently, partially supported, some cross-refs are not resolved)
  * Create Metamodel References
  * Define a Profile (as it is done in Eclipse UML2)
  * Apply a Profile
  * Open a profiled Model
  * Apply a Stereotype

Liberties Regarding the Eclipse implementation
==============================================

The project goal is to be compatible with the Eclipse UML implementation, but it
still takes some liberties:

* the Eclipse implementation pluralizes the name of features when required during
  the code generation. For example, the ``packagedElement`` on ``Package`` in
  the ``UML.ecore`` metamodel is singular, but the code Eclipse Implementation
  pluralizes it as ``packagedElements``. PyUML2 does not perform this
  pluralization (at least not now).

Tests
=====

The project is configured to be used with ``tox``, so, you only need to run:

.. code-block:: shell

    $ tox

Contributing
============

All contributions are welcome and are really appreciated. The project is brand
new so there is a currently a lot to do. If you want to add the implementation
of new derived features or method implementations, the blueprint of each method
and feature is located in the ``pyuml2/uml_mixins.py`` module and can be filled.

There are some examples that can help you tame the code and show how to add a
dedicated implementation. The more representative are:

* the ``isComposite`` methods in the ``PropertyMixin`` class for "non-many" feature
* the ``DerivedSuperclass`` class for "many" feature (manages ``.superClass`` for ``Class``)

Obviously, for each added implementation, a test should be written.
