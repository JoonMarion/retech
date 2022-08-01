import uuid

def upload_logo_formatter(instance, filename):
    ext = filename.split('.')[-1]
    return 'company_logo/logo-{}-{}'.format(instance.name, str(uuid.uuid1()) + '.' + ext)