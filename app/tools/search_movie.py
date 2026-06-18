from langchain_core.tools import tool

from app.services.tmdb_service import TMDBService


@tool
async def search_movie(query: str):
    """
    Search movies by title.
    """

    service = TMDBService()

    return await service.search_movie(query)