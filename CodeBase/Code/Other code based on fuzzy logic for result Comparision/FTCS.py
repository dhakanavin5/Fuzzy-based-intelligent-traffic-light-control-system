import os, sys
import array
if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
else:   
     sys.exit("please declare environment variable 'SUMO_HOME'")
sumoBinary = "/usr/share/sumo/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "/home/dhakadnavin/Desktop/gwalior_map1/gwalior.sumocfg"]
#import membership
import traci
import numpy as np
import copy
import skfuzzy as fuzz
N28={'R15':"GGgrrrrrr",'R104':"rrrGGgrrr",'R35':"rrrrrrGGg"}
N22={'R59':"rrrGGgrrr",'R57':"GGgrrrrrr",'R56':"rrrrrrGGg"}
N21={'R66':"rrrrrrrrrGGggrrrrr",'R3':"GGggrrrrrrrrrrrrrr",'R61':"rrrrGGGggGrrrrrrrr", 'R64':"GrrrrrrrrrrrrGGGgg"}
N27={'R83':"rrrGGgrrr",'R79':"rrrrrrGGg", 'R53':"GGgrrrrrr"}
N20={'R67':"rrrGGGgGrrr",'R65':"GGgrrrrrrrr",'R70':"GrrrrrrGGGg"}
N26={'R51':"rrrGGgrrr",'R47':"GGgrrrrrr",'R54':"rrrrrrGGg"}
N25={'R99':"GGgrrrrrr",'R97':"rrrrrrGGg", 'R26':"rrrGGgrrr"}
N24={'R100':"rrrGGgrrr",'R101':"rrrrrrGGg",'R21':"GGgrrrrrr"}
N8={'R39':"rrrrrrrrrGGggrrrrr",'R8':"GrrrrrrrrrrrrGGGgg", 'R37':"rrrrGGGggGrrrrrrrr",'R33':"GGggrrrrrrrrrrrrrr"}
N9={'R38':"rrrrrrrGGGg",'R42':"rrrGGGgGrrr",'R44':"GGgrrrrrrrr"}
N1={'R6':"GGgggrrGrrr",'R1':"GrrrrrgGGGg",'R4':"GrrgGGgGrrr"}
N2={'R7':"GrrgGGgGrrr",'R10':"GGgggrrGrrr",'R5':"GrrrrrgGGGg"}
N3={'R9':"GrrrrrrGGGg", 'R13':"rrrGGGgGrrr", 'R11':"GGgrrrrrrrr"}
N4={'R14':"GrrrrrrrrrrrrGGGgg", 'R20':"GGggrrrrrrrrrrrrrr", 'R16':"rrrrrrrrrGGggrrrrr", 'R18':"rrrrGGGggGrrrrrrrr"}
N5={'R24':"GGgrrrrrrrr", 'R22':"rrrGGGgGrrr", 'R17':"GrrrrrrGGGg"}
N6={'R25':"rrrGGgrrr", 'R28':"GGgrrrrrr", 'R29':"rrrrrrGGg"}
N7={'R36':"GGggrrrrrrrrrrrr", 'R30':"rrrrGGggrrrrrrrr", 'R32':"rrrrrrrrGGggrrrr", 'R34':"rrrrrrrrrrrrGGgg"}
N12={'R49':"GGggrrrrrrrrrrrrrr", 'R43':"GrrrrrrrrrrrrGGGgg",'R46':"rrrrGGGggGrrrrrrrr",'R48':"rrrrrrrrrGGGgrrrrr"}
N13={'R84':"rrrGGgrrr", 'R55':"GGgrrrrrr", 'R52':"rrrrrrGGg"}
N10={'R50':"rrrrrrGGg", 'R31':"GGgrrrrrr", 'R91':"rrrGGgrrr"}
N11={'R94':"GGgrrrrrr", 'R92':"rrrrrrGGg", 'R96':"rrrGGgrrr"}
N16={'R90':"GGgrrrrrr", 'R88':"rrrrrrGGg", 'R81':"rrrGGgrrr"}
N17={'R82':"rrrGGgGGg", 'R80':"GGgGGgrrr", 'R78':"rrrGGgrrr"}
N14={'R41':"GGgrrrrrr", 'R86':"rrrrrrGGg", 'R89':"rrrGGgrrr"}
N15={'R85':"GGgrrrrrr",'R87':"rrrGGgrrr",'R62':"rrrrrrGGg"}
N18={'R73':"GGgrrrGGg",'R77':"GGgrrrrrr",'R76':"GGgGGgrrr"}
N19={'R68':"rrrrrrGGg", 'R74':"GGgrrrrrr", 'R71':"rrrGGgrrr"}
con={'N1':N1,'N2':N2,'N3':N3,'N4':N4,'N5':N5,'N6':N6,'N7':N7,'N8':N8,'N9':N9,'N10':N10,'N11':N11,'N12':N12,'N13':N13,'N14':N14,'N15':N15,'N16':N16,'N17':N17,'N18':N18,'N19':N19,'N20':N20,'N21':N21,'N22':N22,'N24':N24,'N25':N25,'N26':N26,'N27':N27,'N28':N28}
yellow={}
y_dict={}
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

traci.start(sumoCmd) 
step = 0
 
dict2={}
laneid=[]
#lanelist=list(set(traci.trafficlight.getControlledLanes()))	
detectorids=traci.inductionloop.getIDList()
dict1={}
for de in detectorids:
           if de not in dict1:
	       dict1[de]=[]
def Wqueue():
	dict2={}
	dict5={}
        for id1 in detectorids:
                value=traci.inductionloop.getLastStepVehicleIDs(id1)
                lane_id1=traci.inductionloop.getLaneID(id1)
                if(value ):
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
	for i in dict1:
		lane_id=traci.inductionloop.getLaneID(i)
		count=len(dict1[i])
		dict5[lane_id]=dict1[i]
		dict2[lane_id]=count
	return dict2,dict5
wait_O={}
dict_v={}	
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
			print(" ")
	
	for i in dict_v:
		if i in wait_O:
			wait+=(dict_v[i]+wait_O[i])
		else:
			wait+=dict_v[i]
			
	wait=int(wait/len(dict_v))
	return wait 
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
def fuzzyrule(wq,vf):
	gd=""
	if wq=="L":
		if vf=="L":
			gd="S"
		if vf=="M":
			gd="M"
		if vf=="H":
			gd="H"
	if wq=="M":
		if vf=="L":
			gd="S"
		if vf=="M":
			gd="M"
		if vf=="H":
			gd="M"
	if wq=="H":
		if vf=="L":
			gd="S"
		if vf=="M":
			gd="S"
		if vf=="H":
			gd="S"
	return gd
def rule_evolution(wqr,vfgreen):
	dictw={}
	dictv={}
	Sw=np.array([0,0,6.4])
	Mw=np.array([4,8,12])
	Hw=np.array([9,16,16])
	x=np.array([wqr])
	L=fuzz.membership.trimf(x,Sw)[0]
	M=fuzz.membership.trimf(x,Mw)[0]
	H=fuzz.membership.trimf(x,Hw)[0]
	dict_wqr={'L':L,'M':M,'H':H}
	for i in dict_wqr:
		if dict_wqr[i]>0:
			dictw[i]=dict_wqr[i]

	Sv=np.array([0,0,5])
	Mv=np.array([3,6,9])
	Hv=np.array([7,14,14])
	x1=np.array([vfgreen])
	
	L=fuzz.membership.trimf(x1,Sv)[0]
	M=fuzz.membership.trimf(x1,Mv)[0]
	H=fuzz.membership.trimf(x1,Hv)[0]
	dict_vfg={'L':L,'M':M,'H':H}
	for i in dict_vfg:
		if dict_vfg[i]>0:
			dictv[i]=dict_vfg[i]
	return dictw,dictv
def rule_base(dictw,dictv):
	maxv=0
	maxw='L'
	maxvfg='L'
	for i in  dictw:
		for j in dictv:	
			temp=min(dictw[i],dictv[j])
			if temp>maxv:
				maxv=temp
				maxw=i
				maxvfg=j
	return maxw,maxvfg

	
def settime(gd):
	t=0
	if gd=="S":
		t=10
	elif gd=="M":
		t=15
	else:
		t=20
	return t


def find_time(vfgreen,wqr):
	dictw,dictv=rule_evolution(wqr,vfgreen)
	a,b=rule_base(dictw,dictv)
	gd=fuzzyrule(a,b)
	t=settime(gd)
 	return t
st={}
time1={}
tls_id=traci.trafficlight.getIDList()
control={}
for k in tls_id:
	st[k]=0	
	time1[k]=0
	control[k]=0
dict_t={}
def fix_time(dict2):
	
	for k in dict2:
		dict_t[k]=[]
		y_dict[k]={}
	
		temp=[]
		for i in dict2[k]:
			state=con[k][i]
			y_dict[k][state]=yellow[k][i]
			temp.append((i,10))
			temp.append((y_dict[k][state],5))
		dict_t[k]=temp	
	return dict_t

def matrix_weight(dict2,dict5):
        dict4={}
	temp={}
	ewait1={}
	for id1 in dict3:
		 list3={}
                 list2={}
		 w1=0
		 list1=dict3[id1]
		 for j in list1:
                        w,w2=0,[]
			edge_id=traci.lane.getEdgeID(j[0])
			count=0
			for k in j:
			    count+=1
                            w+=dict2[k]
                            w1+=dict2[k]
                            w2+=dict5[k]
			list2[edge_id]=w/count
			list3[edge_id]=w2
		
		 dict4[id1]=list2
		 temp[id1]=list3
	return dict4,temp
set1={}
wqr={}
def control_tls(step,p,q):
        
	for k in time1:
		if not time1[k]:
			time1[k]=dict_t[k]
			control[k]=0
        for k in time1:
		if control[k]%2==0:
                	if st[k]==step:            
                       		edge=time1[k][0][0]
				state=con[k][edge]
               			traci.trafficlight.setRedYellowGreenState(k,state)
				t=time1[k][0][1]+step
				set1[k]=set(q[k][edge])
				wqr[k]=p[k][edge]
				t1=step
			
			if st[k]+5==step:
				edge=time1[k][0][0]
				set2=set(q[k][edge])
				vfgreen=len(set2-set1[k])
				t=find_time(vfgreen,wqr[k])
				st[k]+=t	
				time1[k].pop(0)
				control[k]+=1
		else:
			if st[k]==step:
				state=time1[k][0][0]
				traci.trafficlight.setRedYellowGreenState(k,state)
				t=time1[k][0][1]+step
				st[k]=t
				control[k]+=1
				time1[k].pop(0)
def AQL():
	n=0
	for id1 in detectorids:
                i=traci.inductionloop.getLaneID(id1)
		n+=traci.lane.getLastStepHaltingNumber(i)
	print(n)
	return (n*2)//len(detectorids)
def ATF(temp12,temp1):
	count=0
	for i in temp12:
		set1=set(temp12[i])
		set2=set(temp1[i])
		count+=len(set1-set2)
	print(count)
	atf=float(count*6)//26
	return atf
def lane_waiting_time_speed():
	wt=0
	sp=0
	for i in list_lane:
		wt+=(traci.lane.getWaitingTime(i))
		sp+=traci.lane.getLastStepMeanSpeed(i)
	no=traci.vehicle.getIDCount()
	if no:
		wt=wt/no
	else:
		wt=0	
	return int(wt),int(sp)/len(list_lane)
aql=[]
awt=[]
asl=[]
atf=[]
atx=[]
k1=0
x=[]
count=0
while traci.simulation.getMinExpectedNumber()>0:
        traci.simulationStep()
	
        wqr1,dict5=Wqueue()
	if k1==0:
		temp12=copy.deepcopy(dict1)
	k1+=1	
	if k1==30:
		temp1=copy.deepcopy(dict1)
		atf.append(ATF(temp12,temp1))
		count+=30
		atx.append(count)
		k1=0
		aql.append(AQL())
		a1,b1=lane_waiting_time_speed()
		awt.append(waiting_time())
   		asl.append(b1)
	
	p,q=matrix_weight(wqr1,dict5)
	fix_time(p)	 
        control_tls(step,p,q)
        step+=1
        waiting_time()
	

print("aql",aql)
print("awt",awt)
print("as",asl)
print("atx",atx)

print("ATF",atf)
plt.plot(atx,awt,color='green')
plt.show()
traci.close()

