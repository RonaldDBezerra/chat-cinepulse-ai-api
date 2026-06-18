import httpx

from app.core.config import settings


class TMDBService:
    BASE_URL = "https://api.themoviedb.org/3"

    async def search_movie(self, query: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/search/movie",
                params={
                    "api_key": settings.TMDB_API_KEY,
                    "query": query,
                },
            )

            return response.json()