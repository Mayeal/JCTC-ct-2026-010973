function data = fixsign(filename, refdata)
  % make the signs of the XMS-CASPT2 and TDDFT NACMEs as consistent as possible.
  % This guarantees that the theta angles in Fig. 2 are within 90 degrees.
  data = reorder_nacme(filename);
  for i=1:28
    inprod = dot(data(12*(i-1)+1:12*i),refdata(12*(i-1)+1:12*i));
    if inprod<0
      data(12*(i-1)+1:12*i) = -data(12*(i-1)+1:12*i);
    end
  end
end
