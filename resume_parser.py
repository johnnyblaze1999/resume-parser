import json
from pyresparser import ResumeParser
import en_core_web_sm
import warnings
import os

RESUME      = 'Data Analyst - RESUME Sample.docx'
JSON_PATH   = 'resume_data/json/'
DATA_PATH   = 'resume_data/data/'

def parse_resume(file_path, output_dir):
    nlp = en_core_web_sm.load()
    warnings.filterwarnings("ignore", category=UserWarning)
    
    # Get the base name of the file (without extension)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    json_file = os.path.join(output_dir, base_name + '.json')

    # Check if the file already exists
    if os.path.exists(json_file):
        print(f"The file already exists. Process stopped.")
        return

    # Parse the resume
    data = ResumeParser(file_path).get_extracted_data()

    # Save data to a JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f)

    return data

# Specify the resume file path
resume_file_path = os.path.join(DATA_PATH, RESUME)

parse_resume(resume_file_path, JSON_PATH)




















### OLD CODE
# from pyresparser import ResumeParser
# import en_core_web_sm
# import warnings

# def parse_resume(file_path):
#     nlp = en_core_web_sm.load()
#     warnings.filterwarnings("ignore", category=UserWarning)
#     data = ResumeParser(file_path).get_extracted_data()
#     return data