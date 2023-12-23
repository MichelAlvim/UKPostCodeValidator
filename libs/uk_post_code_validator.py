import re

class UKPostcodeValidator:
    @staticmethod
    def validate_postcode(postcode):
        # Regular expression for validating UK postcodes
        postcode_pattern = re.compile(
            r'^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$',
            re.IGNORECASE
        )

        return bool(postcode_pattern.match(postcode))

    @staticmethod
    def format_postcode(postcode):
        # Remove any spaces from the postcode and make the postcode uppercase
        postcode = postcode.replace(" ", "").upper()

        # Insert a space before the last three characters
        formatted_postcode = f"{postcode[:-3]} {postcode[-3:]}"

        return formatted_postcode