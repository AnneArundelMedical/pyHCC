import os
import csv
from .models import Beneficiary, EntitlementReason, Diagnosis, ICDType
#import xmltodict
#import pysftp

class Interoperator():
  def __init__(self, config=None, **kwargs):
    self._config = config
    return super().__init__(**kwargs)

  def read_simplecsv_patients(self):
    rtn_patient_list = {}
    with open(os.path.join(self._config['DEFAULT']['BaseRepoDirectory'],"data\\input\\simplecsv\\patient.csv")) as f:
      reader = csv.DictReader(f)
      for l in reader:
        derived_uuid = "{0}|{1}".format(l['PatientId'],l['PatientIdType'])
        pat = Beneficiary(derived_uuid,l['PatientSex'],str(l['PatientDateOfBirth']),EntitlementReason[l['PatientEntitlementReason']])
        pat.add_diagnosis(Diagnosis(pat,"A0223",ICDType.TEN))  # 51
        pat.add_diagnosis(Diagnosis(pat,"A0224",ICDType.TEN))  # 52
        rtn_patient_list[derived_uuid] = pat

    return rtn_patient_list

  def read_simplecsv_diagnoses():
    raise NotImplementedError

  def read_cclf_patients():
    raise NotImplementedError

  def read_cclf_diagnoses():
    raise NotImplementedError
