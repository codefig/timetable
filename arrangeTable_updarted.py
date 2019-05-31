from copy import deepcopy

class Arr(object):
	"""docstring for ClassName"""
	def __init__(self,halls,subj_list,total_time,lect_t):
		self.free_lt = deepcopy(halls);
		self.total_time = 0;
		self.lect_t = [];
		self.subj_list = deepcopy(subj_list);
		self.curr_time = 0;
		self.division = "";
		self.halls = deepcopy(halls);
		self.begin_hour = 9;
		self.begin_minute = 0;
		self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
		self.day = 0;
		# super(ClassName, self).__init__()
		# self.arg = arg

	def arrange(self):
		#if the subj_list is empty, return
		if(len(self.subj_list) == 0):
			#print self.division;
			return

		#Get the current subject
		subj = self.subj_list.keys()[0];

		#Lets' check for friday. Make sure that 12-2 is free for prayers
		if(self.days[self.day] == 'Friday' and self.begin_hour+self.curr_time/60 == 12):
			print "Prayer Break";
			#Lets' reschedule for 2:30
			self.curr_time += 150;
			#free_lt = {'compb':500, 'AST':250};
			self.free_lt = deepcopy(self.halls);

		#Let's check if the days' time is used up
		if(self.begin_hour+self.curr_time/60 >= 16):
			#Clear the time for the day and swicth to the next day
			self.curr_time = 0;
			if((self.day+1) >= len(self.days)):
				self.day = 0;
			else:
				self.day += 1;
			self.free_lt = deepcopy(self.halls);
			self.division = self.division+"*************** "+self.days[self.day]+" ****************\n";
			#print "***************",days[day],"****************";

		#Get the current time and time after this exam
		#time_sch = time(curr_time);
		#Get the total hall capacity
		hall_capacity  = sum(self.free_lt.values());

		#check if the student number for the current subject is greater than the hall
		if(self.subj_list[subj] >= hall_capacity):

			#Reduce the number of student left for the course
			self.subj_list[subj] = self.subj_list[subj] - hall_capacity;

			#Print the hall division
			#print subj , free_lt.keys(); #, time_sch[0],":",time_sch[1] , "-> " , time_sch[2],":",time_sch[3];

			#check if the student left are 0 or positive
			if(self.subj_list[subj] <= 0):
				del self.subj_list[subj];
				time_start = timeStart(self.curr_time-(self.total_time));
				time_end= timeEnd(self.curr_time+30);
				#print "\t\t\t|",time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
				#print subj , lect_t,"\n";
				self.division = self.division + " "+subj+" "+self.lect_t+"| \t";
				self.division = self.division +str(time_start[0])+" : "+str(time_start[1]) + " -> " + str(time_end[0])+" : "+str(time_end[1])+"\n\n"
				
				#print "total time for",subj,"is",total_time+30;
				self.total_time = 0;
				self.lect_t = set([]);
			else:
				self.total_time += 30;
			#increase the time by 30 mins
			self.curr_time += 30;

			#The hall that would be free would be both
			self.free_lt = deepcopy(self.halls);
			#That means the lecture theaters were used
			#Lets add the free lect_t 
			for lect in self.free_lt:
				self.lect_t.add(lect);
			#lect_t.update(free_lt.keys());

			#call back the function
			self.arrange();

		else:
			#Set the abitatry hall of the exam
			hall = 'n';

			for halls in self.free_lt:
				if(self.subj_list[subj] <= self.free_lt[halls]):
					if(hall == 'n'):
						hall = halls;
					if(self.free_lt[halls] < self.free_lt[hall]):
						hall = halls;

			#The class size is greater than each of the theater 		
			if hall =='n':
				#Reduce the number of student left for the course
				self.subj_list[subj] = self.subj_list[subj] - sum(self.free_lt.values());

				#Print the hall division
				#print subj , free_lt.keys() , time_sch[0],":",time_sch[1] , "-> " , time_sch[2],":",time_sch[3];

				#increase the time by 30 mins
				self.curr_time += 30;

				#The hall that would be free would be both
				self.free_lt = deepcopy(self.halls);
				#Lets add the free lect_t 
				for lect in self.free_lt:
					self.lect_t.add(lect);

				#Check if this is an unfinished subject
				if(self.subj_list[subj] <= 0):
					time_start = timeStart(self.curr_time-(self.total_time));
					time_end= timeEnd(self.curr_time+30);
					#print "\t\t\t|",time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
					#print subj , lect_t,"\n";
					self.division = self.division + " "+subj+" "+self.lect_t+"| \t";
					self.division = self.division +str(time_start[0])+" : "+str(time_start[1]) + " -> " + str(time_end[0])+" : "+str(time_end[1])+"\n\n";
					

					#print "total time for",subj,"is",total_time+30;
					self.total_time = 0;
					self.lect_t = set([]);
				

				#Delete the subject since we are done with it
				if(self.subj_list[subj] <= 0):
					del self.subj_list[subj];

				#call back the function
				self.arrange();

			else:
				#Reduce the number of student left for the course
				self.subj_list[subj] = 0;

				
				#Print the hall division
				#print subj , hall , time_sch[0],":",time_sch[1], "-> " ,time_sch[2],":",time_sch[3];

				#remove the hall we are about to use
				del self.free_lt[hall];

				#Check if this is an unfinished subject
				if(self.subj_list[subj] == 0 ):
					time_start = self.timeStart(self.curr_time-self.total_time);
					time_end= self.timeEnd(self.curr_time+30);
					#print "\t\t\t|",time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
					#print subj , hall,"\n";# time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
					self.division = self.division + " "+subj+" "+hall+"| \t";
					self.division = self.division +str(time_start[0])+" : "+str(time_start[1]) + " -> " + str(time_end[0])+" : "+str(time_end[1])+"\n\n"
					

					#print "total time for",subj,"is",total_time+30;
					self.total_time = 0;
					self.lect_t = set([]);

				#if there is still a lecture theater left, then dont increase time, else do
				if(len(self.free_lt) == 0):
					self.curr_time += 30;
					self.free_lt = {'compb':500, 'AST':250};
					#lect_t.clear();
				
				#Delete the subject since we are done with it
				if(self.subj_list[subj] <= 0):
					del self.subj_list[subj];

				#call back the function
				self.arrange();
		return self.division;

	def timeStart(self,curr_time):
		start_hour = self.begin_hour+(curr_time/60);
		start_minute = self.begin_minute + (curr_time - (60*(curr_time/60)));
		time_sch = [start_hour, start_minute];
		return time_sch;

	def timeEnd(self,curr_time):
		end_hour = self.begin_hour+(curr_time/60);
		end_minute = self.begin_minute + (curr_time - (60*(curr_time/60)));
		time_sch = [end_hour, end_minute];
		return time_sch;
