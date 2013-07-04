Force field builder for molecular and ionic liquids
===================================================

_[Agilio Padua](http://tim.univ-bpclermont.fr/apadua)_

_series of papers by A. Padua, J.N. Canongia Lopes et al. J Phys Chem
B (since 2004)_

Contents
--------

* `fftool.py`: python script to build simulation box of ionic or
    molecular liquids and their mixtures. Requires the Packmol software
    to create coordinates. Force field files are written in formats
    suitable for the LAMMPS or DL_POLY molecular dynamics packages.

* `il.ff`: Database of force field parameters for ions of several ionic
    liquids.

* `improper_im.dlp`: "Improper" dihedrals for the aromatic ring in
    imidazolium cations. Retrieved from the AMBER paper.

* `oplsaa.ff`: Database of OPLS-AA force field parameters for some
    molecular compouds. Retrieved from several publications of the
    W.L. Jorgensen group.

* `examples`: directory with some `molecule.zmat` files.


Requirements
------------

* [Python 2.7](http://www.python.org/)

* [Packmol](http://www.ime.unicamp.br/~martinez/packmol/)


Instructions
------------

How to build an initial configuration of a molecular or ionic system.

1. Prepare a file (`molecule.zmat`) containing a z-matrix describing
   each molecule. Check the Wikipedia entry for "Z-matrix
   (chemistry)". After the z-matrix a database of force field
   parameters (`database.ff`) must be supplied. See the `examples`
   directory. The connectivity (which atoms are linked by covalent
   bonds) is determined by the z-matrix. Cyclic molecules require
   additional `connect` records to close cycles (see the example for
   benzene).

2. Use the `fftool.py` script to create `.xyz` files for the molecules
   in your system and an input file for `packmol`. For help type
   `fftool.py -h`. To build a simulation box with 20 ion pairs and a
   density of 3.0 mol/L do:

        fftool.py 20 c4c1im.zmat 20 ntf2.zmat --rho 3.0

3. Use `packmol` with the `pack.inp` file just created to buid the
   simulation box (adjust the density if necessary):

        packmol < pack.inp

    Coordinates of will be written to the file `simbox.xyz`. You can
    use a molecular viewer such as RasMol or VMD to look at the `.xyz`
    files (fftool has an option to write the IUPAC atomic symbols
    instead of the atom names of the force field).

4. Use `fftool.py` to build the input files for LAMMPS or DL_POLY
   containing the force field parameters and the coordinates:

        fftool.py 20 c4c1im.zmat 20 ntf2.zmat --dlpoly


References
----------

* [Packmol](http://www.ime.unicamp.br/~martinez/packmol/):
  L. Martinez et al. J Comp Chem 30 (2009) 2157, DOI:
  [10.1002/jcc.21224](http://dx.doi.org/10.1002/jcc.21224) 
  
* [LAMMPS](http://lammps.sandia.gov/): S. Plimton, J Comp Phys
  117 (1995) 1, DOI:
  [10.1006/jcph.1995.1039](http://dx.doi.org/10.1006/jcph.1995.1039)

* [DL_POLY](http://www.stfc.ac.uk/CSE/randd/ccg/software/DL_POLY/25526.aspx): I.T. Todorov and W. Smith, Daresbury Lab. 

* IL force field: A.A.H. Padua, J.N. Canongia Lopes et al.
  J Phys Chem B 108 (2004) 2038, DOI:
  [10.1021/jp0362133](http://dx.doi.org/10.1021/jp0362133);
  J Phys Chem B 108 (2004) 11250, DOI:
  [10.1021/jp0476996](http://dx.doi.org/10.1021/jp0476996);
  J Phys Chem B 108 (2004) 16893, DOI:
  [10.1021/jp0476545](http://dx.doi.org/10.1021/jp0476545);
  J Phys Chem B 110 (2006) 19586, DOI:
  [10.1021/jp063901o](http://dx.doi.org/10.1021/jp063901o);
  J Phys Chem B 110 (2008) 5039, DOI:
  [10.1021/jp800281e](http://dx.doi.org/10.1021/jp800281e);
  J Phys Chem B 110 (2010) 3592, DOI:
  [10.1021/jp9120468](http://dx.doi.org/10.1021/jp9120468)

* OPLS-AA force field: W.L. Jorgensen et al. JACS 118 (1996) 11225,
  DOI: [10.1021/ja9621760](http://dx.doi.org/10.1021/ja9621760) 

* AMBER force field: P. Kollman et al. JACS 117 (1995) 5179, DOI:
  [10.1021/ja00124a002](http://dx.doi.org/10.1021/ja00124a002) 
