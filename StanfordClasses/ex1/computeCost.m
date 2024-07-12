function [J, dJ_theta]= computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples
J = 0;

% ====================== YOUR CODE HERE ======================
dJ_theta = [0, 0]';
h = zeros(1,m);
for i = 1:m 
    h(i) = theta(1)*X(i,1) + theta(2)*X(i,2);
    J = J + 1/(2*m)*(h(i) - y(i))^2;
	dJ_theta(1) = dJ_theta(1) + (h(i)-y(i));
	dJ_theta(2) = dJ_theta(2) + (h(i)-y(i))*X(i,2);
end
% =========================================================================

end
