import requests
import mylib
response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
city_air = response_data.json()
print(city_air['RealtimeCityAir']['row'][0]['PM10'])


# print(seoul_sum(gu_air_list))

gu_air_list = city_air['RealtimeCityAir']['row']

print(mylib.seoul_sum(gu_air_list))



# print(mylib.seoul_sum(gu_air_list)/mylib.gu_number(gu_air_list))
print(mylib.avg_seoul_air(gu_air_list))




