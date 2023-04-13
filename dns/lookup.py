import subprocess
from urllib.parse import urlparse

def query_and_print_all(domain: str) -> None:
    if not domain.startswith('http'):
        domain = 'https://' + domain

    hostname = urlparse(domain).hostname

    if hostname is None:
        raise ValueError('error: invalid domain')

    types = ['A', 'AAAA', 'CNAME', 'NS', 'PTR',
             'SOA', 'MX', 'SRV', 'TXT', 'CAA', 'DNSKEY']
    for type in types:
        record = subprocess.run(['dig', '+nocmd', '+noall', '+answer', '+nomultiline', '+tries=2',
                                '+time=2', hostname, type], check=True, capture_output=True, text=True).stdout.strip('\n')
        if len(record):
            print(record)
