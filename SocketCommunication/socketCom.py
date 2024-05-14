
import socket

class RobotHandController:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            print("Connected to robot hand server")
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
if __name__ == "__main__":
    host = '192.168.30.200'
    port = 1024

    controller = RobotHandController(host, port)

    # return the fingers to default postion
    #controller.send_command(b'\x00\x01\x00')
    controller.send_command(b'\x00\x01\x00')
    #controller.send_command(b'\x00\x01\x0c')
    #controller.send_command(b'\x02\x01\x00')
    #controller.send_command(b'\x02\x01\x00')
    #0x40, 0x00, 0x00, 0x00

    #controller.send_command(b'\x04\x04\x01\x00\x00\x00')

    feedback = controller.receive_feedback()
    print("Feedback:", feedback)

    #controller.send_command("move_finger2")

    # Close the connection
    controller.close()







