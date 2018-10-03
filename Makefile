METAMODEL_DIRECTORY := 'pyuml2'

all: types uml standard

types:
	python -m pyecoregen.cli -e model/types.ecore -o $(METAMODEL_DIRECTORY)

standard:
	python generator/standard_generator.py

uml:
	python generator/uml_generator.py

sysml:
	python generator/sysml_generator.py
