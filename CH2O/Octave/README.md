**Octave calculations**

Octave is a free and open-source substitute for MATLAB. The Octave scripts (\*.m) here are written in a way such that they should
work with MATLAB as well, but due to a lack of MATLAB license, we cannot verify this at the moment.
All Octave calculations were performed with Octave version 10.3.0 on a Windows machine.

- After obtaining result.csv (from BAGEL) and CH2O-[method]-[func]-result.csv (from BDF), run process.m in Octave.
This generates norms.csv, containing the norms of the XMS-CASPT2 NACMEs, the norm errors of the U-TDDFT and X-TDDFT NACMEs,
as well as the angles between the U/X-TDDFT NACMEs with the XMS-CASPT2 NACMEs.
Note that process.m relies on fixsign.m (fix the global signs of the NACMEs to make the XMS-CASPT2 and TDDFT NACMEs
more comparable) and reorder\_nacme.m (reorder the raw NACME data so that the XMS-CASPT2 and TDDFT NACMEs have the
same order, and can be directly compared with each other).
- Manually reformat norm.csv into norm.xlsx, from which Figures 1-2 were prepared.

