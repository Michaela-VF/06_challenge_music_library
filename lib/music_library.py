'''
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
'''

class MyMusicLibrary():
    def __init__(self):
        self._list_known_tracks = []

    def tracks_register(self, track_entry):
        if track_entry not in self._list_known_tracks:
            self._list_known_tracks.append(track_entry)

    def known_tracks(self):
        return self._list_known_tracks