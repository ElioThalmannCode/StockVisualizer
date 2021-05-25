import configparser
import os
import json

class config:
    def initialize():
        if(not os.path.isfile("config.conf")):
            config.create_config()
        
    def create_config():

        firstConfig = {
    "stocks" : ["BTC-USD","ETH-USD","AAPL","TSLA","NIO"]
}
        firstConfig = json.dumps(firstConfig)

        with open("config.conf", "w") as jsonfile:
            jsonfile.write(firstConfig)
    def getstocks():
        with open("config.conf", "r") as jsonfile:
            data = json.load(jsonfile)
        print("Read successful")
        return(data["stocks"])
    