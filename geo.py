import pygame
import requests
from PIL import Image
from io import BytesIO

API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"
API_SERVER = "http://geocode-maps.yandex.ru/1.x/"
API_MAP = "http://static-maps.yandex.ru/1.x/"


def geocode(address):
    geocoder_params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"}

    response = requests.get(API_SERVER, params=geocoder_params)

    if not response:
        raise RuntimeError(f"Ошибка выволнения запроса {response.url}")

    json_response = response.json()

    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return toponym[0]["GeoObject"] if toponym else None


def get_coordinates(address):
    taponym_cords = geocode(address)
    if taponym_cords:
        coodrinates = taponym_cords["Point"]["pos"]
        return coodrinates.split(" ")
    else:
        return None, None


def show_map(map_type="map", **kwargs):
    params = {"l": map_type}
    # if ll_spn:
    #     params["ll"] = ll_spn
    params.update(kwargs)
    response = requests.get(url=API_MAP, params=params)
    if not response:
        raise RuntimeError(f"Ошибка выволнения запроса {response.url}")

    pilimage = Image.open(BytesIO(response.content)).convert("RGBA")
    map_img = pygame.image.fromstring(pilimage.tobytes(), pilimage.size, pilimage.mode)

    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(map_img, (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


def get_span(address):
    toponym = geocode(address)
    if not toponym:
        return dict()
    longitude, lattitude = get_coordinates(address)
    params = {"ll": ",".join([longitude, lattitude])}
    evelope = toponym["boundedBy"]["Envelope"]
    l, b = evelope["lowerCorner"].split(" ")
    r, t = evelope["upperCorner"].split(" ")
    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0
    params["span"] = f"{dx},{dy}"
    return params