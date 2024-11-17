from unittest.mock import mock_open, patch

def test_pdf_extraction():
    mock_pdf_data = b"%PDF-1.4 example content"
    with patch("builtins.open", mock_open(read_data=mock_pdf_data)) as mock_file:
        with open("sample.pdf", "rb") as f:
            data = f.read()
            assert data == mock_pdf_data

import torch
print(torch.__version__)
print(torch.cuda.is_available())
