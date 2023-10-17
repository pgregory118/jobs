import mysql.connector
import datetime
import sys, getopt
print(sys.version)


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Amber751428!',
    database='jobs'
)
cursor = mydb.cursor()
class Application:
    def __init__(self, job_title, salary, address, company):
        self.job_title = job_title
        self.salary = salary
        self.address = address
        self.company = company
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
    def create(self):
        adding_jobs = ("INSERT INTO jobs (Job_Title, Salary, Address, Company, Date_of_Application, status_ID)" 
            "Values (%s, %s, %s, %s, %s, %s)"
            )
        job_data = (self.job_title, self.salary, self.address, self.company, self.date, '1')
        cursor.execute(adding_jobs, job_data)
        mydb.commit()
    def read(self):
        cursor.execute('SELECT * FROM jobs')
        result = cursor.fetchall()
        for x in result:
            print(x)
job_title_input = input('Enter Job Title: ')
salary_input = input('Enter Job Salary: ')
address_input = input('Enter Job Address: ')
company_input = input('Enter Company Name: ')
apply = Application(job_title_input, salary_input, address_input, company_input)
apply.create()
apply.read()

arg = sys.argv[1:]
action = ""
try:
    opts, args = getopt.getopt(arg, "a:h",
                                ["action =", 
                                "help "])
except:
    print("Error")
for o, v in opts:
    if o in ['-a','--action' ]:
        print(arg[1])
        action = arg[1]
    elif o in ['-h', '--help']:
        print("-h for help \n-a for action")
