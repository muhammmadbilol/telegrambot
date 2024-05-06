import requests

url = "https://background-removal.p.rapidapi.com/remove"


headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "735c1e07cbmsha543aec432261d4p1f0d7ejsnc9dd96092560",
    "X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}


async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.post(url, data=payload, headers=headers)
    return response.json()['response']['image_url']
