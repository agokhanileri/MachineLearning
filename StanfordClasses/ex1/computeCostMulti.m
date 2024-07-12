function [J, dJ_theta]= computeCostMulti(X, y, theta)
%COMPUTECOSTMULTI Compute cost for linear regression with multiple variables
%   J = COMPUTECOSTMULTI(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
[m, n]  = size(X(:, 2:end));
dJ_theta = zeros(n+1, 1);
h = zeros(1,m);
for i = 1:m
    for j = 1:n
        h(i) = h(i) + theta(j)*X(i, j);    
    end
    J = J + 1/(2*m)*(h(i) - y(i))^2;
    dJ_theta(1) = dJ_theta(1) + (h(i)-y(i));
    for j = 1:n
        dJ_theta(j) = dJ_theta(j) + (h(i) - y(i))*X(i, j);
    end        	        
end
% =========================================================================

end
