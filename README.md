# twilio-code-aws-lambda-text-to-voice
In this code i am showing how to create an text message has input and to make a call with text as output using twilio app

first get registered in twilio and get ACCOUNT_SID and AUTH_TOKEN.
also, get the phone registered to whom you are making call and get the number by which you want to get the call from twilio (it is free on trail basis ,also you can pay and get one)

the input text that you have given to the code will generate an xml format which twilio api reads that and render it as voice message.

twiml - twilio markup language.

also i have shown you aws-lambda code, i assume people know lambda and who it works.
else go through these docs
https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

for detail documentation :
https://www.twilio.com/docs/quickstart?filter-product=voice&filter-language=python
