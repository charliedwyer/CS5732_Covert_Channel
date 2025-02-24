import os
import time

# Sender tool
def covert_channel_send_size(message, directory):
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    
    for bit in binary_message:
        filename = os.path.join(directory, f"file_{time.time()}.txt")
        with open(filename, 'w') as f:
            if bit == '1':
                f.write('A')  # Append a small amount of data for '1'
            else:
                f.write('')  # Leave empty for '0'
        time.sleep(0.1)  

# Receiver tool
def covert_channel_receive_size(directory):
    files = sorted(os.listdir(directory))  # Sort files by timestamp order
    message_binary = []
    
    for filename in files:
        file_path = os.path.join(directory, filename)
        size = os.path.getsize(file_path)
        if size > 0:  # If size is greater than 0, it's a '1'
            message_binary.append('1')
        else:
            message_binary.append('0')
    
    # Convert binary back to string
    message = ''.join(message_binary)
    decoded_message = ''.join(chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8))
    print(f"Decoded message: {decoded_message}")

# Example usage
message = "Hello"
directory = "./covert_channel_files_size"
os.makedirs(directory, exist_ok=True)
covert_channel_send_size(message, directory)
covert_channel_receive_size(directory)
