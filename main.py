
from flask import Flask, jsonify, render_template, request
from model.utils import HousePrice
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("We are in House price prediction")
    # return "Home"
    return render_template("index.html")


@app.route('/predict_charges',methods=["POST","GET"])
def get_car_price():
    if request.method=="GET":
        print("we are in GET method")
        CRIM =eval(request.args.get("CRIM"))
        ZN =eval(request.args.get("ZN"))
        INDUS = eval(request.args.get("INDUS"))
        CHAS=eval(request.args.get("CHAS"))
        NOX =eval(request.args.get("NOX"))
        RM =eval(request.args.get("RM"))
        AGE=eval(request.args.get("AGE"))
        DIS=eval(request.args.get("DIS"))
        RAD=eval(request.args.get("RAD"))
        TAX=eval(request.args.get("TAX"))
        PTRATIO=eval(request.args.get("PTRATIO"))
        B=eval(request.args.get("B"))
        LSTAT=eval(request.args.get("LSTAT"))
        

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
        return render_template("index.html",prediction=charges)

    else:
        print("we are in POST method")
        CRIM =eval(request.form.get("CRIM"))
        ZN =eval(request.form.get("ZN"))
        INDUS = eval(request.form.get("INDUS"))
        CHAS=eval(request.form.get("CHAS"))
        NOX =eval(request.form.get("NOX"))
        RM =eval(request.form.get("RM"))
        AGE=eval(request.form.get("AGE"))
        DIS=eval(request.form.get("DIS"))
        RAD=eval(request.form.get("RAD"))
        TAX=eval(request.form.get("TAX"))
        PTRATIO=eval(request.form.get("PTRATIO"))
        B=eval(request.form.get("B"))
        LSTAT=eval(request.form.get("LSTAT"))
        

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
        return render_template("index.html",prediction=charges)
       

    
        
#     print("we are in House price prdction prediction")
#     data=request.form
#     CRIM=eval(data["CRIM"])
#     ZN=eval(data["ZN"])
#     INDUS=eval(data["INDUS"])
#     CHAS=eval(data["CHAS"])
#     NOX=eval(data["NOX"])
#     RM=eval(data["RM"])
#     AGE=eval(data["AGE"])
#     DIS=eval(data["DIS"])
#     RAD=eval(data["RAD"])
#     TAX=eval(data["TAX"])
#     PTRATIO=eval(data["PTRATIO"])
#     B=eval(data["B"])
#     LSTAT=eval(data["LSTAT"])
    
    

    
#     med_ins = HousePrice(CRIM,ZN,
#   INDUS,
#   CHAS,
#   NOX,
#   RM,
#   AGE,
#   DIS,
#   RAD,
#   TAX,
#   PTRATIO,
#   B,
#   LSTAT)
#     charges = med_ins.get_predicted_price()
#     return jsonify({"Result" :f"Predicted House Price in pune  {charges}/- Rs. Only (Lakh)"})

    
    # if request.method == "GET":
    #     print("we are in GET method")

    #     age = eval(request.args.get("age"))
    #     sex = request.args.get("sex")
    #     bmi = eval(request.args.get("bmi"))
    #     children = eval(request.args.get("children"))
    #     smoker = request.args.get("smoker")
    #     region =request.args.get("region")
    #     med_ins = MedicalInsurance(age, sex, bmi,children, smoker, region)
    #     charges = med_ins.get_predicted_price()
    #     return render_template("index.html",prediction=charges)

    # else:
    #     print("we are in POST method")

    #     age = eval(request.form.get("age"))
    #     sex = request.form.get("sex")
    #     bmi = eval(request.form.get("bmi"))
    #     children = eval(request.form.get("children"))
    #     smoker = request.form.get("smoker")
    #     region =request.form.get("region")
    #     med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    #     charges = med_ins.get_predicted_price()
    #     return render_template("index.html",prediction=charges)

    

      

        
if __name__=="__main__":
 app.run(host='0.0.0.0' , port=5000, debug=True)
      