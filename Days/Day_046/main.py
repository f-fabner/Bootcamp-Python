from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configurações do Spotify
CLIENT_ID = "YOUR_ID"  # Substitua pelo seu CLIENT_ID
CLIENT_SECRET = "YOUR_SECRET"  # Substitua pelo seu CLIENT_SECRET
REDIRECT_URI = "YOUR_URI"  # Use uma URL válida

# Função para coletar dados da Billboard, de acordo com a data selecionada pelo usuário
def get_billboard_top_100(date):
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a resposta é válida (HTTP 200)
    html = response.text
    
    # Parseia a resposta usando BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    
    # Encontra os itens das músicas na página
    items = soup.find_all(name="ul", class_="o-chart-results-list-row")
    
    # Extrai as músicas usando a função get_songs
    def get_songs(row_items):
        """ Extrai as músicas da sopa """
        extracted_songs = []
        for item in row_items:
            # Extrai a pontuação, título e artista de cada item
            score = item.find(name="span", class_="c-label").getText().strip()
            title = item.find(name="h3", id="title-of-a-story").getText().strip()
            section = item.find(name="ul", class_="lrv-a-unstyle-list")
            artist = section.find(name="span", class_="c-label").getText().strip()
            extracted_songs.append({"title": title, "artist": artist, "score": score})
        
        return extracted_songs
    
    # Chama a função get_songs para coletar as músicas
    songs = get_songs(items)
    
    # Separar títulos e artistas em listas separadas
    song_titles = [song['title'] for song in songs]
    artists = [song['artist'] for song in songs]
    
    return song_titles, artists

# Função para autenticar com o Spotify
def authenticate_spotify():
    # Configuração da autenticação
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=["playlist-modify-private", "playlist-modify-public"],
            cache_path="spotify_token.txt",  # Arquivo para armazenar o token de acesso
        )
    )
    return sp

# Função para criar uma playlist no Spotify
def create_spotify_playlist(sp, date):
    user_id = sp.current_user()["id"]
    # Cria a playlist
    playlist = sp.user_playlist_create(
        user=user_id,
        name=f"Billboard Top 100 - {date}",
        public=True
    )
    return playlist

# Função para buscar músicas no Spotify e adicionar à playlist
def add_songs_to_playlist(sp, playlist, song_titles, artists):
    uris = []
    
    for index, (song, artist) in enumerate(zip(song_titles, artists)):
        try:
            # Formata a consulta com o título da música e artista
            query = f"track:{song} artist:{artist}"
            
            # Realiza a busca no Spotify
            results = sp.search(q=query, type="track", limit=1)
            
            # Processa os resultados
            tracks = results.get("tracks", {}).get("items", [])
            
            if tracks:
                # Adiciona o URI da música à lista de URIs
                uri = tracks[0]["uri"]
                uris.append(uri)
                print(f"Adicionada música: '{song}' de '{artist}'")
            else:
                # Nenhum resultado encontrado para a música
                print(f"Nenhum resultado encontrado para '{song}' de '{artist}'")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Erro na busca de '{song}' de '{artist}': {e}")
        except Exception as e:
            print(f"Erro desconhecido ao buscar '{song}' de '{artist}': {e}")

    # Verifica se há músicas para adicionar
    if uris:
        # Adiciona as músicas à playlist
        sp.playlist_add_items(playlist_id=playlist["id"], items=uris)
        print(f"Adicionadas {len(uris)} músicas à playlist '{playlist['name']}'.")
    else:
        print("Nenhuma música foi encontrada para adicionar à playlist.")

# Função principal
def main():
    # Recebe a data do usuário
    date = input("\nDigite a data (formato AAAA-MM-DD):\n")

    # Coleta as músicas e artistas do Hot 100 da data escolhida
    song_titles, artists = get_billboard_top_100(date)

    # Verifica se houve um problema na coleta dos dados
    if not song_titles or not artists:
        print("Houve um problema na coleta das músicas ou dos artistas.")
        return

    # Autentica com o Spotify
    sp = authenticate_spotify()

    # Cria uma nova playlist
    playlist = create_spotify_playlist(sp, date)

    # Adiciona as músicas à playlist
    add_songs_to_playlist(sp, playlist, song_titles, artists)

if __name__ == "__main__":
    main()

