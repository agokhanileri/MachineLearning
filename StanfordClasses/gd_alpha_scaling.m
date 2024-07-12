clear all; clc;

% Shmoo
alphas  = 0.01: 0.01 :0.07;
iters   = 2: 1 : 200;

% Data
m = 10;                                 % # of trainings
n = 1;                                  % features (1 input only)
x   = 1:m;                          	% input
y   = [0.9 2.0 3.1 4.2 5.3 6.2 7.1 8.0 9.0 10.2]; 	% output

% GD
cnta = 1;
for alpha = alphas                      % learning rate (alpha
    cnti = 1;
    for iter = iters
        %J_temp = J;                     % save set of J for gradient plot
        a0 = zeros(1, iter); a1 = a0;
        a0(1) = -0.7; a1(1) = 0.8;     % start from somewhere, try =2,2 too
        for k = 2:iter
            J = 0;              % summation
            dJ_a0 = 0; dJ_a1 = 0;
            for i = 1:m
                h(i) = a0(k-1) + a1(k-1)*x(i);
                J = J + 1/(2*m)*(h(i)-y(i))^2;
                dJ_a0 = dJ_a0 + 1/m*(h(i)-y(i));
                dJ_a1 = dJ_a1 + 1/m*(h(i)-y(i))*x(i);
            end
            a0(k) = a0(k-1) - alpha*dJ_a0;     % sign didn't work
            a1(k) = a1(k-1) - alpha*dJ_a1;
        end
        Jmin(cnti, cnta) = J;
        cnti = cnti + 1;
    end
    cnta = cnta + 1;
end
[r, c] = size(Jmin);

figure()
plot(iters, Jmin)
hold on; grid on;
title('Impact of Alpha', 'FontSize', 12, 'FontWeight', 'bold')
ylabel('Jmin', 'FontSize', 12)
xlabel('iter', 'FontSize', 12)
ylim([-1, 1e1])
leg = legend(num2str(alphas(1)), num2str(alphas(2)),  num2str(alphas(3))); % make for loop
leg.FontSize = 11;
%legappend('asd')


%% Convergence
Jsettle = -1.5;         % convergence threshold dB  10^-2
fprintf(['GD settling within Jmin = ' num2str(Jsettle) 'dB:\n'])
Jconv = zeros(m, length(alphas));
for i = 1: length(alphas)
     i = 1
    Jconv = find(log10(Jmin(:, i)) <= Jsettle);        % make for loop      
    %iters(Jconv(i))
    if isempty(Jconv) ~= 1                             % converged at some point
        fprintf([' alpha = ' num2str(alphas(i)) ' --> converged first at ' num2str(iters(min(Jconv))) ' iters, '])
        if length(Jconv) == r-min(Jconv)                  % if all consevutive runs are within the band
            fprintf('stays converged.\n')
        else % last bit isn't settled yet: either diverging, or slow converging
            fprintf('but diverges at some point, ')
            if Jmin(end, i)> Jmin(1, i)                % it went even worse
                fprintf('including the final iter.\n')
            else
                fprintf('but converges back in the end.\n')
            end
        end       
    else
        fprintf([' alpha = ' num2str(alphas(i)) ' --> diverges fully.\n'])
    end    
end

% Jmin(20, 1) = 100     % manually divert to test
% As alpha increases, Tsettle decreases first, then increases back due to overshoot, then = inf.

% AI: implement iteration threshold within the settling band


%% Scaling + Normalization




