from lib.music_library import *

'''
Initially there is no text/empty string;
returns an empty list.
'''

def test_if_empty():
    my_music_library = MyMusicLibrary()
    my_music_library.tracks_register("")
    assert my_music_library.known_tracks() == [""]

'''
Entry of a known track;
returns a list with that track as an item.
'''

def test_if_known_track_returns_append_track_to_list():
    my_music_library = MyMusicLibrary()
    my_music_library.tracks_register("Papaoutai")
    assert my_music_library.known_tracks() == ["Papaoutai"]

'''
Entry of a known track and an unknown track;
radds only the known track into the known_track list.
'''

def test_if_known_and_unknown_tracks_returns_append_known_track_to_list():
    my_music_library = MyMusicLibrary()
    my_music_library.tracks_register("Papaoutai")
    my_music_library.tracks_register("Carmen")
    assert my_music_library.known_tracks() == ["Papaoutai", "Carmen"]

