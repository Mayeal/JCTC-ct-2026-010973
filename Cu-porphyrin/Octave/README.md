**Octave calculations**

Octave is a free and open-source substitute for MATLAB. The Octave scripts (\*.m) here are written in a way such that they should
work with MATLAB as well, but due to a lack of MATLAB license, we cannot verify this at the moment.
All Octave calculations were performed with Octave version 10.3.0 on a Windows machine.

- The various transition rates are manually compiled in the tables CuP-UTDDFT.csv and CuP-XTDDFT.csv.
Note that between these two files, only the IC rates differ; the ISC and fluorescence rates of CuP-UTDDFT.csv are computed using X-TDDFT.
- Run kinetic.m. This generates the X-TDDFT subfigure of Figure 7 directly.
- Uncomment the first line of kinetic.m, and comment out the second line, to generate the U-TDDFT subfigure of Figure 7.
