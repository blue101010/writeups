import OpenEXR
import Imath

# Replace with the path to your EXR file
file_path = 'whiteandblank'

try:
    # Open the EXR file
    exr_file = OpenEXR.InputFile(file_path)

    # Print the header
    header = exr_file.header()
    print('Header:', header)

    # Print the data window
    data_window = header['dataWindow']
    print('Data window:', data_window)

    # Print the display window
    display_window = header['displayWindow']
    print('Display window:', display_window)

    # Print the channels
    channels = header['channels']
    print('Channels:', channels)

    # For each channel, try to read the data and print the first few bytes
    for channel in channels:
        try:
            data = exr_file.channel(channel)
            print(f'First few bytes of data for channel {channel}:', data[:10])
        except Exception as e:
            print(f'Error reading data for channel {channel}:', e)
except Exception as e:
    print('An error occurred:', e)