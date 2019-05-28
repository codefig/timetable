from bisect import bisect_right,bisect_left;
from copy import copy;
class written_exams(object):
	"""docstring for written_exams"""
	def __init__(self,subj_list):
		self.lect_theater = {'JAO3':700, 'MP01':400, 'CAPLT':400};
		self.lect_theater_turbo = {'JAO3':1300, 'MP01':600, 'CAPLT':1400};
		self.lect_t = {'JAO3':700, 'MP01':400, 'CAPLT':400}; #Lecture theater capacity for one course 
		self.lect_ts = [] #For combinig lecture theaters
		self.lect_turbo = {'JAO3':1000, 'MP01':600, 'CAPLT':1400} #Lecture theatre for 2 courses
		self.subj_list = subj_list; #Assign the subject a state
		self.begin_hour = 9; #When the exam began
		self.begin_minute = 0;#When the exam began
		self.time_hour = 9; #Number of hours for the exam
		self.time_minute = 0; #	Number of minutes for the exam
		self.past_minute = 0; #Save the time that has elapsed since first exam
		print "====================",self.time_hour,":",self.time_minute," AM =======================";


	#Function for starting the arrange operation
	def arrange(self):
		if(len(self.subj_list.keys()) <= 0):
			return;
		elif (len(self.lect_t.keys()) <= 0):
			#No more lecture theater at the time, increase time to end of examinations
			#####print "No more time or theater for now";#####
			self.past_minute += 120;
			self.time_hour = self.begin_hour + self.past_minute/60; #increase by number of time for the exam
			self.time_minute = self.begin_minute + (self.past_minute - (60*(self.past_minute/60))); #Increase by number of minutes for the exam
			self.lect_t = copy(self.lect_theater);
			self.lect_turbo = copy(self.lect_theater_turbo);
			print "====================",self.time_hour,":",self.time_minute," AM =======================";

		#Lets' get the first subject
		subject = self.subj_list.keys()[self.subj_list.values().index(max(self.subj_list.values()))];
		#For the each subject, lets' find a lt that is just perfect for the course
		try:
			#Check if there is a perfect fit. If there is, let's see if there is a class that can join them in turbo
			lect_t = self.lect_t.keys()[self.lect_t.values().index(self.subj_list[subject])];
			#####print "Found a perfect fit for ", subject;#####
			self.find_friend(lect_t,subject,False);
			self.arrange();
		except (ValueError,IndexError) as e:
			#No lecture theatre fits the class size
			#####print "No lecture theatre found that matches", subject, "perfectly";#####
			#Lets find the smallest lecture theater that is greater than the size
			lect_t_list = self.lect_t.values(); #get the values as list
			lect_t_list.sort(); #Sort so we can use the bisect right function
			try:
				#Lets find the theater that can fit
				lect_t = self.lect_t.keys()[self.lect_t.values().index(lect_t_list[bisect_right(lect_t_list,self.subj_list[subject])])];
				#####print lect_t, "would contain but is larger" ;#####
				#Now lets see if we could find a class to join them in their turbo mode
				self.find_friend(lect_t,subject,False);
				self.arrange();
			except (ValueError,IndexError) as e:
				#No lecture theater fits perfectly, so the class is quite big, lets' find the perfect combination of lect_t
				#####print "All theater are smaller than the class size"#####
				#TODO: Try turbo first
				#Lets' check if a theater in turbo mode would be big enough and we could find a partner for it
				#Lets find the smallest lecture theater that is greater than the size
				lect_t_list = self.lect_turbo.values(); #get the values as list
				lect_t_list.sort(); #Sort so we can use the bisect right function
				try:
					#Lets find the biggest free turbo theater that can fit it
					lect_t = self.lect_turbo.keys()[self.lect_turbo.values().index(max(self.lect_turbo.values()))];
					if(self.subj_list[subject] == self.lect_turbo[lect_t]):
						#####print "Perfect match is not allowed for turbo";#####
						raise ValueError;
					else:
						#####print lect_t, "would contain but is larger";#####
						#Now lets see if we could find a class to join them in their turbo mode
						if(self.find_friend(lect_t,subject,True) == -1):
							raise ValueError;
						else:
							self.arrange();

				except (ValueError,IndexError) as e:
					#####print self.lect_t.keys();#####
					#First get the biggest lecture theater
					biggest_lect_t = max(self.lect_t.values());
					#Get the lect_t
					lect_t = self.lect_t.keys()[self.lect_t.values().index(biggest_lect_t)];
					#Lets insert it into the list
					self.lect_ts.append(lect_t);
					#Lets' remove that theater
					del self.lect_t[lect_t];
					del self.lect_turbo[lect_t];
					#Find the space needed to occupy the student size
					needed_space = self.subj_list[subject] -  biggest_lect_t;		
					self.find_lect_t_friend(needed_space);
					#TODO: Add a function to find if a subject could join the combination
					#Going naive now
					sum_lecture_t = 0;
					for lects in self.lect_ts:
						sum_lecture_t = sum_lecture_t + self.lect_theater_turbo[lects];

					#The remaining space on turbo
					total_segmented_space = sum_lecture_t - self.subj_list[subject];
					#Lets find the largest class smaller than the space left
					#Get the values of the subject and sort them for the binary search
					subj_list_values = self.subj_list.values();
					temp_subj_list_value = self.subj_list.values();
					subj_list_values.remove(self.subj_list[subject]);
					temp_subj_list_value.remove(self.subj_list[subject]);
					subj_list_values.sort();
					#The subject list excluding the current subject
					subj_list_keys = self.subj_list.keys();
					subj_list_keys.remove(subject);
					#Now lets find the subject that has the largest class smaller than the left space
					try:
						joining_subject = subj_list_keys[temp_subj_list_value.index(subj_list_values[bisect_right(subj_list_values,total_segmented_space)-1])];
						if(self.subj_list[joining_subject] > total_segmented_space):
							raise ValueError;
						#####print "subject to merge with in turbo ", joining_subject;#####
						print "\n",joining_subject;
						#Lets' delete the joining subject
						del self.subj_list[joining_subject];
					except (ValueError,IndexError) as e:
						print "";
					#Clear the list of combined lecture theaters
					self.lect_ts = [];
					#Lets' delete the subject
					del self.subj_list[subject];
					self.arrange();

	#Generic functoin for formated printing
	def print_table(self,subject,joining_subject,lect_t):
		if joining_subject == "":
			print "\n",subject, "=====>\t", lect_t, "\n";
		else:
			print "\n",subject,"\n\t", "=====>", lect_t, "\n",joining_subject;

	#For finding another class to join a class 
	def find_friend(self,lect_t,subject,throttle):
		left_space = self.lect_turbo[lect_t] - self.subj_list[subject];
		#Get the values of the subject and sort them for the binary search
		subj_list_values = self.subj_list.values();
		temp_subj_list_value = self.subj_list.values();
		subj_list_values.remove(self.subj_list[subject]);
		temp_subj_list_value.remove(self.subj_list[subject]);
		subj_list_values.sort();
		#The subject list excluding the current subject
		subj_list_keys = self.subj_list.keys();
		subj_list_keys.remove(subject);
		#Now lets find the subject that has the largest class smaller than the left space
		try:
			joining_subject = subj_list_keys[temp_subj_list_value.index(subj_list_values[bisect_right(subj_list_values,left_space)-1])];
			if(self.subj_list[joining_subject] > left_space):
				raise ValueError;
			#####print "subject to merge with in turbo ", joining_subject;#####
			self.print_table(subject,joining_subject,lect_t);
			#Now, lets remove this classes and subject to start looking for next classes
			del self.subj_list[subject];
			del self.subj_list[joining_subject];
			del self.lect_t[lect_t];
			del self.lect_turbo[lect_t];
			return;
		except (ValueError,IndexError) as e:
			#No class found that can be merged with the class, which means classes are bigger than the turbo spaces.
			#####print "No class to merge with ", subject;#####
			if(throttle):
				return -1;
			self.print_table(subject,"",lect_t);
			#Now, lets remove this classes and subject to start looking for next classes
			del self.subj_list[subject];
			del self.lect_t[lect_t];
			del self.lect_turbo[lect_t];
			return;

	#This function finds the lecture thearters tht accomodates a big class
	def find_lect_t_friend(self,needed_space):
		#First check if there are free lecture theater
		#TODO: Check other subject with the lecture theaters left
		#SOLUTION: Sort the subject in ascending order
		if(len(self.lect_t.keys()) <= 0):
			#No more lecture theater at the time, increase time to end of examinations
			return;

		#We need the subject
		subject = self.subj_list.keys()[self.subj_list.values().index(max(self.subj_list.values()))];
		#We need the list of theaters
		lect_t_list = self.lect_t.values();
		lect_t_list.sort();
		#We will find the largest lecture_t not larger than the needed space that would fit the class
		joining_lect_t = self.lect_t.keys()[self.lect_t.values().index(lect_t_list[bisect_right(lect_t_list,needed_space)-1])];
		#Lets add the lecture theaters to the list
		self.lect_ts.append(joining_lect_t);
		if(self.lect_t[joining_lect_t] < needed_space):
			#The lecture theaters could still not occupy it, lets add more theaters
			#Lets find the remaining space needed
			needed_space = self.subj_list[subject] - (needed_space + self.lect_t[joining_lect_t]);
			#Lets' remove the theater
			del self.lect_t[joining_lect_t];
			del self.lect_turbo[joining_lect_t];
			self.find_lect_t_friend(needed_space);
		else:
			#Found the best combination without turbo mode
			print "\n",subject
			for lect_t in self.lect_ts:
				print "\t=====>", lect_t;
			#Lets' remove the theater
			del self.lect_t[joining_lect_t];
			del self.lect_turbo[joining_lect_t];
			return;


classify = written_exams({'AGRIC':800,'MATH':1400,'CHEMISTRY':2000,'PHYSICS':900,'LIT':500,'POL':400,'math':2000, 
'FST':4000, 
'AG':1250,
'ANOTHER':800,
"AMAKa":530});
classify.arrange();
		