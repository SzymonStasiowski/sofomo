import requests

def get_geolocation(input):
    access_key = '86b66c608cef9b586f3aae03edc471b8'
    url = f"http://api.ipstack.com/{input}?access_key={access_key}&fields=ip,type,continent_code," \
        f"continent_name,country_code,country_name,region_code,region_name,city,zip,latitude,longitude"

    response = requests.get(url)

    return response.json()

print(get_geolocation('89.64.47.10'))