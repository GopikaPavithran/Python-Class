# class A:
#     def funA(self):
#         print('Parent A')
# class B(A):
#     def funB(self):
#         print('Derived B')
# class C(B):
#     def funC(self):
#         print('Derived C')
# obj=C()
# obj.funC()
# obj.funB()
# obj.funA()


# # Q: Create parent class hospital and a child class doctor which inherit hospital. and another class patient
# # which inherit doctor.
# # A:
#                          # without using constructor
# class Hospital:
#     def hos(self,h_name,location):
#         self.hn=h_name
#         self.l=location
# class Doctor(Hospital):
#     def doc(self,d_name,specialization):
#         self.dn=d_name
#         self.s=specialization
# class Patient(Doctor):
#     def pat(self,p_name,token_number):
#         self.pn=p_name
#         self.tn=token_number
#     def display(self):
#         print('Hospital:',self.hn)
#         print('Location:',self.l)
#         print('Doctor:',self.dn)
#         print('Specialization:',self.s)
#         print('Patient:',self.pn)
#         print('Token Number:',self.tn)
# p=Patient()
# p.pat('Rahul',63)
# p.doc('Gopinath','Pediatric')
# p.hos('KAH','Cheruvathur')
# p.display()

#                      # using constructor
#
# class Hospital:
#     def __init__(self,h_name,location):
#         self.hn=h_name
#         self.l=location
# class Doctor(Hospital):
#     def __init__(self,h_name,location,d_name,specialization):
#         Hospital.__init__(self,h_name,location)
#         self.dn=d_name
#         self.s=specialization
# class Patient(Doctor):
#     def __init__(self,h_name,location,d_name,specialization,p_name,token_no):
#         Doctor.__init__(self,h_name,location,d_name,specialization)
#         self.pn=p_name
#         self.tn=token_no
#     def display(self):
#         print('Hospital:', self.hn)
#         print('Location:',self.l)
#         print('Doctor:',self.dn)
#         print('Specialization:',self.s)
#         print('Patient Name:',self.pn)
#         print('Token Number:',self.tn)
# obj=Patient('KAH','Cheruvathur','Muhammad Ali','Neurology','Alex',12)
# obj.display()
        
