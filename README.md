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
$ dns w3.org
w3.org.			3323	IN	A	104.18.23.19
w3.org.			3600	IN	AAAA	2606:4700::6812:1713
w3.org.			3323	IN	NS	ns2.w3.org.
w3.org.			3323	IN	NS	ns1.w3.org.
w3.org.			3323	IN	NS	ns3.w3.org.
w3.org.			3600	IN	SOA	ns1.w3.org. hostmaster.w3.org. 2023022201 28800 3600 604800 1800
w3.org.			3600	IN	MX	10 mimas.w3.org.
w3.org.			3600	IN	MX	50 bart.w3.org.
w3.org.			3600	IN	MX	10 titan.w3.org.
w3.org.			3600	IN	TXT	"v=spf1 a mx ip4:128.30.52.0/22 ip4:203.178.154.0/25 ip4:193.51.208.64/27 include:spf6.w3.org include:_spf.google.com include:spf.braintreegateway.com
```
