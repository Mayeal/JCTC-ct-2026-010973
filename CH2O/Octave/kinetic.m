%filename = 'CuP(2)-UTDDFT.csv';
filename = 'CuP(2).csv';
data = csvread(filename);
data = data(2,:);

% Rate constants in s^(-1)
kIC = data(5);
kf = data(1);
kp = data(2);
kRISC = data(3);
kISC = data(4);

N = 10;
k = zeros(N); % D0, D1, Q1, dd1, dd2, dd3, dd4, fluor, phosp, D0(direct)
% k(final state, initial state) = rate
k(10,2) = kIC;
k(3,2) = kISC;
k(2,3) = kRISC;
k(1,4) = data(13);
k(1,5) = data(11);
% in principle, data(11)==data(12) due to point group symmetry
% however this is not exactly satisfied due to numerical error
% we enforce the equality so that the kinetic simulations are not
% affected by symmetry breaking
k(1,6) = data(11);%data(12);
k(1,7) = data(10);
k(4,2) = data(6);
k(5,2) = data(7);
k(6,2) = data(8);
k(7,2) = data(9);
k(5,7) = data(14);
% same comments as above...
k(6,7) = data(14);%data(15);
k(4,7) = data(16);
k(5,6) = data(17);
k(4,5) = data(18);
k(6,5) = data(19);%data(17);
k(4,6) = data(18);%data(20);
k(8,2) = kf;
k(9,3) = kp;

% set diagonal elements of k
for i=1:N
    k(i,i) = -sum(k(:,i));
end

% simulation
t = 10.^(-12:0.01:-4);
Nt = numel(t);
c = [0 1 0 0 0 0 0 0 0 0]'; % initial state - 100% D1
c_all = zeros(N,Nt);
for i=1:Nt
    c_all(:,i) = expm(k*t(i))*c;
end

% total product yield
tinf = 1000;
c_inf = expm(k*tinf)*c;
c_all(c_all<1e-16)=1e-16;

% plot
pl = loglog(1e12*t,c_all(1,:)+c_all(8,:)+c_all(9,:)+c_all(10,:),1e12*t,c_all(2,:),1e12*t,c_all(3,:),1e12*t,c_all(4,:),'--',...
    1e12*t,c_all(5,:),'--',1e12*t,c_all(6,:),'--',1e12*t,c_all(7,:),'--',1e12*t,c_all(8,:),':',1e12*t,c_all(9,:),':',...
    1e12*t,c_all(10,:),'-.',1e12*t,c_all(1,:),'-.');
axis([1e12*min(t) 1e12*max(t) 1e-11 2])
xlabel('Time (ps)')
ylabel('Relative concentration')
set(gca,'fontsize',20)
legend('^2S_0 (total)','^2T_1','^4T_1','^2dd_1','^2dd_2','^2dd_3','^2dd_4',...
    '^2S_0 (fluor)','^2S_0 (phosp)','^2S_0 (from ^2T_1)','^2S_0 (from ^2dd)',...
    'fontsize',14)
set(pl,'LineWidth',1)

yield = c_inf(8)+c_inf(9);
disp(sprintf('Total quantum yield: %f %%',yield*100))
disp(sprintf('Fluor/phosp ratio: %f',c_inf(8)/c_inf(9)))

% lifetime
for i=1:Nt
    if (c_all(8,i)+c_all(9,i))/yield > 1-exp(-1)
      break
    end
end
disp(sprintf('Lifetime: %f ns',1e9*(t(i)+t(i-1))/2))

disp(sprintf('Direct IC: %f %%',data(5)/sum(data(5:9))*100))
