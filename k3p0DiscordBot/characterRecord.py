class ReadFromSheet:

    def find_lines(file, data):
        data = data.lower()
        lines = []
        try:
            with open(file) as f:
                for line in f:
                    if(data in line.lower()):
                        line = line.replace('\n', '')
                        lines.append(line)
                    else:
                        continue
            return lines
        except FileNotFoundError:
            print("That sheet doesn't exist!")
            return ['That sheet doesn\'t exist!']

    def read_sheet(self, name):
        try:
            with open(name, 'r') as sheet:
                return sheet.read()
        except FileNotFoundError:
            return "That sheet doesn't exist!"

    def read_sheet_data(self, name, data):
        return ReadFromSheet.find_lines(name, data)

class WriteToSheet:

    def add_line(self, name, data):
        try:
            sheet = open(name, 'r')
            if((data + "\n") not in sheet):
                sheet.close()
                with open(name, 'a') as sheet:
                    sheet.write("{0} \n".format(data))
            else:
                print("Didn\'t add line because it was already written to the sheet")
        except FileNotFoundError:
            print("Tried writing to sheet that doesn't exist")

class CreateSheet:

    def new_sheet(self, name):
        sheet = open(name, 'w')
        sheet.write("Name: {0} \n".format(name))
        sheet.close()
