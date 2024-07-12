function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters
    % Save the cost J in every iteration   
    %dJ_theta = [0, 0]';
    [J, dJ_theta] = computeCostMulti(X, y, theta);
    J_history(iter) = J;
    theta = theta - alpha/m*dJ_theta;
end

end
