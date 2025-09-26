import pandas as pd
Customer={
    "cstmr_name":["Arjun","Anurag","Archana","Priyanshu","Akash"],
    "cstmr_age":[54,65,13,54,65],
    "cstmr_address":["Jaunpur","Agra","Mujaffarpur","Patna","Jaunpur"],
    "cstmr_gender":["M","M","F","M","M"]
}
Dtf=pd.DataFrame(Customer)
Dtf.to_csv("output.csv",index=False)