from websocket import create_connection
import random
import json

class GateWs:
    def __init__(self, url):
        self.__url = url

    def gateRequest(self, id, method, params):
        if (params == None):
	        params = []
        ws = create_connection(self.__url)
        data = { 'id' : id, 'method' : method, 'params' : params}
        json_string = json.dumps(data)
        ws.send(json_string)
        json_string = ws.recv()
        return json_string


def main():
    gate = GateWs("wss://ws.gate.io/v3/")

    #Checking server conection.
    responce = json.loads(gate.gateRequest(random.randint(0,99999),'server.ping', []))
    if responce['result'] == 'pong':
        print('server responds\n')

    #Query ticker of specified market, including price, deal volume etc in one day period.
    def ticker_query(market):
        ticker = market
        json_ticker = gate.gateRequest(random.randint(0, 99990), 'ticker.query', ['{0}'.format(ticker), 86400])
        python_ticker = json.loads(json_ticker)
        print(ticker)
        print('price: ' , python_ticker['result']['open'])
        print('last price: ', python_ticker['result']['close'])
        print('base volume: ', python_ticker['result']['baseVolume'])
        print('quote volume: ', python_ticker['result']['quoteVolume'])
        print('lowest: ', python_ticker['result']['low'])
        print('highest: ', python_ticker['result']['high'])
        print()

    ticker_query('BTC_USDT')

if __name__ == "__main__":
    main()