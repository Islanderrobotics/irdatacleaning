# irdatacleaning
This python package is designed to make Artificial Intelligence accessible by starting
with the data cleaning stage.

## DataCorrelation:
this module allows you to be able to view the correlation values of your dataset
allowing you the ability to prevent simple errors
DataCorrelation(df = pandas dataframe)
df: is where you will input the dataset you would like to evaluate 
Correlationmatrix(): is the method you call uppon to view which columns have
correlation relationships. 
LookingAtCorr() is the method is where you will actually make the changes to your dataset
this method returns a pandas dataframe.
Check(): this method will call uppon both LookingAtCorr, and Correlationmatrix for you
this method also will return a pandas dataframe.

## DataDiscovery:
This class is designed to allow you the ability to evaluate your data
so that you may get an idea of what you need to change in the dataset
the best way to use this class is by actaully creating an instance of this
class where it will automate everything.
DataDiscovery(df)
df will be any pandas dataframe you wish to evaluate.

## Encoder
this class is dessigned to help you make encoding your data simple
the input variables for this class are
df: a pandas dataframe
type: by defalult this variable will br set to ONEHOTENCODER if you with to use
OrdinalEncoder you would set type to ordinalencoder
then you can call the check method to make the corretions this method will return a pandas data frame.
if you wish to compare the returned value to the original dataset you may call copy.
