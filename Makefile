METAMODEL_DIRECTORY := 'pyuml2'

all:
	mkdir -p $(METAMODEL_DIRECTORY)
	rm -rf $(METAMODEL_DIRECTORY)/types
	python -m pyecoregen.cli -e model/types.ecore -o .
	mv types $(METAMODEL_DIRECTORY)/
	python generator/uml_generator.py
