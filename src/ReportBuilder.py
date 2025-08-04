import numpy as np
import pandas as pd
class DataCleaner:


    @staticmethod
    def clean_unctuation_marks(column):

        symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
        data_clean = column.str.translate({ord(symbol): "" for symbol in symbols})

        return data_clean

    @staticmethod
    def convert_to_lower(column):
        df_text = column.str.lower()
        return df_text

    @staticmethod
    def remove_nan(column):
        df_biased = column.dropna()
        return df_biased
