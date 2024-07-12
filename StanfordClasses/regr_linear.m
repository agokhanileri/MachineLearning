% cd /Users/gokhanileri/Dropbox/Code/Matlab
clc; close all; clear all;
scrsz = get( groot, 'Screensize' );            % 1680/1050
scrW = scrsz(3);  scrH = scrsz(4);

% Data
m = 10;                                 % # of trainings
n = 1;                                  % features (1 input only)
x   = 1:m;                          	% input
y   = [0.9 2.0 3.1 4.2 5.3 6.2 7.1 8.0 9.0 10.2]; 	% output


%% Case 1: a0 = 0 (2D)
clear h J;
a0  = 0;  
a1_sweep = 0.5: 0.05 :1.5;
k   = 1;
for a1 = 0.5: 0.05 :1.5
    J(k) = 0;
    for i = 1:m                                         % for each h, evaluate J(a0, a1)
        h(i) = a0 + a1*x(i);            % hypothesis
        J(k) = J(k) + 1/(2*m)*(h(i)-y(i))^2; % /2 for convention
    end
    k = k+1;
end
[Jmin, a1opt] = min(J);
fprintf('1) No a0: ')
fprintf([' hopt = ' num2str(a0) ' + ' num2str(a1_sweep(a1opt)) 'x --> Jmin = ' num2str(Jmin) '\n\n'])
%%%%

f = figure();
set(f, 'Name', 'Linear Regression', 'Position', [0  scrH/10*2 scrW/10*5 scrH/10*6])
 subplot(2,3, 1)
p = plot(a1_sweep, J, 'o-b', 'LineWidth', 2);
p.MarkerFaceColor = p.Color;                            % to will the circles with the same color
hold on; grid on;
title('Case 1: a0 = 0', 'FontSize', 12, 'FontWeight', 'bold')
xlabel('a1', 'FontSize', 12)
ylabel('J', 'FontSize', 12)
 subplot(2,3, 4)
p = plot(x, y, 'ob', 'LineWidth', 1);
p.MarkerFaceColor = p.Color;
hold on; grid on;
plot(x, a0 + a1_sweep(a1opt)*x, '-r', 'LineWidth', 2) 
title('Double Check', 'FontSize', 12, 'FontWeight', 'bold')
xlabel('x', 'FontSize', 12)
ylabel('y', 'FontSize', 12)
legend('training set', 'best h', 'Location', 'North')


%% Case 2: a0 ~= 0 but fixed (2D)
clear h J;
a0  = -1;
k   = 1;
for a1 = 0.5: 0.05 :1.5;                             
    J(k) = 0;
    for i = 1:m                                         % for each h, evaluate J(a0, a1)
        h(i) = a0 + a1*x(i);            % hypothesis
        J(k) = J(k) + 1/(2*m)*(h(i)-y(i))^2; % /2 for convention
    end
    k = k + 1;
end
[Jmin, a1opt] = min(J);
fprintf('2) Constant a0: ')
fprintf([' hopt = ' num2str(a0) ' + ' num2str(a1_sweep(a1opt)) 'x --> Jmin = ' num2str(Jmin) '\n\n'])
%%%
 subplot(2,3, 2)
p = plot(a1_sweep, J, 'o-b', 'LineWidth', 2);
p.MarkerFaceColor = p.Color;
hold on; grid on;
title(['Case 2: a0 = ' num2str(a0)], 'FontSize', 12, 'FontWeight', 'bold')
xlabel('a1', 'FontSize', 12)
ylabel('J', 'FontSize', 12)
 subplot(2,3, 5)
p = plot(x, y, 'ob', 'LineWidth', 1);
p.MarkerFaceColor = p.Color;
hold on; grid on;
plot(x, a0 + a1_sweep(a1opt)*x, '-r', 'LineWidth', 2) 
title('Double Check', 'FontSize', 12, 'FontWeight', 'bold')
xlabel('x', 'FontSize', 12)
ylabel('y', 'FontSize', 12)
legend('training set', 'best h', 'Location', 'North')


%% Case 3: a0 variable (3D)
clear h J;
a0_sweep = -1 : 0.2 : 1;
a1_sweep = 0.5: 0.1 :1.5;
a0_cnt = 1;
Jmin = 1000;
for a0 = -1 : 0.2 : 1
    a1_cnt = 1;
    for a1 = 0.5: 0.1 :1.5         % can use repmat too
        J(a0_cnt, a1_cnt) = 0;
        for i = 1:m                                         % for each h, evaluate J(a0, a1)
            h(i) = a0 + a1*x(i);            % hypothesis
            J(a0_cnt, a1_cnt) = J(a0_cnt, a1_cnt) + 1/(2*m)*(h(i)-y(i))^2;           
        end
        if J(a0_cnt, a1_cnt) < Jmin
            a0_opt = a0;
            a1_opt = a1;
            Jmin = J(a0_cnt, a1_cnt);
        end
        %J(a0_cnt, a1_cnt)
        a1_cnt = a1_cnt + 1;
    end
    a0_cnt = a0_cnt + 1;
end
% size(J)
fprintf('3) Variable a0: ')
fprintf([' hopt = ' num2str(a0_opt) ' + ' num2str(a1_opt) 'x --> Jmin = ' num2str(Jmin) '\n\n'])

 subplot(2,3, 3)
contour(a0_sweep, a1_sweep, J, length(a0_sweep)*length(a1_sweep))
hold on; grid on;
title('Case 3: a0 varies', 'FontSize', 12, 'FontWeight', 'bold')
xlabel('a1', 'FontSize', 12)
ylabel('a0', 'FontSize', 12)
colormap('jet');
clb = colorbar('eastoutside');
set(get(clb,'title'),'string','J', 'FontSize', 12, 'FontWeight', 'bold');
% surf(a0_sweep, a1_sweep, J); % surface plot
% hold on; grid on;
% title('Surface Plot', 'FontSize', 12, 'FontWeight', 'bold')
% xlabel('a0', 'FontSize', 12)
% ylabel('a1', 'FontSize', 12)
% zlabel('J', 'FontSize', 12) 
% colormap('jet');        
% clb = colorbar('eastoutside');     % add color bar title
% set(get(clb,'title'),'string','J', 'FontSize', 12, 'FontWeight', 'bold');
 subplot(2,3, 6)
p = plot(x, y, 'ob', 'LineWidth', 1);
p.MarkerFaceColor = p.Color;
hold on; grid on;
plot(x, a0_opt + a1_opt*x, '-r', 'LineWidth', 2) 
title('Double Check', 'FontSize', 12, 'FontWeight', 'bold')
xlabel('x', 'FontSize', 12)
ylabel('y', 'FontSize', 12)
legend('set', 'hopt', 'Location', 'North')


%% Case 4: Gradient Descent
J_temp = J;                     % save set of J for gradient plot
alpha = 0.02;                      % learning rate (alpha), diverges with 0.1 res
runs = 400;                     % learning steps 
a0 = zeros(1, runs); a1 = a0;
a0(1) = -0.7; a1(1) = 0.8;     % start from somewhere, try =2,2 too
for k = 2:runs
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
fprintf('4) Gradient Descent: ')
fprintf([' hinit = ' num2str(a0(1)) ' + ' num2str(a1(1)) 'x, alpha = ' num2str(alpha) ', runs = ' num2str(runs) '\n'])
fprintf([' hopt = ' num2str(a0(end)) ' + ' num2str(a1(end)) 'x --> Jmin = ' num2str(J) '\n\n'])
%%%
f = figure();
set(f, 'Name', 'Gradient Descent', 'Position', [scrW/10*2  scrH/10*2 scrW/10*3 scrH/10*7])
 subplot(2,2, [1 2])
plot(1:runs, a0, '-b', 'LineWidth', 2) 
hold on; grid on;
plot(1:runs, a1, '-r', 'LineWidth', 2)
title('Case 4: Gradient Descent', 'FontSize', 12, 'FontWeight', 'bold')
ylabel('h(a0, a1)', 'FontSize', 12)
xlabel('runs', 'FontSize', 12)
legend('a0', 'a1', 'Location', 'NorthEast')
 subplot(2,2, [3 4])
contourf(a0_sweep, a1_sweep, J_temp, 20);
hold on; grid on;
colormap('jet');
title('Gradient on Contour', 'FontSize', 12, 'FontWeight', 'bold')
xlabel('a0', 'FontSize', 12)
ylabel('a1', 'FontSize', 12)
clb = colorbar('eastoutside');
set(get(clb,'title'),'string','J', 'FontSize', 12, 'FontWeight', 'bold');
for i = 1:1:runs-1
    pt1 = [a0(i), a1(i)];
    pt2 = [a0(i+1), a1(i+1)];
    dp = pt2 - pt1;
    p = quiver(pt1(1),pt1(2),dp(1),dp(2),0,'r','LineWidth', 2);  
    set(get(get(p,'Annotation'),'LegendInformation'),'IconDisplayStyle','off');
end
p = quiver(pt1(1),pt1(2),dp(1),dp(2),0,'r','LineWidth', 2);  
p3 = plot(a0(1), a1(1), '.y', 'MarkerSize', 25); 
p4 = plot(a0(end), a1(end), '.y', 'MarkerSize', 25); 
legend('J', 'h(a0, a1)', 'start', 'finish', 'Location', 'NorthEast')


%% Case 5: Normal Equation
X   = [ones(1, m)', x'];    % design matrix 
Y   = y'; 

% traceA = sum of diagonals ==> commutative + associative for multiplication
% trA = trA'
% f(A) = traceAB --> Gradient wrt A of trAB = B'
% Gradient wrt A of trABA'C = CAB + C'AB' (tricky one)
% Q = inv(X'X)*X' * Y
% if X'X isn't invertible, then you probably have repeating I/O

A = inv(X'*X)*X'*Y;             % normal equation
Agd = [a0(end), a1(end)]';       % found with grad. descent
Adelta = (A-Agd)/Agd;            % deviation minimal for all a's

i = 4;
hh(i) = A'*[1; i];     % = h(x) = A'*x

X

J = [];
for i = 1:m
    H(i) = A'* [1 x(i)]';           % continue to calc H(x)
    J(i) = J(i-1) + 1/(2*m)*(H(i)-y(i))^2;
end
Hdelta = Y - H';                 % deviation from output is minimal

fprintf('5) Normal Equation: ')
fprintf([' hopt = ' num2str(A(1,1)) ' + ' num2str(A(2,1)) 'x --> Jmin = ' num2str(Jmin) '\n\n'])
% no need to choose alpha, no need to iterate, no need for feature scaling
% but slow if n is large mainly due to (X'*X) is n by n --> O(n^3) complexity
% for n > 10e3, switch to GD

% if (X'*X) is singular or degenerate
  % a) if some n are linearly dependen, same but with different scale
  % b) n >=m --> delete some n, or regularize!  
