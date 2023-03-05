king, queen, rook, bishop, knight, pawn = 1, 1, 2, 2, 2, 8

king_input, queen_input, rook_input, bishop_input, knight_input, pawn_input = map(int, input().split())

print(king - king_input, queen-queen_input, rook-rook_input, bishop-bishop_input, knight-knight_input, pawn-pawn_input)