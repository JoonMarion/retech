import uuid

def upload_logo_formatter(instance, filename):
    ext = filename.split('.')[-1]
    return 'company_logo/logo-{}-{}'.format(instance.name, str(uuid.uuid1()) + '.' + ext)

def phone_formatted(phone):
    return f'({phone[0:2]}) {phone[2:7]}-{phone[7:]}'