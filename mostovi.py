from constraint import *

if __name__ == '__main__':

    problem = Problem()
    variables = range(0, 12) #0,1,2,3,4,5,6,7,8,9,10,11
    domain = range(0, 5) #0,1,2,3,4,5
    problem.addVariables(variables, domain)

    problem.addConstraint(ExactSumConstraint(2), [2])
    problem.addConstraint(ExactSumConstraint(2), [1])
    problem.addConstraint(ExactSumConstraint(5), [0,1,5])
    problem.addConstraint(ExactSumConstraint(2), [0,4])
    problem.addConstraint(ExactSumConstraint(1), [4,8,9])
    problem.addConstraint(ExactSumConstraint(1), [3])
    problem.addConstraint(ExactSumConstraint(4), [2,3,6])
    problem.addConstraint(ExactSumConstraint(5), [6,11,7])
    problem.addConstraint(ExactSumConstraint(4), [10,7])
    problem.addConstraint(ExactSumConstraint(3), [5,8,11])
    problem.addConstraint(ExactSumConstraint(3), [9,10])

    solution = problem.getSolution()
    print(solution)
