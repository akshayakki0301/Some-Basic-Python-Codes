import phonenumbers
from phonenumbers import geocoder
phone_numbers1=phonenumbers.parse("9764853806")
phone_numbers2=phonenumbers.parse("9860676163")\

print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_numbers1,"en"))
print(geocoder.description_for_number(phone_numbers2,"en"))
