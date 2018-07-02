
import os,requests,datetime,time,sys,json
print("\033[H\033[J")
filename = 'crypto.csv'
f = open(filename,'a+')
s = []
ListOne=[]
ListTwo=[]

def PriceCheck(ListOne, ListTwo):
	i = 2
	#print(ListOne)
	
	for x,y in zip(ListOne,ListTwo):
		if x != y:
			print("Price has changed from ",x," ",y)
			f.write("".join((str(y),'\n')))
			
		#print(x)
		#for y in ListTwo:
			#print(y)
			#if y != x:
				
			#print('price has changed from ',x,' to ',y)
				#print(x,"has chanaged to",y)
		
		
	GetPrice()
				
def GetPrice():
	ListOne=[]
	ListTwo=[]
	filename = 'ETHSKY.csv'
        #f = open(filename,'a+')
        #r = requests.get('https://www.binance.com/api/v1/ticker/price?symbol=SKYETH')
        #r = requests.get('https://www.binance.com/api/v1/ticker/price')
        #DateS = str(datetime.datetime.now())
        #array = json.loads(json.dumps(r.json()))

	#print("Machine Learning the Crypto World\r\n\r\n")
	while True:
		try:
			

			r = requests.get('https://www.binance.com/api/v1/ticker/price')
			time.sleep(0.1)
			DateS = str(datetime.datetime.now())
			array = json.loads(r.text)
			lastprice = array
			
			
			ticker_list=[]
			
			#print(array)
                        #time.sleep(5)
			s = ""

			for x in array:

				#ListOne.append(x['price'])
				ticker_list.extend([x['symbol'] + "," + x['price']])
			
			
			
			ListOne = ticker_list
			
			
			
			r = requests.get('https://www.binance.com/api/v1/ticker/price')
			time.sleep(0.1)
			DateS = str(datetime.datetime.now())
			array = json.loads(r.text)
			lastprice = array


			ticker_list=[]

                        #print(array)
                        #time.sleep(5)
			s = ""

			for x in array:

                                #ListOne.append(x['price'])
				ticker_list.extend([x['symbol'] + "," + x['price']])



			ListTwo = ticker_list
			PriceCheck(ListOne,ListTwo)
			ListOne = []
			ListTwo = []
						#print(f"",ticker_list[2],end="\r",flush=True)
                        #for x in ticker_list:
                                #print(x)

                                #if lastprice != array:
                                #       f.write(''.join((x['symbol'] , ',' , x['price'] , ",", "%s"%Da$
                                #       print("diffrent")
                                #       print("price has changed " , array,"\r\n")
                                #       print("Last price was", lastprice,"\r\n")
                                #       lastprice = array
                        #print("price is of ",s , "\r\n")
		except KeyboardInterrupt:
			sys.exit()
			print("Something Gone Wrong Trying Again")
			GetPrice()
GetPrice()
