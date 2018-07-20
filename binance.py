
import os,requests,datetime,time,sys,json
print("\033[H\033[J")
filename = 'crypto.csv'
f = open(filename,'a+')


def GetPrice():

	ListOne=[]
	ListTwo=[]
	#infinite loop
	while True:
		try:
			#request One
			r = requests.get('https://www.binance.com/api/v1/ticker/price')
			time.sleep(2)
			DateS = datetime.datetime.now()
			array = json.loads(r.text)
			lastprice = array
			ticker_list=[]
			
			#step thugh list appllying symbol and price to ListOne
			for x in array:
				ticker_list.extend([x['symbol'] + "," + x['price']])
			ListOne = ticker_list
			
			
			#Request Two
			r = requests.get('https://www.binance.com/api/v1/ticker/price')
			time.sleep(0.1)
			DateS = datetime.datetime.now()
			array = json.loads(r.text)
			lastprice = array
			ticker_list=[]
			#step thugh list appllying symbol and price to ListTwo
			for x in array:
				ticker_list.extend([x['symbol'] + "," + x['price']])
			ListTwo = ticker_list
			#step thugh each entry of each list and compair if not eq then price changed
			for x,y in zip(ListOne,ListTwo):
				if x != y:
					Pdiff0 = float(x.split(',')[1])
					Pdiff1 = float(y.split(',')[1])
					pdiff = Pdiff0 - Pdiff1
					PCDIFF = float(pdiff) / float(Pdiff0)
					PCCHANGE = PCDIFF * 100
					if PCCHANGE < 0:
						ColorStart = '\033[91m'
						CEND = '\033[0m'
					if PCCHANGE > 0:
						ColorStart = '\033[32m'
						CEND = '\033[0m'
					SYM = str(x.split(',')[0])
					SYMLNG = len(SYM)
					if SYM[SYMLNG-3] == 'S':
						SYMBOL = "USDT"
					else:
						SYMBOL = SYM[SYMLNG-3]
						SYMBOL += SYM[SYMLNG-2]
						SYMBOL += SYM[SYMLNG-1]
					SYMBOL1 = SYM.split(SYMBOL)[0]
						
					print(DateS.strftime("%d,%m,%Y , %H,%M,%S"),SYMBOL1," Price has changed from ",x.split(',')[1],SYMBOL, " To ",y.split(',')[1],SYMBOL," Percent change of", ColorStart ,round(PCCHANGE, 3),CEND,"%\n\n")
					f.write("".join((DateS.strftime("%d,%m,%Y,%H,%M,%S,"),str(y),',',str(round(PCCHANGE, 3)),'\n')))
			ListOne = []
			ListTwo = []
		#Catch Ctrl+c
		except KeyboardInterrupt:
			sys.exit()
		#except:
			#print("Something Gone Wrong Trying Again")
			#GetPrice()
GetPrice()
