Force field for ionic liquids
=============================

[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.18619.svg)](http://dx.doi.org/10.5281/zenodo.18619)

_[Agilio Padua](http://tim.univ-bpclermont.fr/apadua)_

_series of papers by A. Padua, J.N. Canongia Lopes et al. J Phys Chem
B (since 2004)_

Contents
--------

* `il.ff`: database of force field parameters for ions of several
    ionic liquids (under construction, compatible with the
    [fftool](http://www.github.com/agiliopadua/fftool) script to
    create input files for molecular simulation using the
    [LAMMPS](http://lammps.sandia.gov/) or
    [DL_POLY](http://www.stfc.ac.uk/CSE/randd/ccg/software/DL_POLY/25526.aspx)
    molecular dynamics codes.

* `old.il.ff`: database of force field parameters for ions of several ionic
    liquids (previous format, complete with many ions).

* `*.zmat, *.mol, *.xyz`: input files for ions.

* `topologies`: topology files in gromacs format for pyridinium and
  pyrrolidinium ionic liquids, with refined parameters for better
  representation of transport properties. Contributed by Vitaly
  Chaban.


Requirements
------------

* [fftool](http://www.github.com/agiliopadua/fftool)

* [Python 2.7](http://www.python.org/)

* [Packmol](http://www.ime.unicamp.br/~martinez/packmol/)


Obtaining
---------

Download the files or else clone the repository (easier to stay updated):

    git clone https://github.com/agiliopadua/ilff.git


How to use
----------

How to build an initial configuration of a molecular or ionic system.

1. For each molecule, ion or fragment of a material prepare a file
   with atomic coordinates and/or connectivity (covalent bonds). The
   formats accepted by this tool are `.zmat`, `.mol` or
   `.xyz`. Detailed information is available in the
   [fftool](http://www.github.com/agiliopadua/fftool) page.


2. Use the `fftool` script to create `.xyz` files for the molecules
   in your system and an input file for
   [Packmol](http://www.ime.unicamp.br/~martinez/packmol/). For help
   type `fftool -h`. For example, to build a simulation box with 20
   ion pairs and a density of 3.0 mol/L do:

        fftool 20 c4c1im.zmat 20 ntf2.zmat --rho 3.0

3. Use Packmol with the `pack.inp` file just created to buid the
   simulation box (adjust the density if necessary):

        packmol < pack.inp

    Atom coordinates will be written to a file `simbox.xyz`. You can
    use a molecular viewer such as VMD to look at the `.xyz` files.

4. Use `fftool` to build the input files for LAMMPS or DL_POLY
   containing the force field and the coordinates:

        fftool 20 c4c1im.zmat 20 ntf2.zmat --lammps

Information on the force field file format and on more geeral or
advanced used is available at the
[fftool](http://www.github.com/agiliopadua/fftool) page.


References
----------

* [Packmol](http://www.ime.unicamp.br/~martinez/packmol/):
  L. Martinez et al. J Comp Chem 30 (2009) 2157, DOI:
  [10.1002/jcc.21224](http://dx.doi.org/10.1002/jcc.21224) 

* [LAMMPS](http://lammps.sandia.gov/): S. Plimton, J Comp Phys
  117 (1995) 1, DOI:
  [10.1006/jcph.1995.1039](http://dx.doi.org/10.1006/jcph.1995.1039)

* [DL_POLY](http://www.stfc.ac.uk/CSE/randd/ccg/software/DL_POLY/25526.aspx):
  I.T. Todorov and W. Smith, Daresbury Lab.

* IL force field: J.N. Canongia Lopes, A.A.H. Padua et al.
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
