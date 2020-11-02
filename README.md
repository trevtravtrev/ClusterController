# ClusterController
 Controller for raspberry pi clusters that allows custom messages to be sent to all client pis from command line.  

To use:  
- controller.py runs on server pi (this is the terminal program that allows user input)  
- controller_server.py runs on server pi  
- controller_client.py runs on every client pi  

Current supported messages:  
- shutdown (shuts raspberry pi down after 5 seconds)  
- reboot (reboots raspberry pi after 5 seconds)  
- test (sends a test message to check if client/server socket connections are working correctly)