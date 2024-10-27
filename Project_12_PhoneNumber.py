import phonenumbers
from phonenumbers import PhoneNumberFormat, format_number, geocoder, carrier, timezone

# User input for phone number and region
phone_number_input = input("Enter the phone number with country code (e.g., +8801_________): ")
region_input = input("Enter the region code (e.g., 'BD' for Bangladesh, 'US' for United States): ")

# Parse the phone number
try:
    phone_number = phonenumbers.parse(phone_number_input, region_input.upper())

    # Format the phone number
    formatted_number = format_number(phone_number, PhoneNumberFormat.INTERNATIONAL)
    print(f"Formatted Number: {formatted_number}")

    # Check if the phone number is valid
    is_valid = phonenumbers.is_valid_number(phone_number)
    print(f"Is the Phone Number Valid? : {'Yes' if is_valid else 'No'}")

    # Get the location of the phone number
    location = geocoder.description_for_number(phone_number, "en")
    print(f"Location: {location}")

    # Get the carrier information for the phone number
    phone_carrier = carrier.name_for_number(phone_number, "en")
    print(f"Carrier: {phone_carrier}")

    # Get the time zones for the phone number
    time_zones = timezone.time_zones_for_number(phone_number)
    print(f"Time Zones: {', '.join(time_zones)}")

except phonenumbers.phonenumberutil.NumberParseException as e:
    print(f"Error: {e}")
