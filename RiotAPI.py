import requests
import enum

class PlatformEndpoints(enum.Enum):
    Brazil = "br1"
    EuropeNorth = "eun1"
    EuropeWest = "euw1"
    Japan = "jp1"
    Korea = "kr"
    LatinAmerica1 = "la1"
    LatinAmerica2 = "la2"
    NorthAmerica = "na1"
    Oceania = "oc1"
    Turkey = "tr1"
    Russia = "ru"

class RegionalEndpoints(enum.Enum):
    Americas = "americas"
    Asia = "asia"
    Europe = "europe"

class AutoCache:
    def __init__(self, cache:bool):
        self.cache = cache

    def fetch(self, url:str, headers:str) -> dict:
        #TODO: Build automatic caching system with SQLite here with the line below as a fall-through or "failed to find" case
        return requests.get(url, headers=headers).json()

class RiotPlatformAPI:
    def __init__(self, token:str, cache=False):
        self.cache = cache
        self.platform_endpoints = { #Hard-coded the Endpoints here because .json files will be .gitignore-d
            "br1":"https://br1.api.riotgames.com",
            "eun1":"https://eun1.api.riotgames.com",
            "euw1":"https://euw1.api.riotgames.com",
            "jp1":"https://jp1.api.riotgames.com",
            "kr":"https://kr.api.riotgames.com",
            "la1":"https://la1.api.riotgames.com",
            "la2":"https://la2.api.riotgames.com",
            "na1":"https://na1.api.riotgames.com",
            "oc1":"https://oc1.api.riotgames.com",
            "tr1":"https://tr1.api.riotgames.com",
            "ru":"https://ru.api.riotgames.com"
        }
        self.headers = {'X-Riot-Token':token}
        self.autocache = AutoCache(cache)

    def fetch(self, platform:PlatformEndpoints, endpoint:str):
        return self.autocache.fetch(self.platform_endpoints[platform.value] + endpoint, self.headers)

    ### ACCOUNT-V1
    def get_riot_account_by_puuid(self, platform:PlatformEndpoints, puuid:str) -> dict:
        return self.fetch(platform, "/riot/account/v1/accounts/by-puuid/" + puuid)

    def get_riot_account_by_id(self, platform:PlatformEndpoints, gameName:str, tagLine:str) -> dict:
        return self.fetch(platform, "/riot/account/v1/accounts/by-riot-id/" + gameName + "/" + tagLine)

    def get_riot_active_shards(self, platform:PlatformEndpoints, game:str, puuid:str) -> dict:
        return self.fetch(platform, "/riot/account/v1/active-shards/by-game/" + game + "/by-puuid/" + puuid)

    ### CHAMPION-MASTERY-V4
    def get_champion_mastery_summoner_all(self, platform:PlatformEndpoints, summonerId:str) -> dict:
        return self.fetch(platform, "/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerId)

    def get_champion_mastery_summoner_champion(self, platform:PlatformEndpoints, summonerId:str, championId:str) -> dict:
        return self.fetch(platform, "/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerId + "/by-champion/" + championId)

    def get_champion_master_scores(self, platform:PlatformEndpoints, summonerId:str) -> dict:
        return self.fetch(platform, "/lol/champion-mastery/v4/scores/by-summoner/" + summonerId)

    ### CHAMPION-V3
    def get_champion_rotations(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/platform/v3/champion-rotations")

    ### CLASH-V1
    def get_clash_by_summoner(self, platform:PlatformEndpoints, summonerId:str) -> dict:
        return self.fetch(platform, "/lol/clash/v1/players/by-summoner/" + summonerId)

    def get_clash_team(self, platform:PlatformEndpoints, teamId:str) -> dict:
        return self.fetch(platform, "/lol/clash/v1/teams/" + teamId)

    def get_clash_tournaments(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/clash/v1/tournaments")

    def get_clash_tournament_by_team(self, platform:PlatformEndpoints, teamId:str) -> dict:
        return self.fetch(platform, "/lol/clash/v1/tournaments/by-team/" + teamId)

    def get_clash_tournament_by_id(self, platform:PlatformEndpoints, tournamentId:str) -> dict:
        return self.fetch(platform, "/lol/clash/v1/tournaments/" + tournamentId)

    ### LEAGUE-EXP-V4
    def get_league_exp_entry(self, platform:PlatformEndpoints, queue:str, tier:str, division:str) -> dict:
        return self.fetch(platform, "/lol/league-exp/v4/entries/%s/%s/%s" % (queue, tier, division))

    ### LEAGUE-V4
    def get_league_challenger_by_queue(self, platform:PlatformEndpoints, queue:str) -> dict:
        return self.fetch(platform, "/lol/league/v4/challenger/leagues/by-queue/" + queue)

    def get_league_entry_by_summoner(self, platform:PlatformEndpoints, summonerId:str) -> dict:
        return self.fetch(platform, "/lol/league/v4/entries/by-summoner/" + summonerId)

    def get_league_entry(self, platform:PlatformEndpoints, queue:str, tier:str, division:str) -> dict:
        return self.fetch(platform, "/lol/league/v4/entries/%s/%s/%s" % (queue, tier, division))

    def get_league_grandmastersleague(self, platform:PlatformEndpoints, queue:str) -> dict:
        return self.fetch(platform, "/lol/league/v4/grandmasterleagues/by-queue/" + queue)

    def get_league_by_id(self, platform:PlatformEndpoints, leagueId:str) -> dict:
        return self.fetch(platform, "/lol/league/v4/leagues/" + leagueId)

    def get_league_masterleagues(self, platform:PlatformEndpoints, queue:str) -> dict:
        return self.fetch(platform, "/lol/league/v4/masterleagues/by-queue/" + queue)

    ### LOL-STATUS-V3
    def get_shard_status(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/status/v3/shard-data")

    ### LOL-STATUS-V4
    def get_platform_data(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/status/v4/platform-data")

    ### LOR-MATCH-V1
    def get_lor_match_by_puuid(self, platform:PlatformEndpoints, puuid:str) -> dict:
        return self.fetch(platform, "/lor/match/v1/matches/by-puuid/%s/ids" % puuid)

    def get_lor_match(self, platform:PlatformEndpoints, match_id:str) -> dict:
        return self.fetch(platform, "/lor/match/v1/matches/" + match_id)

    ### LOR-RANKED-V1
    def get_lor_ranked_leaderboards(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lor/ranked/v1/leaderboards")

    ### LOR-STATUS-V1
    def get_lor_status(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lor/status/v1/platform-data")

    ### MATCH-V4
    def get_league_match_by_id(self, platform:PlatformEndpoints, match_id:str) -> dict:
        return self.fetch(platform, "/lol/match/v4/matches/" + match_id)

    def get_league_match_by_account(self, platform:PlatformEndpoints, account_id:str) -> dict:
        return self.fetch(platform, "/lol/match/v4/matchlists/by-account/" + account_id)

    def get_league_match_timeline_by_id(self, platform:PlatformEndpoints, match_id:str) -> dict:
        return self.fetch(platform, "/lol/match/v4/timelines/by-match/" + match_id)

    def get_league_matches_by_tournament_code(self, platform:PlatformEndpoints, tournament_code:str) -> dict:
        return self.fetch(platform, "/lol/match/v4/matches/by-tournament-code/%s/ids" % tournament_code)

    def get_league_match_by_tournament_code(self, platform:PlatformEndpoints, match_id:str, tournament_code:str) -> dict:
        return self.fetch(platform, "/lol/match/v4/matches/%s/by-tournament-code/%s" % (match_id, tournament_code))

    ### SPECTATOR-V4
    def get_league_spectator_by_summoner(self, platform:PlatformEndpoints, summoner_id:str) -> dict:
        return self.fetch(platform, "/lol/spectator/v4/active-games/by-summoner/" + summoner_id)

    def get_league_spectator_featured_games(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/spectator/v4/featured-games")

    ### SUMMONER-V4
    def get_summoner_by_name(self, platform:PlatformEndpoints, name:str) -> dict:
        return self.fetch(platform, "/lol/summoner/v4/summoners/by-name" + name)

    def get_summoner_by_account(self, platform:PlatformEndpoints, account_id:str) -> dict:
        return self.fetch(platform, "/lol/summoner/v1/summoners/by-account/" + account_id)

    def get_summoner_by_puuid(self, platform:PlatformEndpoints, puuid:str) -> dict:
        return self.fetch(platform, "/lol/summoner/v1/summoners/by-puuid/" + puuid)

    def get_summoner_by_id(self, platform:PlatformEndpoints, summonerId:str) -> dict:
        return self.fetch(platform, "/lol/summoner/v1/summoners/" + summonerId)

    ### TFT-LEAGUE-V1
    def get_tft_challenger(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/tft/league/v1/challenger")

    def get_tft_entries_by_summoner(self, platform:PlatformEndpoints, summoner_id:str) -> dict:
        return self.fetch(platform, "/tft/league/v1/entries/by-summoner/" + summoner_id)

    def get_tft_entries(self, platform:PlatformEndpoints, tier:str, division:str) -> dict:
        return self.fetch(platform, "/tft/league/v1/entries/%s/%s" % (tier, division))

    def get_tft_grandmaster(self, platform:PlatformEndpoints):
        return self.fetch(platform, "/tft/league/v1/grandmaster")

    def get_tft_leagues_by_id(self, platform:PlatformEndpoints, league_id:str) -> dict:
        return self.fetch(platform, "/tft/league/v1/leagues/" + league_id)

    def get_tft_master(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/tft/league/v1/master")

    ### TFT-MATCH-V1
    def get_tft_match_by_puuid(self, platform:PlatformEndpoints, puuid:str) -> dict:
        return self.fetch(platform, "/tft/match/v1/matches/by-puuid/%s/ids" % puuid)

    def get_tft_match_by_id(self, platform:PlatformEndpoints, match_id:str) -> dict:
        return self.fetch(platform, "/tft/match/v1/matches/" + match_id)

    ### TFT-SUMMONER-V1
    def get_tft_summoner_by_account(self, platform:PlatformEndpoints, account_id:str) -> dict:
        return self.fetch(platform, "/tft/summoner/v1/summoners/by-account/" + account_id)

    def get_tft_summoner_by_name(self, platform:PlatformEndpoints, name:str) -> dict:
        return self.fetch(platform, "/tft/summoner/v1/summoners/by-name/" + name)

    def get_tft_summoner_by_puuid(self, platform:PlatformEndpoints, puuid:str) -> dict:
        return self.fetch(platform, "/tft/summoner/v1/summoners/by-puuid/" + puuid)

    def get_tft_summoner_by_id(self, platform:PlatformEndpoints, summoner_id:str) -> dict:
        return self.fetch(platform, "/tft/summoner/v1/summoners/" + summoner_id)

    ### THIRD-PARTY-CODE-V4
    def get_third_party_code(self, platform:PlatformEndpoints, summoner_id:str) -> dict:
        return self.fetch(platform, "/lol/platform/v4/third-party-code/by-summoner/" + summoner_id)

    ### TOURNAMENT-STUB-V4
    def get_league_tournament_stub_codes(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/tournament-stub/v4/codes")

    def get_league_tournament_stub_by_code(self, platform:PlatformEndpoints, code:str) -> dict:
        return self.fetch(platform, "/lol/tournament-stub/v4/lobby-events/by-code/" + code)

    def get_league_tournament_stub_providers(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/tournament-stub/v4/providers")

    def get_league_tournament_stubs(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/tournament-stub/v4/tournaments")

    ### TOURNAMENT-V4
    def get_league_tournament_codes(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/tournament/v4/codes")

    def get_league_tournament_code_by_code(self, platform:PlatformEndpoints, code:str) -> dict:
        return self.fetch(platform, "/lol/tournament/v4/codes/" + code)

    def get_league_tournament_lobby_by_code(self, platform:PlatformEndpoints, code:str) -> dict:
        return self.fetch(platform, "/lol/tournament/v4/lobby-events/by-code/" + code)

    def get_league_tournament_providers(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/tournament/v4/providers")

    def get_league_tournament_tournaments(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/lol/tournament/v4/tournaments")

    ### VAL-CONTENT-V1
    def get_valorant_content(self, platform:PlatformEndpoints) -> dict:
        return self.fetch(platform, "/val/content/v1/contents")

    ### VAL-MATCH-V1
    def get_valorant_match_by_id(self, platform:PlatformEndpoints, match_id:str) -> dict:
        return self.fetch(platform, "/val/match/v1/matches/" + match_id)

    def get_valorant_match_by_puuid(self, platform:PlatformEndpoints, puuid:str) -> dict:
        return self.fetch(platform, "/val/match/v1/matchlists/by-puuid/" + puuid)

    def get_valorant_match_by_queue(self, platform:PlatformEndpoints, queue:str) -> dict:
        return self.fetch(platform, "/val/match/v1/recent-matches/by-queue/" + queue)

    ### VAL-RANKED-V1
    def get_valorant_ranked_by_act(self, platform:PlatformEndpoints, act_id:str) -> dict:
        return self.fetch(platform, "/val/ranked/v1/leaderboards/by-act/" + act_id)

    ### VAL-STATUS-V1
    def get_valorant_platform_data(self, platform:PlatformEndpoints):
        return self.fetch(platform, "/val/status/v1/platform-data")


class RiotRegionAPI:
    def __init__(self, token: str, cache=False):
        self.token = token
        self.cache = cache
        self.regional_endpoints = {
            "americas":"https://americas.api.riotgames.com",
            "asia":"https://asia.api.riotgames.com",
            "europe":"https://europe.api.riotgames.com"
        }
        self.headers = {'X-Riot-Token':token}

    def fetch(self, region:RegionalEndpoints, endpoint:str):
        return requests.get(self.regional_endpoints[region], headers=self.headers).json()

    ### ACCOUNT-V1
    def get_riot_account_by_puuid(self, region:RegionalEndpoints, puuid:str) -> dict:
        return self.fetch(region, "/riot/account/v1/accounts/by-puuid/" + puuid)

    def get_riot_account_by_id(self, region:RegionalEndpoints, gameName:str, tagLine:str) -> dict:
        return self.fetch(region, "/riot/account/v1/accounts/by-riot-id/" + gameName + "/" + tagLine)

    def get_riot_active_shards(self, region:RegionalEndpoints, game:str, puuid:str) -> dict:
        return self.fetch(region, "/riot/account/v1/active-shards/by-game/" + game + "/by-puuid/" + puuid)

    ### CHAMPION-MASTERY-V4
    def get_champion_mastery_summoner_all(self, region:RegionalEndpoints, summonerId:str) -> dict:
        return self.fetch(region, "/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerId)

    def get_champion_mastery_summoner_champion(self, region:RegionalEndpoints, summonerId:str, championId:str) -> dict:
        return self.fetch(region, "/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerId + "/by-champion/" + championId)

    def get_champion_master_scores(self, region:RegionalEndpoints, summonerId:str) -> dict:
        return self.fetch(region, "/lol/champion-mastery/v4/scores/by-summoner/" + summonerId)

    ### CHAMPION-V3
    def get_champion_rotations(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/platform/v3/champion-rotations")

    ### CLASH-V1
    def get_clash_by_summoner(self, region:RegionalEndpoints, summonerId:str) -> dict:
        return self.fetch(region, "/lol/clash/v1/players/by-summoner/" + summonerId)

    def get_clash_team(self, region:RegionalEndpoints, teamId:str) -> dict:
        return self.fetch(region, "/lol/clash/v1/teams/" + teamId)

    def get_clash_tournaments(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/clash/v1/tournaments")

    def get_clash_tournament_by_team(self, region:RegionalEndpoints, teamId:str) -> dict:
        return self.fetch(region, "/lol/clash/v1/tournaments/by-team/" + teamId)

    def get_clash_tournament_by_id(self, region:RegionalEndpoints, tournamentId:str) -> dict:
        return self.fetch(region, "/lol/clash/v1/tournaments/" + tournamentId)

    ### LEAGUE-EXP-V4
    def get_league_exp_entry(self, region:RegionalEndpoints, queue:str, tier:str, division:str) -> dict:
        return self.fetch(region, "/lol/league-exp/v4/entries/%s/%s/%s" % (queue, tier, division))

    ### LEAGUE-V4
    def get_league_challenger_by_queue(self, region:RegionalEndpoints, queue:str) -> dict:
        return self.fetch(region, "/lol/league/v4/challenger/leagues/by-queue/" + queue)

    def get_league_entry_by_summoner(self, region:RegionalEndpoints, summonerId:str) -> dict:
        return self.fetch(region, "/lol/league/v4/entries/by-summoner/" + summonerId)

    def get_league_entry(self, region:RegionalEndpoints, queue:str, tier:str, division:str) -> dict:
        return self.fetch(region, "/lol/league/v4/entries/%s/%s/%s" % (queue, tier, division))

    def get_league_grandmastersleague(self, region:RegionalEndpoints, queue:str) -> dict:
        return self.fetch(region, "/lol/league/v4/grandmasterleagues/by-queue/" + queue)

    def get_league_by_id(self, region:RegionalEndpoints, leagueId:str) -> dict:
        return self.fetch(region, "/lol/league/v4/leagues/" + leagueId)

    def get_league_masterleagues(self, region:RegionalEndpoints, queue:str) -> dict:
        return self.fetch(region, "/lol/league/v4/masterleagues/by-queue/" + queue)

    ### LOL-STATUS-V3
    def get_shard_status(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/status/v3/shard-data")

    ### LOL-STATUS-V4
    def get_platform_data(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/status/v4/platform-data")

    ### LOR-MATCH-V1
    def get_lor_match_by_puuid(self, region:RegionalEndpoints, puuid:str) -> dict:
        return self.fetch(region, "/lor/match/v1/matches/by-puuid/%s/ids" % puuid)

    def get_lor_match(self, region:RegionalEndpoints, match_id:str) -> dict:
        return self.fetch(region, "/lor/match/v1/matches/" + match_id)

    ### LOR-RANKED-V1
    def get_lor_ranked_leaderboards(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lor/ranked/v1/leaderboards")

    ### LOR-STATUS-V1
    def get_lor_status(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lor/status/v1/platform-data")

    ### MATCH-V4
    def get_league_match_by_id(self, region:RegionalEndpoints, match_id:str) -> dict:
        return self.fetch(region, "/lol/match/v4/matches/" + match_id)

    def get_league_match_by_account(self, region:RegionalEndpoints, account_id:str) -> dict:
        return self.fetch(region, "/lol/match/v4/matchlists/by-account/" + account_id)

    def get_league_match_timeline_by_id(self, region:RegionalEndpoints, match_id:str) -> dict:
        return self.fetch(region, "/lol/match/v4/timelines/by-match/" + match_id)

    def get_league_matches_by_tournament_code(self, region:RegionalEndpoints, tournament_code:str) -> dict:
        return self.fetch(region, "/lol/match/v4/matches/by-tournament-code/%s/ids" % tournament_code)

    def get_league_match_by_tournament_code(self, region:RegionalEndpoints, match_id:str, tournament_code:str) -> dict:
        return self.fetch(region, "/lol/match/v4/matches/%s/by-tournament-code/%s" % (match_id, tournament_code))

    ### SPECTATOR-V4
    def get_league_spectator_by_summoner(self, region:RegionalEndpoints, summoner_id:str) -> dict:
        return self.fetch(region, "/lol/spectator/v4/active-games/by-summoner/" + summoner_id)

    def get_league_spectator_featured_games(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/spectator/v4/featured-games")

    ### SUMMONER-V4
    def get_summoner_by_name(self, region:RegionalEndpoints, name:str) -> dict:
        return self.fetch(region, "/lol/summoner/v4/summoners/by-name" + name)

    def get_summoner_by_account(self, region:RegionalEndpoints, account_id:str) -> dict:
        return self.fetch(region, "/lol/summoner/v1/summoners/by-account/" + account_id)

    def get_summoner_by_puuid(self, region:RegionalEndpoints, puuid:str) -> dict:
        return self.fetch(region, "/lol/summoner/v1/summoners/by-puuid/" + puuid)

    def get_summoner_by_id(self, region:RegionalEndpoints, summonerId:str) -> dict:
        return self.fetch(region, "/lol/summoner/v1/summoners/" + summonerId)

    ### TFT-LEAGUE-V1
    def get_tft_challenger(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/tft/league/v1/challenger")

    def get_tft_entries_by_summoner(self, region:RegionalEndpoints, summoner_id:str) -> dict:
        return self.fetch(region, "/tft/league/v1/entries/by-summoner/" + summoner_id)

    def get_tft_entries(self, region:RegionalEndpoints, tier:str, division:str) -> dict:
        return self.fetch(region, "/tft/league/v1/entries/%s/%s" % (tier, division))

    def get_tft_grandmaster(self, region:RegionalEndpoints):
        return self.fetch(region, "/tft/league/v1/grandmaster")

    def get_tft_leagues_by_id(self, region:RegionalEndpoints, league_id:str) -> dict:
        return self.fetch(region, "/tft/league/v1/leagues/" + league_id)

    def get_tft_master(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/tft/league/v1/master")

    ### TFT-MATCH-V1
    def get_tft_match_by_puuid(self, region:RegionalEndpoints, puuid:str) -> dict:
        return self.fetch(region, "/tft/match/v1/matches/by-puuid/%s/ids" % puuid)

    def get_tft_match_by_id(self, region:RegionalEndpoints, match_id:str) -> dict:
        return self.fetch(region, "/tft/match/v1/matches/" + match_id)

    ### TFT-SUMMONER-V1
    def get_tft_summoner_by_account(self, region:RegionalEndpoints, account_id:str) -> dict:
        return self.fetch(region, "/tft/summoner/v1/summoners/by-account/" + account_id)

    def get_tft_summoner_by_name(self, region:RegionalEndpoints, name:str) -> dict:
        return self.fetch(region, "/tft/summoner/v1/summoners/by-name/" + name)

    def get_tft_summoner_by_puuid(self, region:RegionalEndpoints, puuid:str) -> dict:
        return self.fetch(region, "/tft/summoner/v1/summoners/by-puuid/" + puuid)

    def get_tft_summoner_by_id(self, region:RegionalEndpoints, summoner_id:str) -> dict:
        return self.fetch(region, "/tft/summoner/v1/summoners/" + summoner_id)

    ### THIRD-PARTY-CODE-V4
    def get_third_party_code(self, region:RegionalEndpoints, summoner_id:str) -> dict:
        return self.fetch(region, "/lol/platform/v4/third-party-code/by-summoner/" + summoner_id)

    ### TOURNAMENT-STUB-V4
    def get_league_tournament_stub_codes(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/tournament-stub/v4/codes")

    def get_league_tournament_stub_by_code(self, region:RegionalEndpoints, code:str) -> dict:
        return self.fetch(region, "/lol/tournament-stub/v4/lobby-events/by-code/" + code)

    def get_league_tournament_stub_providers(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/tournament-stub/v4/providers")

    def get_league_tournament_stubs(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/tournament-stub/v4/tournaments")

    ### TOURNAMENT-V4
    def get_league_tournament_codes(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/tournament/v4/codes")

    def get_league_tournament_code_by_code(self, region:RegionalEndpoints, code:str) -> dict:
        return self.fetch(region, "/lol/tournament/v4/codes/" + code)

    def get_league_tournament_lobby_by_code(self, region:RegionalEndpoints, code:str) -> dict:
        return self.fetch(region, "/lol/tournament/v4/lobby-events/by-code/" + code)

    def get_league_tournament_providers(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/tournament/v4/providers")

    def get_league_tournament_tournaments(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/lol/tournament/v4/tournaments")

    ### VAL-CONTENT-V1
    def get_valorant_content(self, region:RegionalEndpoints) -> dict:
        return self.fetch(region, "/val/content/v1/contents")

    ### VAL-MATCH-V1
    def get_valorant_match_by_id(self, region:RegionalEndpoints, match_id:str) -> dict:
        return self.fetch(region, "/val/match/v1/matches/" + match_id)

    def get_valorant_match_by_puuid(self, region:RegionalEndpoints, puuid:str) -> dict:
        return self.fetch(region, "/val/match/v1/matchlists/by-puuid/" + puuid)

    def get_valorant_match_by_queue(self, region:RegionalEndpoints, queue:str) -> dict:
        return self.fetch(region, "/val/match/v1/recent-matches/by-queue/" + queue)

    ### VAL-RANKED-V1
    def get_valorant_ranked_by_act(self, region:RegionalEndpoints, act_id:str) -> dict:
        return self.fetch(region, "/val/ranked/v1/leaderboards/by-act/" + act_id)

    ### VAL-STATUS-V1
    def get_valorant_platform_data(self, region:RegionalEndpoints):
        return self.fetch(region, "/val/status/v1/platform-data")
