
import sqlite3

'''connect to the database file. The database file and this python file must put in the same location'''
conn=sqlite3.connect('ToyDatabase.db')

'''the below code is needed if there are foreign language in the database, such as chinese'''
#conn.text_factory = lambda x: str(x, "utf-8", "ignore")

''' the cursor is what executes statements & queries for us on the database, each connects to a specific table'''

Cashier=conn.cursor().execute("select * from Cashier")
Sales=conn.cursor().execute("select * from Sales")
Toy=conn.cursor().execute("select * from  Toy")

'''must use [] and append if you need to use for loop'''
cashierlist=[]
for c in Cashier: # upper case matters
    cashierlist.append(c)

saleslist=[]
for s in Sales:
    saleslist.append(s)

toylist=[]
for t in Toy:
    toylist.append(t)
'''information of each table is now in a list (dic)'''

'''use invoice number to output the toy name, company name, total units sold, total revenue, and cashier name'''

#while(True): how to do the auto indent thing????
InvoiceNumber=eval(input("Enter an invoice number, like 659976:"))
print("Invoice Number:", InvoiceNumber)

'''toy name'''
print("-------------------------------------------------------------------------------------------------------------------------------------------")
print("{0:40}{1:15}{2:20}{3:10}".format("Toy", "Company","Units sold","Units Price")) #how to set it automatcally match the length of the string?
for x in saleslist:
    if x[0] ==InvoiceNumber:
        for y in toylist:
            if y[2]==x[3]:
                l=float(x[4].strip('$)'))#without strip out the $, the price and unit stick together
                print("{0:40}{1:10}{2:10}{3:22}".format(x[3],y[1],x[5],l)) #toylist[x3][1] cant because
                break
print("-------------------------------------------------------------------------------------------------------------------------------------------")
'''
company name--no invoice number in Toy table, need to use toyname is the bridge,
problem-toyname and company name are both strings, invoice number is int, so i guess this is the cause of the problem
name of the companies product the toys, or i can just use toylist[x[2]][1]
'''
'''total units sold'''
total=0
for x in saleslist:
    if x[0]==InvoiceNumber:
        total+=x[5]
print("Total Units sold:",total)

'''Amount total--problem is how to remove the $ sign and convert it to float'''

total=0
for x in saleslist:
    if x[0]==InvoiceNumber:
        l=x[4]#cant just use x[4], reason???
        l=float(l.strip('$'))
        total+=l*x[5]
print("{0:1}{1:.2f}".format("Total: $",total))#the 0 in 0:1 is for "total", the 1 in


'''cashier's name'''
for x in cashierlist:
    if x[0]==InvoiceNumber:
        print("Cashier Name:", x[1],'\n')
        break




'''output the file as txt file'''
print("Outputing file...",'\n')

f=open("Output file.txt", "w")
#how to create a different file so i can save all the record?
f.write("{0:5}{1:5}".format("Invoice Number:",str(InvoiceNumber)))
f.write('\n')
f.write("---------------------------------------------------------------------------------------------")
f.write('\n')

f.write("{0:40}{1:15}{2:20}{3:10}".format("Toy", "Company","Units sold","Units Price"))
f.write('\n')
for x in saleslist:
    if x[0] ==InvoiceNumber:
        for y in toylist:
            if y[2]==x[3]:
                l = float(x[4].strip('$)'))
                f.write("{0:40}{1:10}{2:10}{3:22}".format(x[3],y[1],x[5],l))
                f.write('\n')
                break#break follow by f.write('\n) solved the print out all same name problem
f.write("---------------------------------------------------------------------------------------------")
f.write('\n')

total=0
for x in saleslist:
    if x[0]==InvoiceNumber:
        total+=x[5]
f.write("{0:5}{1:5}".format("Total Units sold:",total))
f.write('\n')

total=0
for x in saleslist:
    if x[0]==InvoiceNumber:
        l=x[4]#cant just use x[4], reason???
        l=float(l.strip('$'))
        total+=l*x[5]
f.write("{0:1}{1:.2f}".format("Total: $",total))#the 0 in 0:1 is for "total", the 1 in
f.write('\n')

'''cashier's name'''
for x in cashierlist:
    if x[0]==InvoiceNumber:
        f.write("{0:5}{1:5}".format("Cashier Name:", x[1]))
        f.write('\n')
        break

print("File output successful.")


f.close()
conn.cursor().close()
b.close()
c.close()
