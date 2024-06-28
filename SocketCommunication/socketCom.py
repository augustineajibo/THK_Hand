
import socket

class THK_Hand_Controller:

    def __init__(self):
       self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def is_valid_ip(self,ip_address):
        parts = ip_address.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            try:
                if not 0 <= int(part) <= 255:
                   return print("Incorrect IP address {}".format(*ip_address))
            except ValueError:

                return print("Incorrect IP address {}".format(*ip_address))
        return ip_address



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


    def move(self, pos, speed, id):
        cmd = []
        cmd.append(0x01)
        speed = [speed & 0x00FF, (speed & 0xFF00) >> 8]

        if isinstance(pos, list):
            for inx in range(0,len(id)):
                pos_new = [pos[inx] & 0x00FF, (pos[inx] & 0xFF00) >> 8]
                data = [pos_new[1], pos_new[0], speed[1], speed[0]]
                cmd.append(id[inx])
                cmd.extend(data)

        else:
            pos = [pos & 0x00FF, (pos & 0xFF00) >> 8]
            # speed = [speed & 0x00FF, (speed & 0xFF00) >> 8]
            data = [pos[1], pos[0], speed[1], speed[0]]
            for id_no in id:
                cmd.append(id_no)
                cmd.extend(data)

        result = self.commandSend(cmd)
        if result[0] == 1:
            if result[2] == 1:
                return True
            else:
                return False

    def MoveOrigin(self):
        # move_origin = [0x00, 0x01, 0x01]
        cmd = [0x00,0x00]
        result = self.commandSend(cmd)
        #print(result)
        if result[2] == 2:
            print("Error")
        else:
            print("OK")

    def MoveAllGrip(self, pos, speed):
        finger_id = [2, 4, 6, 8]

        if isinstance(pos, list):
            result = self.move(pos, speed, finger_id)
        else:
            result = self.move(pos, speed, finger_id)
        return result

    def MoveAllFingers(self, pos, speed):
        finger_id = [1, 3, 5, 7]
        result = self.move(pos, speed, finger_id)
        return result



    def Specific_Rotation(self, pos, speed,finger_id):
        #finger_id = [9, 10, 11, 12]
        #finger_id = [9]
        result = self.move(pos, speed, finger_id)
        return result

    def Specific_Linear(self, pos, speed,finger_id):
        # finger_id =[1,3,5,7]
        #finger_id = [1]
        result = self.move(pos, speed, finger_id)
        return result

    def Specific_Grip(self, pos, speed,finger_id):
        #finger_id = [2, 4, 6, 8]
        #finger_id = [2]

        if isinstance(pos, list):
            result = self.move(pos, speed, finger_id)
        else:
            result = self.move(pos, speed, finger_id)
        return result
    def get_data(self,data):
        str_data = []
        cmd = []
        cmd.append(0x04)  # Head
        cmd.extend(data)
        result = self.commandSend(cmd)
        #print(type(result))
        bytes_data = list(result)
        # bytes_data = [chr(r) for r in receive]
        #print(bytes_data)

        if bytes_data[2] == 2:
            return False

        sub_data = bytes_data[3:]

        if sub_data[0] == 0:
            print("Version")
            sub_data_len = sub_data[1]
            data = sub_data[2:]
            print(f'sub data:{data}')
            str_data.append(data[0] & 0x000000FF)
            str_data.append(data[1] & 0x000000FF)
            str_data.append(data[2] & 0x000000FF)
            str_data.append(data[4] << 8 & 0x0000FF00 | data[3] & 0x000000FF)
            return str_data
        elif sub_data[0] == 1: # System Status
            print("System Status")
            msg=['Normal operation','Invalid model number','MCU version acquisition failure','MCU startup failure','MCU reset detected at startup',
                'MCU communication failure at startup','Hand voltage error', 'Motor driver VREF error',
                 'Motor driver overcurrent/thermal shut signal detectio','Abnormality occurred during MCU communication',
                 'DMA transfer error','Alarm: Electronic thermal error','Alarm: Overspeed error','Alarm: Position error error (current position cannot be maintained while motor is stopped)',
                'Alarm: Position error error (reverse rotation detected while motor is rotating)']
            data = sub_data[2:]
            for i in data:
                str_data.append(msg[i])
            return str_data

        elif sub_data[0] == 2: # Overcurrent/thermal condition
            print("Overcurrent/thermal condition")
            data = sub_data[2:]
            str_data.append(data[1] << 8 & 0x0000FF00 | data[0] & 0x000000FF)
            return str_data

        elif sub_data[0] == 3: #Action mode
            print("Action mode")
            msg=['Return to origin','Keep current position','Illegal instruction received','Execute servo off with command 0x07',
                'Execute angle command (touch stop)','Illegal instruction received','Execute angle command (grip)',
                 'Angle command execution','Stopped because the current position could not be kept (reverse input possible)']
            data = sub_data[2:]
            for i in data:
                str_data.append(msg[i])
            return str_data

        elif sub_data[0] == 4: #Operating condition
            print("Operating condition")
            data = sub_data[2:]
            txt = (data[1] << 8) & 0x0000FF00 | (data[0] & 0x000000FF)
            str_data.append(txt)
            return str_data

        elif sub_data[0] == 5: # Encoder count
            print("Encoder count")
            sub_data_len = sub_data[1]
            data = sub_data[2:]
            print(data)

            for i in range(0,sub_data_len, 2):
                txt = (data[i + 1] << 8) & 0x0000FF00 | (data[i] & 0x000000FF)
                str_data.append(txt)
            return str_data

        elif sub_data[0] == 6:  #Sensor reaction status
            # print("Sensor reaction status")
            sub_data_len = sub_data[1]
            data = sub_data[2:]

            # txt = (data[0] & 0x000000FF)
            # str_data.append(txt)
            txt = data[1] << 8 & 0x0000FF00
            str_data.append(data)
            return str_data


        elif sub_data[0] == 7: # Sensor Value
            #print("Sensor Value")
            sub_data_len = sub_data[1]
            data = sub_data[2:]
            #print(data)
            for i in range(0,sub_data_len, 2):
                txt = (data[i+1] << 8) & 0x0000FF00 | (data[i] & 0x000000FF)
                str_data.append(txt)

            return str_data


    def close(self):
        self.client_socket.close()







