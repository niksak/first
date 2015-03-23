#Owner: Nikos Sakellariou 
#Date : 10.2.2015
#
#
import csv
import time
import sys
# ------------variables -----------------------------
stocks = []
#------------------------------------------------

#----------------------------------------------
def init_stocks_csv():
	with open('mystocks.csv', 'w') as csvfile:
		fieldnames = ['Name', 'Pieces','Bought Price','Minimum Sell Price','Ratio','Date']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
def add_stock_csv(lista):
	
	with open('mystocks.csv', 'a') as csvfile:
		fieldnames = ['Name', 'Pieces','Bought Price','Minimum Sell Price','Ratio','Date']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({'Name': lista[0],'Pieces': lista[2],'Bought Price': lista[1],'Date' :time.strftime("%d/%m/%Y")})
	
def read_from_csv():
	with open('mystocks.csv','r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			print(row['Name'], row['Pieces'],row['Bought Price'],row['Date'])	
#def search_file():		
		
def calculate_minimum_sell():
	pass
	k = 15 			#constant of commission ~ 0.033
	stock_name = raw_input("Enter the stock name. > ")
	bought_price = raw_input("Enter the price which your stock was bought. > ")
	pieces = raw_input("Enter the number of pieces you bought. > ")
	
	minimum_sell = float(bought_price) * int(pieces) + k #~1 euro profit
	print "minimum sell price is " , minimum_sell / int(pieces)
	
def buy_new():
	
	global stocks
	stock_name = raw_input("Enter the stock's name. > ")
	bought_price = raw_input("Enter the price which your stock was bought. > ")
	pieces = raw_input("Enter the number of pieces you bought. > ")
	
	stocks.append([stock_name,bought_price,pieces])
	add_stock_csv([stock_name,bought_price,pieces])
	
def sell():
	pass


def print_myportfolio():
	read_from_csv()


def main():
	while 1:
		answer = ''
		print "1: find minimum sell price per stock  2: my portfolio 3: Reset Portfolio  or exit for quit"
		
		choice = raw_input()
		if  choice == '1':
			calculate_minimum_sell()
		elif choice == '2':
			print "my portfolio is consisted of these stocks: \n"
			print_myportfolio()
			print "1: buy, 2: sell, 5: return "
			choice = raw_input()
			if choice == '1':
				buy_new()
			elif choice == '2':
				print 'choice is 2'
				pass
			elif choice == '5':
				pass
		elif choice == '3':
			answer = raw_input('Are you sure you want to reset your portfolio? "yes/no" \n')
			if answer == 'yes':
				init_stocks_csv()
			else:
				pass
			
			
		elif choice == 'exit':
			break
			
	print 'quiting'

#if __name__ == __main__:
main()
