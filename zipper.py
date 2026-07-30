import io
from zipfile import ZipFile as zf

class Zipper:

    def __init__(self):
        
        self.zip_buffer = io.BytesIO()
    
    def zip_frames(self, df_list: list):

        filenames = []
        for i in range(len(df_list)):

            filenames.append(str(f"dataframe_{i}.csv"))
            print(filenames[i])

            with zf(self.zip_buffer, mode="a") as zip_file:
                with zip_file.open(filenames[i], "w") as buffer:
                    print(buffer)
                    df_list[i].to_csv(buffer, index=False)
    
    def save_zip(self, filename: str):

        with open(filename, "wb") as file:
            file.write(self.zip_buffer.getvalue())
