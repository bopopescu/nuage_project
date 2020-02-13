import json
from flask import Flask, request, jsonify
from flasgger import Swagger
from flasgger.utils import swag_from
from flasgger import LazyString, LazyJSONEncoder
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
# def del_employee(emp_id2):
#     output = {"Null"}
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='employee',
#                                              user='root',
#                                              password='')
#         employee_info = """DELETE FROM emp_table where emp_id =%s"""
#         cursor = connection.cursor()
#         vari = (emp_id2)
#         cursor.execute(employee_info, (vari,))
#         connection.commit()
#         print('Sucess')
#         cursor.close()
#     except Error as e:
#         print("Error while connecting to MySQL", e)
#     finally:
#         if (connection.is_connected()):
#             cursor.close()
#             connection.close()
#     output = {"Null"}
#     del_employee = "Sucess"
#     output["Sucess"] = del_employee
#     return output
#
# def add_employee(emp_name1, emp_id1, emp_email1, emp_number1,password1):
#     output = {"Null"}
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='employee',
#                                              user='root',
#                                              password='')
#         employee_info = """INSERT INTO emp_table(emp_name, emp_id, emp_mail, emp_number, password) VALUES (%s,%s,%s,%s,%s)"""
#         cursor = connection.cursor()
#         vari = (emp_name1, emp_id1, emp_email1, emp_number1, password1)
#         cursor.execute(employee_info, vari)
#         connection.commit()
#         print(cursor.rowcount, 'Sucess')
#         cursor.close()
#     except Error as e:
#         print("Error while connecting to MySQL", e)
#     finally:
#         if (connection.is_connected()):
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")
#     output = {"Null"}
#     add_employee = "Sucess"
#     output["Sucess"] = add_employee
#     return output
#
# def update_employee(emp_number3,password3,emp_id3):
#     output={"Null"}
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='employee',
#                                              user='root',
#                                              password='')
#         employee_info = """Update emp_table set emp_number = %s, password = %s where emp_id = %s"""
#         cursor = connection.cursor()
#         vari = (emp_number3, password3, emp_id3)
#         cursor.execute(employee_info, vari)
#         connection.commit()
#         print('Sucess')
#         cursor.close()
#     except Error as e:
#         print("Error while connecting to MySQL", e)
#     finally:
#         if (connection.is_connected()):
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")
#     output = {"Null"}
#     update_employee = "Sucess"
#     output["Sucess"] = update_employee
#     return output
#
# def login_employee(emp_id4,password4):
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='employee',
#                                              user='root',
#                                              password='')
#         employee_info = "select password from emp_table where emp_id =%s"
#         cursor = connection.cursor()
#         vari = (emp_id4)
#         cursor.execute(employee_info, (vari,))
#         record = cursor.fetchone()
#         print(record[0])
#         connection.commit()
#         print('Sucess')
#         cursor.close()
#     except Error as e:
#         print("Error while connecting to MySQL", e)
#     finally:
#         if (connection.is_connected()):
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")
#     if(record[0]==password4):
#
#         output = ("Your Status Login")
#         return output
#     else:
#         output=("NOT")
#         return output
#

def add_items(product_id1, product_name1, Product_avail1, product_price1):
    output = {"Null"}
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='employee',
                                             user='root',
                                             password='')
        employee_info = """INSERT INTO elect_items(product_id, product_name, Product_avail, product_price) VALUES (%s,%s,%s,%s)"""
        cursor = connection.cursor()
        vari1 = (product_id1, product_name1, Product_avail1, product_price1)
        cursor.execute(employee_info, vari1)
        connection.commit()
        print(cursor.rowcount, 'Sucess')
        cursor.close()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    output = {"Null"}
    add_items = "Sucess"
    output["Sucess"] = add_items
    return output


def update_stock(product_id2,product_avail2):
    output={"Null"}
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='employee',
                                             user='root',
                                             password='')
        employee_info = """Update elect_items set product_avail = %s where product_id = %s"""
        cursor = connection.cursor()
        vari = (product_avail2,product_id2)
        cursor.execute(employee_info, vari)
        connection.commit()
        print('Sucess')
        cursor.close()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    update = "Sucess Entered"
    output["Sucess"] = update
    return output




# def views(emp_id):
    # a=emp_id
    # try:
    #     connection = mysql.connector.connect(host='localhost',
    #                                          database='employee',
    #                                          user='root',
    #                                          password='')
    #     employee_info = "select * from elect_items"
    #     cursor = connection.cursor()
    #     cursor.execute(employee_info)
    #     records = cursor.fetchall()
    #     # record = cursor.fetchone()
    #     # print(record[0])
    #     a = []
    #     b = []
    #     for row in records:
    #         a.append(row[1])
    #         b.append(row[2])
    #
    #     connection.commit()
    #     # print('Sucess')
    #     cursor.close()
    # except Error as e:
    #     print("Error while connecting to MySQL", e)
    # finally:
    #     if (connection.is_connected()):
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed")
    # res = {}
    # res = {a[i]: b[i] for i in range(len(a))}
    # print("Resultant dictionary is : " + str(res))
    # return res
    #


app = Flask(__name__)
app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 2}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/swagger/",
}

template = dict(
    swaggerUiPrefix=LazyString(lambda: request.environ.get("HTTP_X_SCRIPT_NAME", ""))
)

app.json_encoder = LazyJSONEncoder
swagger = Swagger(app, config=swagger_config, template=template)


@app.route("/")
def index():
    return "Add Employee"


# @app.route("/Add Employee", methods=["POST"])
# @swag_from("swagger_config.yml")
# def add_emp():
#     input_json = request.get_json()
#     try:
#         emp_name1 = input_json["x1"]
#         emp_id1 = input_json["x2"]
#         emp_email1 = input_json["x3"]
#         emp_number1 =input_json["x4"]
#         password1 = input_json["x5"]
#         res = add_employee(emp_name1, emp_id1, emp_email1, emp_number1,password1)
#     except:
#         res = {"success": False, "message": "Unknown error"}
#
#     return json.dumps(res)
#
# @app.route("/Delete Employee", methods=["DELETE"])
# @swag_from("swagger_config.yml")
# def del_emp():
#     input_json = request.get_json()
#     try:
#         emp_id2 = input_json["y1"]
#         res = del_employee(emp_id2)
#     except:
#         res = {"success": False, "message": "Unknown error"}
#     return json.dumps(res)
#
# @app.route("/Update Employee", methods=["PUT"])
# @swag_from("swagger_config.yml")
# def update_emp():
#     input_json = request.get_json()
#     try:
#         emp_number3 = input_json["z1"]
#         password3 = input_json["z2"]
#         emp_id3 = input_json["z3"]
#         res = update_employee(emp_number3,password3,emp_id3)
#     except:
#         res = {"success": False, "message": "Unknown error"}
#     return json.dumps(res)
#
# @app.route("/Login Employee", methods=["GET"])
# @swag_from("swagger_config.yml")
# def login_emp():
#     input_json = request.get_json()
#     print(input_json)
#     try:
#         emp_id4 = str(input_json["username"])
#         password4 = str(input_json["password"])
#         print(emp_id4,password4)
#         res = login_employee(emp_id4,password4)
#     except:
#         res = {"success": True, "message": "Unknown error"}
#     return json.dumps(res)

@app.route("/Add Electronic Items", methods=["POST"])
@swag_from("swagger_config.yml")
def add_item():
    input_json = request.get_json()
    try:
        product_id1 = str(input_json["q1"])
        product_name1 = str(input_json["q2"])
        product_avail1 = str(input_json["q3"])
        product_price1 =str(input_json["q4"])
        res = add_items(product_id1,product_name1,product_avail1,product_price1)
    except:
        res = {"success": False, "message": "Unknown error"}
        return json.dumps(res)

@app.route("/Update Stock", methods=["PUT"])
@swag_from("swagger_config.yml")
def update_stk():
    input_json = request.get_json()
    try:
        product_id2 = input_json["s1"]
        product_avail2 = int(input_json["s2"])
        res = update_stock(product_id2,product_avail2)
    except:
        res = {"success": False, "message": "Unknown error"}
    return json.dumps(res)


@app.route("/Views", methods=["POST"])
@swag_from("swagger_config.yml")
def view():
    input_json = request.get_json()
    try:
        product_id2 = input_json["v1"]
        connection = mysql.connector.connect(host='localhost',
                                                database='employee',
                                                user='root',
                                                password='')
        employee_info = "select * from elect_items"
        cursor = connection.cursor()
        cursor.execute(employee_info)
        records = cursor.fetchall()
            # record = cursor.fetchone()
            # print(record[0])
        a = []
        b = []
        for row in records:
            a.append(row[1])
            b.append(row[2])
        # print(a)
        connection.commit()
            # print('Sucess')
        cursor.close()
    except Error as e:
        res1 = {"success": False, "message": "Unknown error"}
        print(res1)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    res1 = {}
    res1 = {a[i]: b[i] for i in range(len(a))}
    print("Resultant dictionary is : " + str(res1))


    return json.dumps(str(res1))


if __name__ == "__main__":
    app.run(debug=True, port=8793)
