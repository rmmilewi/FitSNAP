import importlib

def test_LAMMPS_canImportPackage():
	lammpsPackage = importlib.import_module("lammps")

def test_LAMMPS_canInstantiateInstance():
	lammpsPackage = importlib.import_module("lammps")
	lmps = lammpsPackage.lammps()

def test_LAMMPS_instanceHasExceptionsFlagAttribute():
	"""
	Older versions of lammps.py do not define a 'has_exceptions' attribute, and
	FitSNAP attempts to access this attribute directly to check for that capability,
	which can cause an AttributeError.

	This is a sanity check to make sure that whatever version of LAMMPS we have has
	a Python interface that matches FitSNAP's expectations. 
	"""
	lammpsPackage = importlib.import_module("lammps")
	lmps = lammpsPackage.lammps()
	assert(hasattr(lmps, 'has_exceptions'))

