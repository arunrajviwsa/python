import csv
with open('portfolio.csv',mode='w',newline='') as pfile:
    pfile_writer = csv.writer(pfile,delimiter="'",quotechar='"',quoting=csv.quote_minimal)
    #pfile_writer.writerow("portfoli List,arun raj")
    pfile_writer.writerow(['stock name','Quantity','Stock Price'])
    pfile_writer.writerow(['Infosys',10,2700])
    pfile_writer.writerow(['ust',5,3200])
with open('portfolio.csv',mode="r") as pfile:
    csv_reader =csv.reader(pfile,delimter=",")
    line_count=0;
    for row in csv_reader:
        if line_count ==0:
            print(f'{",".join(row)}')
        else:
            print(f'{row[0]}\t{row[1]}\t{row[2]}')
            line_count +=1;
            """ 
            print(f')
            """