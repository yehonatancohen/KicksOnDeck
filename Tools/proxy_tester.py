import requests, json

# Enter the proxy server's IP address and port number
proxy_raw = "103.104.193.22:8080"
proxy = {"http": f"http://{proxy_raw}"}



def proxy_anonymity():
    level = 3
    # Make an HTTP request to a website that displays your IP address
    response = requests.get("https://api.myip.com", proxies=proxy)

    # Extract the IP address from the response
    ip_address = json.loads(response.text.strip())["ip"]

    print(ip_address)
    # Check if the IP address is the same as the proxy's IP address
    if ip_address == proxy["http"].split(":")[1][2:]:
        level -= 1

    # Check for headers that reveal the user's personal information
    headers = response.headers
    if "x-forwarded-for" not in headers and "via" not in headers and "proxy-connection" not in headers:
        level -= 1

    leaks = requests.get("http://www.ipleak.net/json", proxies=proxy)
    print(leaks)

    return level

    # Check for leaks that could reveal the user's real IP address
    
    #if leaks["ip"] == ip_address:
    #    level -= 1

print(proxy_anonymity())