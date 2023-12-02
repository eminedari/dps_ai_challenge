# DPS BATCH#21 - AI Track Challenge : Accident Forecasting

This repository includes the source code for the challenge. You can find the deployed application at [this page](https://dps-ai-challenge-9c7b337d5bbd.herokuapp.com/). By POST requests, you can get the predictions as a response.

### How to POST Request?
-  **With all features:** returns the prediction for that specific accident.
Example request:
```json
{
    "year":2021,
    "month":1,
    "category":"Alkoholunfälle",
    "type":"insgesamt"
}
```
Example response:
```json
{
    "prediction": 21
}
```
- **With month and year feature only:** returns the prediction for total number of accidents predicted to happen on that month and year.
Example request:
```json
{
    "year":2021,
    "month":1,
}
```
Example response:
```json
{
    "prediction": 5589
}
```

### Source Code Structure
In the jupyter notebook file "main.ipynb", the implementation as visualizations are included in a step-by-step manner. The following is the structure of the cells:

```bash
main.ipynb
├── Import libraries
├── Read the dataset
├── ├── 1. Examine entries
├── Encode categorical data
├── Preprocess the data
├── Visualize the data
├── ├── 1.Plot number of accidents in each category per year
├── ├── 2. Plot number of accidents per month in chosen years
├── Prepare Train and Test Setup
│   ├── 1. Data split
│   ├── 2. Training on Entire Dataset
│   ├── 3. Plot predictions on Ground Truth
│   ├── 4. Training on Categories Seperately
├── Single Sample Prediction
├── Save Model
```

### Author
Emine Dari (eminedari0703@gmail.com)
