import os


def main() -> None:
    print("Hello from fims!")
__app_name__ = "fims"
__version__ = "0.1.0"
TITLE = "File Integrity Monitoring System"


monitor = [
   {
     'path':r'C:\Users\User\Documents\Lessons-Py\monitor_files',
     'recursive':True
   },
   {
      'path':r'C:\Users\User\Documents\Lessons-Py\no_monitor_files', 
      'recursive':False
   }
]


DATABASE_PATH = os.path.dirname(os.path.realpath(__file__))

DATABASE_NAME = "shelve.db"

DATABASE = f"{DATABASE_PATH}/{DATABASE_NAME}"
