CMD CHALLENGE https://cmdchallenge.com/#/hello_world is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

Uploading Files to Remote Sandbox Server via SFTP
This guide demonstrates the steps to upload files from a local PC to a remote sandbox server using the SFTP (SSH File Transfer Protocol) client.

Requirements
  Local PC with files to upload
  Access credentials (username, password, or SSH key) for the remote sandbox server
  SFTP client installed (e.g., OpenSSH, WinSCP, FileZilla)

Steps
1. Connect to the Remote Sandbox Server
Open your terminal (or SFTP client) and initiate an SFTP connection to the remote sandbox server using the following command:

`sftp username@remote_server_ip`
Replace username with your username and remote_server_ip with the IP address or hostname of your sandbox server.

2. Authenticate
Enter your password or provide your SSH key passphrase when prompted to authenticate and establish the connection.

3. Navigate to the Desired Directory
Once connected, navigate to the directory where you want to upload your files using the cd command. For example:

`lcd /path/to/upload/directory`

4. Upload Files
Upload your local files to the remote server using the put command. Replace local_file.txt with the file(s) you want to upload:


`put local_file.png`
To upload multiple files, you can use a wildcard (*):


`put /local/path/to/files/*.png`
5. Verify Upload
To confirm that the files were successfully uploaded, you can list the contents of the remote directory using the ls command:


`lls`
This will display the files present in the current directory on the remote server.

Additional Notes
Always ensure secure file transfer by using SFTP over SSH.
Make sure you have appropriate permissions to access and write to the destination directory on the remote server.
Be cautious when deleting or overwriting files on the remote server to avoid unintended data loss.

https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server
