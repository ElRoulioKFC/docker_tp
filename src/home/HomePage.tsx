import { Button, TextField, Typography } from "@mui/material";
import React, { useEffect } from "react";

export function HomePage(){

    return<div>
            <h1>Bonjour et bienvenue</h1>
            <p>Entrez dans notre monde de spleen en cliquant</p>
            <Button variant="contained" onClick={() => 
                window.location.href = "/content"
            }>Cliquez ici</Button>
            
            
        </div>
        
}
