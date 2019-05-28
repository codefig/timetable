begin_hour = 9;
begin_minute = 0;
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

class Arr(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.division = "";
		# super(ClassName, self).__init__()
		# self.arg = arg

	def arrange(self,subj_list, curr_time, free_lt,day,total_time,lect_t):
		#if the subj_list is empty, return
		if(len(subj_list) == 0):
			#print self.division;
			return

		#Get the current subject
		subj = subj_list.keys()[0];

		#Lets' check for friday. Make sure that 12-2 is free for prayers
		if(days[day] == 'Friday' and begin_hour+curr_time/60 == 12):
			print "Prayer Break";
			#Lets' reschedule for 2:30
			curr_time += 150;
			free_lt = {'compb':500, 'AST':250};

		#Let's check if the days' time is used up
		if(begin_hour+curr_time/60 >= 16):
			#Clear the time for the day and swicth to the next day
			curr_time = 0;
			if((day+1) >= len(days)):
				day = 0;
			else:
				day += 1;
			free_lt = {'compb':500, 'AST':250};
			self.division = self.division+"*************** "+days[day]+" ****************\n";
			#print "***************",days[day],"****************";

		#Get the current time and time after this exam
		#time_sch = time(curr_time);
		#Get the total hall capacity
		hall_capacity  = sum(free_lt.values());

		#check if the student number for the current subject is greater than the hall
		if(subj_list[subj] >= hall_capacity):

			#Reduce the number of student left for the course
			subj_list[subj] = subj_list[subj] - hall_capacity;

			#Print the hall division
			#print subj , free_lt.keys(); #, time_sch[0],":",time_sch[1] , "-> " , time_sch[2],":",time_sch[3];

			#check if the student left are 0 or positive
			if(subj_list[subj] <= 0):
				del subj_list[subj];
				time_start = timeStart(curr_time-(total_time));
				time_end= timeEnd(curr_time+30);
				#print "\t\t\t|",time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
				#print subj , lect_t,"\n";
				self.division = self.division + " "+subj+" "+lect_t+"| \t";
				self.division = self.division +str(time_start[0])+" : "+str(time_start[1]) + " -> " + str(time_end[0])+" : "+str(time_end[1])+"\n\n"
				
				#print "total time for",subj,"is",total_time+30;
				total_time = 0;
				lect_t = set([]);
			else:
				total_time += 30;
			#increase the time by 30 mins
			curr_time += 30;

			#The hall that would be free would be both
			free_lt = {'compb':500, 'AST':250};
			#That means the lecture theaters were used
			#Lets add the free lect_t 
			for lect in free_lt:
				lect_t.add(lect);
			#lect_t.update(free_lt.keys());

			#call back the function
			self.arrange(subj_list, curr_time, free_lt,day,total_time,lect_t);

		else:
			#Set the abitatry hall of the exam
			hall = 'n';

			for halls in free_lt:
				if(subj_list[subj] <= free_lt[halls]):
					if(hall == 'n'):
						hall = halls;
					if(free_lt[halls] < free_lt[hall]):
						hall = halls;

			#The class size is greater than each of the theater 		
			if hall =='n':
				#Reduce the number of student left for the course
				subj_list[subj] = subj_list[subj] - sum(free_lt.values());

				#Print the hall division
				#print subj , free_lt.keys() , time_sch[0],":",time_sch[1] , "-> " , time_sch[2],":",time_sch[3];

				#increase the time by 30 mins
				curr_time += 30;

				#The hall that would be free would be both
				free_lt = {'compb':500, 'AST':250};
				#Lets add the free lect_t 
				for lect in free_lt:
					lect_t.add(lect);

				#Check if this is an unfinished subject
				if(subj_list[subj] <= 0):
					time_start = timeStart(curr_time-(total_time));
					time_end= timeEnd(curr_time+30);
					#print "\t\t\t|",time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
					#print subj , lect_t,"\n";
					self.division = self.division + " "+subj+" "+lect_t+"| \t";
					self.division = self.division +str(time_start[0])+" : "+str(time_start[1]) + " -> " + str(time_end[0])+" : "+str(time_end[1])+"\n\n";
					

					#print "total time for",subj,"is",total_time+30;
					total_time = 0;
					lect_t = set([]);
				

				#Delete the subject since we are done with it
				if(subj_list[subj] <= 0):
					del subj_list[subj];

				#call back the function
				self.arrange(subj_list, curr_time, free_lt,day,total_time,lect_t);

			else:
				#Reduce the number of student left for the course
				subj_list[subj] = 0;

				
				#Print the hall division
				#print subj , hall , time_sch[0],":",time_sch[1], "-> " ,time_sch[2],":",time_sch[3];

				#remove the hall we are about to use
				del free_lt[hall];

				#Check if this is an unfinished subject
				if(subj_list[subj] == 0 ):
					time_start = self.timeStart(curr_time-total_time);
					time_end= self.timeEnd(curr_time+30);
					#print "\t\t\t|",time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
					#print subj , hall,"\n";# time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
					self.division = self.division + " "+subj+" "+hall+"| \t";
					self.division = self.division +str(time_start[0])+" : "+str(time_start[1]) + " -> " + str(time_end[0])+" : "+str(time_end[1])+"\n\n"
					

					#print "total time for",subj,"is",total_time+30;
					total_time = 0;
					lect_t = set([]);

				#if there is still a lecture theater left, then dont increase time, else do
				if(len(free_lt) == 0):
					curr_time += 30;
					free_lt = {'compb':500, 'AST':250};
					#lect_t.clear();
				
				#Delete the subject since we are done with it
				if(subj_list[subj] <= 0):
					del subj_list[subj];

				#call back the function
				self.arrange(subj_list, curr_time, free_lt,day,total_time,lect_t);
		return self.division;

	def timeStart(self,curr_time):
		start_hour = begin_hour+(curr_time/60);
		start_minute = begin_minute + (curr_time - (60*(curr_time/60)));
		time_sch = [start_hour, start_minute];
		return time_sch;

	def timeEnd(self,curr_time):
		end_hour = begin_hour+(curr_time/60);
		end_minute = begin_minute + (curr_time - (60*(curr_time/60)));
		time_sch = [end_hour, end_minute];
		return time_sch;
