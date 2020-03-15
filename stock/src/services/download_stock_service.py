import os
from time import strptime

import requests
from zipfile import ZipFile
from calendar import monthrange

class DownloadStocksService:
    @staticmethod
    def download_and_parse_files(base_url, file_name_format, year, month, download_path=None):
        downloaded_files = list()

        month_range = monthrange(year, strptime(month,'%b').tm_mon)
        for date in range(1, month_range[1]+1):
            date = "{0:0=2d}".format(date)
            file_name = file_name_format.format(date, month, year)
            file_url = base_url.format(year, month, file_name)

            print("Downloading file from", file_url)

            try:
                response = requests.get(file_url, stream=True, timeout=2)
                file_name = download_path + file_name
                print(file_name)
                with open(file_name, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                DownloadStocksService.extract_downloaded_files(download_path, file_name)
                os.remove(file_name)

                file_name = file_name.replace('.zip', '')
                downloaded_files.append(file_name)
            except Exception as e:
                print("Download of stock data failed for " + str(date) + str(month) + str(
                    year) + ", exception: " + str(e))
                continue

        return downloaded_files

    @staticmethod
    def extract_downloaded_files(download_path, file_name):
        try:
            with ZipFile(file_name, 'r') as zip:
                zip.extractall(path=download_path)
        except Exception as e:
            print("Extracting Zip file - {} failed".format(file_name) + ", exception: " + str(e))