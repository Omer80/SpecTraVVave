# The file includes the solver class. 
# wave = solver(matrix, guess_vector) 
# wave.matrix = the matrix of the system bieng solved
# wave.guess = the initial guess with which the system is solved
# wave.compute() = the solution of the system
from __future__ import division

import numpy as np
import navigation
from scipy.optimize import fsolve


class solver(object):
    def __init__(self, Equation, guess):
        self.guess = guess
        self.equation = Equation

    def compute_fsolve(self):
       
        return fsolve(self.equation.residual, self.guess, fprime=self.equation.Jacobian)
        # in the case of fsolve being slow, it is to be replaced by Newton method 
        
    
    def compute_newton(self, c1, a1, c2, a2, tol=1e-12):
        u = self.guess
        N = self.equation.size
        
        nav = navigation.navigation(c1, a1, c2, a2)
        (c3, a3, alpha, beta, gamma) = nav.compute_line()                       # computing the init guess for (c, a) 
        
        #ah = np.zeros(N); ah[0] = 1; ah[-1] = -1
        #ch = np.zeros(N)
        #Vmatrix = np.vstack((self.equation.Jacobian(u), ah, ch))                   # adding 2 rows from below to Jacobian
        
        #av0 = np.zeros(N);                 cv0 = (-1)*np.ones(N)
        #av = np.hstack((av0,[-1,alpha]));      cv = np.hstack((cv0, [0, beta]))
        #Matrix = np.hstack((Vmatrix, av.reshape(N+2,1), cv.reshape(N+2,1)))        # adding 2 columns 
        
        for it in range(10000):

            #du = np.linalg.solve(self.equation.Jacobian(u),-self.equation.residual(u) )
            ah = np.zeros(N); ah[0] = 1; ah[-1] = -1
            ch = np.zeros(N)
            Vmatrix = np.vstack((self.equation.Jacobian(u), ah, ch))                   # adding 2 rows from below to Jacobian
        
            av0 = np.zeros(N);                 cv0 = (-1)*np.ones(N)
            av = np.hstack((av0,[-1,alpha]));      cv = np.hstack((cv0, [0, beta]))
            Matrix = np.hstack((Vmatrix, av.reshape(N+2,1), cv.reshape(N+2,1)))        # adding 2 columns
             
            du = np.linalg.solve(Matrix, np.hstack((-self.equation.residual(u), [u[0] - u[-1] - a3, alpha*a3 + beta*c3 + gamma])) )
            
            unew = u + du[:-2]
            cnew = c3 + du[-1]
            anew = a3 + du[-2]
            change = np.abs(du).max()
            u = unew
            a3 = anew
            c3 = cnew
            print it
            if change < tol:             # Newton iterative solver for the obtained system of equations
                break

        else:
            print 'Iterations\' limit reached: 10000'

            
        return (u, c3, a3)
