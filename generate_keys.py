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

print("Start generating private keys from seed phrases")
seed_phrases = parse_txt('seed_phrases.txt')

for i, seed_phrase in enumerate(seed_phrases):
    try:
        hd_wallet = BIP44HDWallet(symbol='ETH')
        wallet = hd_wallet.from_mnemonic(seed_phrase)
        worksheet.append([seed_phrase, wallet.private_key()])
    except Exception as e:
        print(f'Seed phrase \"{seed_phrase}\" is invalid. {e}')
        exit()

alignment = Alignment(horizontal='center', vertical='center')
for row in worksheet.rows:
    for cell in row:
        cell.alignment = alignment

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name = f'private_keys_{timestamp}.xlsx'
workbook.save(file_name)

print(f'Generation finished. File name: \"{file_name}\"')



