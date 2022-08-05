import uuid
import unicodedata

def upload_logo_formatter(instance, filename):
    """ Format the logo filename """
    ext = filename.split('.')[-1]
    return 'company_logo/logo-{}-{}'.format(instance.name, str(uuid.uuid1()) + '.' + ext)

def phone_formatted(phone: str) -> str:
    """ Format a phone number """
    return f'({phone[0:2]}) {phone[2:7]}-{phone[7:]}'

def remove_text_accents(txt: str) -> str:
    """ Remove accents from a string """
    process = unicodedata.normalize("NFD", txt)
    process = process.encode("ascii", "ignore")
    process = process.decode("utf-8")
    
    return process