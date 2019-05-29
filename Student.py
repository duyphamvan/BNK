import psycopg2

class Student:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="exam_management",
            user="postgres",
            password="123456"
        )

    def create_new_student(self):
        file = open('student.txt', 'r')
        content = file.read()
        names_list = [y for y in (x.strip() for x in content.splitlines()) if y]
        students = names_list[3::]
        arr = []

        for i in students:
            i = i.split(',')
            i = tuple(i)
            arr.append(i)

        cur = self.conn.cursor()
        sql = "INSERT INTO student (id, name, birthday, home_town, math, physical, chemistry) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.executemany(sql, arr)
        self.conn.commit()
        print(cur.rowcount, "record inserted.")

    def import_to_admissions(self):
        file = open('student.txt', 'r')
        content = file.read()
        names_list = [y for y in (x.strip() for x in content.splitlines()) if y]
        admissions = names_list[0:3:1]
        pass_point = int(admissions[0])
        amount = int(admissions[1])
        total_student = int(admissions[2])
        cur = self.conn.cursor()
        sql_admissions = "INSERT INTO admissions (pass_point, amount, total_student) VALUES (%s,%s,%s)"
        arr_admissions = (pass_point, amount, total_student)
        cur.executemany(sql_admissions, (arr_admissions,))
        self.conn.commit()
        print(cur.rowcount, "record inserted.")

    def get_total_student(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM student")
        result = cur.fetchall()
        sort = sorted(result,  key=lambda x: (x[1]))
        print(sort)
        return sort
    def print_list_student_pass_point(self):
        file = open('student.txt', 'r')
        content = file.read()
        names_list = [y for y in (x.strip() for x in content.splitlines()) if y]
        admissions = names_list[0:3:1]
        pass_point = int(admissions[0])
        amount = int(admissions[1])
        total_student = int(admissions[2])
        data = self.get_total_student()
        data = list(data)

        list_student_pass_point = []
        for i in data:
            sum = float(i[4]) + float(i[5]) + float(i[6])
            if sum > pass_point:
                list_student_pass_point.append(i)
        sort = sorted(list_student_pass_point, key=lambda x: (x[4]+x[5]+x[6]) ,reverse=True)
        print(len(sort))
        while len(sort) > amount:
            sort.pop()
        print(sort)


student = Student()
# student.create_new_student()
# student.import_to_admissions()
student.get_total_student()
# student.print_list_student_pass_point()
