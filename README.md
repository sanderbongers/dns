# DNS

A command to query all DNS records for a (sub)domain.

## Requirements
- Python >= 3.7, `pip`, and `setuptools`
    - Install at once via Homebrew: `$ brew install python` (macOS)

## Installation
```
$ pip install git+https://github.com/sanderbongers/dns.git
```

## Usage
```
$ dns bonge.rs
bonge.rs.		1138	IN	A	    37.97.229.40
bonge.rs.		3350	IN	AAAA	2a01:7c8:fffd:40:5054:ff:fed7:8e0c
bonge.rs.		3600	IN	NS	    ns01.bonge.rs.
bonge.rs.		3600	IN	SOA	    bonge.rs. sander.bonge.rs. 2023041401 10800 3600 604800 3600
bonge.rs.		3600	IN	MX	    10 mx01.mail.icloud.com.
bonge.rs.		3600	IN	MX	    10 mx02.mail.icloud.com.
bonge.rs.		3600	IN	TXT	    "apple-domain=rBm4PHrden4V12Zm"
bonge.rs.		3600	IN	TXT	    "v=spf1 a mx include:icloud.com ~all"
bonge.rs.		3350	IN	DNSKEY	257 3 13 4eD1EdQy6fN+zo/94UMfBgD6X2Kf7mzSoU0fRSYt6X9kLbR+rt7vnRUg kI+hLe1ecyrML95YcnmVu5xsQ920hw==
```
