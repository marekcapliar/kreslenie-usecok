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
    k = [int(x_vector/small_vector), int(y_vector/small_vector)]
else:
    k = [x_vector, y_vector]
    small_vector = 1

img = Image.new('RGB', (250, 250), 'white')
pixels = img.load()

count = sum(vector)
errorx = 0      # abs(x_vector/small_vector - k[0])
errory = 0      # abs(y_vector/small_vector - k[1])

while count > 0:
    for x in range(abs(k[0])):
        pixels[a[0], a[1]] = (0, 0, 0)
        a[0] += x_vector//abs(x_vector)
        count -= 1
        errorx += abs(x_vector/small_vector - k[0])
        if errorx >= 1:
            pixels[a[0], a[1]] = (0, 0, 0)
            a[0] += x_vector//abs(x_vector)
            count -= 1
            errorx -= 1
    for y in range(abs(k[1])):
        pixels[a[0], a[1]] = (0, 0, 0)
        a[1] += y_vector//abs(y_vector)
        count -= 1
        errory += abs(y_vector/small_vector - k[1])
        if errory >= 1:
            pixels[a[0], a[1]] = (0, 0, 0)
            a[1] += y_vector//abs(y_vector)
            count -= 1
            errory -= 1

img.show()
