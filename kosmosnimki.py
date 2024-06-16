from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import requests
from datetime import datetime, timedelta
import os


client_id = 'c2d69d63-1df5-4b80-98de-a05e0e203514'
client_secret = '6I2b3IDPn10CDMnVj921DJ9m2X015xsX'


def fetch_oauth_token():
    token_url = 'https://services.sentinel-hub.com/auth/realms/main/protocol/openid-connect/token'
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)

    def sentinelhub_compliance_hook(response):
        response.raise_for_status()
        return response

    oauth.register_compliance_hook("access_token_response", sentinelhub_compliance_hook)

    token = oauth.fetch_token(token_url=token_url, client_secret=client_secret)
    print(token)
    return token


def fetch_images(token, bbox, index_photo):
    # Пример координат из доков
    # bbox = [13.822174072265625,
    #         45.85080395917834,
    #         14.55963134765625,
    #         46.29191774991382]

    end_time = datetime.utcnow()
    print(end_time)
    start_time = end_time - timedelta(hours=24)
    print(start_time)

    start_str = start_time.strftime('%Y-%m-%dT00:00:00Z')
    end_str = end_time.strftime('%Y-%m-%dT00:00:00Z')

    url = "https://services.sentinel-hub.com/api/v1/process"
    headers = {
        "Authorization": f"Bearer {token['access_token']}",
        "Content-Type": "application/json",
        "Accept": "image/jpeg"
    }

    request_data = {
        "input": {
            "bounds": {
                "properties": {
                    "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
                },
                "bbox": bbox
            },
            "data": [{
                "type": "sentinel-2-l2a",
                "dataFilter": {
                    "timeRange": {
                        "from": start_str,
                        "to": end_str
                    }
                }
            }]
        },
        "evalscript": """
            //VERSION=3

            function setup() {
              return {
                input: ["B02", "B03", "B04"],
                output: {
                  bands: 3
                }
              };
            }

            function evaluatePixel(
              sample,
              scenes,
              inputMetadata,
              customData,
              outputMetadata
            ) {
              return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];
            }
        """
    }

    try:
        response = requests.post(url, headers=headers, json=request_data)
        response.raise_for_status()
        print(response)
        image_data_list = response.content.split(b'\r\n\r\n')
        os.makedirs("images", exist_ok=True)
        # print(image_data_list)
        for index, image_data in enumerate(image_data_list):
            if image_data.startswith(b'\xff\xd8'):
                filename = f'images/image_{index_photo}.jpg'
                with open(filename, 'wb') as f:
                    f.write(image_data)

                print(f'Изображение сохранено как {filename}')

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")


def main():
    token = fetch_oauth_token()

    min_lat, min_lon = 50.0, 156.0
    max_lat, max_lon = 60.0, 165.0

    lat_step = (max_lat - min_lat) / 100
    lon_step = (max_lon - min_lon) / 100

    index = 0
    for i in range(100):
        for j in range(100):
            bbox = [
                min_lon + j * lon_step,
                min_lat + i * lat_step,
                min_lon + (j + 1) * lon_step,
                min_lat + (i + 1) * lat_step
            ]
            fetch_images(token, bbox, index)
            index += 1


if __name__ == "__main__":
    main()
