import ftplib

# connect to the server
ftp = ftplib.FTP('13.69.253.140','iblog', 'xj7BW5owX4NOJDdd7kKE')
ftp.login() 

# switch to the directory containing the data
ftp.cwd('/var/www/wordpress/wp-content/')
ftp.pwd()

# get the list of files in this ftp dir
all_files= ftp.nlst()
hail_files = [i for i in all_files if i.startswith('hail')]

# now download to the desired path
for filename in hail_files:
    print("Downloading " + filename, end=" | ")
    with open(r'.\\' 
              + filename, "wb") as file_handle:
        ftp.retrbinary("RETR " + filename, file_handle.write)
    print(" finished")
