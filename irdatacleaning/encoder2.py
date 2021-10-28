import pandas as pd
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder
from .stringtodatetime import StringToDateTime
class Encoder:
    def __init__(self,df,type = ""):
        ''' this class is dessigned to help you make encoding your data simple
        the input variables for this class are
        df: a pandas dataframe
        type: by defalult this variable will br set to ONEHOTENCODER if you with to use
        OrdinalEncoder you would set type to ordinalencoder
        then you can call the check method to make the corretions
        this method will return a pandas data frame
        if you wish to compare the returned value to the original dataset you may
        call copy'''
        self.df = df
        self.copy = df.copy()
        self.type = type

        # datetime = StringToDateTime(self.df)
        # self.df = datetime.check()

    def check(self):
        self.object_column = []
        self.time_column = []
        for i in self.df.columns:
            if (self.df[i].dtype == "object"):
                self.object_column.append(i)


        self.Correct()
        return self.df
    def Correct(self):
        self.Universal()
        if (self.type == "" or self.type.upper() == "ONEHOTENCODER"):
            self.OneHotEncoder()
        elif (self.type.upper() == "ORDINALENCODER"):
            self.OrdinalEncoder()
        if(len(self.time_column) >0):
            self.TimeCorrection()
    def OrdinalEncoder(self):
        for i in self.object_column:
            translate = OrdinalEncoder()
            final = translate.fit_transform(self.df[i].array.reshape(-1, 1))
            self.df.drop(columns=i, inplace=True)
            self.df[i] = final

    def OneHotEncoder(self):
        for i in self.object_column:
            encoder = OneHotEncoder()

            finalencoder = encoder.fit_transform(self.df[i].array.reshape(-1, 1)).toarray()
            finalencoder = pd.DataFrame(finalencoder, columns=encoder.categories_)

            for j in finalencoder.columns:
                self.df[j] = finalencoder[j]
            self.df.drop(columns=i, inplace=True)
    # def TimeCorrection(self):
    #     for i in self.time_column:
    #         changes = pd.to_datetime(self.df[i], format="%m/%d/%y")
    #         self.df.drop(columns=i, inplace=True)
    #         self.df[i] = changes
    def Universal(self):
        new_list = []
        for i in self.object_column:
            for j in self.df[i]:
                new_list.append(j.lower().strip())
            # print(self.df[i])
            self.df.drop(columns = i, inplace = True)
            # print(new_list.u)
            self.df[i] = new_list
