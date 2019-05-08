class FileProcessor():

    def __init__(self, file):
        self.file = file
        self.headers = []
        self.headers_index_dict = {}

    def _get_headers_from_file(self):
        first_row_as_byte = self.file.stream.readline()
        first_row_as_string = first_row_as_byte.decode("UTF8")
        first_row_without_new_line_chars = first_row_as_string.rstrip("\n")
        self.headers = [header.strip() for header in first_row_without_new_line_chars.split(",")]

    def _create_headers_index_dict(self):
        self.headers_index_dict = {
            header:index for index,header in enumerate(self.headers)
        }

    def process(self, row_processor):
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream)
        for row in csv_input:
            print(row)

            amount = row[amount_index]
            # ['-1.36', 'SWEETGREEN UNION SQUAR NEW YORK, NY, US']
            # ['200.16', 'PAYROLL~ Future Amount: 200.16 ~ Tran: DDIR']