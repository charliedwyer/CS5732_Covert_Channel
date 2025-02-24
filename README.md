# Covert Channel: File Size-Based Communication

This project demonstrates a covert channel technique for communicating messages by encoding and decoding data based on file sizes.

## Requirements

- Python 3.x
- Required libraries: `os`, `time`

## Setup Instructions

### 1. Clone the repository

If you haven't already, clone the repository to your local machine:

```bash
git clone https://github.umn.edu/DWYER316/CS5732_covert_channel.git
cd CS5732_covert_channel
```

### 2. Create a directory for covert channel files

The code uses a directory to store files that represent the binary message. You can create a directory named `covert_channel_files_size`, or the program will automatically create it in the current working directory if it doesn't already exist:

```bash
mkdir covert_channel_files_size
```

### 3. Run the code

Ensure the script is located in the repository directory. Then, run the following command:

```bash
python covert_channel.py
```

- **Encoding the message**: The `covert_channel_send_size()` function will take a message (e.g., "Hello") and create files in the directory `covert_channel_files_size`. Each file will represent a bit of the message:
  - A non-empty file (e.g., with a single letter like `A`) represents a `1`.
  - An empty file represents a `0`.

- **Decoding the message**: The `covert_channel_receive_size()` function will read the files, check their sizes, and convert the file sizes back to the original message.

### Example Output

After running the code, the decoded message should be printed to the console:

```bash
Decoded message: Hello
```

## Notes

- You can change the 'message' variable to any message you want to test ("Hello" by default)



