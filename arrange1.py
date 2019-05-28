begin_hour = 9;
begin_minute = 0;
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

def arrange(subj_list, curr_time, free_lt,day,total_time):

	#if the subj_list is empty, return
	if(len(subj_list) == 0):
		return;

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
		print "***************",days[day],"****************";

	#Get the current time and time after this exam
	#time_sch = time(curr_time);
	#Get the total hall capacity
	hall_capacity  = sum(free_lt.values());

	#check if the student number for the current subject is greater than the hall
	if(subj_list[subj] >= hall_capacity):
		#Reduce the number of student left for the course
		subj_list[subj] = subj_list[subj] - hall_capacity;

		#Print the hall division
		print subj , free_lt.keys(); #, time_sch[0],":",time_sch[1] , "-> " , time_sch[2],":",time_sch[3];

		#check if the student left are 0 or positive
		if(subj_list[subj] <= 0):
			del subj_list[subj];
			total_time = 0;
		else:
			total_time += 30;
		#increase the time by 30 mins
		curr_time += 30;

		#The hall that would be free would be both
		free_lt = {'compb':500, 'AST':250};

		#call back the function
		arrange(subj_list, curr_time, free_lt,day,total_time);

	else:
		#Set the abitatry hall of the exam
		hall = 'n';

		for halls in free_lt:
			if(subj_list[subj] <= free_lt[halls]):
				hall = halls;

		if hall =='n':
			#Reduce the number of student left for the course
			subj_list[subj] = 0;

			#Print the hall division
			#print subj , free_lt.keys() , time_sch[0],":",time_sch[1] , "-> " , time_sch[2],":",time_sch[3];

			#Delete the subject since we are done with it
			del subj_list[subj];

			#increase the time by 30 mins
			curr_time += 30;

			#The hall that would be free would be both
			free_lt = {'compb':500, 'AST':250};

			#Check if this is an unfinished subject
			if(total_time > 0):
				time_start = timeStart(curr_time-(total_time));
				time_end= timeEnd(curr_time+30);
				print "\t\t\t|",time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
				print subj , hall,"\n";
				#print "total time for",subj,"is",total_time+30;
				total_time = 0;
			else:
				print subj , free_lt.keys();

			#call back the function
			arrange(subj_list, curr_time, free_lt,day,total_time);

		else:
			#Reduce the number of student left for the course
			subj_list[subj] = 0;

			#Delete the subject since we are done with it
			del subj_list[subj];

			#Print the hall division
			#print subj , hall , time_sch[0],":",time_sch[1], "-> " ,time_sch[2],":",time_sch[3];

			#remove the hall we are about to use
			del free_lt[hall];

			#if there is still a lecture theater left, then dont increase time, else do
			if(len(free_lt) == 0):
				curr_time += 30;
				free_lt = {'compb':500, 'AST':250};

			#Check if this is an unfinished subject
			if(total_time > 0):
				time_start = timeStart(curr_time-total_time);
				time_end= timeEnd(curr_time+30);
				print "\t\t\t|",time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
				print subj , hall,"\n";# time_start[0],":",time_start[1] , "-> " , time_end[0],":",time_end[1];
				#print "total time for",subj,"is",total_time+30;
				total_time = 0;
			else:
				print subj , hall;

			#call back the function
			arrange(subj_list, curr_time, free_lt,day,total_time);

def timeStart(curr_time):
	start_hour = begin_hour+(curr_time/60);
	start_minute = begin_minute + (curr_time - (60*(curr_time/60)));
	time_sch = [start_hour, start_minute];
	return time_sch;

def timeEnd(curr_time):
	end_hour = begin_hour+(curr_time/60);
	end_minute = begin_minute + (curr_time - (60*(curr_time/60)));
	time_sch = [end_hour, end_minute];
	return time_sch;

# def time(curr_time):
# 	start_hour = begin_hour+(curr_time/60);
# 	start_minute = begin_minute + (curr_time - (60*(curr_time/60)));
# 	#To get the end hour, add 30 min to the curr_time
# 	curr_time += 30;
# 	end_hour = begin_hour+(curr_time/60);
# 	end_minute = begin_minute + (curr_time - (60*(curr_time/60)));
# 	time_sch = [start_hour, start_minute, end_hour, end_minute];
# 	return time_sch;

print "***************",days[0],"****************";
arrange({'agric':1500,'chemistry':1250,
'math':2000, 
'FST':4000, 
'AG':1250,
'ANOTHER':800,
"AMAKa":530},0,{'compb':500, 'AST':250},0,0);