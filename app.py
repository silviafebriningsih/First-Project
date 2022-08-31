def luas_lingkaran(r):
    return 3.14 * (r * r)

r = input('masukan jari-jari lingkaran: ')
luas = luas_lingkaran(int(r))

print('Luasnya: {}' .format(luas))