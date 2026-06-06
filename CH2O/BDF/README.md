**BDF calculations**

- Optimize the ground state geometry of the $CH_2O$ radical cation, by running CH2O-opt.inp using BDF. Output: CH2O-opt.optgeom (optimized coordinates in Bohr)
- Calculate NACMEs. Example input and output files for B3LYP are shown (CH2O-UTDDFT-B3LYP.inp and CH2O-XTDDFT-B3LYP.inp);
replacing B3LYP in the input files by SVWN5/BLYP/BHandHLYP gives the results of these functionals instead.
Comments have been added to CH2O-UTDDFT-B3LYP.inp to explain some important keywords;
for more detailed explanation, refer to the BDF manual (https://bdf-manual-en-new.readthedocs.io/en/latest/User%20Guide.html#calculation-of-the-first-order-non-adiabatic-coupled-matrix-element-fo-nacme).
The NACMEs with ETF contributions are given after "Gradient contribution from Final-NAC(S)-Escaled".
- Read the U-TDDFT and X-TDDFT state compositions from CH2O-[method]-[functional].out, after the occurrences of "w=".
The output is basically self-explanatory; for more information refer to the BDF manual (https://bdf-manual-en-new.readthedocs.io/en/latest/User%20Guide.html#time-dependent-density-functional-theory).
Note: for X-TDDFT, the double excitation contributions are not explicitly printed. Instead, one must (1) convert the spin-orbital basis compositions (CV(aa), CV(bb)) to the spin-adapted spin-tensor basis
(Eqs.(17-18)); (2) read out the "true" CV(aa), CV(bb) and CV\* contributions from Eq.(3).
Moreover, we choose the phase such that the excitation with the biggest contribution percentage has a positive coefficient.
- Run extract.sh. This extracts the NACME data and outputs them to CH2O-[method]-[functional]-result.csv.
