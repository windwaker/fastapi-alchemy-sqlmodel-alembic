from fastapi import Depends, FastAPI, status, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session

# It's worth noting that "from app.models import Song" is required.
# Without it, the song table will not be created.
from app.models import Song, SongCreate

app = FastAPI()


@app.get("/songs/{song_id}", response_model=Song, status_code=status.HTTP_200_OK)
async def get_song(song_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song).where(Song.id == song_id))
    song = result.scalars().first()
    if not song:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Song with id of {song_id} is not available.')
    return song


@app.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    results = await session.execute(select(Song))
    songs = results.scalars().all()
    return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]


@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist, year=song.year)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song


@app.put("/songs/{song_id}", response_model=Song, status_code=status.HTTP_202_ACCEPTED)
async def update_song(song_id: int, song_request: Song, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song).where(Song.id == song_id))
    song = result.scalars().first()
    if not song:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Song with id of {song_id} is not available.')

    song.year = song_request.year
    song.name = song_request.name
    song.artist = song_request.artist
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song


@app.delete("/songs/{song_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_song(song_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song).where(Song.id == song_id))
    song = result.scalars().first()

    await session.delete(song)
    await session.commit()

    return song


















