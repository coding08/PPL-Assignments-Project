% Air Traffic Management Database in Prolog

% Facts for airports with taxes and min. security delay
airport(toronto,50,60).
airport(madrid,75,45).
airport(barcelona,40,30).
airport(valencia,40,20).
airport(malega,50,30).
airport(london,75,80).
airport(paris,50,60).
airport(tolouse,40,30).

% Facts for directly linked cities
dir(toronto,london).
dir(toronto,madrid).
dir(barcelona,london).
dir(barcelona,madrid).
dir(barcelona,valencia).
dir(madrid,valencia).
dir(madrid,malega).
dir(valencia,malega).
dir(paris,tolouse).

% Facts listing all given routes with src,dest,airline,price,tax
route(toronto,london,aircanada,500,360).
route(toronto,london,united,650,420).

route(toronto,madrid,united,950,540).
route(toronto,madrid,iberia,800,480).
route(toronto,madrid,aircanada,900,480).

route(madrid,barcelona,aircanada,100,60).
route(madrid,barcelona,iberia,120,65).

route(barcelona,valencia,iberia,110,75).

route(madrid,malega,iberia,50,60).

route(malega,valencia,iberia,80,120).

route(barcelona,london,iberia,220,240).

route(paris,tolouse,united,35,120).

% Rules
% Rule to state wheather there is a direct connection between 2 citiess
direct(X,Y) :- dir(Y,X) ; dir(X,Y).

% Rule to list all possible airlines option for travelling betn 2 cities
routes(X,Y,A,B,C) :- route(Y,X,A,B,C) ; route(X,Y,A,B,C).

% Rule to check if journey is cheap from src to dest with given airline
cheap(X,Y,A) :- routes(X,Y,A,B,C) , B < 400.

% to check if indirect route exsists betn 2 cities
% For demo only a 2 flights are considered in a definition of indirect
indirect(X,Y) :- direct(X,Z) , direct(Z,Y).

% Rule to check if journey is preferred from src to dest with given airline
preferred(X,Y,A) :- cheap(X,Y,A) ; A == aircanada.

% Fake rule
isaircanada(X,Y) :- route(X,Y,united,B,C).
