import pandas as pd
import numpy as np

def Data_Load(file_path) :

    """ Load A Data Of Any Type """

    data = str(file_path)
    if data.endswith(".csv"):
        d = pd.read_csv(data)

    elif data.endswith(".xlsx"):
        d = pd.read_excel(data)

    elif data.endswith(".json"):
        d = pd.read_json(data)
        
    else:
        print("Invalid Data")  
    return d      




def Data_save(file_path,data,extance) :

    """ Load A Data Of Any Type """

    d = str(file_path)
    if extance == ".csv":
        d = data.to_csv(f"{d}/clean_data.csv")
        print("File Save")

    elif extance == ".xlsx":
        d = data.to_excel(f"{d}/clean_data.xlsx")

    elif extance == ".json":
        d = data.to_json(f"{d}/clean_data.json")
        
    else:
        print("Invalid Data")       


def Show_Data_Type(data) :
    """Show All Data Type"""

    return data.dtypes
    

def Change_Data_Type_into_Number(data , col):
     """ Number Data Type in Convert"""
     data[col] = pd.to_numeric(data[col],errors = 'coerce')



def Change_Data_Type_into_Date(data , col):
     """ Date Data Type in Convert"""
     data[col] = pd.to_datetime(data[col],errors = 'coerce')


def Change_Data_Type_into_Category(data , col):
     """ Category Data Type in Convert"""
     data[col] = data[col].astype("category")


def Missing_Value_Show(data):

     """ Show the Number Of Missing Value """
     d =  data.isnull().sum()
     return d


def Numberic_Value_Handel(data,col):
    """ Numberic Value Fill By Mean"""
    d = data[col] = data[col].fillna(data[col].mean())
    return d


def Category_Value_Handel(data,col):
    """ Categorical Data Fill Random"""
    val = data[col].isna()
    data.loc[val,col]=np.random.choice(data[col].dropna(),size=val.sum())


def Remove_Missing_Value(data):
    """ Remove Missing Value"""
    return data.dropna(axis=0,inplace=True)


def Show_Duplicated_Value(data):
    """ Display Duplicated Value"""
    return data.duplicated().sum() 

def Show_Duplicated_Coumn(data,col):
    """ Sepcifix Column In Show Duplicated"""
    return data[col].duplicated().sum() 

def Remove_Dupicated_Value(data):
    """ Remove Duplicated Value"""
    data = data.drop_duplicates(inplace=True)
    return data


def Drop_Any_Column(data,col):
    "Drop Any Column"
    data.drop(col,axis=1,inplace=True)
    return data

def Show_Data_Info(data):
    """ Show Information Dataset"""
    return data.info()


def Summery_Data(data):
    """ Describe Dataset"""
    return data.describe()


def Dataset_Short_Summery(data):
    """  Show Row And Cloumn"""
    print("Data Set Shape",data.shape)
    print("Data Set All Cloumn",data.columns)
    print("Total Rows",data.shape[0])
    print("Total Cloumn",data.shape[1])


def Data_In_Value(data):
    """ Data Quality Show"""
    for i in data.columns:
        print(data[i].value_counts())
    

def Category_Object_Value(data):
    """  Value Clean"""
    slect = data.select_dtypes(include=object)
    for i in slect:
        print(data[i].str.title()) 

    print()
    select1 = data.select_dtypes(include="number")

    for i in select1:
            print(abs(data[i]))   
     


def Data_Quality_Report(data):

    report = pd.DataFrame({
        "Column":data.columns,
        "Unique Value":data.nunique(),
        "Missing Value":data.isnull().sum(),
        "Duplicate":[ data[i].duplicated().sum() for i in data.columns],
        "Data Type":data.dtypes.astype(str)
    })

    return report