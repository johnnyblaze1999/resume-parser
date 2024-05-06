from pyresparser import ResumeParser
import en_core_web_sm
import warnings

def parse_resume(file_path):
    nlp = en_core_web_sm.load()
    warnings.filterwarnings("ignore", category=UserWarning)
    data = ResumeParser(file_path).get_extracted_data()
    return data