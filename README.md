# README #

SMS-Sender for Link Mobility PSWincom SMS Gatway. (wiki.pswin.com)
Written as a learning experience in Python. 

### Uses the XML interface for the SMS Gateway developed by PSWinCom AS ###

Sends single or multiple messages with configurable batchsize. 

Contains two classes. You need to use the sms class in SMSMessage.py to get started
like this. 
import SMSMessage as s
sender = s.sms(username,password) 

Then add messages with 
sender.sms_add('message','phonenumber with countrycode','Optional senderid') # of course replace these with proper values (sender.sms_add('Good morning Phoo','470000000','Piglet')

when all messages are added use sms_send to push messages to gateway. 
it uses the SMS_Batchsize property to build message batches. for instance setting it to 50 will send 50 messages for each POST. It will then do this until all messages are sendt. 

### status tracking - Not yet implemented ###