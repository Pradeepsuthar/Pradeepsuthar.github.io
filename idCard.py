import pyqrcode
import pandas as pd

def getCSVdata():
  df = pd.read_csv('identityCard.csv')
  for index, values in df.iterrows():
    roll_no = values['Roll No.']
    name = values['Name ']
    father_name = values["Father's Name"]
    branch = values['Branch']
    dob = values['Date of Birth']
    address = values['Resi Address']
    mobile_no = values['Mobile No.']
    batch = values['Betch No.']

    data = f'''
      Roll No. : {roll_no} \n
      Name : {name} \n
      Father's Name : {father_name} \n
      Branch : {branch} \n
      Date of Birth : {dob} \n
      Address : {address} \n
      Mobile Number : {mobile_no} \n
      Batch No. : {batch} \n
    '''

    QRCodeImage = pyqrcode.create(data)
    QRCodeImage.svg(f"{name}.svg", scale='5')
  
getCSVdata()