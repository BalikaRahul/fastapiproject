from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from models import Candidates_registation,Job,Job_applications
from database import Base, engine,LocalSession
app = FastAPI()
Base.metadata.create_all(bind=engine)

class Candidates_registation_details(BaseModel):
    candidate_id :Optional[int] = None
    first_name :str
    last_name :str
    phone_number :str
    email :str
    city :str
    graduation_year :int
    skill :str
    password:str
class  Post_a_job(BaseModel):
    job_id: Optional[int] = None
    company_name : str
    role : str
    required_experience : int 
    ctc : int
    skills : str
    bond : bool
class View_job_applications_admin(BaseModel):
    job_id:int
class Apply_job(BaseModel):
    job_id:int
    candidate_id:int
class View_job_applications_candidate(BaseModel):
    candidate_id : int
    candidate_phone_number:str
class Delete_profile(BaseModel):
    candidate_id : int
    phone_number:str

@app.get("/")
def home():
    return {"message": "Hello World"}


# @app.post('/validation')
# def validation(userName):
#     if userName == 'admin':
#         count = 0
#         while count < 3:
#             password = input('enter your admin password: ')
#             if password == 'admin@123':
#                 print("Admin login successful")
#                 what_to_do_admin()
#                 return
#             else:
#                 count += 1
#                 print(f'you have entered wrong password and you have {3-count} chances')
#         print("Login failed")

#     elif userName == 'candidates':
#         first_name = input('enter your first_name: ')
#         write.execute('SELECT candidate_id, password FROM candidates_registration WHERE first_name = %s', (first_name,))
#         founduser = write.fetchone()
#         if founduser:
#             given_name_id = founduser["candidate_id"]
#             count = 0
#             while count < 3:
#                 password = input('enter your password: ')
#                 if password == founduser["password"]:
#                     print("Candidate login successful")
#                     what_to_do_candidate(given_name_id)
#                     return
#                 else:
#                     count += 1
#                     print(f'you have entered wrong password and you have {3-count} chances')
#             print("Login failed")
#         else:
#             print("Candidate not found")
#             candidates_registration()

# def what_to_do_admin():
#     print("\n========== ADMIN MENU ==========")
#     print("1. Registration")
#     print("2. Post a job")
#     print("3. View job applications")
#     print("4. Exit")
#     while True:
#         operation = input('enter what do you want to do?: ').strip().lower()
#         if operation in ['1', 'registration']:
#             candidates_registration()
#         elif operation in ['2', 'post a job']:
#             jobs()
#         elif operation in ['3', 'view job applications']:
#             view_applications()
#         elif operation in ['4', 'exit']:
#             break
#         else:
#             print("Invalid option")

# def what_to_do_candidate(given_name_id):
#     print("\n========== CANDIDATE MENU ==========")
#     print("1. Apply for job")
#     print("2. View application")
#     print("3. View job openings")
#     print("4. Delete your profile")
#     print("5. Exit")
#     while True:
#         operation = input('enter what do you want to do?: ').strip().lower()
#         if operation in ['1', 'apply for job']:
#             apply_for_job(given_name_id)
#         elif operation in ['2', 'view application']:
#             view_application(given_name_id)
#         elif operation in ['3', 'view job openings']:
#             view_job_openings()
#         elif operation in ['4', 'delete your profile']:
#             delete_your_profile(given_name_id)
#         elif operation in ['5', 'exit']:
#             break
#         else:
#             print("Invalid option")
# @app.get('/view_application')
# def view_application(request:):
#     write.execute("""SELECT ja.application_id, j.company_name, j.role, j.ctc, ja.application_date FROM job_applications ja JOIN jobs j ON ja.job_id = j.job_id WHERE ja.candidate_id = %s""", (given_name_id,))
#     applications = write.fetchall()
#     if applications:
#         for application in applications:
#             print("\n------------------------")
#             print("Application ID:", application["application_id"])
#             print("Company:", application["company_name"])
#             print("Role:", application["role"])
#             print("CTC:", application["ctc"])
#             print("Application Date:", application["application_date"])
#     else:
#         print("You have not applied for any jobs")
@app.post('/apply_for_job')
def apply_for_job(request:Apply_job):
    post = Job_applications(
    job_id = request.job_id,
    candidate_id = request.candidate_id,)
    db = LocalSession()
    db.add(post)
    db.commit()
    db.close()
    return "job posted succesfully"
    # try:
    #     job_id = int(input("\nEnter the job ID you want to apply for: "))
    # except ValueError:
    #     print("Invalid Job ID")
    #     return
    # Check whether job exists
    # write.execute("""SELECT job_id FROM jobs WHERE job_id = %s""", (job_id,))
    # job = write.fetchone()
    # if job:
    #     # Check whether already applied
    #     write.execute("""SELECT application_id FROM job_applications WHERE candidate_id = %s AND job_id = %s""", (given_name_id, job_id))
    #     already_applied = write.fetchone()
    #     if already_applied:
    #         print("You already applied for this job")
    #     else:
    #         write.execute("""INSERT INTO job_applications (candidate_id, job_id) VALUES (%s, %s)""", (given_name_id, job_id))
    #         connection.commit()
    #         print("Application submitted successfully")
    # else:
    #     print("Job does not exist")
@app.delete('/delete_profile')
def delete_profile(request:Delete_profile):
    candidate_id = request.candidate_id
    phone_number = request.phone_number
    db = LocalSession()
    candidate =db.query(Candidates_registation).filter(Candidates_registation.candidate_id == candidate_id ,Candidates_registation.phone_number == phone_number ).first()
    if candidate:
        candidates_registration.phone_number = phone_number
        db.delete(candidate)
    db.commit()
    db.close()
# def view_job_openings():
#     print("\n========== JOB OPENINGS ==========")
#     write.execute("""SELECT * FROM jobs""")
#     job_list = write.fetchall()
#     if job_list:
#         for job in job_list:
#             print("\n------------------------")
#             print("Job ID:", job["job_id"])
#             print("Company:", job["company_name"])
#             print("Role:", job["role"])
#             print("Required Experience:", job["required_experience"])
#             print("CTC:", job["ctc"])
#             print("Skills:", job["skills"])
#             print("Bond:", job["bond"])
#     else:
#         print("No jobs available")
@app.post('/candidates_registration')
def candidates_registration(request:Candidates_registation_details):
    
    db = LocalSession()
    candidates_details = Candidates_registation(
        first_name=request.first_name,
        last_name=request.last_name,
        phone_number=request.phone_number,
        email=request.email,
        city=request.city,
        graduation_year=request.graduation_year,
        skill=request.skill,
        password=request.password
    )
    db.add(candidates_details)
    db.commit()
    db.close()
    return "candidate registration succesfully"
@app.post('/post_job')
def jobs(request:Post_a_job):
    post = Job(
    company_name = request.company_name,
    role = request.role,
    required_experience = request.required_experience,
    ctc = request.ctc,
    skills = request.skills,
    bond = request.bond,)
    db = LocalSession()
    db.add(post)
    db.commit()
    db.close()
    return "job posted succesfully"

@app.get('/view_applications')
def view_applications(request:View_job_applications_candidate):
    db =LocalSession()
    candidate =db.query(Candidates_registation).filter(
        Candidates_registation.candidate_id ==request.candidate_id,
        Candidates_registation.phone_number ==request.candidate_phone_number,
    ).first()
    if not candidate:
        db.close()
        return {'message:' " candidate not found"}
    else:
        candidate_application =db.query(Job_applications).filter(Job_applications.candidate_id==Candidates_registation.candidate_id  ).all()
        db.close()
        return candidate_application
# def main():
#     while True:
#         print("\n========== JOB PORTAL ==========")
#         print("1. Admin")
#         print("2. Candidate")
#         print("3. Exit")
#         choice = input("Enter your choice: ").strip()
#         if choice == "1":
#             validation("admin")
#         elif choice == "2":
#             validation("candidates")
#         elif choice == "3":
#             print("Thank you for using the Job Portal")
#             break
#         else:
#             print("Invalid choice")

# if __name__ == "__main__":
#     main()
#     connection.close()

