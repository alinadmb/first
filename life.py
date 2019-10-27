import random
import copy
from tkinter import *
from tkinter import messagebox

# Заполняем поле рандомно (1 - клетка заполнена, 0 - клетка пуста)
def fillMatrix(matrix, n, m):
    for i in range(n):
        col = []
        for j in range(m):
            col.append(random.randint(0, 1))
        matrix.append(col)
    return matrix

# Описание одной итерации
def makeIteration(matrix, n, m):
    # копируем исходную матрицу, чтобы все изменения в клетках заносить сразу
    # в исходную матрицу, а копию использовать для проверки соседей
    copyOfMatrix = copy.deepcopy(matrix)
    # в зависимости от положения клетки (в середине, на границе, в угле) проверяем ее соседей на заполненность
    # количество заполненных соседей сохраняем в переменную k
    for i in range(0, n):
        for j in range(0, m):
            k = 0  # количество заполненных соседей
            if i == 0 and j != 0 and j != m - 1:
                for f in range(i, i + 2):
                    for q in range(j - 1, j + 2):
                        if copyOfMatrix[f][q] == 1:
                            k += 1
            elif i == n - 1 and j != 0 and j != m - 1:
                for f in range(i - 1, i + 1):
                    for q in range(j - 1, j + 2):
                        if copyOfMatrix[f][q] == 1:
                            k += 1
            elif j == 0 and i != 0 and i != n - 1:
                for f in range(i - 1, i + 2):
                    for q in range(j, j + 2):
                        if copyOfMatrix[f][q] == 1:
                            k += 1
            elif j == m - 1 and i != 0 and i != n - 1:
                for f in range(i - 1, i + 2):
                    for q in range(j - 1, j + 1):
                        if copyOfMatrix[f][q] == 1:
                            k += 1
            elif i == 0 and j == 0:
                for f in range(i, i + 2):
                    for q in range(j, j + 2):
                        if copyOfMatrix[f][q] == 1:
                            k += 1
            elif i == 0 and j == m - 1:
                for f in range(i, i + 2):
                    for q in range(j - 1, j + 1):
                        if copyOfMatrix[f][q] == 1:
                            k += 1
            elif i == n - 1 and j == 0:
                for f in range(i - 1, i + 1):
                    for q in range(j, j + 2):
                        if copyOfMatrix[f][q] == 1:
                            k += 1
            elif i == n - 1 and j == m - 1:
                for f in range(i - 1, i + 1):
                    for q in range(j - 1, j + 1):
                        if copyOfMatrix[f][q] == 1:
                            k += 1
            else:
                for f in range(i - 1, i + 2):
                    for q in range(j - 1, j + 2):
                        if copyOfMatrix[f][q] == 1:
                            k += 1
            if copyOfMatrix[i][j] == 1:
                k -= 1  # вычитаем из k едииницу, т.к. при подсчете сама клетка подошла под условие и засчиталась в k
            # в зависимости от количества "живых" соседей присваиваем клетке определенное значение
            if k == 3:
                matrix[i][j] = 1
            elif k < 2 or k > 3:
                matrix[i][j] = 0
    # в случае, когда развитие жизни прекращается, т.е. когда предыдущее поколение совпадает с текущим,
    # отправляем оповещение об этом
    if copyOfMatrix == matrix:
        messagebox.showinfo('Конец', 'Развитие жизни остановилось')

# функция для построения поля
def showCells(matrix, n, m):
    for i in range(n):
        for j in range(m):
            x1, y1 = j * cellSize, i * cellSize
            x2, y2 = j * cellSize + cellSize, i * cellSize + cellSize
            canvas.create_rectangle((x1, y1), (x2, y2), fill=cell_colors[matrix[i][j]])
    canvas.pack()

# функция начала игры
def beginGame():
    makeIteration(cells, n, m)
    showCells(cells, n, m)
    beginBtn.configure(text='Следующее поколение')
    rowsLbl.destroy()
    rows.destroy()
    colsLbl.destroy()
    cols.destroy()


# создаем окно для игры
root = Tk()
root.title('Игра "Жизнь"')
cellSize = 30
cell_colors = ['white', 'blue']

# Распологаем окно по центру
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))

n = 10  # количество строк поля
m = 10  # количество столбцов поля
# элементы начальной страницы
rowsLbl = Label(root, text='Количество строк:')
rowsLbl.pack()
var1 = IntVar()
var1.set(n)
rows = Entry(root, width=5, textvariable=var1)
rows.pack()
colsLbl = Label(root, text='Количество столбцов:')
colsLbl.pack()
var2 = IntVar()
var2.set(m)
cols = Entry(root, width=5, textvariable=var2)
cols.pack()

# элементы игры
cells = []
fillMatrix(cells, n, m)
canvas = Canvas(root, width=cellSize*n, height=cellSize*m)
beginBtn = Button(root, text='Начать', command=beginGame)
beginBtn.pack()

root.mainloop()
