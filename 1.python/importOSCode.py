import os

# Specify the directory path
directory_path = "/"  # change this to the path you want

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print each item
print(contents)

'''
Output
listed folder from my c drive 
['$Recycle.Bin', 'Documents and Settings', 'DumpStack.log', 'DumpStack.log.tmp', 'hiberfil.sys', 'inetpub', 'Intel', 'MSOCache', 'pagefile.sys', 'PerfLogs', 'Program Files', 'Program Files (x86)', 'ProgramData', 'Recovery', 'swapfile.sys', 'System Volume Information', 'Users', 'Windows']
'''
