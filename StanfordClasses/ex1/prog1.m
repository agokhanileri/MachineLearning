clear all; clc

data = load('ex1data1.txt'); % read comma separated data
x   = data(:, 1);           % city pop
y   = data(:, 2);           % revenue from that city
m   = length(y);

% plot(x, y, 'rx', 'MarkerSize', 10);
% ylabel('Profit in $10,000s');
% xlabel('Population of City in 10,000s')

X = [ones(m, 1), x];    % Add a column of ones to x
theta = zeros(2, 1);            % initialize fitting parameters
iterations = 1500;
alpha = 0.01;


J_history = zeros(iterations, 1);
dJ_theta(1) = 0;        % J(theta(1))'
dJ_theta(2) = 0;

for iter = 1:iterations
    % Save the cost J in every iteration 
    dJ_theta(1) = 0;        % J(theta(1))'
    dJ_theta(2) = 0;        %
    J = 0;
    for i = 1:m 
        h(i) = theta(1)*X(i,1) + theta(2)*X(i,2);
        J = J + 1/(2*m)*(h(i) - y(i))^2;
        dJ_theta(1) = dJ_theta(1) + (h(i)-y(i));
        dJ_theta(2) = dJ_theta(2) + (h(i)-y(i))*X(i,2);
    end
    J_history(iter) = J;        
    %theta(1) = theta(1) + alpha*(J_history(iter+1) - J_history(iter))
 	%theta(2) = theta(2) + alpha*(J_history(iter+1) - J_history(iter))
    theta(1) = theta(1) - alpha/m*dJ_theta(1)
    theta(2) = theta(2) - alpha/m*dJ_theta(2)    
    %theta(1) = theta(2) - sqrt(2*J_history(iter)/m)            
end



%token = '2EhF2cSGkNIn00L2';
%addpath('C:\Users\atpde\Dropbox\Code\Matlab\dsml\andrew\ex1')
%addpath('C:\Users\atpde\Dropbox\Code\Matlab\dsml\andrew\ex1\lib')
%addpath(genpath('code_folder_path'))
%submit