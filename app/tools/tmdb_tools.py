from langchain_core.tools import tool

from app.services.tmdb_service import TMDBService


@tool
async def search_movie(query: str, page: int = 1):
    """
    Search movies by title.
    """

    service = TMDBService()

    return await service.search_movie(query, page)


@tool
async def search_tv_show(query: str, page: int = 1):
    """
    Search TV shows by title.
    """

    service = TMDBService()

    return await service.search_tv_show(query, page)


@tool
async def discover_content(
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
    """
    Discover movies or TV shows using TMDB filters.
    """

    service = TMDBService()

    return await service.discover_content(
        media_type=media_type,
        genres=genres,
        year=year,
        rating=rating,
        page=page,
        first_air_date_gte=first_air_date_gte,
        first_air_date_lte=first_air_date_lte,
        release_date_gte=release_date_gte,
        release_date_lte=release_date_lte,
        vote_count_gte=vote_count_gte,
    )


@tool
async def get_movie_details(movie_id: int):
    """
    Get detailed movie information by TMDB id.
    """

    service = TMDBService()

    return await service.get_movie_details(movie_id)


@tool
async def get_tv_details(tv_id: int):
    """
    Get detailed TV show information by TMDB id.
    """

    service = TMDBService()

    return await service.get_tv_details(tv_id)


@tool
async def get_cast(media_type: str, content_id: int):
    """
    Get cast information for a movie or TV show.
    """

    service = TMDBService()

    return await service.get_cast(media_type, content_id)


@tool
async def get_person_details(person_id: int):
    """
    Get person details by TMDB id.
    """

    service = TMDBService()

    return await service.get_person_details(person_id)


@tool
async def get_similar_movies(media_type: str, content_id: int):
    """
    Get similar movies or TV shows by TMDB id.
    """

    service = TMDBService()

    return await service.get_similar_movies(media_type, content_id)


@tool
async def get_recommendations(media_type: str, content_id: int):
    """
    Get recommendations for a movie or TV show by TMDB id.
    """

    service = TMDBService()

    return await service.get_recommendations(media_type, content_id)


@tool
async def get_trending(media_type: str = "all", page: int = 1):
    """
    Get trending movies, TV shows, or all content for the week.
    """

    service = TMDBService()

    return await service.get_trending(media_type, page)