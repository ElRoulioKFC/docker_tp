export type Game = {
    id: number;
    board:Board;
    player : string;
};
export type Board = {
    id: number;
    cells : Cell[][];
};
// value is 0 if the cell is empty, 1 if it's a player 1 cell, 2 if it's a computer cell
export type Cell = {
    id: number;
    value: number;
};