from searching_framework.utils import Problem
from searching_framework.informed_search import astar_search
from searching_framework.uninformed_search import *


def getManhattanDistance(pacman_x, pacman_y, x, y):
    return abs(pacman_x - x) + abs(pacman_y - y)

def compare_two_lists(current_state, final_state):
    for item in current_state:
        if item not in final_state:
            return False
    return True

def isValid(new_pacman, yellow_pacmans, green_pacmans):
    if new_pacman not in yellow_pacmans and new_pacman not in green_pacmans and 1 <= new_pacman[0] <= n and 1 <= new_pacman[1] <= m:
        return True
    return False

class Pacman(Problem):

    def __init__(self,m, n,zolti_final,zeleni_final, initial, goal=None):
        super().__init__(initial, goal)
        self.m = m
        self.n = n
        self.zolti_final = zolti_final
        self.zeleni_final = zeleni_final

    def successor(self, state):
        succesors = {}
        yellow_pacmans = state[0]
        green_pacmans = state[1]

        #DVIZENJE NA ZOLTI PACMANI
        yellowpacman_number = 1
        for pacman in yellow_pacmans:
            pacman_name = 'Zolt Pacman #' + str(yellowpacman_number)
            #DVIZENJE DESNO ZA ZOLT PACMAN
            for i in range(1,n):
                new_pacman = [pacman[0]+i,pacman[1]]
                if isValid(new_pacman, yellow_pacmans, green_pacmans):
                    key = pacman_name + ' ' + str(i) + ' vo desno'
                    succesors[key] = (tuple([new_pacman if pman==pacman else pman for pman in yellow_pacmans]), green_pacmans)

            #DVIZENJE DOLU ZA ZOLT PACMAN
            for i in range(1,m):
                new_pacman = [pacman[0],pacman[1]-i]
                if isValid(new_pacman, yellow_pacmans, green_pacmans):
                    key = pacman_name + ' ' + str(i) + ' nadolu'
                    succesors[key] = (tuple([new_pacman if pman==pacman else pman for pman in yellow_pacmans]), green_pacmans)

            #DVIZENJE LEVO ZA ZOLT PACMAN
            for i in range(1,n):
                new_pacman = [pacman[0]-i,pacman[1]]
                if isValid(new_pacman, yellow_pacmans, green_pacmans):
                    key = pacman_name + ' ' + str(i) + ' vo levo'
                    succesors[key] = (tuple([new_pacman if pman==pacman else pman for pman in yellow_pacmans]), green_pacmans)

            #DVIZENJE NAGORE ZA ZOLT PACMAN
            for i in range(1,m):
                new_pacman = [pacman[0],pacman[1]+i]
                if isValid(new_pacman, yellow_pacmans, green_pacmans):
                    key = pacman_name + ' ' + str(i) + ' nagore'
                    succesors[key] = (tuple([new_pacman if pman==pacman else pman for pman in yellow_pacmans]), green_pacmans)

            yellowpacman_number = yellowpacman_number + 1

        #DVIZENJE NA ZELENI PACMANI
        greenpacman_number = 1
        for pacman in green_pacmans:
            pacman_name = 'Zelen Pacman #' + str(greenpacman_number)
            #DVIZENJE DESNO ZA ZELEN PACMAN
            for i in range(1,n):
                new_pacman = [pacman[0]+i,pacman[1]]
                if isValid(new_pacman, yellow_pacmans, green_pacmans):
                    key = pacman_name + ' ' + str(i) + ' vo desno'
                    succesors[key] = (yellow_pacmans,tuple([new_pacman if pman==pacman else pman for pman in green_pacmans]))

            #DVIZENJE DOLU ZA ZELEN PACMAN
            for i in range(1,m):
                new_pacman = [pacman[0],pacman[1]-i]
                if isValid(new_pacman, yellow_pacmans, green_pacmans):
                    key = pacman_name + ' ' + str(i) + ' nadolu'
                    succesors[key] = (yellow_pacmans,tuple([new_pacman if pman==pacman else pman for pman in green_pacmans]))

            #DVIZENJE LEVO ZA ZELEN PACMAN
            for i in range(1,n):
                new_pacman = [pacman[0]-i,pacman[1]]
                if isValid(new_pacman, yellow_pacmans, green_pacmans):
                    key = pacman_name + ' ' + str(i) + ' vo levo'
                    succesors[key] = (yellow_pacmans,tuple([new_pacman if pman==pacman else pman for pman in green_pacmans]))

            #DVIZENJE NAGORE ZA ZELEN PACMAN
            for i in range(1,m):
                new_pacman = [pacman[0],pacman[1]+i]
                if isValid(new_pacman, yellow_pacmans, green_pacmans):
                    key = pacman_name + ' ' + str(i) + ' nagore'
                    succesors[key] = (yellow_pacmans,tuple([new_pacman if pman==pacman else pman for pman in green_pacmans]))

            yellowpacman_number = yellowpacman_number + 1

        return succesors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return compare_two_lists(state[0], zolti_final) and compare_two_lists(state[1], zeleni_final)



    def h(self,node):
        state = self.state
        x,y = state[0] #x,y na pakmanot koj go sledime
        goal_coordinates = state[1] #lista od koordinati [x1,y1] koi bi sakale da gi dostigneme so x,y
        M,N = state[2] #M broj na redovi i N broj na koloni
        minimum_distance = M+N
        for coordinates in goal_coordinates:
            current_distance = getManhattanDistance(x,y,coordinates[0],coordinates[1])
            if current_distance < minimum_distance:
                minimum_distance = current_distance
        return minimum_distance




if __name__ == '__main__':
    m = int(input())
    n = int(input())
    k = m // 2
    zolti_initial = list()
    zeleni_initial = list()
    yellow_shifting_digit = k + 1
    for i in range(k):
        final = [1,yellow_shifting_digit]
        zolti_initial.append(final)
        yellow_shifting_digit = yellow_shifting_digit + 1
        final2 = [i + 1, n]
        zeleni_initial.append(final2)
    zolti_final = tuple(zeleni_initial)
    zeleni_final = tuple(zolti_initial)
    pacman_problem = Pacman(m,n,zolti_final,zeleni_final,(tuple(zolti_initial),tuple(zeleni_initial)))
    final = depth_first_graph_search(pacman_problem)
    print(final.solution())

    #state = (([1,k+1],[1,k+2]..[1,m]),([1,n],[2,n]..[k,n]))






