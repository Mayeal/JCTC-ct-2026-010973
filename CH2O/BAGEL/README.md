**BAGEL calculations**

After optimizing the geometry of the $CH_2O$ radical cation by BDF, the following operations are performed in order:

- Generate the converged CASSCF orbitals, by running CH2O-activespace.json. This generates CH2O.casscf.molden.
- Read CH2O.casscf.molden as initial guess, and perform XMS-CASPT2 NACME calculations.
As an example, to calculate the ground state-first excited state NACME, one runs CH2O-nacme-0-1.json.
The CASSCF state compositions (rotated by the XMS-CASPT2 rotation matrix) are found after the sections starting with "\* ci vector",
immediately after the occurrence of "Extended multi-state CASPT2 (XMS-CASPT2) rotation matrix" in the output file.
Refer to the comments in CH2O-nacme-0-1.json for how to calculate the NACMEs between other pairs of states.
- Run extract.sh, generating result.csv. This is a collection of all NACME data between all pairs of states,
which are then processed by our Octave script (see ../Octave/README.md).
