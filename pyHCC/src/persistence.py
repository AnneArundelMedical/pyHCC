import os
import csv
from .models import Beneficiary, EntitlementReason, Diagnosis, ICDType

class Persistence():
  def __init__(self, config=None, **kwargs):
    self._config = config
    return super().__init__(**kwargs)

  def save_scores():
    raise NotImplementedError