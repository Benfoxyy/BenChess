<h1>♟️ BenChess – Interactive Chess with Stockfish AI</h1>
BenChess is a fully interactive chess web application that lets you play against the Stockfish engine using an elegant browser interface. It uses Django REST Framework for the backend and a modern JavaScript frontend to communicate with Stockfish through a powerful API.

<h1>🎞️ Demo</h1>

![BenChess Presentation](/Document/Video/BenChess.gif)

<h1>🚀 Features</h1>

- ✔️ Play against Stockfish via browser

- ✔️ Modern chessboard with intuitive controls

- ✔️ Move validation and automatic Stockfish replies

- ✔️ Board updates with check/checkmate/draw detection

- ✔️ Dockerized with one-command setup

- ✔️ Responsive frontend UI

<h1>🛠️ Getting Started</h1>

<b>1. Clone the repository</b>

```bash
git clone https://github.com/Benfoxyy/BenChess.git
cd BenChess
```
<b>2. Run with Docker Compose</b>

Make sure Docker and Docker Compose are installed.

```bash
docker-compose up --build
```
The backend API will be available at: http://localhost:8000/swagger/

The frontend (static HTML/JS) will be available at: http://localhost:5500/frontend/ (if served with Live Server or similar)

<h1>✅ TODO / Roadmap</h1>

- Add legal move highlighting

- Add countdown time

- User account

- Add move history panel

- Improve mobile responsiveness

- Add difficulty levels (time depth)

<h1>📄 License</h1>
MIT License © 2025 <a href='https://github.com/Benfoxyy'>Benyamin Medghalchi</a>
