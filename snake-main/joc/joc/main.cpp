#include<iostream>

#include<conio.h>
#include<Windows.h>

using namespace std;
struct Obiect
{
	int x;
	int y;
};
enum Directii {
	STOP,
 LEFT,
 RIGHT,
 DOWN,
 UP,
};

Obiect tail[200];

bool GameOver;
int height;
int width;
Obiect snake;
Obiect point;
Directii dir;
int score = 0;
int ntail=0;


void Setup() {
	GameOver = false;
	height = 15;
	width = 30;
	snake.x = 5;
	snake.y = 5;
	point.x = rand() % width;
	point.y = rand() % height;
	dir = STOP;
}
void Logic()
{
	switch (dir)
	{
	case LEFT:
		snake.x--; break;
	case RIGHT:
		snake.x++; break;
	case DOWN:
		snake.y++; break;
	case UP:
		snake.y--; break;
	}
	int xprev, yprev;
	xprev = snake.x;
	yprev = snake.y;
	int xprev2, yprev2;
	for (int i = 0; i <= ntail; i++) {
		xprev2 = tail[i].x;
		yprev2 = tail[i].y;
		tail[i].x = xprev;
		tail[i].y = yprev;
		xprev = xprev2;
		yprev = yprev2;
	}
	if (snake.x  == point.x && snake.y == point.y) {
		ntail++;
		score++;
		point.x = rand() % width;
		point.y = rand() % height;
	}
	if (snake.x == 0)
		GameOver = true;
	if (snake.x == width)
		GameOver = true;
	if (snake.y == 0)
		GameOver = true;
	if (snake.y == height)
		GameOver = true;
	for (int i = 1; i <= ntail; i++)
	{
		if (snake.x == tail[i].x && snake.y == tail[i].y) {
			GameOver = true;
			break;
		}
	}


}

void Draw() {
	system("cls");
	for (int i = 0; i < width; i++)
		cout << "#";
	cout << "\n";
	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width;j++)
		{
			if (j == 0 || j == width - 1)
				cout << "#";
			else
				if (i == snake.y && j == snake.x)
					cout << "O";
				else
					if (i == point.y && j == point.x)
						cout << "*";
					else {

						bool ecoada = false;
						for (int k = 0; k <= ntail; k++) {
							if (tail[k].x == j && tail[k].y == i) {
								ecoada = true;
								break;
							}
						}

						if (!ecoada)
							cout << " ";
						else cout << "o";
					}
		}
		cout << "\n";
	}
	for (int i = 0; i < width; i++)
		cout << "#";
		cout << endl;
	cout << "Scor:" << score;
}

void Input() {
	if (_kbhit())
	{
		switch (_getch())
		{
		case 'a':dir = LEFT; break;
		case 's':dir = DOWN; break;
		case 'd' : dir = RIGHT; break;
		case 'w' : dir = UP; break;
		}
	}

}
int main() {

	Setup();
	while (!GameOver)
	{
		Input();
		Logic();
		Draw();
		Sleep(40);
	}
	return 0;
}



