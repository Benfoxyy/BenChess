from rest_framework.views import APIView
from rest_framework.response import Response
from .stockfish_engine import StockfishWrapper

class GameView(APIView):
    def get(self, request, *args, **kwargs):
        engine = StockfishWrapper()
        fen = request.query_params.get("fen", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        board = engine.get_board(fen)
        return Response({"Board": str(board), "FEN": board.fen()})

    def post(self, request, *args, **kwargs):
        engine = StockfishWrapper()
        fen = request.data.get("fen", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        move = request.data.get("move")
        board = engine.get_best_move(fen, move)

        detail = "Your Turn"
        if board.is_game_over():
            detail = "Game Over"
        elif board.is_checkmate():
            detail = "Checkmate"
        elif board.is_stalemate():
            detail = "Stalemate"
        elif board.is_insufficient_material():
            detail = "Insufficient Material"
        elif board.is_seventyfive_moves():
            detail = "Draw by 75-move rule"
        elif board.is_fivefold_repetition():
            detail = "Draw by fivefold repetition"
        elif board.is_variant_draw():
            detail = "Variant Draw"
        elif board.is_check():
            detail = "Check"

        return Response({"Board": str(board), "FEN": board.fen(), "Detail": detail})
