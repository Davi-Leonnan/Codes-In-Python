# Slicing 2.0:

website_1 = "https://www.rockstargames.com"

website_2 = "https://www.capcom.com"

slice = slice(12,-4)  # Descarta os endereços de página e deixa apenas o nome do site.

print(website_1[slice])
print(website_2[slice])