from datetime import datetime
   

class CSVFile:
    def __init__(self, name):
        self.name=name

    def get_data(self):
        dates = []

        my_file=open(self.name, 'r')

        for line in my_file:
            elements= line.split(',')
            if elements[0] != 'Date':
                my_date=elements[0]
                value=elements[1]
                my_date=datetime.strptime(elements[0],'%d-%m-%Y')
                 
                dates.append(my_date)

        my_file.close()

        for data in dates:
            print(data.strftime('%d-%m-%Y'))
       

mio_file=CSVFile('shampoo_sales.csv')
print(mio_file.get_data())
#