import chess
import chess.engine
from core.settings import STOCKFISH_PATH

class StockfishWrapper:
    def __init__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci("/app/stockfish/stockfish-ubuntu-x86-64-modern")

    def get_board(self, fen):
        board = chess.Board(fen)
        return board
    
    def get_best_move(self, fen, move, time_limit=0.1):
        board = chess.Board(fen)
        if move:
            try:
                board.push_san(move)  # push the move in standard algebraic notation
            except ValueError as e:
                return board
        result = self.engine.play(board, chess.engine.Limit(time=time_limit))
        board.push(result.move)
        return board  # return the updated board with the move pushed
    
    def undo_move(self, fen):
        board = chess.Board(fen)
        if board.move_stack:
            board.pop()  # undo Stockfish move
        if board.move_stack:
            board.pop()  # undo player move
        return board

    def quit(self):
        self.engine.quit()