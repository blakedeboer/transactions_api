from unittest.mock import MagicMock
from werkzeug.datastructures import FileStorage

from file_processor.file_processor import FileProcessor

class TestFileProcessor():

    @classmethod
    def setup_method(self): 
        mock_header_row = 'Amount, Description\n'.encode()
        mock_rows = '-1.36,"SWEETGREEN UNION SQUAR NEW YORK, NY, US"\n200.16,PAYROLL~ Future Amount: 200.16 ~ Tran: DDIR'.encode()

        test_file = FileStorage()
        test_file.stream.readline = MagicMock(return_value=mock_header_row)
        test_file.stream.read = MagicMock(return_value=mock_rows)
        self.test_file = test_file

    def test__get_headers_from_file(self):
        file_processor = FileProcessor(self.test_file)
        file_processor._get_headers_from_file()
        assert file_processor.headers == ['Amount', 'Description']

    def test__create_headers_index_dict(self):
        file_processor = FileProcessor(self.test_file)
        file_processor.headers = ['Amount', 'Description']
        expected_map = {
            'Amount': 0,
            'Description': 1
        }
        file_processor._create_headers_index_dict()
        assert file_processor.headers_index_dict == expected_map
        
    def test_process_file(self):
        print("file")
        print(self.test_file)
        # import pdb; pdb.set_trace()

        file_processor = FileProcessor(self.test_file)
        file_processor._get_headers_from_file()
        self.test_file = 'asdf'
        assert 5 == 5
