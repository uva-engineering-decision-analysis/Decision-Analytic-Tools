# Richard-Liu-Project-SYS-6014
Problem title:   
Demand-side Management of Smart Appliance Based on Optimization Prediction Tools

Summary:
Demand-side management is one approach that can be applied to efficiently manage a site’s energy consumption with the aim of cutting the costs of electrical energy supply. Based on this approach, we try to build an optimization tool for smart appliance to save energy cost for consumers. We collect historic prediction and real-time price data from NYISO to build models for our decision basis. To prove our model's reliability, we  examine its performance and examine our assumptions, the test result shows that our optimization tool can save cost. In the future, we will make calibration to improve our model and integrate our model to make better prediction. We are hoping that we can approach the best optimal decision for the smart appliance to work step by step.

The source of data:  
https://www.nyiso.com/  

Data we have:  
Forecast electricity price data: every hour's LBMP based on forecast everyday(locational based marginal pricing) .   
Historic real-time electricity price data: real-world recorded LBMP every 5 minutes everyday(continuously updating to today).

Background:   
Demand-side management is one the approach that can be applied to save the cost of energy for both individual's and world's benefit.  
If we can allocate electricity to smart appliance according to current flowing price, we can make great benefits.  
In this scenario, we will be using the forecast electricity price data as our basis to predict the realized price. We will use historic real-time and forecast price data to generalize a model that can fit both data. Then we can predict the realized price one-day ahead according to the day-ahead predicted data. The result of the real-time updated data will be used to refine the model.  
Based on that predicted realized price value and the given working hour range, we can find the optimal working time for the smart appliance.

The decision problem:  
The decision-maker should be the smart appliance itself, to decide which time to start doing the job in order to get the lowest cost of electricity based on predicted realized LBMP.
