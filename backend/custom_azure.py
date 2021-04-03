from storages.backends.azure_storage import AzureStorage
from dotenv import load_dotenv
load_dotenv()
import os

class AzureMediaStorage(AzureStorage):
    account_name = os.getenv('account_name', 'account_n') # Must be replaced by your <storage_account_name>
    account_key = os.getenv('account_key', 'account_key') # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = os.getenv('account_name', 'account_n') # Must be replaced by your storage_account_name
    account_key = os.getenv('account_key', 'account_key') # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None