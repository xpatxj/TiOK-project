from locust import HttpUser, task, between
import time

class TiOKUser(HttpUser):
    # Ustawienie czasu oczekiwania między zadaniami na 1 do 10 sekund.
    wait_time = between(1, 10)

    @task
    def view_homepage(self):
        # Wykonanie żądania GET do strony głównej serwisu.
        # To zadanie symuluje wejście użytkownika na stronę główną.
        self.client.get("/")
    @task
    def view_albums(self):
        # Wykonanie żądania GET do strony z albumami.
        # To zadanie symuluje wejście użytkownika na stronę z albumami.
        self.client.get("/albums")



    @task(5)
    def view_post(self):
        # Wykonanie żądania GET do podstrony z postem.
        # Zadanie to jest wykonywane 5 razy częściej niż inne zadania
        # Testujemy przeglądanie wszystkich 100 postów
        # Na każdy post użytkonik przeznacza 5 sekund
        for post_id in range(1,100):
            self.client.get(f"/post/{post_id}", name="/post")
            time.sleep(5)

    @task(3)
    def view_album(self):
        # Wykonanie żądania GET do podstrony z albumami.
        # Zadanie to jest wykonywane 3 razy częściej niż inne zadania
        # Testujemy przeglądanie 100 albumów
        # Na każdy album użytkonik przeznacza 10 sekund
        for album_id in range(1,100):
            self.client.get(f"/albums/{album_id}/photos", name="/album")
            time.sleep(10)
    @task
    def post_filter(self):
        # Wykonanie żądania POST do zafiltrowania długości postów
        # Symuluje działanie użytkownika, który postanawia wyszukać posty o długości od 100 do 200 znaków
        self.client.post("/filter", {"range_left": 100, "range_right": 200})