from enum import Enum,IntEnum
from datetime import datetime
from pyDatalog import pyDatalog

class EntitlementReason(IntEnum):
  OASI=0
  DIB=1
  ESRD=2
  DIB_AND_ESRD = 3

class ICDType(IntEnum):
  NINE = 9
  TEN = 0

class Diagnosis(pyDatalog.Mixin):
  def __init__(self,
              beneficiary,
              icdcode,
              codetype=ICDType.NINE):
    super().__init__()
    self.beneficiary = beneficiary
    self.icdcode = icdcode
    self.codetype = codetype

  def __repr__(self): # specifies how to display an Employee
    return str(self.beneficiary) + str(self.icdcode) + str(self.codetype)

class Beneficiary(pyDatalog.Mixin):
  def __init__(self, hicno
              ,sex,dob,
              original_reason_entitlement=EntitlementReason.OASI,
              medicaid=False,
              newenrollee_medicaid=False,):
    super().__init__()
    self.hicno = hicno
    self.sex = sex
    self.dob = datetime.strptime(dob,"%Y%m%d")
    self.age = age_as_of(self.dob,datetime.now())
    self.medicaid = medicaid
    self.newenrollee_medicaid = newenrollee_medicaid
    self.original_reason_entitlement = original_reason_entitlement
    self.diagnoses = []

  def __repr__(self): # specifies how to display an Employee
    return "ID:" + str(self.hicno) + ",DOB:" + str(self.dob)

  def add_diagnosis(self,diag):
    self.diagnoses.append(diag)

def age_as_of(dob,date_as_of):
  return date_as_of.year - dob.year - ((date_as_of.month, date_as_of.day) < (dob.month, dob.day))
