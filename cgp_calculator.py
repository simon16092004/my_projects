import pandas as pd
class cgp:
    def __init__(self):
        self.mark_status = {"Subject":[],"Mark":[],"Grade_Point":[],"Credit":[]}
        self.weigtedgradepoints = 0
        self.sum_of_credits = 0
        self.cgpis = 0

    def get_input(self):
     
     while True:
          
           subject = input("Enter the subject:")
           if subject == " " or subject == "/t":
               break 
           mark = int(input("Enter the mark:"))
           grade_point = 0
           if mark>=90:
               grade_point = 10
           elif 80 <= mark <90:
               grade_point = 9
           elif 70 <= mark < 80:
               grade_point = 8
           elif 60 <= mark < 70 :
               grade_point = 7
           elif 50 <= mark < 60:
               grade_point = 6
           elif 40 <= mark < 50:
               grade_point = 5
           elif mark<40:
               grade_point = 0

           credit = int(input("Enter the credit:"))
           self.mark_status["Subject"].append(subject)
           self.mark_status["Mark"].append(mark)
           self.mark_status["Grade_Point"].append(grade_point)
           self.mark_status["Credit"].append(credit)
    def total_credits(self):
       self. sum_of_credits = sum(self.mark_status["Credit"])
        
    def weigthed_grade_points(self):
        self.weigtedgradepoints =sum(grade_point*credit for grade_point,credit in zip(self.mark_status["Grade_Point"],self.mark_status["Credit"]))
        
    def cgp_calculation(self):
        self.cgpis = self.weigtedgradepoints/self.sum_of_credits
        
    

    def display_data(self):
        pd_data = pd.DataFrame(self.mark_status)
        print(pd_data)
        print("The CGPA is:",self.cgpis)
    def save_excel(self):
        excel_data = pd.DataFrame(self.mark_status)
        excel_data.to_excel("cgpa.xlsx",index=False)

obj = cgp()
obj.get_input()
obj.total_credits()
obj.weigthed_grade_points()
obj.cgp_calculation()
obj.display_data()
obj.save_excel()


