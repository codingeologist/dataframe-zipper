import pandas as pd
from zipper.zipper import Zipper

class DummyData:
    
    def __init__(self):
        
        self.df1 = pd.DataFrame.from_dict({
            "field1": [1, 2, 3, 4],
            "field2": [4, 3, 2, 1]
            })

        self.df2 = pd.DataFrame.from_dict({
            "field3": ["a", "b", "c", "d"],
            "field4": ["d", "c", "b", "a"]
            })

def main():

    data = DummyData()
    zippy = Zipper()

    zippy.zip_frames(df_list=[data.df1, data.df2])

    zippy.save_zip(filename="./test_zip.zip")

if __name__ == "__main__":

    main()
