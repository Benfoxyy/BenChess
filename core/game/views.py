from rest_framework.generics import GenericAPIView
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
        move = request.data.get("move", None)
        board = engine.get_best_move(fen, move)
        if board.is_game_over():
            return Response({"Board": str(board), "FEN": board.fen(), "Detail": "Game Over"})
        if board.is_checkmate():
            return Response({"Board": str(board), "FEN": board.fen(), "Detail": "Checkmate"})
        if board.is_stalemate():
            return Response({"Board": str(board), "FEN": board.fen(), "Detail": "Stalemate"})
        if board.is_insufficient_material():
            return Response({"Board": str(board), "FEN": board.fen(), "Detail": "Insufficient Material"})
        if board.is_seventyfive_moves():
            return Response({"Board": str(board), "FEN": board.fen(), "Detail": "Draw by 75-move rule"})
        if board.is_fivefold_repetition():
            return Response({"Board": str(board), "FEN": board.fen(), "Detail": "Draw by fivefold repetition"})
        if board.is_variant_draw():
            return Response({"Board": str(board), "FEN": board.fen(), "Detail": "Variant Draw"})
        if board.is_check():
            return Response({"Board": str(board), "FEN": board.fen(), "Detail": "Check"})
        return Response({"Board": str(board), "FEN": board.fen(), "Detail": "Your Turn"})