import requests

# vurnability Server-Side Request Forgery
# issue allowing the user to input any url is problamatic

url = input("Enter URL: ")
response = requests.get(url)
print(response.text)

# fixed version
# time outs, allowlist, Log and audit requests

from urllib.parse import urlparse
import socket
import ipaddress

ALLOWED_HOSTS = ("example.com", "api.trusted-service.com")  

PRIVATE_NETWORKS = (
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("127.0.0.0/8"),        
    ipaddress.ip_network("169.254.0.0/16"),    
    ipaddress.ip_network("::1/128"),           
    ipaddress.ip_network("fc00::/7"),         
)

def is_private_ip(ip_str):
    ip = ipaddress.ip_address(ip_str)
    return any(ip in net for net in PRIVATE_NETWORKS)

def hostname_allowed(hostname, allowlist=ALLOWED_HOSTS):
    hostname = hostname.lower()
    for allowed in allowlist:
        if hostname == allowed or hostname.endswith("." + allowed):
            return True
    return False

def resolve_host(hostname):
    """Return a set of IP strings for the hostname (both IPv4 & IPv6)."""
    infos = socket.getaddrinfo(hostname, None)
    ips = {info[4][0] for info in infos}
    return ips

def fetch_url_safe(url, allowlist=ALLOWED_HOSTS, timeout=5, max_bytes=2_000_000):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError("Only http/https schemes allowed")

    hostname = parsed.hostname
    if not hostname:
        raise ValueError("Invalid URL: missing hostname")

    if allowlist:
        if not hostname_allowed(hostname, allowlist):
            raise ValueError("Hostname not allowed")

    try:
        ips = resolve_host(hostname)
    except Exception as e:
        raise ValueError(f"Failed to resolve host: {e}")

    for ip in ips:
        if is_private_ip(ip):
            raise ValueError(f"Resolved IP {ip} is private/forbidden")

    sess = requests.Session()
    resp = sess.get(url, timeout=timeout, allow_redirects=False, stream=True)

    if 300 <= resp.status_code < 400 and 'Location' in resp.headers:
        redirect = resp.headers['Location']
        redirect_parsed = urlparse(redirect)
        if redirect_parsed.netloc and redirect_parsed.hostname != hostname:
            raise ValueError("Redirect to other host is not allowed")

    total = 0
    chunks = []
    for chunk in resp.iter_content(chunk_size=4096):
        if not chunk:
            break
        total += len(chunk)
        if total > max_bytes:
            raise ValueError("Response too large")
        chunks.append(chunk)

    content = b"".join(chunks)
    return content

if __name__ == "__main__":
    try:
        data = fetch_url_safe("https://example.com/some/path")
        print(data[:500])
    except Exception as e:
        print("Blocked request:", e)