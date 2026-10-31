import pandas as pd
import numpy as np

data=pd.read_csv("hospital_data.csv")
df=pd.DataFrame(data)


print("===========================================")
print("        Hospital Management System          ")
print("===========================================")
print("1. Display All Patients")
print("2. Add New Patients ")
print("3. Search Patients")
print("4. Update Patient")
print("5. Delete Patient")
print("6. Department-wise Patient Count")
print("7. Disease-wise Analysis")
print("8. Highest Hospital Bill")
print("9. Average Hospital Bill")
print("10. Show Pending Payments")
print("11. Sort Patients By Bill")
print("12. Save Data")
print("13. Exit")


# =====================project==================
while True:
    user=input("Choose the option:" )
    if user=="13":
        print("============= Exit ==============")
        break

    elif user=="1":
        print("========== All Patients Data ==========\n")
        print(df)
        print("total_patients :",len(df))

    elif user=="2":
        print("=========== Add New Patient ===========\n")
        Patient_ID=input("Enter the  patient_id:")
        Name=input("Enter the patient's_name:")
        Age=int(input("Enter the age:"))
        Gender=input("Enter the gender (M/F):")
        Department=input("Enter the department:")
        Disease=input("Enter the disease:")
        Doctor=input("Enter the doctor name:")
        Admission_Date=input("Enter the admission_date:")
        Discharge_Date=input("Enter the discharge_date:")
        Bill=int(input("Enter the bill:"))
        Payment=input("Is payment paid or pending?")

        df.loc[len(df)]=[Patient_ID,Name, Age, Gender, Department, Disease, Doctor, 
                         Admission_Date, Discharge_Date, Bill, Payment]
        print(df)

    elif user=="3":
        print("=========== Search Patient ==============")
        name=input("Enter the name:")
        patient=df[df["Name"].str.lower()==name.lower()]
        if patient.empty:
            print("Patient not found.")
        else:
            print(patient.T.to_string(header=False))

    elif user=="4":
        
        print(" ==========what you want to update============= ")
        print("1 Name")
        print("2 Age")
        print("3 Gender")
        print("4 Department")
        print("5 Disease")
        print("6 Doctor")
        print("7 Admission_Date")
        print("8 Discharge_Date")
        print("9 Bill")
        print("10 Payment")
        print("11 Exit")


        Patient_ID=input("enter the patient_id:")
        while True:
            choice=input("enter the choice:")

            if choice=="11":
                print("================ Exit ===============")
                break

            elif choice=="1":
                Name=input("Enter the patient's_name:")
                df.loc[df["Patient_ID"].str.lower()==Patient_ID.lower(),"Name"]=Name

            elif choice=="2":
                Age=input("Enter the patient's_Age:")
                df.loc[df["Patient_ID"].str.lower()==Patient_ID.lower(),"Age"]=Age

            elif choice=="3":
                Gender=input("Enter the patient's_Gender:")
                df.loc[df["Patient_ID"].str.lower()==Patient_ID.lower(),"Gender"]=Gender

            elif choice=="4":
                Department=input("Enter the Department:")
                df.loc[df["Patient_ID"].str.lower()==Patient_ID.lower(),"Department"]=Department

            elif choice=="5":
                Disease=input("Enter the Disease:")
                df.loc[df["Patient_ID"].str.lower()==Patient_ID.lower(),"Disease"]=Disease

            elif choice=="6":
                Doctor=input("Enter the Doctor:")
                df.loc[df["Patient_ID"].str.lower()==Patient_ID.lower(),"Doctor"]=Doctor

            elif choice=="7":
                Admission_Date=input("Enter the admission_date:")
                df.loc[df["Patient_ID"].str.lower()==Patient_ID.lower(),"Admission_Date"]=Admission_Date

            elif choice=="8":
                Discharge_Date=input("Enter the Discharge_date:")
                df.loc[df["Patient_ID"].str.lower()==Patient_ID.lower(),"Discharge_Date"]=Discharge_Date

            elif choice=="9":
                Bill=input("Enter the Bill:")
                df.loc[df["Patient_ID"].str.lower()==Patient_ID.lower(),"Bill"]=Bill

            elif choice=="10":
                Payment=input("Enter the Payment:")
                df.loc[df["Patient_ID"].str.lower()==Patient_ID.lower(),"Payment"]=Payment

    elif user =="5":
        print("================ Delete The Patient =================")
        patient=input("enter the patient id:")
        df.drop(df[df["Patient_ID"].str.lower() == patient.lower()].index ,inplace=True)
        print(df)

    elif user=="6":
        print("=============== Department-wise Patient Count ==============")
        abc=df.groupby("Department")["Patient_ID"].count()
        print(abc)

    elif user=="7":
        print("=============== Disease-wise Analysis =================")
        bcd=df.groupby("Disease")["Patient_ID"].count()
        print(bcd)

    elif user=="8":
        print("=============== Highest Hospital Bill =================")
        max_bill=df[df["Bill"]==df["Bill"].max()]
        print(max_bill.T.to_string(header=False))

    elif user=="9":
        print("================ Averagr Hospital Bill ================")
        avg_bill=df["Bill"].mean()
        print("Average_bill :",avg_bill)

    elif user=="10":
        print("=============== Pending Bills ========================")
        pending_bill=df[df["Payment"].str.lower()=="pending"] [["Patient_ID","Name"]]
        print(pending_bill.to_string(index=False))
        

    elif user=="11":
        print("=============== Data Sorted By Bill =================")
        sorted_data=df.sort_values(by="Bill")
        sorted_data.reset_index(drop=True)

    elif user=="12":
        print("================ Save Data ==================")
        df.to_csv("Hospital.csv",index=False)

    

     




















