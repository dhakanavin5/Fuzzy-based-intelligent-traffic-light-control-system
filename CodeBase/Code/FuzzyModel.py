import os, sys
import matplotlib.pyplot as plt
if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
else:   
     sys.exit("please declare environment variable 'SUMO_HOME'")
sumoBinary = "/home/user/sumo/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "/home/user/Desktop/Naveen/gwalior10.sumocfg"]
#sys.path.append(os.path.join(os.environ.get("SUMO_HOME"), 'tools'))

import copy
import traci
import numpy as np
import skfuzzy as fuzz
traci.start(sumoCmd)
step=0
timer=10
st1={}

dict4={}
dict41={}
st={}

time1={}
yellow={}
y_dict={}
# dictionary of junctions 
N28={'R15':"GGgrrrrrr",'R104':"rrrGGgrrr",'R35':"rrrrrrGGg"}
N22={'R59':"rrrGGgrrr",'R57':"GGgrrrrrr",'R56':"rrrrrrGGg"}
N21={'R66':"rrrrrrrrrGGGGGrrrr",'R3':"GGGggrrrrrrrrrrrrr",'R61':"rrrrGGGGgrrrrrrrrr", 'R64':"rrrrrrrrrrrrrGGGGg"}
N27={'R83':"rrrGGgrrr",'R79':"rrrrrrGGg", 'R53':"GGgrrrrrr"}
N20={'R67':"rrrGGGgGrrr",'R65':"GGgrrrrrrrr",'R70':"GrrrrrrGGGg"}
N26={'R51':"rrrGGgrrr",'R47':"GGgrrrrrr",'R54':"rrrrrrGGg"}
N25={'R99':"GGgrrrrrr",'R97':"rrrrrrGGg", 'R26':"rrrGGgrrr"}
N24={'R100':"rrrGGgrrr",'R101':"rrrrrrGGg",'R21':"GGgrrrrrr"}
N8={'R39':"rrrrrrrrrGGggrrrrr",'R8':"GrrrrrrrrrrrrGGGgg", 'R37':"rrrrGGGggGrrrrrrrr",'R33':"GGggrrrrrrrrrrrrrr"}
N9={'R38':"GGggGrrGGGg",'R42':"GGgGGGgGrrr",'R44':"GGgrrrrrrrr"}
N1={'R6':"GGgggrrGrrr",'R1':"GrrrrrgGGGg",'R4':"GrrgGGgGrrr"}
N2={'R7':"GrrgGGgGrrr",'R10':"GGgggrrGrrr",'R5':"GrrrrrgGGGg"}
N3={'R9':"GrrrrrrGGGg", 'R13':"rrrGGGgGrrr", 'R11':"GGgrrrrrrrr"}
N4={'R14':"GrrrrrrrrrrrrGGGgg", 'R20':"GGggrrrrrrrrrrrrrr", 'R16':"rrrrrrrrrGGggrrrrr", 'R18':"rrrrGGGggGrrrrrrrr"}
N5={'R24':"GGgrrrrrrrr", 'R22':"rrrGGGgGrrr", 'R17':"GrrrrrrGGGg"}
N6={'R25':"rrrGGgrrr", 'R28':"GGgrrrrrr", 'R29':"rrrrrrGGg"}
N7={'R36':"GGggrrrrrrrrrrrr", 'R30':"rrrrGGggrrrrrrrr", 'R32':"rrrrrrrrGGggrrrr", 'R34':"rrrrrrrrrrrrGGgg"}
N12={'R49':"GGggrrrrrrrrrGGGgg", 'R43':"GrrrrrrrrrrrrGGGgg",'R46':"rrrrGGGggGrrrGGGgg",'R48':"rrrrrrrrrGGggGGGgg"}
N13={'R84':"rrrGGgrrr", 'R55':"GGgrrrrrr", 'R52':"rrrrrrGGg"}
N10={'R50':"rrrrrrGGg", 'R31':"GGgrrrrrr", 'R91':"rrrGGgrrr"}
N11={'R94':"GGgrrrrrr", 'R92':"rrrrrrGGg", 'R96':"rrrGGgrrr"}
N16={'R90':"GGgrrrrrr", 'R88':"rrrrrrGGg", 'R81':"rrrGGgrrr"}
N17={'R82':"rrrGGgGGg", 'R80':"GGgGGgrrr", 'R78':"rrrGGgrrr"}
N14={'R41':"GGgrrrrrr", 'R86':"rrrrrrGGg", 'R89':"rrrGGgrrr"}
N15={'R85':"GGgrrrrrr",'R87':"rrrGGgrrr",'R62':"rrrrrrGGg"}
N18={'R73':"GGgrrrGGg",'R77':"GGgrrrrrr",'R76':"GGgGGgrrr"}
N19={'R68':"rrrrrrGGg", 'R74':"GGgrrrrrr", 'R71':"rrrGGgrrr"}

time_s=[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85,90]
con={'N1':N1,'N2':N2,'N3':N3,'N4':N4,'N5':N5,'N6':N6,'N7':N7,'N8':N8,'N9':N9,'N10':N10,'N11':N11,'N12':N12,'N13':N13,'N14':N14,'N15':N15,'N16':N16,'N17':N17,'N18':N18,'N19':N19,'N20':N20,'N21':N21,'N22':N22,'N24':N24,'N25':N25,'N26':N26,'N27':N27,'N28':N28}
j_weight={}
detectorIDs = traci.inductionloop.getIDList()
tls_id=traci.trafficlight.getIDList()
dict1={}
for de in detectorIDs:
	if de not in dict1:
		dict1[de]=[]
for k in tls_id:
	time1[k]=[]
	st[k]=0
ratio_p=1
for k in con:
	yellow[k]={}
	for j in con[k]:
		a=con[k][j]
		b=""
		for i in a:
			if i=='G' or i=='g':
        			b+="y"
			else:
				b+=str(i)
		yellow[k][j]=b
wait_O={}
dict_v={}
# function is used for calulation of total average waiting time of vehicles till time t. 
def waiting_time():
	
	wait=0
	list_v=traci.vehicle.getIDList()
	for i in list_v:
		if i not in dict_v:
			dict_v[i]=0
	for i in dict_v:
		try:
			wt1=traci.vehicle.getWaitingTime(i)
		
			if wt1:
				wait_O[i]=wt1
			else:
				if i in wait_O:
					dict_v[i]+=wait_O[i]
					wait_O.pop(i)
		except:
			print("")
	
	for i in dict_v:
		if i in wait_O:
			wait+=(dict_v[i]+wait_O[i])
		else:
			wait+=dict_v[i]
			
	wait=int(wait/len(dict_v))
	return wait

	 
#function is used for find vehicle on each lane between detector and taffic signal. 						
def cross_detector():
	for id1 in detectorIDs:
		value=traci.inductionloop.getLastStepVehicleIDs(id1)
		lane_id1=traci.inductionloop.getLaneID(id1)
		if(value):
			lane_id2=traci.vehicle.getLaneID(value[0])
			if(lane_id1==lane_id2):
				temp=dict1[id1]
				temp.append(value[0])
				dict1[id1]=temp 
				temp=set(dict1[id1])
				dict1[id1]=list(temp)
	for id1 in dict1:
		lane_id1=traci.inductionloop.getLaneID(id1)
		for i in dict1[id1]:
			try:
				lane_id2=traci.vehicle.getLaneID(i)
				if(lane_id1!=lane_id2):
                        		dict1[id1].remove(i)
				 
			except:
				print("")
	return dict1

def find_emergency_vehicle(list1):
	count=0
	for vid in list1:
		try:
			type1=traci.vehicle.getTypeID(vid)
			if type1=="ambu" or type1 == "fire" or type1 == "police" :
				count+=1
			else:
				count+=0
		except:
			print("")
	return count		
# calculation of priority_weight for each lane at each junction
def vehicle_weight(list1):
	weight=0
	for vid  in list1:
		try:
			type1=traci.vehicle.getTypeID(vid)
			if(type1=="police"):
                       		weight+=1
			elif(type1=="bus"):
                	       weight+=1
			elif(type1=="truck"):
                       		weight+=1
			elif(type1=="motorcycle"):
                       		weight+=1
			elif(type1=="ambu"):
                       		weight+=1
			elif(type1=="fire"):
                       		weight+=1
			else:
                 		weight+=1
		except:
               		print("")
	return weight

# calcualtion of load for each lane at each junction
def fair_weight(list1):
	weight=0
	for vid  in list1:
		try:
			type1=traci.vehicle.getTypeID(vid)
			if(type1=="police"):
                       		weight+=3
			elif(type1=="bus"):
                       		weight+=5
			elif(type1=="truck"):
                       		weight+=5
			elif(type1=="motorcycle"):
                       		weight+=0.5
			elif(type1=="ambu"):
                       		weight+=3
			elif(type1=="fire"):
                		weight+=5
			else:
                		weight+=3
		except:
               		print("")
	return weight
#to find average waiting time of emergency vehicle
def avg_waiting_timeof_emergencyvehicle():
	waiting_time=0
	total_no_of_emergency_vehicle=0
	
	for key in dict1:
		list1=dict1[key]
		for vid in list1:
			try:
				type1=traci.vehicle.getTypeID(vid)
				if type1 == "ambu" or type1 == "fire" or type1 == "police" :
					total_no_of_emergency_vehicle+=1
					waiting_time+=traci.vehicle.getWaitingTime(vid)
					
			except:
				print("")
	if total_no_of_emergency_vehicle :
		return int(waiting_time/total_no_of_emergency_vehicle)
	else:
		return 0
def avg_speed_ofemergencyvehicle():
	vehicle_list=traci.vehicle.getIDList()
	total_speed=0
	v_total=0
	for vid in vehicle_list:
		type1=traci.vehicle.getTypeID(vid)
		if type1 == "ambu" or type1 == "fire" or type1 == "police" :
			total_speed+=traci.vehicle.getSpeed(vid)
			v_total+=1
			
	if v_total==0:
		return 0
	else:
		return int(total_speed)/v_total

# function is used for find the weight of lanes
def lane_weight():
	dict2={}
	dict21={}
	e_vehicles_onlane={}
	for key in dict1:
		lane_id=traci.inductionloop.getLaneID(key)
		dict2[lane_id]=fair_weight(dict1[key])
		dict21[lane_id]=vehicle_weight(dict1[key])
		no_of_evehicle=find_emergency_vehicle(dict1[key])
		if no_of_evehicle > 0:
			e_vehicles_onlane[lane_id]=no_of_evehicle
	return dict2,dict21,e_vehicles_onlane          		

def tls_lane():
	list_lane1=[]
	dict3={}
	tls_id=traci.trafficlight.getIDList()
	for id1 in tls_id:
		list_lane=traci.trafficlight.getControlledLanes(id1)
		temp=set(list_lane)
		list_lane=list(temp)
		list_lane1+=list_lane
		temp=[]
		for i in list_lane: 
			edge_id= traci.lane.getEdgeID(i)
			if not temp:
                        	temp.append([i])
			else:
				for k in temp:
					if edge_id==traci.lane.getEdgeID(k[0]):
						k.append(i)
						break
					else:
						temp.append([i])
                        
	dict3[id1]=temp
	return dict3,list_lane1
dict3,list_lane=tls_lane()
# this function is used for set fuzzy range and decide the time of traffic light
def fuzzy(a):
	w1=np.array([0,0,10])
	w2=np.array([8,8,15])
	w3=np.array([13,13,20])
	w4=np.array([18,18,25])
	w5=np.array([23,23,30])
	w6=np.array([28,28,35])
	w7=np.array([33,33,40])
	w8=np.array([38,38,45])
	w9=np.array([43,43,50])
	w10=np.array([48,48,55])
	w11=np.array([53,53,100])
	x=np.array([a])
	w1=fuzz.membership.trimf(x,w1)[0]
	w2=fuzz.membership.trimf(x,w2)[0]
	w3=fuzz.membership.trimf(x,w3)[0]
	w4=fuzz.membership.trimf(x,w4)[0]
	w5=fuzz.membership.trimf(x,w5)[0]
	w6=fuzz.membership.trimf(x,w6)[0]
	w7=fuzz.membership.trimf(x,w7)[0]
	w8=fuzz.membership.trimf(x,w8)[0]
	w9=fuzz.membership.trimf(x,w9)[0]
	w10=fuzz.membership.trimf(x,w10)[0]
	w11=fuzz.membership.trimf(x,w11)[0]
	b=[w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11]
	maxi=max(b)
	max_index=b.index(maxi)
	t=10+((max_index+1)-1)*5
	return t
# find weight of edge from it's lane 
def matrix_weight(dict2,dict21,lanew,e_vehicles_onlane):
	lane_weight()
	ewait1={}
	e_vehicle_on_edges={}
	for id1 in dict3:
		ewait={}
		list2={}
		list21={}
		e_vehicles_on_edge=[]
		w1=0
		list1=dict3[id1]
		for j in list1:
			w,w2,w3,w4=0,0,0,0
			edge_id=traci.lane.getEdgeID(j[0])
			count=0
			for k in j:
				count+=1
				w+=dict2[k]
				w1+=dict2[k]
				w2+=dict21[k]
				w3+=lanew[k]
				if k in e_vehicles_onlane:
					w4+=e_vehicles_onlane[k]
				list2[edge_id]=w/count
				list21[edge_id]=w2
				ewait[edge_id]=w3
				if w4 > 0:
					e_vehicles_on_edge.append(edge_id)
			j_weight[id1]=w1
			dict4[id1]=list2
			dict41[id1]=list21
			e_vehicle_on_edges[id1]=e_vehicles_on_edge
			ewait1.update(ewait)
	return dict4,dict41,ewait1,e_vehicle_on_edges
	
# time calculation for each junction and it's each phase
dict_t={}
def cal_time(dict12,dict13,c_dict):
	j1={'N17':"rrrGGgrrr",'N18':"GGgrrrrrr"}
	for k in dict12:
		total=j_weight[k]
		dict_t[k]=[]
		y_dict[k]={}
		temp1={}
		temp2={}
		for i in dict12[k]:
			state=con[k][i]
			if k in j1 and state==j1[k]:
				temp1[state]=1
				temp2[state]=dict13[k][i]
                                
			else:
				y_dict[k][state]=yellow[k][i]
				if c_dict[i] :
					temp1[state]=10
					temp2[state]=dict13[k][i]
				else:
					a=dict12[k][i]
					t=fuzzy(a)
					temp1[state]=t
					temp2[state]=dict13[k][i]
	                                 
                	
		b=sorted(temp2.items(), key = lambda kv:[kv[1],kv[0]])
		b=b[::-1]
		temp=[]
		for i in b:
			temp.append((i[0],temp1[i[0]]))
			if i[0] in y_dict[k]:
				temp.append((y_dict[k][i[0]],5))
		dict_t[k]=temp		
	
	return dict_t
# function is used for set the time duration to traffic light
dict_l={}
def control_tls(step,e_dict):
	
	for k in time1:
		if not time1[k]:
			time1[k]=dict_t[k]
	print(time1)
	for k in time1:
		if e_dict[k]:
			state=con[k][e_dict[k][0]]
			traci.trafficlight.setRedYellowGreenState(k,state)
			st[k]=step+1
			time1[k]=dict_t[k]
		if st[k]==step:            
			state=time1[k][0][0]
			traci.trafficlight.setRedYellowGreenState(k,state)
			t=time1[k][0][1]+step
			st[k]=t
			time1[k].pop(0)
			
	for k in time1:
		if time1[k]:
			tem={}
			for i in dict_t[k]:
				tem[i[0]]=i[1]
			for j in range(0,(len(time1[k]))):
				if time1[k][j][0] in tem:
					a=(time1[k][j][0],tem[time1[k][j][0]])
					time1[k][j]=a

# average queue length	
def AQL():
	n=0
	for id1 in detectorIDs:
		i=traci.inductionloop.getLaneID(id1)
		n+=traci.lane.getLastStepHaltingNumber(i)
	return (n*2)//len(detectorIDs)
#average traffic flow
def ATF(temp12,temp1):
	count=0
	for i in temp12:
		set1=set(temp12[i])
		set2=set(temp1[i])
		count+=len(set1-set2)
	atf=(count*6)//26
	return atf
# congestion
outgoing_edge={}
incoming_edge={}
def get_edge():
	for id1 in tls_id:
		a=traci.trafficlight.getControlledLinks(id1) 
		for i in a:
			b=traci.lane.getEdgeID(i[0][1])
			c=traci.lane.getEdgeID(i[0][0])
			if b not in outgoing_edge:
				outgoing_edge[b]=id1
			if c not in incoming_edge:
				incoming_edge[c]=id1
	return outgoing_edge,incoming_edge

get_edge()	
# function is used for average speed of lane at time t
def lane_waiting_time_speed():
	wt={}
	sp=0
	wt1=0
	for i in list_lane:
		wt1+=traci.lane.getWaitingTime(i)
		wt[i]=traci.lane.getWaitingTime(i)
		sp+=traci.lane.getLastStepMeanSpeed(i)
	
	return wt,int(wt1)/len(list_lane),int(sp)/ len(list_lane)
# function is used for average waiting time of lane 
def avg_wait(dictw):
	sum1=0
	avg=0
	for i in dictw:
		sum1+=dictw[i]
	no=traci.vehicle.getIDCount()
	if no:
		avg=int((sum1)/no)
	else:
		avg=0
	return avg
con_dict={}
conj_edge={}
for i in incoming_edge:
	con_dict[i]=0
	conj_edge[i]=0
# function is used for find conjestion edge 
def find_cog_edge(avg,ewait,dict12,con_dict):
	co_dict={}        
	co_dict=con_dict.copy()
	for i in ewait:
		jun=incoming_edge[i]
		load=dict12[jun][i]
		if ewait[i]>avg and load >=40:
			if i in outgoing_edge:
				jun=outgoing_edge[i]
				conj_edge[i]=1
				for j in incoming_edge:
					if incoming_edge[j]==jun:
						if not conj_edge[j]:
							co_dict[j]==1
						else:
							co_dict[j]=0				
				
						
	return co_dict

awt1=[]
step1=[]
k=0
aql=[]
asl=[]
atf=[]
awtofemegency=[]
asofemergency=[]
x=[]
count=0
count1=0
while traci.simulation.getMinExpectedNumber()>0 :#main loop 
	traci.simulationStep()
	cross_detector()
	if k==0:
		temp_pre=copy.deepcopy(dict1)
	k+=1	
	if k==30:
		temp_next=copy.deepcopy(dict1)
		print(temp_next)
		atf.append(ATF(temp_pre,temp_next))
		lanew,wt1,avgs=lane_waiting_time_speed()
		e_awt=avg_waiting_timeof_emergencyvehicle()
		avg_wait(ewait)
		k=0
		awt1.append(wt1)
		aql.append(AQL())
		asl.append(avgs)
		awtofemegency.append(e_awt)
		asofemergency.append(avg_speed_ofemergencyvehicle())
		x.append(count)
		count+=30
	dict2,dict21,e_vehicle_onlane=lane_weight()
	lanew,wt1,avgs=lane_waiting_time_speed()
	dict12,dict13,ewait,e_vehicle_on_edges=matrix_weight(dict2,dict21,lanew,e_vehicle_onlane)
	awt=avg_wait(ewait)
	step1.append(step)
	cdict=find_cog_edge(awt,ewait,dict12,con_dict)
	cal_time(dict12,dict13,cdict)
	control_tls(step,e_vehicle_on_edges)
	waiting_time()
	step+=1
print("aql",aql)
print("as",asl)
print("ATF",atf)
print("awt1",awt1)
print("e_awt",awtofemegency)
print("e_as",asofemergency)
traci.close()
