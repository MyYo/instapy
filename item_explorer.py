import requests
import sys

URL_TEMPLATE = 'https://www.instacart.com/v3/containers/items/item_{item}'
HEADERS = {
    'authority': 'www.instacart.com',
    'method': 'GET',
    'path': '/v3/containers/items/item_192139112',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,he;q=0.8',
    'cache-control': 'no-cache',
    'cookie': "_ga=GA1.2.1182894543.1546381925; _gid=GA1.2.458901356.1546381925; _parsely_visitor={%22id%22:%22pid=4375f6f70a4e16f304274f82666b3f07%22%2C%22session_count%22:1%2C%22last_session_ts%22:1546381925133}; build_sha=5b6265ba96f23c9fa3ce2ab22124ee0a3077b565; amplitude_idundefinedinstacart.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; _gcl_au=1.1.94154404.1546382065; ab.storage.userId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%2245073255%22%2C%22c%22%3A1546384295233%2C%22l%22%3A1546384295233%7D; ab.storage.deviceId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%2248a35bdb-9814-4633-2ed6-5ffcf643a481%22%2C%22c%22%3A1546384295243%2C%22l%22%3A1546384295243%7D; __ssid=a0ad6de098b1f57281fb9581ddbf38d; ajs_anonymous_id=%2287674ef2-4917-4237-b1e4-833cfc915f24%22; ahoy_visitor=ccafdf41-7eda-4db4-b0cf-252a952c7d94; ahoy_visit=3bc7608b-40a9-4b12-90a1-9b94c94dcb6b; ajs_group_id=null; remember_user_token=W1s0NTA3MzI1NV0sIiQyYSQxMCRoRFJ3TncxWElETGVqemdnVVFxOHBPIiwiMTU0NjM4NDQxMS44ODE3NTQiXQ%3D%3D--39ec879046cb2eb24e391856371d2879a78ed8f9; ajs_user_id=45073255; _derived_epik=v%3D1%26u%3D5NmVSp77nhTOdGy12mbRyv1bB6bNhGoh%26n%3Dr6XiDlW5Px5FetEBXnYwmg%3D%3D%26m%3D7; ab.storage.sessionId.6f8d91cb-99e4-4ad7-ae83-652c2a2c845d=%7B%22g%22%3A%220929b83b-ad63-6401-02ed-5c381166e899%22%2C%22e%22%3A1546384514260%2C%22c%22%3A1546384483524%2C%22l%22%3A1546384484260%7D; amplitude_id_b87e0e586f364c2c189272540d489b01instacart.com=eyJkZXZpY2VJZCI6ImM0MzY3YTc1LWNmMDktNDc1NC1hZmVhLWM5NDI2OGU3NTI1MFIiLCJ1c2VySWQiOiI0NTA3MzI1NSIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU0NjM4NDE3NjU2NywibGFzdEV2ZW50VGltZSI6MTU0NjM4NDQ4NDI2NCwiZXZlbnRJZCI6NzQsImlkZW50aWZ5SWQiOjE4LCJzZXF1ZW5jZU51bWJlciI6OTJ9; _instacart_session=NnVQRTd6bVVENWJjMzJqR1hDZ1NrSCtjaGg1OUtvM21MZWszNTV3Rm1YR2o5ZlNHWUJrWjcxV09aZW9FUE5oRS9DaTJZYnE5ZFdpTmIyZEJnbnJ2UXhOcTJLUjNFZWl6UVdneUEwY04wT2laVE1MUTEwVEh3bFFiblppY2k2eExDNzIvWlpIKzBTQVprSjZPYXZIdVpjSHBiaXJ3S1E1TlFRa0lUUGVpZHh0UGFFM3l3QTBkK2Z3ZUNkR0kvZ0l3L2R2MngwWlZnaWNVYWRZR080UEU5VWZRR2V1WWs2NFdlT3QrNmRKcnBzQ29BWGhHL3dPSndTb2JsZk5EY3RzS1pKdXIyM0lsQmp0bnp5Q0JOeVdpZGVQSHhmZmRkNEcyWFVRVkVjU0Frajg9LS1aa3NiQjBzemQwZ2lTRHJ1WFRGcit3PT0%3D--25b33bd374a833bf9f15048e7141f7f2ca1a3bb8",
    'pragma': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'",
}


def get_item_price(item_id):
    url = URL_TEMPLATE.format(item=item_id)
    response = requests.get(url, headers=HEADERS)
    if not response.ok:
        raise Exception(str(response.status_code) +  str(response.reason))
    data = response.json()
    name = data['container']['title']
    price = data['container']['modules'][0]['data']['item']['pricing']['price']
    # price = data['container']['modules'][0]['data']['item']['variable_estimate']['price_per_unit']
    return name, price



if __name__ == '__main__':
    # item = 173628440
    # item = 192139112
    if len(sys.argv) != 2:
        print('Error. usage: {} <item_id>'.format(sys.argv[0]))
        exit(1)
    name, price = get_item_price(sys.argv[1])
    print('{name}: {price}'.format(name=name, price=price))

