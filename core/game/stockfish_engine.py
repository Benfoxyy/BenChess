import chess
import chess.engine

class StockfishWrapper:
    def __init__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci("/app/stockfish/stockfish-ubuntu-x86-64-modern")

    def get_board(self, fen):
        return chess.Board(fen)

    def get_best_move(self, fen, move, time_limit=0.1):
        board = chess.Board(fen)
        if move:
            try:
                board.push_uci(move)
            except ValueError:
                return board
        result = self.engine.play(board, chess.engine.Limit(time=time_limit))
        board.push(result.move)
        return board