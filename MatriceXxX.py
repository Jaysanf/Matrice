def matriceXxX():
	print("Entrez vos nombres de gauche à droite de haut en bas:")
	matXxX = []
	for i in range(1,dimension + 1):
		print('Entrez les chiffres de la ligne #',i)
		Ligne = [float(input()) for i in range(0,dimension)]
		matXxX.append(Ligne)
	return matXxX

def IXxX():
	I = []
	for d in range(0,dimension):
		l = []
		for i in range(0,dimension):
			if d == i:
				x = 1
			else:
				x = 0
			l.append(x)
		I.append(l)
	return I

def determinantXxX(mat):
	det = 1
	signe = 0
	if  (detcheck2(mat) == False):
		for d in range(0,dimension-1):
			while mat[d][d] == 0:
				x = mat.pop(d)
				mat.append(x)
				signe += 1*(dimension - (d + 1))
			for i in range(d+1,dimension):
				nombre = (mat[i][d]/mat[d][d])
				l1 = (list(map(lambda x: x*nombre,mat[d])))
				mat[i] = [z - l for z, l in zip(mat[i], l1) ]
		for i in range(0,dimension):
			det *= float(mat[i][i])
		det *= (-1)**(signe)
	else:
		det = 0
	if det == -0:
		det = 0
	return det

def transXxX(y):
	mattranspose = []
	for d in range(0,dimension):
		colonne = []
		for i in range(0,dimension):
			colonne.append(y[i][d])
		mattranspose.append(colonne)
	return mattranspose

def detcheck2(y):
	mattranspose = transXxX(y)
	for  i in range(0,dimension):
		if sum(mattranspose[i]) == 0:
			etat1 = True
			break
		else:
			etat1 = False
	return etat1


c = 0
r = 0

while (c == 0) :
	print('Entrez une dimension X de votre matrice carré?')
	try:
		dimension = int(input())
		if dimension > 0 :
			c = 1
		else:
			print('Nombre invalide, - ou nul')
			question = str(input('Réessayer? OUI ou NON'))
			if question == 'NON' or  question == 'non' or question == 'Non':
				break
	except Exception as e:
		print("Nombre invalide", e)
		question = str(input('Réessayer? OUI ou NON'))
		if question == 'NON' or  question == 'non' or question == 'Non':
			break
		else:
			c = 0
if c == 1:
	r = 0
	while r == 0 :
		mat = matriceXxX()
		matT = transXxX(mat)
		I = IXxX()
		matI = invXxX(mat,I)
		for i in range(0,dimension):
			print(mat[i])
		question1 = str(input('Est-ce la bonne matrice? OUI ou NON'))
		if question1 == 'NON' or  question1 == 'non' or question1 == 'Non':
			r = 0
		else:
			r = 1

if r == 1:
	det = determinantXxX(mat)
	question2 = str(input('Voulez vous calculer le déterminant? OUI ou NON'))
	if question2 != 'NON' or  question2 != 'non' or question2 != 'Non':
		print('Le determinant de votre matrice est ',det)

question3 = str(input('Voulez vous calculer la matrice transposé ? OUI ou NON'))
if question3 != 'NON' or  question3 != 'non' or question3 != 'Non':
	print('La matrice transposé est:')
	for i in range(0,dimension):
		print(matT[i])

