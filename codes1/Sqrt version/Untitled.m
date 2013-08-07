
N=64;
L = pi;
h = L/N;
cstar = sqrt(tanh(1));
c = 0.95*cstar;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%
%%
%
%  space variable x and Fourier variable xi = k
%
%  coefficient w
%
%%
%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x = (h/2:h:L-h/2)';
xi = (0:1:N-1)';
ww = sqrt(2/N)*ones(N,1);
ww(1) = sqrt(1/N);
uini=0.015 - 0.1*cos(x);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%
%%
%
%  Compute differentiation matrix D_N^2 
%
%  and operator L
% 
%%
%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Tau=zeros(N);
for m=1:N;
   for n=1:N;
      Tau(m,n) = ww(1)*ww(1)*cos(x(n)*xi(1))*cos(x(m)*xi(1));
      for k=2:N;
      Tau(m,n) = Tau(m,n) + sqrt((1/xi(k))*tanh(xi(k)))*ww(k)*ww(k)*cos(x(n)*xi(k))*cos(x(m)*xi(k));
      end;
   end;
end;

ScriptL = -c*eye(N) + Tau;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%
%%
%
%  Newton loop
% 
%%
%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

u=uini;  
change = 2; it = 0;
% for nn=1:5;
% unew = 2*(u+1).^(3/2)-3*u-2;
%     u = unew 
% end;    


for kk=1:50;
    DFu = ScriptL + diag(3*(u+1).^(1/2)-3);          %square root test
     corr = -DFu\( ScriptL*u + 2*(u+1).^(3/2)-3*u-2);   %square root test
    unew = u + corr;
    change = norm(corr,inf)
    u = unew; 
end;

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %%%
% %%
% %
% %  Fixed Point Iterations
% % 
% %%
% %%%
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% u=uini;  

    
% it = it+1;
% end;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%
%%
%
%  Output
% 
%%
%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

out = u;