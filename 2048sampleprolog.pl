:- dynamic(boardScore/2).
play :-
	generate(Board),
	showBoard(Board),
	printHelp,
	game(Board).
ai :-
	ai(2).

ai(Depth) :-
	generate(Board),
	showBoard(Board),
	aigame(Board, Depth).

aigame(Board, _) :-
	max_list(Board, 2048),
	nl,write('AI succeded!'),nl,
	abort.
aigame(Board, _) :-
	noMoreMoves(Board),
	nl,write('AI failed :('),nl,
	abort.
aigame(Board, Depth) :-
	write('Scores:'),
	once(moveLeft(Board, L)),
	evaluate(Board, L, Depth, ScoreL),
	write(' L='),write(ScoreL),
	once(moveRight(Board, R)),
	evaluate(Board, R, Depth, ScoreR),
	write(' R='),write(ScoreR),
	once(moveUp(Board, U)),
	evaluate(Board, U, Depth, ScoreU),
	write(' U='),write(ScoreU),
	once(moveDown(Board, D)),
	evaluate(Board, D, Depth, ScoreD),
	write(' D='),write(ScoreD),
	selectMove(ScoreL, ScoreR, ScoreU, ScoreD, Move),
	aimove(Board, Move, NewBoard),
	showBoard(NewBoard),
	aigame(NewBoard, Depth).

aimove(Board, l, NewBoard) :-
	write(', Move: left'),nl,
	once(moveLeft(Board, B)),
	addNew(B, NewBoard).
aimove(Board, r, NewBoard) :-
	write(', Move: right'),nl,
	once(moveRight(Board, B)),
	addNew(B, NewBoard).
aimove(Board, d, NewBoard) :-
	write(', Move: down'),nl,
	once(moveDown(Board, B)),
	addNew(B, NewBoard).
aimove(Board, u, NewBoard) :-
	write(', Move: up'),nl,
	once(moveUp(Board, B)),
	addNew(B, NewBoard).

equal([],[]).
equal([H1|T1],[H2|T2]) :-
	H1 == H2,
	equal(T1,T2).

move(Board, 119, NewBoard) :-
	write('up'),nl,nl,
	once(moveUp(Board, NewBoard)).
move(Board, 107, NewBoard) :-
	write('up'),nl,nl,
	once(moveUp(Board, NewBoard)).

move(Board, 115, NewBoard) :-
	write('down'),nl,nl,
	once(moveDown(Board, NewBoard)).
move(Board, 106, NewBoard) :-
	write('down'),nl,nl,
	once(moveDown(Board, NewBoard)).

move(Board, 97, NewBoard) :-
	write('left'),nl,nl,
	once(moveLeft(Board, NewBoard)).
move(Board, 104, NewBoard) :-
	write('left'),nl,nl,
	once(moveLeft(Board, NewBoard)).

move(Board, 100, NewBoard) :-
	write('right'),nl,nl,
	once(moveRight(Board, NewBoard)).
move(Board, 108, NewBoard) :-
	write('right'),nl,nl,
	once(moveRight(Board, NewBoard)).

move(_, 113, _) :-
	write('quit'),nl,nl,
	write('Bye...'), nl,nl,
	abort.

showBoard([]).
showBoard([H|T]) :-
	printNumber(H),
	showBoard1(T).
showBoard1([H|T]) :-
	printNumber(H),
	showBoard2(T).
showBoard2([H|T]) :-
	printNumber(H),
	showBoard3(T).
showBoard3([H|T]) :-
	printNumber(H),nl,
	showBoard(T).

printHelp :-
	nl,write('Left: h/a, Down: j/s, Up: k/w, Right: l/d, Show board: b, Quit: q, Help: ?'),nl.

printNumber(N) :-
	N >= 1000,
	write(' '),write(N).
printNumber(N) :-
	N >= 100,
	write('  '),write(N).
printNumber(N) :-
	N >= 10,
	write('   '),write(N).
printNumber(N) :-
	N == 0,
	write('    _').
printNumber(N) :-
	write('    '),write(N).