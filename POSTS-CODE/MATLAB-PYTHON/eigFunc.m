function [V,D] = eigFunc(A)
%returns diagonal matrix D of eigenvalues and matrix V 
% whose columns are the corresponding right eigenvectors, 
% so that A*V = V*D.
[V, D] = eig(A);
end

