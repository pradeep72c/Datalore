import os

from datalore.settings import BASE_DIR

BASE_URL = "https://archives.nseindia.com/content/historical/EQUITIES/{}/{}/{}"
FILE_NAME_FORMAT = 'cm{}{}{}bhav.csv.zip'
DOWNLOAD_FILE_PATH = os.path.join(BASE_DIR, 'downloads\\')