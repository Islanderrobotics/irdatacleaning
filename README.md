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
columns: when you have specific columns you want to be be corrected a specific way
then import the column or column names to this variable and only those columns will get corrected
they type you specificed
then you can call the check method to make the corretions
this method will return a pandas data frame
if you wish to compare the returned value to the original dataset you may
call copy

## InconsistentData
this class is dessigned to help you in the process of correcting inconsitent data
you have the ability to use use,
seperatingwords(origin,change):
this method is created so that you will be able to make sure all the columns
names with more then one word is seperated correctly
origin is the original format used to seperate the words
change is the format you would like to be used to seperate words
changeing_column_cases(case = "title")
this method is used to correct the columns nanes so that they are all in
full caps, full lower, or title case
case will be used to tell the method what case you would like
by defalut case will be set equal to title but by saying
case = upper the column names will be put to full lower
and the same for case = upper
column_names_white_space():
this method will be used to correct white space in column names
data_white_space():
this method will be used to correct white space in the dataset
correcting(column_name, corrections ):
this method is dessigned to help you make the needed changes to the data in the cells
so that your data is more consistent
column_name is the var used to identify which column will get the corrections
corrections is the dictionary with the corrected valuescheck(seperatingwords = False, origin = "", corrections = "" , change_case = False,case = "title", correcting = False, column_name = "", cell_corrections=None):
this methode is designed to automate all the steps. needed except you will have to provide some
input arguments
first is seperatingwords by defalut is false when you set this to true you will be calling the
seperatingwords words method
therefore you will have to add what the origin is set equal
as well as corrections these will both be some kind string values
next input value will be case

change_case = False to be able to have all your column names changed to the same case you will want change the value of change_case to true
case = "title"
you can change this depending on how you would like to formate your column names
when you want to correct specifica values in the data you will set correcting to true as well as
column_name = to the column name that will get these corrections done
then
cell_corrections = to a dictionary
the corrected pandas data frame will be return
autocheck():
does the same as what check does but walks you through the proccess of making all the changes
resources():
a method dessigned to give you links for more information on the class
## MissingValues:
MissingValues(df, stategy, columns, fillna)
df: is where you will enter in the pandas dataframe you wish to correct
stategy: is where you will define the strategy you with to use to correct the missing values
the strategy options you have are median, fillna and dropna enter one of those options to have your missing values
corrected in that strategy, by default this var is set to median
columns: is where you will enter the list of columns you wish to have the missing values corrected in
fillna: when you enter fillna for the stategy this is where you will enter the value you wish for the columns missing
values to be set to, currently you are only able to set this input variable to one value so i sugest that if you
have multiple columns that have misisng values use the median strategy to correct them or if you wish to still use the
fillna strategy with multiple columns use this class more than once there will be a version of this module in the
future that will allow you to use fillna on multiple columns with different values
check(): this is the method that you will use to tell the module to start making changes to the pandas data frame that you entered
this method will return the corrected pandas data frame.
copy_df: is the original unaltered dataframe
currently this module is only designed to be used with columns that are not object columns
## StringToDateTime:
this class is designed to make converting strings to datetime more accessable
this is done by creating an instance of the class StringToDateTime(df, column_names)
df is where you will define the pandas dataframe that you will work with
column_names is when you have a column names for columns you wish have converted to datetime
that is not not ["date","dates","starttime","start_time","start time"], to use this input argument
successfully you must pass in a list
check(): to tell the module to make the corrections you must call the check method
resources(): will give you the link to the youtube video about this module as well as the github
## Resources:
this class is used to allow you islanders the ability to get additional resources on the module or classes

## FeatureScaler:
This class is designed to allow you to scale your data with ease. You have the ability to scaler your
by using StandardScaler or normalize. Not only that, but you can also scale either the whole dataset or
you can just scale one column at a time.
the initialization of this module is
FeatureScaler(data,scaler=StandardScaler,columns=[])
data is where you can either enter a pandas data frame or a NumPy array,
by default the scaler this module will use is StandardScaler, but you can change this variable to normalize to use
normalization.
the columns input argument is to allow you the ability to have more control over what columns get scaled if you leave this
empty, you will end up scaling the whole dataset
to tell the module to do something with the data, all you have to do is call the check method by .check()
this will return the scaled data that you imported in the same format that you entered it as

```python
import irdatacleaning as ird
import numpy as np
scaler_data= np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
scaler = ird.FeatureScaler(data = scaler_data)
scaler_data = scaler.check()
norm_data= np.array([[ 1., -1.,  2.],
            [ 2.,  0.,  0.],
            [ 0.,  1., -1.]])
norm = ird.FeatureScaler(data = norm_data,scaler = "normalize", columns = [1])
norm_data = norm.check()
```