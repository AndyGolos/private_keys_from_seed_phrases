import datetime

from hdwallet import BIP44HDWallet
from openpyxl import Workbook
from openpyxl.styles import Alignment

from file_utils import parse_txt

workbook = Workbook()

worksheet = workbook.active
worksheet.column_dimensions['A'].width = 80
worksheet.column_dimensions['B'].width = 80

worksheet.append(['Seed Phrase', 'Private Key'])

seed_phrases = parse_txt("seed_phrases.txt")

for i, seed_phrase in enumerate(seed_phrases):
    hd_wallet = BIP44HDWallet(symbol="ETH")
    wallet = hd_wallet.from_mnemonic(seed_phrase)
    worksheet.append([seed_phrase, wallet.private_key()])

alignment = Alignment(horizontal='center', vertical='center')
for row in worksheet.rows:
    for cell in row:
        cell.alignment = alignment

workbook.save(f'private_keys_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.xlsx')



