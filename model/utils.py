
import pickle
import json
import pandas as pd
import numpy as np
import config


class HousePrice():
    def __init__ (self,CRIM,ZN,
  INDUS,
  CHAS,
  NOX,
  RM,
  AGE,
  DIS,
  RAD,
  TAX,
  PTRATIO,
  B,
  LSTAT):
        self.CRIM = CRIM
        self.ZN = ZN
        self.INDUS = INDUS
        self.CHAS = CHAS
        self.NOX = NOX
        self.RM = RM
        self.AGE = AGE
        self.DIS = DIS
        self.RAD = RAD
        self.TAX = TAX
        self.PTRATIO = PTRATIO
        self.B = B
        self.LSTAT = LSTAT
        

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):

        self.load_model()  # Calling load_model method to get model and json_data

        
        array = np.zeros(len(self.json_data['column']))

        array[0]=self.CRIM
        array[1]=self.ZN
        array[2]=self.INDUS
        array[3]=self.CHAS
        array[4]=self.NOX
        array[5]=self.RM
        array[6]=self.AGE
        array[7]=self.DIS
        array[8]=self.RAD
        array[9]=self.TAX
        array[10]=self.PTRATIO
        array[11]=self.B
        array[12]=self.LSTAT
        

        print("Test Array -->\n",array)
        predicted_charges = self.model.predict([array])[0]
        #print("predicted_car",predicted_charges)
        return np.around(predicted_charges, 2)


if __name__ == "__main__":
    CRIM=0.00632
    ZN=18.00000
    INDUS=2.31000
    CHAS=0.00000
    NOX=0.53800
    RM=6.57500
    AGE=65.20000
    DIS=4.09000
    RAD=1.00000
    TAX=296.00000
    PTRATIO=15.30000
    B=396.90000
    LSTAT=4.98000

    med_ins = HousePrice(CRIM,ZN,
  INDUS,
  CHAS,
  NOX,
  RM,
  AGE,
  DIS,
  RAD,
  TAX,
  PTRATIO,
  B,
  LSTAT)
    charges = med_ins.get_predicted_price()
    print()
    print(f"Predicted Price of House is  {charges}/- Rs. Only (Lakh)")