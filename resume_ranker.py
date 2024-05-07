from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

def match_keywords(resume_data, job_desc_text):
    # Convert the resume data to text
    resume_text = ' '.join([str(v) for v in resume_data.values()])

    # Create the Document Term Matrix
    text = [resume_text, job_desc_text]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)

    # Get the match percentage
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2) # round to two decimal places
    return matchPercentage

def rank_resumes(resume_files, job_desc_text):
    # Parse and match keywords for each resume
    match_percentages = []

    for file in resume_files:
        with open(file, 'r') as f:
            resume_data = json.load(f)
        match_percentages.append((resume_data, match_keywords(resume_data, job_desc_text)))

    # Sort by match percentage
    ranked_resumes = sorted(match_percentages, key=lambda x: x[1], reverse=True)
    return ranked_resumes

resume_files = ['deedy-cv.pdf', 'jakes-resume.pdf']
job_desc_text = """

Requirements:

    6 or more years of Application Software development.
    Proficiency in C# and .NET.
    Experience with SQL databases.
    Knowledge of JSON and XML.
    Understanding of Visual Studio.
    Understanding of DevOps principles.
    PowerBI experience preferred.
    Excellent communication and mentoring skills.

Responsibilities:

    Collaborate with project integration teams.
    Resolve software issues and improve products.
    Streamline workflows and enhance existing products.
    Develop projects using C#, SQL, and .NET Technologies.
    Report project status accurately.
    Specialize in ASP.NET MVC architectures.
    Work with AWS development tools.
    Utilize Source & Version Controls like Azure DevOps and GIT.
    Knowledge of Mainframe backend systems is a plus.

About SMART TECH SKILLS LLC:

Established in 2004, Smart Tech Skills is a leading technology and professional services organization focusing on cutting-edge technologies.

The company, headquartered in Marlborough, MA, effectively meets clients' technology needs nationwide, simplifying advanced technology management."""

ranked_resumes = rank_resumes(resume_files, job_desc_text)

for resume, match_percentage in ranked_resumes:
    print(f"Resume: {resume['name']}... Match Percentage: {match_percentage}%")













### OLD CODE
# from collections import Counter
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from resume_parser import parse_resume

# def match_keywords(resume_data, job_desc_text):
#     # Convert the resume data to text
#     resume_text = ' '.join([str(v) for v in resume_data.values()])

#     # Create the Document Term Matrix
#     text = [resume_text, job_desc_text]
#     cv = CountVectorizer()
#     count_matrix = cv.fit_transform(text)

#     # Get the match percentage
#     matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
#     matchPercentage = round(matchPercentage, 2) # round to two decimal places
#     return matchPercentage

# def rank_resumes(resume_files, job_desc_text):
#     # Parse and match keywords for each resume
#     match_percentages = [(parse_resume(file), match_keywords(parse_resume(file), job_desc_text)) for file in resume_files]

#     # Sort by match percentage
#     ranked_resumes = sorted(match_percentages, key=lambda x: x[1], reverse=True)
#     return ranked_resumes

# # Example usage:
# resume_files = ['deedy-cv.pdf', 'jakes-resume.pdf']
# job_desc_text = """

# Requirements:

#     6 or more years of Application Software development.
#     Proficiency in C# and .NET.
#     Experience with SQL databases.
#     Knowledge of JSON and XML.
#     Understanding of Visual Studio.
#     Understanding of DevOps principles.
#     PowerBI experience preferred.
#     Excellent communication and mentoring skills.

# Responsibilities:

#     Collaborate with project integration teams.
#     Resolve software issues and improve products.
#     Streamline workflows and enhance existing products.
#     Develop projects using C#, SQL, and .NET Technologies.
#     Report project status accurately.
#     Specialize in ASP.NET MVC architectures.
#     Work with AWS development tools.
#     Utilize Source & Version Controls like Azure DevOps and GIT.
#     Knowledge of Mainframe backend systems is a plus.

# About SMART TECH SKILLS LLC:

# Established in 2004, Smart Tech Skills is a leading technology and professional services organization focusing on cutting-edge technologies.

# The company, headquartered in Marlborough, MA, effectively meets clients' technology needs nationwide, simplifying advanced technology management."""
# ranked_resumes = rank_resumes(resume_files, job_desc_text)

# for resume, match_percentage in ranked_resumes:
#     print(f"Resume: {resume['name']}... Match Percentage: {match_percentage}%")
