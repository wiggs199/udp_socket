# udp_socket

## Basic UPD Socket that returns requested data from the server back to the client in uppercase form.  

## Purpose

    The client will send a line of text to the server.
    The server will receive the data and convert each character to uppercase.
    The server will send the uppercase characters to the client.
    The client will receive and display them on its screen.

Setup - 

Ensure Python3 is installed on your endpoint device. 

Create a new directory , then cd into that directory .

Clone this repository -> https://github.com/wiggs199/udp_socket.git 

Runtime -

Open termminal - Our first terminal window will be for our server. 

Run python3 udp.py server 
![Screen Shot 2021-03-22 at 3 18 44 PM](https://user-images.githubusercontent.com/46654803/112046028-e5c4e580-8b21-11eb-991a-f06b463e8aa5.png)

Server will begin to listen for the clients message 

![Screen Shot 2021-03-22 at 3 07 04 PM](https://user-images.githubusercontent.com/46654803/112044495-46ebb980-8b20-11eb-8941-b7a582999036.png)

Open a new window of terminal - This will be for our client 

Run udp.py client

![Screen Shot 2021-03-22 at 3 09 59 PM](https://user-images.githubusercontent.com/46654803/112044950-acd84100-8b20-11eb-9dbf-77391ddf4be0.png)

Enter your lowercase message for the server - 

![Screen Shot 2021-03-22 at 3 12 59 PM](https://user-images.githubusercontent.com/46654803/112045319-18baa980-8b21-11eb-82a6-7d21138f1c4a.png)

The server will respond by capitalizing your message - 

![Screen Shot 2021-03-22 at 3 15 17 PM](https://user-images.githubusercontent.com/46654803/112045603-6afbca80-8b21-11eb-803b-ed6fdbf8c1de.png)




