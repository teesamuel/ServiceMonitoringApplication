
"""
Author name: Samuel olufemi
Author email: olufemititilayosamuel@gmail.com

This service checks of a service is running on a port and 
restarts it based on the command suppilied
"""
class ServiceMonitor():
    def __init__(self,command,port,host='localhost') -> None:
        self.host = host 
        self.port = port 
        self.command = command 
        
    def main(self)->None:
        print("Application monitor begins")
        self.check_service()
        print("End Application monitor begins")

    def check_service(self)-> None:
        if(not self.is_port_in_use()):
            print("Application is not running on the specified "+self.host+" port "+str(self.port))
            print("BEGIN APPLICATION RESTART ")
            import subprocess
            subprocess.call(self.command, shell=True)
            print("END APPLICATION RESTART ")
        else:
            print("Application is currently running on "+self.host+" port "+str(self.port))

    def is_port_in_use(self) -> bool:
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex((self.host, self.port)) == 0


#This is a test use usage for thr  monitoring service This will restart my java application runnig on port 7777
service = ServiceMonitor('cd /www/javaapp && java -jar myjavaapp.jar &',7777)
service.main()