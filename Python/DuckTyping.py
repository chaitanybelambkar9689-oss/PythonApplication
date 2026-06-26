#Basics of DuckTyping :It is concept where the type of an object is determined by its behaviour not its by classs
class InkJetPrinter:
    
    def printdocument(self,document):
        print("InkjetPrinter  printing :",document)


class LaserPrinter:
    def printdocument(self,document):
        print("LaserPrinter  printing :",document)

class PDFWriter:

    def printdocument(self,document):
        print(f"Saving  {document} as pdf")    


def StartPrinting(Device):
    Device.printdocument("Marvellous notes  ")

def main():
    StartPrinting(InkJetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()        































