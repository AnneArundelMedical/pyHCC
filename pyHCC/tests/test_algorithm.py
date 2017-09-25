from src import app

jane = app.Beneficiary(2,"female","19740824",app.EntitlementReason.DIB,True)
jane.add_diagnosis(app.Diagnosis(jane,"D66",app.ICDType.TEN))  
jane.add_diagnosis(app.Diagnosis(jane,"C182",app.ICDType.TEN))  
# 
daniel = app.Beneficiary(1,"male","19740824",app.EntitlementReason.DIB)
daniel.add_diagnosis(app.Diagnosis(daniel,"A0223",app.ICDType.TEN))  # 51
daniel.add_diagnosis(app.Diagnosis(daniel,"A0224",app.ICDType.TEN))  # 52
daniel.add_diagnosis(app.Diagnosis(daniel,"D66",app.ICDType.TEN))  
daniel.add_diagnosis(app.Diagnosis(daniel,"C163",app.ICDType.TEN))  
daniel.add_diagnosis(app.Diagnosis(daniel,"C163",app.ICDType.TEN))  
daniel.add_diagnosis(app.Diagnosis(daniel,"C182",app.ICDType.TEN))  
daniel.add_diagnosis(app.Diagnosis(daniel,"C800",app.ICDType.TEN))  
daniel.add_diagnosis(app.Diagnosis(daniel,"A072",app.ICDType.TEN))  
# 
bob = app.Beneficiary(3,"male","20040824",app.EntitlementReason.DIB,True)
bob.add_diagnosis(app.Diagnosis(bob,"A0223",app.ICDType.TEN))
bob.add_diagnosis(app.Diagnosis(bob,"A0224",app.ICDType.TEN))
# 
jacob = app.Beneficiary(4,"male","1940824",app.EntitlementReason.DIB,True)
# 
antonio = app.Beneficiary(3,"male","20040824",app.EntitlementReason.DIB,True)
antonio.add_diagnosis(app.Diagnosis(antonio,"A0223",app.ICDType.TEN))
antonio.add_diagnosis(app.Diagnosis(antonio,"49320",app.ICDType.NINE))
# 
john = app.Beneficiary(5,"male","19920824",app.EntitlementReason.DIB,True)
john.add_diagnosis(app.Diagnosis(john,"A0223",app.ICDType.TEN))
john.add_diagnosis(app.Diagnosis(john,"49320",app.ICDType.NINE))

app.get_hcc_score(daniel,"community")
app.get_hcc_score(daniel,"institutional")
app.get_hcc_score(daniel,"new_enrollee")
app.get_all_hcc_scores(daniel)['community']
app.get_all_hcc_scores(daniel)['institutional']
app.get_all_hcc_scores(daniel)['new_enrollee']
