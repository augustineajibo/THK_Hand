
import socket

class THK_Hand_Controller:
    #def __init__(self, host, port):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

    def connect(self,host,port):
        #host, port =self.get_ip_port()
        #print(host)
        #print(port)
        try:
            self.socket.connect((host, port))
            print("Connected to THK hand at {} and port {}".format(host,port))
        except ConnectionRefusedError:
            print("Connection to robot hand server failed")
            exit(1)


    def send_command(self, command):
        try:
            self.socket.send(command)

        except ConnectionResetError:
            print("Connection to robot hand server lost")
            exit(1)

    def receive_feedback(self):
        try:
            feedback = self.socket.recv(1024)
            return feedback
        except ConnectionResetError:
            print("Connection to robot hand server lost")
            exit(1)

    def adjust_joint_orientation(current_orientation, movement_steps, linear_limit, rotational_limit):
    # Check the joint type (linear or rotational)
        joint_type = "linear" if "linear" in movement_steps else "rotational"

    # Extract movement steps for linear and rotational movements
        linear_step = movement_steps.get('linear', 0)
        rotational_step = movement_steps.get('rotational', 0)

    # Adjust joint orientation based on the steps while checking limits
        if joint_type == "linear":
            new_orientation = current_orientation + linear_step
        if abs(new_orientation) > linear_limit:
            print("Linear movement limit exceeded")
            return current_orientation
        else:  # rotational joint
            new_orientation = current_orientation + rotational_step
            if abs(new_orientation) > rotational_limit:
                print("Rotational movement limit exceeded")
            return current_orientation

        return new_orientation

    def close(self):
        self.socket.close()

# Example usage:
#if __name__ == "__main__":

    #hand=THK_Hand_Controller()
    #host = '192.168.30.200'
    #port = 1024
    #hand.connect(host,port)


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







