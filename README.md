# ML_model_houseprice_soulai
This repository delivers an end-to-end ML solution for predicting house prices using the Melbourne City Housing dataset. It covers data processing, feature engineering, hyperparameter tuning, and model training, with deployment via FastAPI for real-time predictions.

## Melbourne House Price Prediction
### Overview
This project predicts house prices in Melbourne using Machine Learning. The model is built with Random Forest Regressor and deployed as an API using FastAPI.

## How to Use This Project
### Clone the Repository

```sh
CopyEdit
git clone https://github.com/anjumshaik7/ml-model-houseprice-soulai.git
```

```sh
cd ml-model-houseprice-soulai
```

### Install Required Packages
```sh
CopyEdit
pip install -r requirements.txt
```

### Run a file (.ipynb)

Open Google Colab or Jupyter Notebook.
Run House_Price_Prediction.ipynb to train and evaluate the model.
It will save the trained model as model.pkl.
Start FastAPI for Predictions

```sh
CopyEdit
uvicorn app:app --reload
```

API will be available at: http://127.0.0.1:8000
Swagger UI for testing: http://127.0.0.1:8000/docs

## Make Predictions (Example)
```json
Run this in Command Prompt:
CopyEdit
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{
  "Rooms": 3,
  "Distance": 10.5,
  "Postcode": 3000,
  "Bedroom2": 3,
  "Bathroom": 2,
  "Car": 1,
  "Latitude": -37.8136,
  "Longitude": 144.9631,
  "Propertycount": 5000,
  "TotalArea": 150,
  "PropertyAge": 15,
  "Type_t": false,
  "Type_u": false,
  "Method_S": true,
  "Method_SA": false,
  "Method_SP": false,
  "Method_VB": false,
  "Regionname_Eastern_Victoria": false,
  "Regionname_Northern_Metropolitan": true,
  "Regionname_Northern_Victoria": false,
  "Regionname_South_Eastern_Metropolitan": false,
  "Regionname_Southern_Metropolitan": false,
  "Regionname_Western_Metropolitan": false,
  "Regionname_Western_Victoria": false
}'
```

### Expected Output:

```json
{
  "predicted_price": 850000
}
```

## Model Performance
### Metric	Score

Random Forest MAE: 165811.84223157307 <br>
Random Forest R2 Score: 0.8091180324689073<br>
RMSE : 275356.06401834794


## NOTE: For detailed summary of model building Kindly check  "House_Price_Prediction.ipynb" file.

## Below are the images demonstrating the project execution using FastAPI 


![Alt Text](https://raw.githubusercontent.com/anjumshaik7/ml-model-houseprice-soulai/refs/heads/main/image.png))

![Alt Text](https://github.com/anjumshaik7/ml-model-houseprice-soulai/blob/main/image%20(1).png))

![Alt Text](https://github.com/anjumshaik7/ml-model-houseprice-soulai/blob/main/image%20(2).png)





