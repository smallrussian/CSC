from gpiozero import LED
from gpiozero import MotionSensor
import requests###do 'pip install requests' in the command line 
def send_sms(phone, msg, apikey):
    """
    Sends an SMS through the Textbelt API.
    :param phone: Phone number to send the SMS to.
    :param msg: SMS message. Should not be more than 160 characters.
    :param apikey: Your textbelt API key. 'textbelt' can be used for free for 1 SMS per day.
    :returns: True if the SMS could be sent. False otherwise.
    :rtype: bool
    """
    result = True
    json_success = False
    # Attempt to send the SMS through textbelt's API and a requests instance.
    try:
        resp = requests.post('https://textbelt.com/text', {
            'phone': phone,
            'message': msg,
            'key': apikey,
        })
    except:
        result = False
    # Extract boolean API result
    if result:
        try:
            json_success = resp.json()["success"]
        except:
            result = False
    # Evaluate if the SMS was successfully sent.
    if result:
        if not json_success:
            result = False
    # Give the result back to the caller.
    return result

api="abf83665ccb402dbfbd24f4cd03edb6d5975eee2WBBQPbsE52XUOypRVMAp0fI"
green_led = LED(17)
pir = MotionSensor(4)
green_led.off() 
#https://www.pragmaticlinux.com/2021/02/how-to-send-an-sms-message-using-python/

######I made this a function so it can easily be called in the GUY file
def detectMotion(number):
        if number=="":
            print("Please enter a vald phone number.",endl="")
            return
        while True:
            try:
                pir.wait_for_motion()
                send_sms(number, "Motion Detected",api)
                print("motion detected")
                green_led.on()
                pir.wait_for_no_motion()
                green_led.off()
                send_sms(number,"motion stopped", api)
                print("motion stopped")
            except KeyboardInterrupt:
                print("Have a nice day!")
                break
        return


    ###that is the API key 
    #abf83665ccb402dbfbd24f4cd03edb6d5975eee2WBBQPbsE52XUOypRVMAp0fIg
    #abf83665ccb402dbfbd24f4cd03edb6d5975eee2WBBQPbsE52XUOypRVMAp0fIgK
    #abf83665ccb402dbfbd24f4cd03edb6d5975eee2WBBQPbsE52XUOypRVMAp0fIgK