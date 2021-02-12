from RiotAPI import RiotPlatformAPI, PlatformEndpoints
import datetime

print("Assuming NA for Platform, you can change this by editing the file.\n\n")

token = input("Please enter your Riot API token: ")
summoner_name = input("Please enter the summoner's name: ")

rpapi = RiotPlatformAPI(token)
resp = rpapi.get_summoner_by_name(PlatformEndpoints.NorthAmerica, summoner_name)
print("For summoner named:", resp.json()['name'])
print('\tid:', resp.json()['id'])
print('\taccountId:', resp.json()['accountId'])
print('\tsummonerLevel:', resp.json()['summonerLevel'])
print('\tpuuid:', resp.json()['puuid'])
print('\tLast edited:', datetime.datetime.fromtimestamp(resp.json()['revisionDate']/1000))
