#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import requests
import json
from schematics.models import Model
from schematics.types import StringType, URLType,IntType,BooleanType
from schematics.types.compound import MultiType, ModelType
from schematics.types.serializable import serializable

class Id(Model):
	id = IntType()		

class Task(Model):
	id 				= IntType()				
	backlog 		= MultiType(ModelType(Id))		
	blocked 		= BooleanType()		
	color 			= StringType()		
	creationDate 	= StringType()		
	creator 		= MultiType(ModelType(Id))		
	description 	= StringType()	
	doneDate 		= StringType()	
	estimation 		= IntType()		
	inProgressDate	= StringType()	
	initial 		= IntType()			
	lastUpdated		= StringType()	
	name 			= StringType()		
	notes 			= StringType()		
	parentStory 	= MultiType(ModelType(Id))	
	participants 	= MultiType(ModelType(Id))	
	rank			= IntType()			
	responsible 	= MultiType(ModelType(Id))		
	state 			= IntType()			
	type 			= StringType()		
	uid 			= IntType()				
	tags 			= MultiType(ModelType(Id))	
	comments 		= MultiType(ModelType(Id))

	@serializable
	def getState(self):
		if self.state == 0:
			return "Task"
		elif self.state == 1:
			return "in Progress"
		else:
			return "Done"

	@serializable
	def getUser(self):
		if task.responsible != None:
			id = task.responsible['id']
			if id == 102:
				return "user 102"
			elif id == 106:
				return "user 106"
			elif id == 107:
				return "user 107"
			else:
				return None



def restRequest(type):
    headers = {'Accept': 'application/json','Content-Type': 'application/json; charset=UTF-8'}
    uri = 'http://:server/ws/p/:pkey/'
    r = requests.get(uri+type,headers=headers,auth=('user', 'password'))
    return json.loads(unicode(r.text.encode('utf-8'), errors='ignore'))  

obj = restRequest('task')

Tasks = []

for o in obj:
	task = Task(o)
	Tasks.append(task)

sSum = 0
n = 0
done_sSum_sure = 0
done_sSum_task = 0

for task in Tasks:
	sSum +=  1
	if task.estimation != None:
		n += task.estimation
	if task.state == 2 :
		done_sSum_tim += task.estimation
		done_sSum_task += 1

print "Task : " ,sSum 
print "Sum Tim : ", n

print "------------------------------------------------------"
print "Done Task : " ,done_sSum_task 
print "Done Sum Tim : ", done_sSum_tim 
print "------------------------------------------------------"


for task in Tasks:
	if task.initial != None or task.estimation!= None:
		if task.getUser != None:
			print task.getUser,"-->", task.getState,"-> ", task.name, "-> initial:",task.initial ,"estimation:", task.estimation

