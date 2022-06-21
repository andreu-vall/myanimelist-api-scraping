# MyAnimeList Official API Scraping

Scraping the MyAnimeList official API for Anime and Mangas, really fast

Data uploaded on [kaggle](https://www.kaggle.com/datasets/andreuvallhernndez/myanimelist)

## Abstract
With the new version of the official MyAnimeList API (v2), there are 2 endpoints
[/anime/ranking](https://myanimelist.net/apiconfig/references/api/v2#operation/anime_ranking_get) and
[/manga/ranking](https://myanimelist.net/apiconfig/references/api/v2#operation/manga_ranking_get) that give nearly all the information
of an Anime and a Manga at up to 500 items (Animes or Mangas) per querie, so scraping the entire 24.000 Animes only takes 50 calls and the 66.500
Mangas takes around 133 calls. Important: only the ranking_type=favorite contains all the Animes/Mangas, the other ones don't have the nsfw entries.

That means that instead of scraping just one Anime per call at 1 querie / second, which would take over 6 Hours, we can scrap the entire Anime Database
in under 3 minutes! The Mangas database takes a bit more, but with 10 minutes it should be done.

There is no restriction of queries / time specified on the API, but please use it with moderation and following the
[API license](https://myanimelist.net/static/apiagreement.html). Before manually scraping check if the data available is recent.

## Necessary
To use the [MyAnimeList official API](https://myanimelist.net/apiconfig/references/api/v2) it's needed a Client ID,
which is an unique identifier that must be requested at [MyAnimeList](https://myanimelist.net/apiconfig).
Also check the [Official MAL page](https://myanimelist.net/clubs.php?cid=13727).

Once obtained, put it in a file named "client_id.txt" at the root directory


## Acknowledgements
Special thanks to MyAnimeList and its users for the awesome Database, as well as the new Official API for being so fast.
