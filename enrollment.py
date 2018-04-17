import pandas as pd

if __name__=="__main__":
	data=pd.read_csv("data/CRDC2013_14.csv",encoding="Latin-1")
	data["total_enrollment"]=data["TOT_ENR_M"]+data["TOT_ENR_F"]
	all_enrollment=data["total_enrollment"].sum()
	US_population=325.7e6
	#education_per=(all_enrollment/US_population)*100 
	total_M=(data["TOT_ENR_M"].sum()/all_enrollment)*100
	total_F=(data["TOT_ENR_F"].sum()/all_enrollment)*100
	total_HI=((data["SCH_ENR_HI_M"].sum()+data["SCH_ENR_HI_F"].sum())/all_enrollment)*100
	total_AM=((data["SCH_ENR_AM_M"].sum()+data["SCH_ENR_AM_F"].sum())/all_enrollment)*100
	total_AS=((data["SCH_ENR_AS_M"].sum()+data["SCH_ENR_AS_F"].sum())/all_enrollment)*100
	total_HP=((data["SCH_ENR_HP_M"].sum()+data["SCH_ENR_HP_F"].sum())/all_enrollment)*100
	total_BL=((data["SCH_ENR_BL_M"].sum()+data["SCH_ENR_BL_F"].sum())/all_enrollment)*100
	total_WH=((data["SCH_ENR_WH_M"].sum()+data["SCH_ENR_WH_F"].sum())/all_enrollment)*100
	total_TR=((data["SCH_ENR_TR_M"].sum()+data["SCH_ENR_TR_F"].sum())/all_enrollment)*100
	print("Total Enrollment is US:", all_enrollment)
	#print("Education percent in US:",education_per)
	print("Total Male Enrollment percentage is:",total_M)
	print("Total Female Enrollment percentage is:", total_F)
	print("Hispanic per:", total_HI)
	print("Americal Indian per:", total_AM)
	print("Asian per:", total_AS)
	print("Hawaiian or Pacific Islander per:", total_HP)
	print("Black per:", total_BL)
	print("White per:", total_WH)
	print("Two or more Races per:", total_TR)
