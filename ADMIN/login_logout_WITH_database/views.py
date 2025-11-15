from django.shortcuts import render , redirect
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "raka",
    database = "login"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")
users_and_passwd = mycursor.fetchall()
#[(email1, passwd1),
# (email2, passwd2)]

def index(request):
    submitted_email = request.GET.get("email")
    submitted_passwd = request.GET.get("passwd")
    
    for a in users_and_passwd:#a is basically just (email, passwd)
        
        int_passwd = a[1]
        string_passwd = str(int_passwd)
        if a[0] == submitted_email and string_passwd == submitted_passwd:
            return redirect('result')
        
    context = {'error_msg' : 'Invalid Password or Email'}
    return render(request, 'index.html', context)

def result_page(request):
    return render(request, 'result.html')

# Create your views here.
