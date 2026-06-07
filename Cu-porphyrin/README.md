**Rate Calculation Workflow**

IC

- The equilibrium geometries, Hessian matrices, and NACMEs were obtained using BDF.
- Use the scripts in BDF/scripts to convert BDF output files into MOMAP-compatible input files.  
  For example:    
  python extract-hessian.py cup-2T1-opt-freq.out $\rightarrow$ hessian_2t1.out   
  python extract-nacme.py cup-2t1-2dd1-XTDDFT.out $\rightarrow$ nacme.out
- Use MOMAP to calculate IC rates.   

  The workflows for fluorescence calculations are analogous to that described above for IC calculations.  
  Detailed instructions for MOMAP calculations can be found on the official MOMAP website: http://www.momap.net.cn/

ISC and RISC

  ISC and RISC rates were calculated using ORCA. 
  The ORCA directory contains the input and output files for the rate calculations, together with the source output files used to extract the SOCMEs and Ead.