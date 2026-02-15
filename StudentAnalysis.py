import pandas as pd
import os 
                                  
df = pd.read_csv("students.csv")             #Importing csv file raw student data for analysis of students 
print(df)

print(df.groupby("City")["Percentile"].mean())     #Checking City wise average marks of Student 

print(df.groupby("City").agg(
    Average_percentile = ("Percentile","mean"),          #Checking all Maximum and Minimum , Average marks of student for better
    Maximum_percentile = ("Percentile","max"),           #analyizing the performance city wise of student 
    Minimum_percentile = ("Percentile","min")
))

result = df.groupby(["City","Gender"]).agg(                #Checking all Average, Maximum and Minimum percentile City and Gender wise
    Average_Percentile = ("Percentile","mean"),           #to check which is making best performance Female or Male city wise 
    Maximum_Percentile = ("Percentile","max"),
    Minimum_Percentile = ("Percentile","min")
)

result = result.reset_index()                      
print(result)

print(df.iloc[0:4,0:4])   #selecting rows and columns 
print(df.iloc[:,-1])     #Selecting last column
print(df.iloc[-1])      #last row 
df.iloc[0:1,4] = 89     #Changing at a particular position 
print(df)


Top_Student_index = result["Maximum_Percentile"].idxmax()           #checking top student percentile and which city he belong                
print(result.loc[Top_Student_index])

Lower_Student_index = result["Minimum_Percentile"].idxmin()        #checking lower percentile student and which city he belong 
print(result.loc[Lower_Student_index])

start = df.loc[df.groupby("City")["Percentile"].idxmax()]       #Finding Topper form each City 
print(start)

result_N = df.loc[df["City"].isin(["Pune","Nashik"]) &        #Finding that students that belongs to Nashik and Pune whoose percentile is between 95 to 99
                  df["Percentile"].between(95,99
                                           )]
df["Avg_Percentile_City"] = df.groupby("City")["Percentile"].transform("mean")   #adding new column that show average of each city 
print(result_N)
print(df)
print(df.to_excel("StudentAna.xlsx",index = False))    #Creating a file of excel that can store this data properly row and column
                                                       #wise 

File_path = r"C:\Users\HP\Abhijeet Jagtap\python\StudentAna.xlsx"     #File_path the file where excel file("StudentAna") is located
os.startfile(File_path)           #opening file to excel format directly 




