# Richard-Liu-Project-SYS-6014
This is the first iteration of my project proposal.
Problem title:   
Demand-side Management of Smart Appliance Based on Optimization Prediction Tools

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
