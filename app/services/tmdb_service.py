import httpx

from app.core.config import settings


TMDBQueryValue = str | int | float | bool


class TMDBService:
    BASE_URL = "https://api.themoviedb.org/3"

    def _build_params(
        self,
        extra_params: dict[str, TMDBQueryValue] | None = None,
    ) -> dict[str, TMDBQueryValue]:
        if not settings.TMDB_API_KEY:
            raise RuntimeError("TMDB_API_KEY não configurada")

        params: dict[str, TMDBQueryValue] = {"api_key": settings.TMDB_API_KEY}

        if extra_params:
            params.update(extra_params)

        return params

    async def _get(
        self,
        path: str,
        params: dict[str, TMDBQueryValue] | None = None,
    ):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}{path}",
                params=self._build_params(params),
            )

            response.raise_for_status()

            return response.json()

    async def search_movie(self, query: str, page: int = 1):
        return await self._get(
            "/search/movie",
            {"query": query, "page": page},
        )

    async def search_tv_show(self, query: str, page: int = 1):
        return await self._get(
            "/search/tv",
            {"query": query, "page": page},
        )

    async def discover_content(
        self,
        media_type: str = "movie",
        genres: str | None = None,
        year: int | None = None,
        rating: float | None = None,
        page: int = 1,
        first_air_date_gte: str | None = None,
        first_air_date_lte: str | None = None,
        release_date_gte: str | None = None,
        release_date_lte: str | None = None,
        vote_count_gte: int | None = None,
    ):
        params: dict[str, TMDBQueryValue] = {"page": page}

        if genres:
            params["with_genres"] = genres
        if year is not None:
            if media_type == "tv":
                params["first_air_date_year"] = year
            else:
                params["primary_release_year"] = year
        if rating is not None:
            params["vote_average.gte"] = rating
        if first_air_date_gte:
            params["first_air_date.gte"] = first_air_date_gte
        if first_air_date_lte:
            params["first_air_date.lte"] = first_air_date_lte
        if release_date_gte:
            params["release_date.gte"] = release_date_gte
        if release_date_lte:
            params["release_date.lte"] = release_date_lte
        if vote_count_gte is not None:
            params["vote_count.gte"] = vote_count_gte

        discover_path = "/discover/tv" if media_type == "tv" else "/discover/movie"

        return await self._get(discover_path, params)

    async def get_movie_details(self, movie_id: int):
        return await self._get(f"/movie/{movie_id}")

    async def get_tv_details(self, tv_id: int):
        return await self._get(f"/tv/{tv_id}")

    async def get_cast(self, media_type: str, content_id: int):
        if media_type == "tv":
            return await self._get(f"/tv/{content_id}/credits")

        return await self._get(f"/movie/{content_id}/credits")

    async def get_person_details(self, person_id: int):
        return await self._get(f"/person/{person_id}")

    async def get_similar_movies(self, media_type: str, content_id: int):
        if media_type == "tv":
            return await self._get(f"/tv/{content_id}/similar")

        return await self._get(f"/movie/{content_id}/similar")

    async def get_recommendations(self, media_type: str, content_id: int):
        if media_type == "tv":
            return await self._get(f"/tv/{content_id}/recommendations")

        return await self._get(f"/movie/{content_id}/recommendations")

    async def get_trending(self, media_type: str = "all", page: int = 1):
        return await self._get(
            f"/trending/{media_type}/week",
            {"page": page},
        )