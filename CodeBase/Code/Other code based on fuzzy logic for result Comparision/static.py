import os, sys
if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
else:   
     sys.exit("please declare environment variable 'SUMO_HOME'")
sumoBinary = "/usr/share/sumo/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "/home/dhakadnavin/Desktop/gwalior_map1/gwalior.sumocfg"]
import copy
import traci
traci.start(sumoCmd)
step=1
dict1={}
dict2={}
dict3={}
dict4={}
j_weight={}
detectorids = traci.inductionloop.getIDList()
for de in  detectorids:
           if de not in dict1:
	       dict1[de]=[]

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
def cal_weight(list1):
        weight=0
  	for vid  in list1:
          try:
		type1=traci.vehicle.getTypeID(vid)
		if(type1=="police"):
                       weight+=4
                elif(type1=="bus"):
                       weight+=4
		elif(type1=="truck"):
                       weight+=5
		elif(type1=="motorcycle"):
                       weight+=0.5
		elif(type1=="ambu"):
                       weight+=10
		elif(type1=="fire"):
                       weight+=10
                else:
                    weight+=1
	  except:
		print("")  
	return weight
def cross_detector():
        
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
	return dict1

	                 
        return dict1
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
def lane_weight():
	for key in dict1:
        	lane_id=traci.inductionloop.getLaneID(key)
	        dict2[lane_id]=cal_weight(dict1[key])
           
        return dict2	  
def matrix_weight():
        lane_weight()
	for id1 in dict3:
                 list2={}
		 w1=0
		 list1=dict3[id1]
		 for j in list1:
                        w=0
			edge_id=traci.lane.getEdgeID(j[0])
			for k in j:
                            w+=dict2[k]
                            w1+=dict2[k]
			list2[edge_id]=w
		 j_weight[id1]=w1
		 dict4[id1]=list2
	return dict4

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
		wt=int(wt/no)
	else:
		wt=0
	return wt,int(sp)/len(list_lane)

awt=[]
k=0
aql=[]
asl=[]
atf=[]
atx=[]
count=0		 	   
while traci.simulation.getMinExpectedNumber()>0 :
	traci.simulationStep()
	cross_detector()
	if k==0:
		temp12=copy.deepcopy(dict1)
	k+=1	
	if k==30:
		temp1=copy.deepcopy(dict1)
		atf.append(ATF(temp12,temp1))
		awt1,avgs=lane_waiting_time_speed()
		k=0
		atx.append(count)
		count+=30
		awt.append(waiting_time())
		aql.append(AQL())
   		asl.append(avgs)
        x=matrix_weight()
        
        
        step+=1
print("aql",aql)
print("awt",awt)
print("as",asl)
print("ATF",atf)
traci.close()
