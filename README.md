# Stock Price Predictor

To get started fork this repo

Create a local installation of MindsDB following this [guide](https://docs.mindsdb.com/contribute/install#installing-mindsdb)

After download these datasets:
[Tesla Stock Data](https://www.kaggle.com/datasets/varpit94/tesla-stock-data-updated-till-28jun2021)
<br/>
[Microsoft Stock Data](https://www.kaggle.com/datasets/vijayvvenkitesh/microsoft-stock-time-series-analysis)
<br/>
[Apple Stock Data](https://www.kaggle.com/datasets/varpit94/apple-stock-data-updated-till-22jun2021)
<br/>
[Amazon Stock Data](https://www.kaggle.com/datasets/josehenriqueroveda/historical-amazon-stock-prices)
<br/>

Import these datasets on your installation and run these commands to create the predictor models required for the application:

`
CREATE PREDICTOR mindsdb.ApplePredictor
FROM files
(SELECT * FROM ApplePrices)              
PREDICT Close 
`
<br/>
`
CREATE PREDICTOR mindsdb.TeslaPredictor  
FROM files
(SELECT * FROM TeslaPrices)              
PREDICT Close 
`
<br/>
`
CREATE PREDICTOR mindsdb.AmazonPredictor 
FROM files
(SELECT * FROM AmazonPrices)              
PREDICT Close 
`
<br/>
`
CREATE PREDICTOR mindsdb.MicrosoftPredictor
FROM files
(SELECT * FROM MicrosoftPrices)              
PREDICT High
`
<br/>

Run the app with `python main.py` and get predicting!
