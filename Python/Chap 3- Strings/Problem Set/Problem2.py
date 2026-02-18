# 2. WAP to fill in a letter template given below with name and date.

letter = '''
         Dear <|NAME|>,
         You are selected!
         <|DATE|>'''

print(letter.replace("<|NAME|>","Suvojit").replace("<|DATE|>","11 Feb"))