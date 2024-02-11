#Import your dependencies
import platform
from hdbcli import dbapi

#verify the architecture of Python
print ("Platform architecture: " + platform.architecture()[0])

try :
    #Initialize your connection
    conn = dbapi.connect(
       
        #Option2, specify the connection parameters
        address='8c7295c3-3335-4f4b-b3b8-2af24af9da50.hana.trial-us10.hanacloud.ondemand.com',
        port='443',
        user='SSURAMPALLY',
        password='Python@1',

        #Additional parameters
        #encrypt=True, # must be set to True when connecting to HANA as a Service
        #As of SAP HANA Client 2.6, connections on port 443 enable encryption by default (HANA Cloud)
        sslValidateCertificate=False #Must be set to false when connecting
        #to an SAP HANA, express edition instance that uses a self-signed certificate.
    )
except dbapi.Error as er:
    print('Connect failed, exiting')
    print(er)
    exit()

#If no errors, print connected
print('connected')

cursor = conn.cursor()
sql_command = "SELECT id, app_name, data_format FROM SSURAMPALLY.PYTHON_APPLICATION;"
cursor.execute(sql_command)

rows = cursor.fetchall()
for row in rows:
    for col in row:
        print ("%s" % col, end=" ")
    print ("  ")
cursor.close()
print("\n")


conn.close()
