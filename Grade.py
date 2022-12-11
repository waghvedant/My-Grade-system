# importing Flask and other modules
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__,template_folder='template',static_folder='static')

# A decorator used to tell the application
# which URL is associated function

@app.route('/', methods=["GET", "POST"])
def grade():
    CAmar = 0
    CNmar = 0
    SETmar=0
    OSmar=0
    ERPmar=0
    EEmar=0
    CALmar=0
    CNLmar=0
    SETLmar=0
    OSLmar=0
    OS1mar=0

    if request.method == "POST":
        gradeCA = request.form.get("CA")
        if gradeCA=='A++':
            CAmar = 3*10
        elif gradeCA=='A+':
            CAmar = 3*9
        elif gradeCA=='A':
            CAmar = 3*8
        elif gradeCA=='B+':
            CAmar = 3*7
        elif gradeCA=='B':
            CAmar = 3*6
        elif gradeCA=='C':
            CAmar = 3*5
        elif gradeCA=='D':
            CAmar = 3*4

        gradeCN = request.form.get("CN")
        if gradeCN == 'A++':
            CNmar = 3 * 10
        elif gradeCN == 'A+':
            CNmar = 3 * 9
        elif gradeCN == 'A':
            CNmar = 3 * 8
        elif gradeCN == 'B+':
            CNmar = 3 * 7
        elif gradeCN == 'B':
            CNmar = 3 * 6
        elif gradeCN == 'C':
            CNmar = 3 * 5
        elif gradeCN == 'D':
            CNmar = 3 * 4

        gradeSET = request.form.get("SET")
        if gradeSET == 'A++':
            SETmar = 3 * 10
        elif gradeSET == 'A+':
            SETmar = 3 * 9
        elif gradeSET == 'A':
            SETmar = 3 * 8
        elif gradeSET == 'B+':
            SETmar = 3 * 7
        elif gradeSET == 'B':
            SETmar = 3 * 6
        elif gradeSET == 'C':
            SETmar = 3 * 5
        elif gradeSET == 'D':
            SETmar = 3 * 4

        gradeOS = request.form.get("OS")
        if gradeOS == 'A++':
            OSmar = 3 * 10
        elif gradeOS == 'A+':
            OSmar = 3 * 9
        elif gradeOS == 'A':
            OSmar = 3 * 8
        elif gradeOS == 'B+':
            OSmar = 3 * 7
        elif gradeOS == 'B':
            OSmar = 3 * 6
        elif gradeOS == 'C':
            OSmar = 3 * 5
        elif gradeOS == 'D':
            OSmar = 3 * 4

        gradeERP = request.form.get("ERP")
        if gradeERP == 'A++':
            ERPmar = 5 * 10
        elif gradeERP == 'A+':
            ERPmar = 5 * 9
        elif gradeERP == 'A':
            ERPmar = 5 * 8
        elif gradeERP == 'B+':
            ERPmar = 5 * 7
        elif gradeERP == 'B':
            ERPmar = 5 * 6
        elif gradeERP == 'C':
            ERPmar = 5 * 5
        elif gradeERP == 'D':
            ERPmar = 5 * 4

        gradeEE = request.form.get("EE")
        if gradeEE == 'A++':
            EEmar = 3 * 10
        elif gradeEE == 'A+':
            EEmar = 3 * 9
        elif gradeEE == 'A':
            EEmar = 3 * 8
        elif gradeEE == 'B+':
            EEmar = 3 * 7
        elif gradeEE == 'B':
            EEmar = 3 * 6
        elif gradeEE == 'C':
            EEmar = 3 * 5
        elif gradeEE == 'D':
            EEmar= 3 * 4

        gradeLCA = request.form.get("LCA")
        if gradeLCA == 'A++':
            CALmar = 1 * 10
        elif gradeLCA == 'A+':
            CALmar = 1 * 9
        elif gradeLCA == 'A':
            CALmar = 1 * 8
        elif gradeLCA == 'B+':
            CALmar = 1 * 7
        elif gradeLCA == 'B':
            CALmar = 1 * 6
        elif gradeLCA == 'C':
            CALmar = 1 * 5
        elif gradeLCA == 'D':
            CALmar = 1 * 4

        gradeLCN = request.form.get("LCN")
        if gradeLCN == 'A++':
            CNLmar = 1 * 10
        elif gradeLCN == 'A+':
            CNLmar = 1 * 9
        elif gradeLCN == 'A':
            CNLmar = 1 * 8
        elif gradeLCN == 'B+':
            CNLmar = 1 * 7
        elif gradeLCN == 'B':
            CNLmar = 1 * 6
        elif gradeLCN == 'C':
            CNLmar = 1 * 5
        elif gradeLCN == 'D':
            CNLmar = 1 * 4

        gradeLSET = request.form.get("LSET")
        if gradeLSET == 'A++':
            SETLmar = 1 * 10
        elif gradeLSET == 'A+':
            SETLmar = 1 * 9
        elif gradeLSET == 'A':
            SETLmar = 1 * 8
        elif gradeLSET == 'B+':
            SETLmar = 1 * 7
        elif gradeLSET == 'B':
            SETLmar = 1 * 6
        elif gradeLSET == 'C':
            SETLmar = 1 * 5
        elif gradeLSET == 'D':
            SETLmar = 1 * 4

        gradeLOS = request.form.get("LOS")
        if gradeLOS == 'A++':
            OSLmar = 1 * 10
        elif gradeLOS == 'A+':
            OSLmar = 1 * 9
        elif gradeLOS == 'A':
            OSLmar = 1 * 8
        elif gradeLOS == 'B+':
            OSLmar = 1 * 7
        elif gradeLOS == 'B':
            OSLmar = 1 * 6
        elif gradeLOS == 'C':
            OSLmar = 1 * 5
        elif gradeLOS == 'D':
            OSLmar = 1 * 4

        gradeOS1 = request.form.get("LOS1")
        if gradeOS1 == 'A++':
            OS1mar = 1 * 10
        elif gradeOS1 == 'A+':
            OS1mar = 1 * 9
        elif gradeOS1 == 'A':
            OS1mar = 1 * 8
        elif gradeOS1 == 'B+':
            OS1mar = 1 * 7
        elif gradeOS1 == 'B':
            OS1mar = 1 * 6
        elif gradeOS1 == 'C':
            OS1mar = 1 * 5
        elif gradeOS1 == 'D':
            OS1mar = 1 * 4

        Total = (CAmar+CNmar+SETmar+OSmar+ERPmar+EEmar+CALmar+CNLmar+SETLmar+OSLmar+OS1mar)/25
        return "Your SGPA is :"+ str(Total)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)