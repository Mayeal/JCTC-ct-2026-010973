function data = reorder_nacme(filename)
  data0 = csvread(filename);
  % if mapping(i)=j, the i-th BDF calculation corresponds to the j-th BAGEL calculation
  mapping = [4	5	1	3	7	2	6	23	10	19	11	20	15	16	25	27	9	13	22	14	18	28	8	24	26	12	21	17];
  % we reorder the BDF results to the BAGEL order
  data = zeros(size(data0));
  for i=1:28
    data(12*(mapping(i)-1)+1:12*mapping(i)) = data0(12*(i-1)+1:12*i);
  endfor
endfunction
