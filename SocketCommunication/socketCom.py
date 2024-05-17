
import socket

class THK_Hand_Controller:

    def __init__(self):
        #client_socket=socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def is_valid_ip(self,ip_address):
        parts = ip_address.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            try:
                if not 0 <= int(part) <= 255:
                    #print("Incorrect IP address {}".format(*ip_address))
                    return print("Incorrect IP address {}".format(*ip_address))
            except ValueError:

                return print("Incorrect IP address {}".format(*ip_address))
        return ip_address

    """
    def get_ip_port(self):
        host=[]
        port=[]

        ip = str(input("Enter a number (or a non-numeric value to stop): "))
        host.append(ip)
        prt = int(input("Enter a number (or a non-numeric value to stop): "))
        port.append(prt)

        if host[0] == "192.168.30.200" and port[0] == 1024:
            print("correct IP and Port entered")
            return host[0], port[0]
        else:
            print("Invalid ip or port entered")

        return (host[0], port[0])
    """

    def connect(self,host,port):
        status=[]
        try:
            self.client_socket.connect((host, port))
            status.append(1)
            print("Connected to THK hand at {} and port {}".format(host,port))
        except ConnectionRefusedError:
            status.append(0)
            print("Connection to THK hand failed!")
        return status


    def send_command(self, command):
        try:
            self.client_socket.send(command)

        except ConnectionResetError:
            print("Connection to robot hand server lost")
            exit(1)

    def add_command_length(self, cmd):
        length = len(cmd[1:])
        cmd.insert(1, length)
        return cmd
    def send(self,cmd):
        self.client_socket.sendall(bytearray(cmd))
        result = self.client_socket.recv(1024)
        return result
    def commandSend(self,cmd):
        cmd = self.add_command_length(cmd)
        response_data = self.send(cmd)
        # result = list(response_data)
        # no = output_numbers[0]
        # print(f'Response from hand {output_numbers}')
        # msg = self.status_message(no)
        return response_data

    def MoveOrigin(self):
        # move_origin = [0x00, 0x01, 0x01]
        cmd = [0x00,0x00]
        result = self.commandSend(cmd)
        print(result)
        if result[2] == 2:
            print("Error")
        else:
            print("OK")





    def close(self):
        self.client_socket.close()

# Example usage:
#if __name__ == "__main__":

    #hand=THK_Hand_Controller()
    #host = '192.168.30.200'
   # port = 1024
    #hand.connect(host,port)
    #hand.MoveOrigin()


    #controller = RobotHandController(host, port)

    # return the fingers to default postion
    #controller.send_command(b'\x00\x01\x00')

    #controller.send_command(b'\x00\x01\x00')

    #controller.send_command(b'\x00\x01\x0c')
    #controller.send_command(b'\x02\x01\x00')
    #controller.send_command(b'\x02\x01\x00')
    #0x40, 0x00, 0x00, 0x00

    #controller.send_command(b'\x04\x04\x01\x00\x00\x00')

    #feedback = controller.receive_feedback()
    #print("Feedback:", feedback)

    #controller.send_command("move_finger2")

    # Close the connection
    #controller.close()







