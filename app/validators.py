# class PhoneNumberValidator:

#     @staticmethod
#     def country_code(self):
#         self.phone_number.replace(' ', '')
#         if '+' in self.phone_number:
#             if '989' != self.phone_number[1:4]:
#                 raise ValueError('The phone number format should be like this -> +98 9xx xxx xxxx')
#             self.phone_number = '0' + self.phone_number[3:]
#         elif self.phone_number[:2] != '09':
#             raise ValueError('The phone number format should be like this -> 09xx xxx xxxx')
    
#     @staticmethod
#     def number(self):
#         try:
#             int(self.phone_number)
#         except Exception as e:
#             raise ValueError('only digits(and "+" for the country code) are allowed.')
#         if len(self.phone_number) != 11:
#             raise ValueError('Incorrect phone number')
        
#     @staticmethod
#     def validate(phone_number):
#         PhoneNumberValidator.country_code()
#         PhoneNumberValidator.number()

from django.core.exceptions import ValidationError


def validate_phone_number(phone_number):
    phone_number = phone_number.replace(' ', '')

    if '+' in phone_number:
        if '989' != phone_number[1:4]:
            raise ValidationError('The phone number format should be like this -> +98 9xx xxx xxxx')
        phone_number = '0' + phone_number[3:]
    elif phone_number[:2] != '09':
        raise ValidationError('The phone number format should be like this -> 09xx xxx xxxx')

    try:
        int(phone_number)
    except ValueError:
        raise ValidationError('Only digits (and "+" for the country code) are allowed.')

    if len(phone_number) != 11:
        raise ValidationError('Incorrect phone number')

    return phone_number
