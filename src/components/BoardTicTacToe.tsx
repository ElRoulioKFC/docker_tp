import React from "react";
import { Board } from "../common";
import { CellTicTacToe } from "./CellTicTacToe";
import { Stack } from "@mui/material";

export interface BoardTicTacToeProps {
    board: Board;
}

export function BoardTicTacToe(props: BoardTicTacToeProps) {
    const { board } = props;
    return (
        <>
            <Stack direction="column" spacing={1} alignItems="center" justifyContent="center">
                {board.cells.map((row, i) => (
                    <Stack key={i} direction="row" spacing={1} alignItems="center" justifyContent="center">
                        {row.map((cell, j) => (
                            <CellTicTacToe key={j} cell={cell} />
                        ))}
                        </Stack>
                ))}
            </Stack>
        </>
        );
        
}