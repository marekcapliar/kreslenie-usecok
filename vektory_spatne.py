from PIL import Image

a = input('zadaj bod A v tvare x,y (0-249):')
b = input('zadaj bod B v tvare x,y (0-249):')
a = a.split(',')
b = b.split(',')
a = list(map(lambda x: int(x), a))
b = list(map(lambda x: int(x), b))

x_vector = b[0] - a[0]
y_vector = b[1] - a[1]
vector = [abs(x_vector), abs(y_vector)]
small_vector = sorted(vector)[0]
if small_vector != 0:
    k = [x_vector//small_vector, y_vector//small_vector]
else:
    k = [x_vector, y_vector]
    small_vector = 1

img = Image.new('RGB', (250, 250), 'white')
pixels = img.load()

vychylka_x = 0
vychylka_y = 0

for i in range(small_vector):
    for x in range(abs(k[0])):
        pixels[a[0], a[1]] = (0, 0, 0)
        a[0] += x_vector//abs(x_vector)
        vychylka_x += x_vector/small_vector - x_vector//small_vector
        if 0.8 <= vychylka_x <= 1.2:
            vychylka_x -= 1
            pixels[a[0], a[1]] = (0, 0, 0)
            a[1] += y_vector//abs(y_vector)
    for y in range(abs(k[1])):
        pixels[a[0], a[1]] = (0, 0, 0)
        a[1] += y_vector//abs(y_vector)
        vychylka_y += y_vector/small_vector - y_vector//small_vector
        if 0.5 <= vychylka_y <= 1.5:
            vychylka_y -= 1
            pixels[a[0], a[1]] = (0, 0, 0)
            a[0] += x_vector//abs(x_vector)

img.show()
