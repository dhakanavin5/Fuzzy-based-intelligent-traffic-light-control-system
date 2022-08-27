


import numpy
import matplotlib.pyplot as plt
import sys
import os
import copy
import numpy as np
import skfuzzy as fuzz
sys.path.insert(0, '/home/ubuntu_1/gwalior_map1/anfis')
sys.path.insert(0, '/home/ubuntu_1/gwalior_map1/anfis/membership')
import anfis
import membershipfunction
import mfDerivs
ts = np.loadtxt(
    '/home/ubuntu_1/gwalior_map1/anfis/trainingSet.txt', usecols=[1, 2, 3])

X = ts[:, 0:2]
Y = ts[:, 2]

mf = [[['gaussmf', {'mean': 9., 'sigma': 7.}], ['gaussmf', {'mean': 20., 'sigma': 7.}], ['gaussmf', {'mean': 29., 'sigma': 6.}], ['gaussmf', {'mean': 35., 'sigma': 5.}], ['gaussmf', {'mean': 50., 'sigma': 9.}], ['gaussmf', {'mean': 65., 'sigma': 11.}], ['gaussmf', {'mean': 85., 'sigma': 12.}]],
      [['gaussmf', {'mean': 5.5, 'sigma': 2.5}], ['gaussmf', {'mean': 10., 'sigma': 3.5}], ['gaussmf', {'mean': 14.5, 'sigma': 5.}], ['gaussmf', {'mean': 21, 'sigma': 5.5}], ['gaussmf', {'mean': 28.5, 'sigma': 6.5}]]]


mfc = membershipfunction.MemFuncs(mf)
anf = anfis.ANFIS(X, Y, mfc)
anf.trainHybridJangOffLine(epochs=2)


if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
sys.path.append(os.path.join('c:', os.sep, 'whatever',
                             'path', 'to', 'sumo', 'tools'))

sumoBinary = "/usr/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c",
           "gwalior.sumocfg"]
import traci
traci.start(sumoCmd)
step = 0
timer = 10
st1 = {}


dict4 = {}
dict41 = {}
st = {}


time1 = {}
yellow = {}
y_dict = {}
# these are dictionary of junctions
N28 = {'R15': "GGgrrrrrr", 'R104': "rrrGGgrrr", 'R35': "rrrrrrGGg"}
N22 = {'R59': "rrrGGgrrr", 'R57': "GGgrrrrrr", 'R56': "rrrrrrGGg"}
N21 = {'R66': "rrrrrrrrrGGggrrrrr", 'R3': "GGggrrrrrrrrrrrrrr",
       'R61': "rrrrGGGggGrrrrrrrr", 'R64': "GrrrrrrrrrrrrGGGgg"}
N27 = {'R83': "rrrGGgrrr", 'R79': "rrrrrrGGg", 'R53': "GGgrrrrrr"}
N20 = {'R67': "rrrGGGgGrrr", 'R65': "GGgrrrrrrrr", 'R70': "GrrrrrrGGGg"}
N26 = {'R51': "rrrGGgrrr", 'R47': "GGgrrrrrr", 'R54': "rrrrrrGGg"}
N25 = {'R99': "GGgrrrrrr", 'R97': "rrrrrrGGg", 'R26': "rrrGGgrrr"}
N24 = {'R100': "rrrGGgrrr", 'R101': "rrrrrrGGg", 'R21': "GGgrrrrrr"}
N8 = {'R39': "rrrrrrrrrGGggrrrrr", 'R8': "GrrrrrrrrrrrrGGGgg",
      'R37': "rrrrGGGggGrrrrrrrr", 'R33': "GGggrrrrrrrrrrrrrr"}
N9 = {'R38': "rrrrrrrGGGg", 'R42': "rrrGGGgGrrr", 'R44': "GGgrrrrrrrr"}
N1 = {'R6': "GGgggrrGrrr", 'R1': "GrrrrrgGGGg", 'R4': "GrrgGGgGrrr"}
N2 = {'R7': "GrrgGGgGrrr", 'R10': "GGgggrrGrrr", 'R5': "GrrrrrgGGGg"}
N3 = {'R9': "GrrrrrrGGGg", 'R13': "rrrGGGgGrrr", 'R11': "GGgrrrrrrrr"}
N4 = {'R14': "GrrrrrrrrrrrrGGGgg", 'R20': "GGggrrrrrrrrrrrrrr",
      'R16': "rrrrrrrrrGGggrrrrr", 'R18': "rrrrGGGggGrrrrrrrr"}
N5 = {'R24': "GGgrrrrrrrr", 'R22': "rrrGGGgGrrr", 'R17': "GrrrrrrGGGg"}
N6 = {'R25': "rrrGGgrrr", 'R28': "GGgrrrrrr", 'R29': "rrrrrrGGg"}
N7 = {'R36': "GGggrrrrrrrrrrrr", 'R30': "rrrrGGggrrrrrrrr",
      'R32': "rrrrrrrrGGggrrrr", 'R34': "rrrrrrrrrrrrGGgg"}
N12 = {'R49': "GGggrrrrrrrrrrrrrr", 'R43': "GrrrrrrrrrrrrGGGgg",
       'R46': "rrrrGGGggGrrrrrrrr", 'R48': "rrrrrrrrrGGGgrrrrr"}
N13 = {'R84': "rrrGGgrrr", 'R55': "GGgrrrrrr", 'R52': "rrrrrrGGg"}
N10 = {'R50': "rrrrrrGGg", 'R31': "GGgrrrrrr", 'R91': "rrrGGgrrr"}
N11 = {'R94': "GGgrrrrrr", 'R92': "rrrrrrGGg", 'R96': "rrrGGgrrr"}
N16 = {'R90': "GGgrrrrrr", 'R88': "rrrrrrGGg", 'R81': "rrrGGgrrr"}
N17 = {'R82': "rrrGGgGGg", 'R80': "GGgGGgrrr", 'R78': "rrrGGgrrr"}
N14 = {'R41': "GGgrrrrrr", 'R86': "rrrrrrGGg", 'R89': "rrrGGgrrr"}
N15 = {'R85': "GGgrrrrrr", 'R87': "rrrGGgrrr", 'R62': "rrrrrrGGg"}
N18 = {'R73': "GGgrrrGGg", 'R77': "GGgrrrrrr", 'R76': "GGgGGgrrr"}
N19 = {'R68': "rrrrrrGGg", 'R74': "GGgrrrrrr", 'R71': "rrrGGgrrr"}

time_s = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
con = {'N1': N1, 'N2': N2, 'N3': N3, 'N4': N4, 'N5': N5, 'N6': N6, 'N7': N7, 'N8': N8, 'N9': N9, 'N10': N10, 'N11': N11, 'N12': N12, 'N13': N13, 'N14': N14,
       'N15': N15, 'N16': N16, 'N17': N17, 'N18': N18, 'N19': N19, 'N20': N20, 'N21': N21, 'N22': N22, 'N24': N24, 'N25': N25, 'N26': N26, 'N27': N27, 'N28': N28}
j_weight = {}
detectorIDs = traci.inductionloop.getIDList()
tls_id = traci.trafficlight.getIDList()
dict1 = {}
for de in detectorIDs:
    if de not in dict1:
        dict1[de] = []
for k in tls_id:
    time1[k] = []
    st[k] = 0
ratio_p = 1
for k in con:
    yellow[k] = {}
    for j in con[k]:
        a = con[k][j]
        b = ""
        for i in a:
            if i == 'G' or i == 'g':
                b += "y"
            else:
                b += str(i)
        yellow[k][j] = b
wait_O = {}
dict_v = {}

# this function is used for calulation of total average waiting time of vehicles till time t.


def waiting_time():

    wait = 0
    list_v = traci.vehicle.getIDList()
    for i in list_v:
        if i not in dict_v:
            dict_v[i] = 0
    for i in dict_v:
        try:
            wt1 = traci.vehicle.getWaitingTime(i)

            if wt1:
                wait_O[i] = wt1
            else:
                if i in wait_O:
                    dict_v[i] += wait_O[i]
                    wait_O.pop(i)
        except:
            print("")

    for i in dict_v:
        if i in wait_O:
            wait += (dict_v[i]+wait_O[i])
        else:
            wait += dict_v[i]

    wait = int(wait/len(dict_v))
    return wait
# this function is used for find vehicle on each lane between detector and taffic signal.
# we fix one detector on each lane at a fixed point.


def cross_detector():
    for id1 in detectorIDs:
        value = traci.inductionloop.getLastStepVehicleIDs(id1)
        lane_id1 = traci.inductionloop.getLaneID(id1)
        if(value):
            lane_id2 = traci.vehicle.getLaneID(value[0])
            if(lane_id1 == lane_id2):
                temp = dict1[id1]
                temp.append(value[0])
                dict1[id1] = temp
                temp = set(dict1[id1])
                dict1[id1] = list(temp)
    for id1 in dict1:
        lane_id1 = traci.inductionloop.getLaneID(id1)
        for i in dict1[id1]:
            try:
                lane_id2 = traci.vehicle.getLaneID(i)
                if(lane_id1 != lane_id2):
                    dict1[id1].remove(i)

            except:
                print("")
    return dict1


# calculation of priority_weight for each lane at each junction
def priority_weight(list1):
    weight = 0
    for vid in list1:
        try:
            type1 = traci.vehicle.getTypeID(vid)
            if(type1 == "police"):
                weight += 4
            elif(type1 == "bus"):
                weight += 4
            elif(type1 == "truck"):
                weight += 1
            elif(type1 == "motorcycle"):
                weight += 0.5
            elif(type1 == "ambu"):
                weight += 10
            elif(type1 == "fire"):
                weight += 10
            else:
                weight += 2
        except:
            print("")
    return weight

# calcualtion of load for each lane at each junction


def fair_weight(list1):
    weight = 0
    for vid in list1:
        try:
            type1 = traci.vehicle.getTypeID(vid)
            if(type1 == "police"):
                weight += 3
            elif(type1 == "bus"):
                weight += 5
            elif(type1 == "truck"):
                weight += 5
            elif(type1 == "motorcycle"):
                weight += 0.5
            elif(type1 == "ambu"):
                weight += 3
            elif(type1 == "fire"):
                weight += 5
            else:
                weight += 3
        except:
            print("")
    return weight

# this function is used for find the weight of lanes


def lane_weight():
    dict2 = {}
    dict21 = {}
    for key in dict1:
        lane_id = traci.inductionloop.getLaneID(key)
        dict2[lane_id] = fair_weight(dict1[key])
        dict21[lane_id] = priority_weight(dict1[key])
    return dict2, dict21


def tls_lane():
    list_lane1 = []
    dict3 = {}
    tls_id = traci.trafficlight.getIDList()
    for id1 in tls_id:
        list_lane = traci.trafficlight.getControlledLanes(id1)
        temp = set(list_lane)
        list_lane = list(temp)
        list_lane1 += list_lane
        temp = []
        for i in list_lane:
            edge_id = traci.lane.getEdgeID(i)
            if not temp:
                temp.append([i])
            else:
                for k in temp:
                    if edge_id == traci.lane.getEdgeID(k[0]):
                        k.append(i)
                        break
                else:
                    temp.append([i])

        dict3[id1] = temp
    return dict3, list_lane1


dict3, list_lane = tls_lane()
# print('dict3')
# print(list_lane)


def tls_edge():
    list_lane1 = []
    dict3 = {}
    temp1 = []
    tls_id = traci.trafficlight.getIDList()
    for id1 in tls_id:
        list_lane = traci.trafficlight.getControlledLanes(id1)
        temp = set(list_lane)
        list_lane = list(temp)
        list_lane1 += list_lane

    for i in list_lane1:
        edge_id = traci.lane.getEdgeID(i)
        if edge_id not in temp1:
            temp1.append(edge_id)
    return temp1


def awt_edge():
    edge_ids = tls_edge()
    awt_edge_dict = {}
    for i in edge_ids:
        awt = traci.edge.getWaitingTime(i)

        count = traci.edge.getLastStepVehicleNumber(i)
        if count != 0:
            awt_edge_dict[i] = (awt//count)
        else:
            awt_edge_dict[i] = 0
    return awt_edge_dict


# this function is used for set fuzzy range and decide the time of traffic light


# find weight of edge from it's lanea


def matrix_weight(dict2, dict21, lanew):
    lane_weight()
    ewait1 = {}
    for id1 in dict3:
        ewait = {}
        list2 = {}
        list21 = {}
        w1 = 0
        list1 = dict3[id1]
        for j in list1:
            w, w2, w3 = 0, 0, 0
            edge_id = traci.lane.getEdgeID(j[0])
            count = 0
            for k in j:
                count += 1
                w += dict2[k]
                w1 += dict2[k]
                w2 += dict21[k]
                w3 += lanew[k]
            list2[edge_id] = w/count
            list21[edge_id] = w2
            ewait[edge_id] = w3
        j_weight[id1] = w1
        dict4[id1] = list2
        dict41[id1] = list21
        ewait1.update(ewait)
    return dict4, dict41, ewait1


# time calculation for each junction and it's each phase
dict_t = {}


def cal_time(dict12, dict13, c_dict, awt_dict, aql_dict):
    #print(awt_dict)
    j1 = {'N17': "rrrGGgrrr", 'N18': "GGgrrrrrr"}

    for k in dict12:
        total = j_weight[k]
        dict_t[k] = []
        y_dict[k] = {}
        temp1 = {}
        temp2 = {}
        for i in dict12[k]:
	    
            state = con[k][i]
            if k in j1 and state == j1[k]:
                temp1[state] = 1
                temp2[state] = dict13[k][i]

            else:
                y_dict[k][state] = yellow[k][i]
                if c_dict[i]:
                    temp1[state] = 10
                    temp2[state] = dict13[k][i]
                else:
                    a = dict12[k][i]
                    
                    awt_edge = awt_dict[i]
                    aql_edge = aql_dict[i]
                    t = fuzzy(a, awt_edge, aql_edge)
                    temp1[state] = t
                    temp2[state] = dict13[k][i]

        b = sorted(temp2.items(), key=lambda kv: [kv[1], kv[0]])
        b = b[::-1]
        temp = []
        for i in b:
            temp.append((i[0], temp1[i[0]]))
            if i[0] in y_dict[k]:
                temp.append((y_dict[k][i[0]], 5))
        dict_t[k] = temp

    return dict_t


def fuzzy(weight, awt_edge, aql_edge):
    time = anfis.predict(anf, np.array([[weight, (awt_edge+aql_edge)/2]]))
    if(time < 10):
        return 10
    else:
        return(int(t))


#
# this function is used for set the time duration to traffic light
dict_l = {}


def control_tls(step):
    if not time1['N12']:
        time1['N9'] = dict_t['N9']
        time1['N12'] = dict_t['N12']
    N12_N9(time1, st)
    for k in time1:
        if not time1[k]:
            time1[k] = dict_t[k]

    for k in time1:
        if st[k] == step:
            state = time1[k][0][0]
            traci.trafficlight.setRedYellowGreenState(k, state)
            t = time1[k][0][1]+step
            st[k] = t
            time1[k].pop(0)
            if time1['N9'] == []:
                N12_N9(time1, st)
    for k in time1:
        if time1[k]:
            tem = {}
            for i in dict_t[k]:
                tem[i[0]] = i[1]
            for j in range(0, (len(time1[k]))):
                if time1[k][j][0] in tem:
                    a = (time1[k][j][0], tem[time1[k][j][0]])
                    time1[k][j] = a

# average queue length


def AQL():
    n = 0
    for id1 in detectorIDs:
        i = traci.inductionloop.getLaneID(id1)
        n += traci.lane.getLastStepHaltingNumber(i)
    return (n*2)//len(detectorIDs)


def AQL_edge():
    edge_ids = tls_edge()
    aql_edge_dict = {}
    for i in edge_ids:

        x = traci.edge.getLastStepLength(i)

        aql_edge_dict[i] = x
    return (aql_edge_dict)

# average traffic flow


def ATF(temp12, temp1):
    count = 0
    for i in temp12:
        set1 = set(temp12[i])
        set2 = set(temp1[i])
        count += len(set1-set2)
    atf = (count*2)//26
    return atf


# congestion
outgoing_edge = {}
incoming_edge = {}


def get_edge():
    for id1 in tls_id:
        a = traci.trafficlight.getControlledLinks(id1)
        for i in a:
            b = traci.lane.getEdgeID(i[0][1])
            c = traci.lane.getEdgeID(i[0][0])
            if b not in outgoing_edge:
                outgoing_edge[b] = id1
            if c not in incoming_edge:
                incoming_edge[c] = id1
    return outgoing_edge, incoming_edge


get_edge()
# this function is used for average speed of lane at time t


def lane_waiting_time_speed():
    wt = {}
    sp = 0
    for i in list_lane:

        wt[i] = (traci.lane.getWaitingTime(i))
        sp += traci.lane.getLastStepMeanSpeed(i)

    return wt, int(sp) / len(list_lane)
# this function is used for average waiting time of lane


def avg_wait(dictw):
    sum1 = 0
    avg = 0
    for i in dictw:
        sum1 += dictw[i]
    no = traci.vehicle.getIDCount()
    if no:
        avg = int((sum1)/no)
    else:
        avg = 0
    return avg


con_dict = {}
conj_edge = {}
for i in incoming_edge:
    con_dict[i] = 0
    conj_edge[i] = 0
# this function is used for find conjestion edge


def find_cog_edge(avg, ewait, dict12, con_dict):
    co_dict = {}
    co_dict = con_dict.copy()
    for i in ewait:
        jun = incoming_edge[i]
        load = dict12[jun][i]
        if ewait[i] > avg and load >= 40:
            if i in outgoing_edge:
                jun = outgoing_edge[i]
                conj_edge[i] = 1
                for j in incoming_edge:
                    if incoming_edge[j] == jun:
                        if not conj_edge[j]:
                            co_dict[j] == 1
                        else:
                            co_dict[j] = 0

    return co_dict
# this is used for Junction N12 and N9


def N12_N9(time1, st):
    temp, temp1 = (), ()
    list12 = time1['N12']
    list9 = time1['N9']
    l12 = ["GGggrrrrrrrrrrrrrr", "rrrrGGGggGrrrrrrrr", "rrrrrrrrrGGGgrrrrr",
           "yyyyrrrrrrrrrrrrrr", "rrrryyyyyyrrrrrrrr", "rrrrrrrrryyyyrrrrr"]
    l9 = ["rrrrrrrGGGg", "rrrGGGgGrrr", "rrrrrrryyyy", "rrryyyyyrrr"]
    for i in time1['N12']:

        if i[0] == "GrrrrrrrrrrrrGGGgg":
            temp = i
            break
    for i in time1['N9']:
        if i[0] == "GGgrrrrrrrr":
            temp1 = i
            break
    if time1['N9']:
        if time1['N9'][0][0] in l9:
            if temp in time1['N12']:
                time1['N12'].remove(temp)
            t = time1['N9'][0][1]
            if ("yrrrrrrrrrrrryyyyy", 5) in time1['N12']:
                time1['N12'].remove(("yrrrrrrrrrrrryyyyy", 5))
            temp = [("GrrrrrrrrrrrrGGGgg", t)]
            time1['N12'] = temp+time1['N12']

    if time1['N12'][0][0] in l12 or time1['N9'] == []:

        if temp1 in time1['N9']:
            time1['N9'].remove(temp1)
        if ("yyyrrrrrrrr", 5) in time1['N9']:
            time1['N9'].remove(("yyyrrrrrrrr", 5))
        t = time1['N12'][0][1]
        temp1 = [("GGgrrrrrrrr", t)]

        time1['N9'] = temp1+time1['N9']

    return time1


awt1 = []
step1 = []
k = 0
aql = []
asl = []
atf = []
x = []
count = 0
count1 = 0
while traci.simulation.getMinExpectedNumber() > 0:  # main loop

    x = []
    traci.simulationStep()
    cross_detector()
    if k == 0:
        temp12 = copy.deepcopy(dict1)
    k += 1
    if k == 30:
        temp1 = copy.deepcopy(dict1)
        atf.append(ATF(temp12, temp1))
        lanew, avgs = lane_waiting_time_speed()
        avg_wait(ewait)
        k = 0
        awt1.append(waiting_time())
        aql.append(AQL())
        asl.append(avgs)
        x.append(count)
        count += 30
    abc = awt_edge()
    dict2, dict21 = lane_weight()
    lanew, avgs = lane_waiting_time_speed()
    dict12, dict13, ewait = matrix_weight(dict2, dict21, lanew)
    awt = avg_wait(ewait)
    step1.append(step)
    cdict = find_cog_edge(awt, ewait, dict12, con_dict)
    xyz= AQL_edge()
    cal_time(dict12, dict13, cdict,abc,xyz)
   
    control_tls(step)
    waiting_time()
    step += 1
print("aql", aql)
print("as", asl)
print("ATF", atf)
print("awt1", awt1)

traci.close()
