import audioextractor as a

song_name = "Sakhiyaan"
raw_track_data = a.extract_raw_info(song_name)
track_data = a.extract_info(song_name)
print(raw_track_data)
print(track_data)
