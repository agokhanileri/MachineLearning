clc; close all; clear all;


scrsz = get( groot, 'Screensize' );    	% 1680/1050
scrW = scrsz(3);  scrH = scrsz(4);

 
%% Data
x   = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5;  0.1: 0.1 :1]';
y   = [0.9 2.0 3.1 4.2 5.3 6.2 7.1 8.0 9.0 10.2]';

[m, n] = size(x);                       % features, trainings
X   = [ones(1, m)' x];                  % design matrix


%% Feature Scaling
% before
if det(X'*X) == 0;                      % check invertibility
    X(m,n) = X(m,n)+ 1;                 % close to singular --> Rcondition =? 
end
T 	= inv(X'*X)*X'*y;                   % normal equation
H   = X*T;                              % initial hypothesis
E   = H - y;                            % // error     
J   = sum(E.^2)/(2*m);                  % // (optimal) cost function

% after 
mu   = mean(X(:, 2:end));
sigma = std(X(:, 2:end));
% Xn = [ones(1,m)'  (  X(:, 2:end) - mu  )./sigma; % needs Matlab2016+
for i = 1:n
    if ~(sigma(i) == 0)
        X(:, i+1) = (X(:, i+1) - mu(i))/sigma(i);
    else 
        X(:, i+1) = (X(:, i+1) - mu(i));
    end
end
if det(X'*X) == 0;                      % check invertibility
    X(m,n) = X(m,n)+ 1;                 % close to singular --> Rcondition =? 
end
T   = inv(X'*X)*X'*y                    % normal eqn
H   = X*T;                           	% hypothesis set
E   = H - y;                            % errors for this H
J   = sum(E.^2)/(2*m)                   % resulting J


%% Weighted 








