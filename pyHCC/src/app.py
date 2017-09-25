import configparser
from .interoperator import Interoperator
from .algorithm import *


def main():

  # Configurations
  config = configparser.ConfigParser()
  config.read('config.ini')

  # Load HCC Algorithm Engine
  load_facts()
  load_rules()

  # Execution method
  load_simple(config)
  return

def load_simple(config):

  # Load Data
  data = Interoperator(config=config)
  l = data.read_simplecsv_patients()


if __name__ == "__main__":
  main()

