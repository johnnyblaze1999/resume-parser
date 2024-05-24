# How to operate the program

1. Open resume_parser.py (NOT resume-parser.py in resume_parser directory)
2. Edit the `RESUME` variable to the resume name you want to parse, including the file extension (.pdf or .docx). Your resume should be available in the same directory with resume_parser.py
3. Run the code in Python. A json version of the resume should be available in /resume_data/json/[your_resume.json]
4. Once the json version of your resume is created, open resume_ranker.py
5. Edit `JOB_DESC_TEXT` as the job description you are looking for the best fit
6. Run the code in Python. It will read all data from the /json/ directory and return the best to worst resume that fits the job description
