import rebot
import time
import json

def send_to_rebot(ticker):
	
	content = rebot.getContent(ticker)
	readable = rebot.getHtml(content)

	stockName 			= readable.search("h1")
	tickerPrice 		= readable.search("span", "class", "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
	prevTickerPrice = readable.search("span", "class", "C(black) Fz(24px) Fw(b)")
	previousClose 	= readable.search("td", "data-test", "PREV_CLOSE-value")
	openPrice 			= readable.search("td", "data-test", "OPEN-value")
	bid 						= readable.search("td", "data-test", "BID-value")
	ask 						= readable.search("td", "data-test", "ASK-value")
	dayRange 				= readable.search("td", "data-test", "DAYS_RANGE-value")
	volume 					= readable.search("td", "data-test", "TD_VOLUME-value")
	avgVolume 			= readable.search("td", "data-test", "AVERAGE_VOLUME_3MONTH-value")
	marketCap 			= readable.search("td", "data-test", "MARKET_CAP-value")
	beta 						= readable.search("td", "data-test", "BETA-value")
	peratio 				= readable.search("td", "data-test", "PE_RATIO-value")
	eps 						= readable.search("td", "data-test", "EPS_RATIO-value")
	earningsdate 		= readable.search("td", "data-test", "EARNINGS_DATE-value")
	fwdDividend 		= readable.search("td", "data-test", "DIVIDEND_AND_YIELD-value")
	exDividend 			= readable.search("td", "data-test", "EXDIVIDEND_DATE-value")
	yearTarget 			= readable.search("td", "data-test", "ONE_YEAR_TARGET_PRICE-value")

	latestNews 			= readable.search("a", "class", "Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 Td(n) C(#0078ff):h C(#000)")

	# stockName = readable.find("h1").getText()
	# tickerPrice = readable.find("span", { "class" : "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" }).getText()
	# #prevTickerPrice = readable.find("span", { "class" : "C(black) Fz(24px) Fw(b)" }).getText()
	# previousClose = readable.find("td", {"data-test": "PREV_CLOSE-value"}).getText()
	# openPrice = readable.find("td", {"data-test": "OPEN-value"}).getText()
	# bid = readable.find("td", {"data-test": "BID-value"}).getText()
	# ask = readable.find("td", {"data-test": "ASK-value"}).getText()
	# dayRange = readable.find("td", {"data-test": "DAYS_RANGE-value"}).getText()
	# volume = readable.find("td", {"data-test": "TD_VOLUME-value"}).getText()
	# avgVolume = readable.find("td", {"data-test": "AVERAGE_VOLUME_3MONTH-value"}).getText()
	# marketCap = readable.find("td", {"data-test": "MARKET_CAP-value"}).getText()
	# beta = readable.find("td", {"data-test": "BETA-value"}).getText()
	# peratio = readable.find("td", {"data-test": "PE_RATIO-value"}).getText()
	# eps = readable.find("td", {"data-test": "EPS_RATIO-value"}).getText()
	# earningsdate = readable.find("td", {"data-test": "EARNINGS_DATE-value"}).getText()
	# fwdDividend = readable.find("td", {"data-test": "DIVIDEND_AND_YIELD-value"}).getText()
	# exDividend = readable.find("td", {"data-test": "EXDIVIDEND_DATE-value"}).getText()
	# yearTarget = readable.find("td", {"data-test": "ONE_YEAR_TARGET_PRICE-value"}).getText()

	if float(beta) > 1.5:
		action = "OMG! TOO RISKY"
	else:
		action = "MODERATE RISK"

	message = rebot.createEmptyMessage()
	message.addText("Here are the results from Yahoo Finance!")
	message.addText(action)
	message.addLink("https://finance.yahoo.com", "Click this link")
	message.addImage("https://urlimage")
	message.addText(latestNews)

	message.addData("Stock Name", stockName)
	message.addData("Ticker Price", tickerPrice)
	message.addData("Previous Ticker Price", prevTickerPrice)
	message.addData("Previous Close", previousClose)
	message.addData("Open Price", openPrice)
	message.addData("Bid", bid)
	message.addData("Ask", ask)
	message.addData("Day Range", dayRange)
	message.addData("Volume", volume)
	message.addData("Average Volume", avgVolume)
	message.addData("Market Cap.", marketCap)
	message.addData("Beta", beta)
	message.addData("PE Ratio", peratio)
	message.addData("EPS", eps)
	message.addData("Earnings Date", earningsdate)
	message.addData("Forward Dividend", fwdDividend)
	message.addData("Ex Dividend", exDividend)
	message.addData("1st Year Target", yearTarget)

	return message

def testcall():
	message = rebot.createEmptyMessage()
	message.addText("this is my new message!!")
	return message
        
#------------ 

start = time.time()

#message = send_to_rebot("MSFT")
message = testcall()
print(json.loads(str(message)))


print("--- %s seconds ---" % (time.time() - start))
