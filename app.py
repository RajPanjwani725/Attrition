from flask import *
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import plotly
import plotly.express as px



app = Flask(__name__)
app.secret_key = "ajgdcvwjn"


def db_connect():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='pythondb',
        cursorclass=pymysql.cursors.DictCursor,
        port=3306
    )


@app.route("/",methods=['GET'])
def indexPage():
    return render_template("index.html")


@app.route("/insertPage")
def insertData():
    return render_template('insertPage.html')


@app.route("/insertData", methods=["POST"])
def insertDatas():
    Age = request.form.get("Age")
    Attrition = request.form.get("Attrition")
    BusinessTravel = request.form.get("BusinessTravel")
    DailyRate = request.form.get("DailyRate")
    Department = request.form.get("Department")
    DistanceFromHome = request.form.get("DistanceFromHome")
    Education = request.form.get("Education")
    EducationField = request.form.get("EducationField")
    EmployeeCount = '1'
    # EmployeeCount = request.form.get("EmployeeCount")
    EmployeeNumber = request.form.get("EmployeeNumber")
    EnvironmentSatisfaction = request.form.get("EnvironmentSatisfaction")
    Gender = request.form.get("Gender")
    HourlyRate = request.form.get("HourlyRate")
    JobInvolvement = request.form.get("JobInvolvement")
    JobLevel = request.form.get("JobLevel")
    JobRole = request.form.get("JobRole")
    JobSatisfaction = request.form.get("JobSatisfaction")
    MaritalStatus = request.form.get("MaritalStatus")
    MonthlyIncome = request.form.get("MonthlyIncome")

    MonthlyRate = '0'
    # MonthlyRate = request.form.get("MonthlyRate")
    NumCompaniesWorked = request.form.get("NumCompaniesWorked")
    Over18 = "Y"
    OverTime = request.form.get("OverTime")
    PercentSalaryHike = request.form.get("PercentSalaryHike")
    PerformanceRating = request.form.get("PerformanceRating")
    RelationshipSatisfaction = request.form.get("RelationshipSatisfaction")
    StandardHours = '80'
    StockOptionLevel = request.form.get("StockOptionLevel")
    TotalWorkingYears = request.form.get("TotalWorkingYears")
    TrainingTimesLastYear = request.form.get("TrainingTimesLastYear")
    WorkLifeBalance = request.form.get("WorkLifeBalance")
    YearsAtCompany = request.form.get("YearsAtCompany")
    YearsInCurrentRole = request.form.get("YearsInCurrentRole")
    YearsSinceLastPromotion = request.form.get("YearsSinceLastPromotion")
    YearsWithCurrManager = request.form.get("YearsWithCurrManager")

    connection = db_connect()
    cursor1 = connection.cursor()
    cursor1.execute(
        "INSERT INTO finalproject(Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,"
        "Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,"
        "Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,"
        "TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,"
        "YearsWithCurrManager) VALUES ('" + Age + "','" + Attrition + "','" + BusinessTravel + "','" + DailyRate + "','" + Department + "','" + DistanceFromHome + "','" + Education + "','" + EducationField + "','" + EmployeeCount + "','" + EmployeeNumber + "','" + EnvironmentSatisfaction + "','" + Gender + "','" + HourlyRate + "','" + JobInvolvement + "','" + JobLevel + "','" + JobRole + "','" + JobSatisfaction + "','" + MaritalStatus + "','" + MonthlyIncome + "','" + MonthlyRate + "','" + NumCompaniesWorked + "','" + Over18 + "','" + OverTime + "','" + PercentSalaryHike + "','" + PerformanceRating + "','" + RelationshipSatisfaction + "','" + StandardHours + "','" + StockOptionLevel + "','" + TotalWorkingYears + "','" + TrainingTimesLastYear + "','" + WorkLifeBalance + "','" + YearsAtCompany + "','" + YearsInCurrentRole + "','" + YearsSinceLastPromotion + "','" + YearsWithCurrManager + "')")
    connection.commit()

    # cursor1.execute(
    #     "INSERT INTO finalproject(Age,Attrition) VALUES ('" + Age + "','" + Attrition + "')")
    #     # "INSERT INTO finalproject(Age,Attrition) VALUES ('" + Age + "','" + Attrition + "')")
    # connection.commit()

    print("Insert Successfully")
    cursor1.close()
    connection.close()

    return redirect('/')


@app.route("/searchPage", methods=["GET"])
def viewData():
    connection = db_connect()
    cursor1 = connection.cursor()
    cursor1.execute("select * from finalproject")
    searchData = cursor1.fetchall()
    # prsearchData)
    cursor1.close()
    connection.close()
    print(searchData)

    return render_template("Search.html", data=searchData)



@app.route("/getAllAttrition", methods=["GET"])
def getAllAttrition():
    connection = db_connect()
    cursor1 = connection.cursor()
    cursor1.execute("select * from finalproject")
    searchData = cursor1.fetchall()
    # prsearchData)
    cursor1.close()
    connection.close()

    # return render_template("Search.html", data=searchData)
    return jsonify(searchData),200








@app.route("/analysisPage", methods=["GET"])
def temp():
    print("temp")
    data = pd.read_csv(
        "C:/Users/User/Documents/Big Data Analyst/SEM 1/Data Programming/Final Project/Dataset/Attrition.csv")
    print(data)

    bar_chart = pd.DataFrame(data.Department.value_counts()).reset_index()
    bar_chart = bar_chart.rename({'index': 'Department', 'Department': 'count'}, axis=1)

    bar_chart_no = data.Department[data['Attrition'] == 'No'].value_counts()
    bar_chart_no = pd.DataFrame(bar_chart_no).reset_index()
    bar_chart_no = bar_chart_no.rename({'index': 'Department', 'Department': 'count'}, axis=1)

    bar_chart_yes = data.Department[data['Attrition'] == 'Yes'].value_counts()
    bar_chart_yes = pd.DataFrame(bar_chart_yes).reset_index()
    bar_chart_yes = bar_chart_yes.rename({'index': 'Department', 'Department': 'count'}, axis=1)

    # temp_data = data[['Age', 'MonthlyIncome', 'Gender']]
    # temp_data = temp_data.sort_values(by='Age')

    # temp_data_male = temp_data[temp_data['Gender'] == 'Male']

    pie_attrition = data.Gender.value_counts()
    pie_attrition_yes = data.Gender[data['Attrition'] == 'Yes'].value_counts()
    # attrition_yes.index[0], attrition_yes[0]

    pie_attrition_no = data.Gender[data['Attrition'] == 'No'].value_counts()
    # attrition_yes.index[0], attrition_yes[0]

    box_attrition_yes = data[data['Attrition'] == 'Yes']
    box_attrition_no = data[data['Attrition'] == 'No']

    bar_chart = px.bar(bar_chart, x='Department', y='count', title="Attrition and Department")
    bar_chart_no = px.bar(bar_chart_no, x='Department', y='count', title="Attrition(No) and Department")
    bar_chart_yes = px.bar(bar_chart_yes, x='Department', y='count', title="Attrition(Yes) and Department")

    # fig2=px.line(temp_data,x='Age', y='MonthlyIncome',line_dash='Gender',title='Age Vs Income')

    pie_chart = px.pie(pie_attrition, names=[pie_attrition.index[0], pie_attrition.index[1]],
                       values=[pie_attrition[0], pie_attrition[1]], title="Attrition Vs Gender")

    pie_chart_yes = px.pie(pie_attrition_yes, names=[pie_attrition_yes.index[0], pie_attrition_yes.index[1]],
                           values=[pie_attrition_yes[0], pie_attrition_yes[1]], title="Attrition(Yes) Vs Gender")

    pie_chart_no = px.pie(pie_attrition_no, names=[pie_attrition_no.index[0], pie_attrition_no.index[1]],
                          values=[pie_attrition_no[0], pie_attrition_no[1]], title="Attrition(No) Vs Gender")

    box_chart = px.box(data, x='Attrition', y='MonthlyIncome', title="Attrition Vs MonthlyIncome")
    box_chart_yes = px.box(box_attrition_yes, x='Gender', y='MonthlyIncome',
                           title="Attrition(Yes,Gender) Vs MonthlyIncome")
    box_chart_no = px.box(box_attrition_no, x='Gender', y='MonthlyIncome',
                           title="Attrition(No,Gender) Vs MonthlyIncome")



    # fig=sns.barplot(x=data['Attrition'],y=data['MonthlyIncome'],hue=data['Gender'])
    graphJSON = json.dumps(bar_chart, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(bar_chart_no, cls=plotly.utils.PlotlyJSONEncoder)
    # graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(bar_chart_yes, cls=plotly.utils.PlotlyJSONEncoder)
    # graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(pie_chart, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON5 = json.dumps(pie_chart_yes, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON6 = json.dumps(pie_chart_no, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON7 = json.dumps(box_chart, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON8 = json.dumps(box_chart_yes, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON9 = json.dumps(box_chart_no, cls=plotly.utils.PlotlyJSONEncoder)

    # Line Graph
    labels = [row for row in data['Age']]

    values = [row for row in data['MonthlyIncome']]

    return render_template('Analysis.html', graphJSON=graphJSON, graphJSON2=graphJSON2, graphJSON3=graphJSON3,
                           graphJSON4=graphJSON4, graphJSON5=graphJSON5, graphJSON6=graphJSON6, graphJSON7=graphJSON7,
                           graphJSON8=graphJSON8,graphJSON9=graphJSON9)


@app.route('/deleteData', methods=["GET"])
def deleteData():
    id = request.args.get('id')
    print("id::::", id)
    connection = db_connect()
    cursor1 = connection.cursor()
    cursor1.execute("Delete from finalproject WHERE id=" + id)
    connection.commit()
    print("Delete Successfully")
    cursor1.close()
    connection.close()
    return redirect(url_for('viewData'))


@app.route('/editData', methods=['GET'])
def editData():
    id = request.args.get('id')

    print("register_id::::", id)

    connection = db_connect()

    cursor1 = connection.cursor()

    cursor1.execute("select * from finalproject WHERE id=" + id)

    data = cursor1.fetchall()

    connection.commit()

    cursor1.close()

    connection.close()

    return render_template('Edit.html', data=data)



@app.route('/getApiById', methods=['GET'])
def getApiById():
    id = request.args.get('id')

    print("register_id::::", id)

    connection = db_connect()

    cursor1 = connection.cursor()

    cursor1.execute("select * from finalproject WHERE id=" + id)

    data = cursor1.fetchall()

    connection.commit()

    cursor1.close()

    connection.close()

    if len(data)==0:
        return jsonify({"MESSAGE":"Id Not Found"}),404
    else:
        return jsonify(data),200



@app.route('/getApiByRange', methods=['GET'])
def getApiByRange():




    connection = db_connect()

    cursor1 = connection.cursor()

    cursor1.execute('select * from finalproject WHERE  DailyRate >={0} and DailyRate <={1}'.format(150,200))

    data = cursor1.fetchall()

    connection.commit()

    cursor1.close()

    connection.close()
    print(data)

    if len(data)==0:
        return jsonify({"MESSAGE":"Id Not Found"}),404
    else:
        return jsonify(data),200










@app.route('/updateData', methods=['POST'])
def updateData():
    registration_id = request.form.get('id')
    Age = request.form.get("Age")
    Attrition = request.form.get("Attrition")
    BusinessTravel = request.form.get("BusinessTravel")
    DailyRate = request.form.get("DailyRate")
    Department = request.form.get("Department")
    DistanceFromHome = request.form.get("DistanceFromHome")
    Education = request.form.get("Education")
    EducationField = request.form.get("EducationField")
    EmployeeCount = '1'
    # EmployeeCount = request.form.get("EmployeeCount")
    EmployeeNumber = request.form.get("EmployeeNumber")
    EnvironmentSatisfaction = request.form.get("EnvironmentSatisfaction")
    Gender = request.form.get("Gender")
    HourlyRate = request.form.get("HourlyRate")
    JobInvolvement = request.form.get("JobInvolvement")
    JobLevel = request.form.get("JobLevel")
    JobRole = request.form.get("JobRole")
    JobSatisfaction = request.form.get("JobSatisfaction")
    MaritalStatus = request.form.get("MaritalStatus")
    MonthlyIncome = request.form.get("MonthlyIncome")

    MonthlyRate = '0'
    # MonthlyRate = request.form.get("MonthlyRate")
    NumCompaniesWorked = request.form.get("NumCompaniesWorked")
    Over18 = "Y"
    OverTime = request.form.get("OverTime")
    PercentSalaryHike = request.form.get("PercentSalaryHike")
    PerformanceRating = request.form.get("PerformanceRating")
    RelationshipSatisfaction = request.form.get("RelationshipSatisfaction")
    StandardHours = '80'
    StockOptionLevel = request.form.get("StockOptionLevel")
    TotalWorkingYears = request.form.get("TotalWorkingYears")
    TrainingTimesLastYear = request.form.get("TrainingTimesLastYear")
    WorkLifeBalance = request.form.get("WorkLifeBalance")
    YearsAtCompany = request.form.get("YearsAtCompany")
    YearsInCurrentRole = request.form.get("YearsInCurrentRole")
    YearsSinceLastPromotion = request.form.get("YearsSinceLastPromotion")
    YearsWithCurrManager = request.form.get("YearsWithCurrManager")

    connection = db_connect()
    cursor1 = connection.cursor()
    # cursor1.execute(
    #     "Update finalproject (Age,Attrition,BusinessTravel,DailyRate,Department,DistanceFromHome,Education,EducationField,EmployeeCount,EmployeeNumber,EnvironmentSatisfaction,"
    #     "Gender,HourlyRate,JobInvolvement,JobLevel,JobRole,JobSatisfaction,MaritalStatus,MonthlyIncome,MonthlyRate,NumCompaniesWorked,"
    #     "Over18,OverTime,PercentSalaryHike,PerformanceRating,RelationshipSatisfaction,StandardHours,StockOptionLevel,"
    #     "TotalWorkingYears,TrainingTimesLastYear,WorkLifeBalance,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,"
    #     "YearsWithCurrManager) VALUES ('" + Age + "','" + Attrition + "','" + BusinessTravel + "','" + DailyRate + "','" + Department + "','" + DistanceFromHome + "','" + Education + "','" + EducationField + "','" + EmployeeCount + "','" + EmployeeNumber + "','" + EnvironmentSatisfaction + "','" + Gender + "','" + HourlyRate + "','" + JobInvolvement + "','" + JobLevel + "','" + JobRole + "','" + JobSatisfaction + "','" + MaritalStatus + "','" + MonthlyIncome + "','" + MonthlyRate + "','" + NumCompaniesWorked + "','" + Over18 + "','" + OverTime + "','" + PercentSalaryHike + "','" + PerformanceRating + "','" + RelationshipSatisfaction + "','" + StandardHours + "','" + StockOptionLevel + "','" + TotalWorkingYears + "','" + TrainingTimesLastYear + "','" + WorkLifeBalance + "','" + YearsAtCompany + "','" + YearsInCurrentRole + "','" + YearsSinceLastPromotion + "','" + YearsWithCurrManager + "')where id='"+registration_id+"'")
    # connection.commit()

    cursor1.execute(
        "Update finalproject SET"
        " Age ='" + Age + "',Attrition='" + Attrition + "',BusinessTravel='" + BusinessTravel + "',DailyRate='" + DailyRate + "',Department='" + Department + "',DistanceFromHome='" + DistanceFromHome + "',Education='" + Education + "',"
                                                                                                                                                                                                                                        "EducationField='" + Education + "',EmployeeCount='" + EmployeeCount + "',EmployeeNumber='" + EmployeeNumber + "',EnvironmentSatisfaction='" + EnvironmentSatisfaction + "',"
                                                                                                                                                                                                                                                                                                                                                                                                                 "Gender='" + Gender + "',HourlyRate='" + HourlyRate + "',JobInvolvement='" + JobInvolvement + "',JobLevel='" + JobLevel + "',JobRole='" + JobRole + "',JobSatisfaction='" + JobSatisfaction + "',MaritalStatus='" + MaritalStatus + "',MonthlyIncome='" + MonthlyIncome + "',MonthlyRate='" + MonthlyRate + "',NumCompaniesWorked='" + NumCompaniesWorked + "',"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             "Over18='" + Over18 + "',OverTime='" + OverTime + "',PercentSalaryHike='" + PercentSalaryHike + "',PerformanceRating='" + PerformanceRating + "',RelationshipSatisfaction='" + RelationshipSatisfaction + "',StandardHours='" + StandardHours + "',StockOptionLevel='" + StockOptionLevel + "',"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         "TotalWorkingYears='" + TotalWorkingYears + "',TrainingTimesLastYear='" + TrainingTimesLastYear + "',WorkLifeBalance='" + WorkLifeBalance + "',YearsAtCompany='" + YearsAtCompany + "',YearsInCurrentRole='" + YearsInCurrentRole + "',YearsSinceLastPromotion='" + YearsSinceLastPromotion + "',"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       "YearsWithCurrManager='" + YearsWithCurrManager + "' where id='" + registration_id + "'")
    connection.commit()

    print("Update Successfully")
    cursor1.close()
    connection.close()

    return redirect('/')


@app.route("/about")
def aboutPage():
    return render_template("about.html")


app.run(port="5678", threaded=True, debug=True)
