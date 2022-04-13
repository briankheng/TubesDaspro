import FungsiBuatan

# Variabel Global
users = FungsiBuatan.CSVParser(open('FileEksternal/user.csv', 'r').readlines())
games = FungsiBuatan.CSVParser(open('FileEksternal/game.csv', 'r').readlines())
kepemilikan = FungsiBuatan.CSVParser(open('FileEksternal/kepemilikan.csv', 'r').readlines())
riwayat = FungsiBuatan.CSVParser(open('FileEksternal/riwayat.csv', 'r').readlines())