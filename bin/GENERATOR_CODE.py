import barcode

class GeneratorCode:
    def Generator_Code(TYPECODE: str, CODEB: str, ADDRESS: str):
        image = barcode.get_barcode_class(TYPECODE)
        ean = image(CODEB, writer=ImageWriter())
        ean.save(ADDRESS)