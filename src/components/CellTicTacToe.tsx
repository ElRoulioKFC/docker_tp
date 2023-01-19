import { Button, Stack } from "@mui/material";
import React from "react";
import { Cell } from "../common";


export interface CellTicTacToeProps {
    cell: Cell;
}
export const CellTicTacToe = (props: CellTicTacToeProps) => {
    const handleClick = () => {
        if (props.cell.value === 0){
            props.cell.value = 1;
        }
    };
    return (
       <Stack direction="row" spacing={1} alignItems="center" justifyContent="center">
            <Button variant="contained" color="primary" onClick={handleClick}>
                {props.cell.value === 0 ? "" : props.cell.value === 1 ? "X" : "O"}
            </Button>
        </Stack>
    );
};