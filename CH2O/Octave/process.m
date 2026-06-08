% read XMS-CASPT2 NACMEs
refdata0 = csvread('result.csv');
refdata = zeros(12,8,8);
k=1;
for ii=1:8
  for jj=ii+1:8
    refdata(:,ii,jj) = refdata0(k:k+11);
    refdata(:,jj,ii) = -refdata0(k:k+11);
    k=k+12;
  end
end

method = {'UTDDFT','XTDDFT'};
func = {'SVWN5','BLYP','B3LYP','BHandHLYP'};

% read TDDFT NACMEs
dftdata = zeros(12,2,4,8,8);
for i=1:2
  for j=1:4
    filename = ['CH2O-' method{i} '-' func{j} '-result.csv'];
    data = fixsign(filename, refdata0);
    k=1;
    for ii=1:8
      for jj=ii+1:8
        dftdata(:,i,j,ii,jj) = data(k:k+11);
        dftdata(:,i,j,jj,ii) = -data(k:k+11);
        k=k+12;
      end
    end
  end
end

% calculate norms and angles
refnorms = zeros(8,8);
norms = zeros(8,8,2,4);
theta = zeros(8,8,2,4);
normMD = zeros(2,4);
normMAD = zeros(2,4);
thetaMAD = zeros(2,4);
normMaxD = zeros(2,4);
thetaMaxD = zeros(2,4);
refnormmean = 0;
for i=1:2
  for j=1:4
    for ii=1:8
      for jj=ii+1:8
        norms(ii,jj,i,j) = norm(dftdata(:,i,j,ii,jj))-norm(refdata(:,ii,jj));
        theta(ii,jj,i,j) = acos(dot(dftdata(:,i,j,ii,jj),refdata(:,ii,jj))...
          /norm(dftdata(:,i,j,ii,jj))/norm(refdata(:,ii,jj)))*180/pi;
        refnorms(ii,jj) = norm(refdata(:,ii,jj));
        if ii~=7 && jj~=7 % exclude 1A2 state
          normMD(i,j) = normMD(i,j) + norms(ii,jj,i,j);
          normMAD(i,j) = normMAD(i,j) + abs(norms(ii,jj,i,j));
          normMaxD(i,j) = max(normMaxD(i,j),abs(norms(ii,jj,i,j)));
          thetaMAD(i,j) = thetaMAD(i,j) + abs(theta(ii,jj,i,j));
          thetaMaxD(i,j) = max(thetaMaxD(i,j),abs(theta(ii,jj,i,j)));
          if i==1 && j==1 % to avoid double counting
            refnormmean = refnormmean + refnorms(ii,jj);
          end
        end
      end
    end
  end
end
normMD = normMD / 21;
normMAD = normMAD / 21;
thetaMAD = thetaMAD / 21;
refnormmean = refnormmean / 21;

% excitation energies
% first column: XMS-CASPT2
% other columns in order: U-SVWN5, X-SVWN5, U-BLYP, ...
ene0 = [3.934986993	4.2772	4.1903	3.9252	3.5409	4.2184	4.0872	3.7784	3.3023
5.271696756	5.272	5.3716	5.3774	5.3775	5.2319	5.2813	5.2447	5.1532
5.506724315	5.1726	5.5073	5.7642	6.1797	5.1251	5.4363	5.6951	6.1632
6.253461464	6.5	6.3932	6.5335	6.5792	6.4767	6.3316	6.4218	6.9859
7.983539421	7.0858	6.7386	6.6567	7.1268	7.9771	7.6666	7.6378	7.6731
9.617708369	8.5768	8.5708	8.8339	9.172	9.4168	9.462	9.7187	10.0869
9.875591813	9.6162	9.4194	9.2571	9.0111	9.8111	9.7303	9.6486	9.5212
];
ene0 = ene0/27.2113834;
refene = [0;ene0(:,1)];
dftene = zeros(2,4,8);
k=2;
for i=1:2
  for j=1:4
    dftene(i,j,:) = [0;ene0(:,k)];
    k=k+1;
  end
end

% output to file
outname = 'norms.csv';
csvwrite(outname,refnorms);
for i=1:2
  for j=1:4
    csvwrite(outname,norms(:,:,i,j),'append','on');
  end
end
for i=1:2
  for j=1:4
    csvwrite(outname,theta(:,:,i,j),'append','on');
  end
end
