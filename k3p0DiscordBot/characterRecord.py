class ReadFromSheet:

    def read_sheet(self, name):
        with open(name, 'r') as sheet:
            return sheet.read()

    def read_sheet_data(self, name, data):
        with open(name, 'r') as sheet:
            for line in sheet:
                if(data in line):
                    return line

class WriteToSheet:

    def add_line(self, name, data):
        with open(name, 'a') as sheet:
            sheet.write("{0} \n".format(data))

class CreateSheet:

    def new_sheet(self, name):
        sheet = open(name, 'w')
        sheet.write("Name: {0} \n".format(name))
        sheet.close()
